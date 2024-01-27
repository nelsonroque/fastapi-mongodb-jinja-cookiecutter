import pymongo
from jose import JWTError, jwt
from passlib.context import CryptContext

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from utils.log import logger
from models.auth import *
from config.constants import *
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def create_unique_index(dbname, collection, index_name, index_field):
    client = pymongo.MongoClient(SETTINGS.mongodb_connection_string.get_secret_value())
    db = client[dbname]
    db[collection].create_index([(index_field, ASCENDING)], unique=True)


def get_password_hash(password):
    pwd_context = CryptContext(schemes=[SETTINGS.cryptcontext], deprecated="auto")
    ph = pwd_context.hash(password)
    return ph

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(
    db, form_data: OAuth2PasswordRequestForm, additional_data: AdditionalUserDataForm
):
    new_user = {
        "username": form_data.username,
        "hashed_password": get_password_hash(form_data.password),
        "email": additional_data.email,
        "phone_number": additional_data.phone_number,
        "first_name": additional_data.first_name,
        "last_name": additional_data.last_name,
        "affiliation": additional_data.affiliation,
        "studies": [],
    }
    logger.info("Creating user in Pydantic...")
    db_user = UserInDB(**new_user)
    logger.info("Pydantic created!")

    # check if user exists
    user = db.users.find_one({"email": db_user.email})

    # register user if not exists
    if user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )
    else:
        try:
            logger.info("Inserting user into MongoDB...")
            db.users.insert_one(db_user.model_dump())
            logger.info("User inserted!")
        except pymongo.errors.DuplicateKeyError:
            raise HTTPException(
                status_code=400,
                detail="Email already registered",
            )
        return db_user


def is_admin(token):
    user = decode_token(token)
    if user.get("email") in SETTINGS.superuser_emails:
        return True
    else:
        return False


def get_user(db, username: str):
    user = db.users.find_one({"username": username})
    logger.info("User found (get_user)!")
    return user


def find_user_by_email(db, email: str):
    user = db.users.find_one({"email": email})
    logger.info("User found (find_user_by_email)!")
    return user


def get_user_otp(db, otp: str):
    user = db.users.find_one({"otp": otp})
    return user


def authenticate_user(db, username: str, password: str):
    logger.info("Authenticating user...")
    user = get_user(db, username)
    logger.info("User found!")
    if "username" not in user:
        logger.info("User not found!")
        return False
    if not verify_password(password, user.get("hashed_password")):
        logger.info("User not authenticated!")
        return False
    logger.info("User authenticated!")
    return user


def authenticate_otp(db, otp: str):
    user = get_user_otp(db, otp)
    if not user:
        return False
    return user


def decode_token(token: str):
    tk = jwt.decode(token, SETTINGS.secret_key, algorithms=[SETTINGS.algorithm])
    return tk


def create_access_token(data: dict, expires_delta: timedelta = None):
    logger.info("Creating access token...")
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, SETTINGS.secret_key, algorithm=SETTINGS.algorithm
    )
    logger.info("Access token created!")
    return encoded_jwt


#async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, SETTINGS.secret_key, algorithms=[SETTINGS.algorithm]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def update_password(db, user_id, email, hashed_password):
    validated_email = db.users.find_one({"uid": user_id, "email": email})
    if not validated_email:
        return False
    else:
        db.users.update_one(
            {"uid": user_id}, {"$set": {"hashed_password": hashed_password}}
        )
    return True


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
