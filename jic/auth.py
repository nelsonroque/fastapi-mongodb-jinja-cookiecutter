from random import randint

import pymongo
from fastapi import FastAPI, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Json
from starlette.status import *
from models.auth import *

from models.base import *
from utils.storage import *
from utils.auth import *
from config.constants import *

router = APIRouter(prefix="/auth", tags=["authentication"])

client = pymongo.MongoClient(SETTINGS.mongodb_connection_string.get_secret_value())
db = client[SETTINGS.mongodb_db_name]

# async def login_for_access_token_otp(token: Annotated[str, Depends(oauth2_scheme)]):
@router.get("/whoami", status_code=200)
async def login_for_access_token_otp(token: str=  Depends(oauth2_scheme)):
    tk = decode_token(token)
    return tk


@router.post("/register", status_code=201)
async def sign_up(
    form_data: OAuth2PasswordRequestForm = Depends(),
    additional_data: AdditionalUserDataForm = Depends(),
):
    logger.info("Connecting to MongoDB")
    user = create_user(db, form_data, additional_data)
    logger.info("Inserted record into MongoDB")
    return {"msg": "User created successfully"}


@router.post("/reset_password", status_code=200)
async def reset_password(email: str, form_data: OAuth2PasswordRequestForm = Depends()):
    user = find_user_by_email(db, email)
    if user:
        hashed_password = get_password_hash(form_data.password)
        update_password(db, user["uid"], email, hashed_password)
        return HTTPException(status_code=200, detail="Password reset successful.")
    else:
        return {"msg": "User not found"}


@router.post("/token", response_model=Token, status_code=200)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    logger.info("===============")
    print(user)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    logger.info("==============")
    access_token_expires = timedelta(minutes=int(SETTINGS.access_token_expire_minutes))
    logger.info(f"Access token expires: {access_token_expires}")
    access_token = create_access_token(
        data={
            "sub": user.get("username"),
            "email": user.get("email"),
            "studies": user.get("studies"),
            "uid": user.get("uid"),
        },
        expires_delta=access_token_expires,
    )
    tk = {"access_token": access_token, "token_type": "bearer"}
    return tk


@router.post("/update-email/{uid}", status_code=200)
async def update_user_email(
    uid: str, email: str, token: str = Depends(oauth2_scheme)
):
    logger.info(f"Adding email to user's studies list")
    user = decode_token(token)
    if user.get("email") in SETTINGS.superuser_emails:
        logger.info("Connecting to MongoDB")
        print("Connecting to MongoDB")
        client, db, collection = init_mongodb_customdb(
            db, SETTINGS.mongodb_collection_users
        )
        user2 = collection.find_one({"uid": uid})
        if user2 is not None:
            collection.update_one({"uid": uid}, {"$set": {"email": email}})
            client.close()
            logger.info("User updated")
            return "User updated"
        else:
            logger.info("User not found")
            return "User not found"
    else:
        return HTTPException(status_code=401, detail="You do not have permission to access this endpoint.")

@router.post("/allow/{email}", status_code=200)
async def add_study_to_user(
    email: str, study: str, token: str = Depends(oauth2_scheme)
):
    print(f"Adding study {study} to user's studies list")
    user = decode_token(token)
    print(user)
    if user.get("email") in SETTINGS.superuser_emails:
        logger.info("Connecting to MongoDB")
        client, db, collection = init_mongodb_customdb(
            SETTINGS.mongodb_db_name, SETTINGS.mongodb_collection_users
        )
        logger.info("Connected to MongoDB!")
        user_r = collection.find_one({"email": email})
        print(user_r)

        if user_r is None:
            # Return a 404 error if user not found
            return {"error": f"User with email: {email} not found"}

        # Add the study to the user's studies list
        if "studies" not in user_r:
            user_r[
                "studies"
            ] = []  # Initialize the studies list if it doesn't exist yet

        if study not in user_r["studies"]:
            # TODO: if study is really a study
            user_r["studies"].append(study)

            # Update the user record in the database
            db["users"].update_one({"email": email}, {"$set": user_r})
            return "Success"
        else:
            return HTTPException(status_code=200, detail=f"User with email: {email} already has access to study: {study}")
    else:
        return HTTPException(status_code=401, detail="You do not have permission to access this endpoint.")


@router.post("/deny/{email}", status_code=200)
async def remove_study_from_user(
    email: str, study: str, token: str = Depends(oauth2_scheme)
):
    print(f"Adding study {study} to user's studies list")
    user = decode_token(token)
    print(user)
    if user.get("email") in SETTINGS.superuser_emails:
        logger.info("Connecting to MongoDB")
        client, db, collection = init_mongodb_customdb(
            SETTINGS.mongodb_db_name, SETTINGS.mongodb_collection_users
        )
        logger.info("Connected to MongoDB!")
        user_r = collection.find_one({"email": email})

        if user_r is None:
            # Return a 404 error if user not found
            return {"error": f"User with email: {email} not found"}

        # Add the study to the user's studies list
        if "studies" not in user_r:
            user_r[
                "studies"
            ] = []  # Initialize the studies list if it doesn't exist yet

        if study in user_r["studies"]:
            user_r["studies"].remove(study)

            # Update the user record in the database
            collection.update_one({"email": email}, {"$set": user_r})
            return "Success"
        else:
            return HTTPException(status_code=401, detail=f"User with email: {email} does not currently have access to study: {study}")
    else:
        return HTTPException(status_code=401, detail="You do not have permission to access this endpoint.")


@router.post("/study", status_code=201)
async def create_study(study: Study, token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    if user.get("email") in SETTINGS.superuser_emails:
        client, db, collection = init_mongodb("studies")
        study_exists = collection.find_one({"title": study.title})
        if study_exists is not None:
            return "Study already exists"
        else:
            # then insert
            collection.insert_one(study.dict())
            return "Study created"
            # TODO: return API key to faciliate this step?
        # TODO: create with pydantic model to autopipe fields
    else:
        return HTTPException(status_code=401, detail="You are not authorized to create a study.")