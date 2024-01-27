
# # Endpoint for sending the OTP
# @router.post("/otp/request")
# async def request_otp(otp_request: OTPRequest):
#     # Generate a random 6-digit OTP
#     otp = str(randint(100000, 999999))
#     client = pymongo.MongoClient(Settings.MONGODB_ENDPOINT_URL)
#     db = client[Settings.AUTH_DB]
#     db.users.update_one(
#         {"email": otp_request.email},
#         {"$set": {"otp": otp, "otp_generated_at": datetime.now()}},
#     )
#     db.otp_logs.insert_one(
#         {"email": otp_request.email, "otp": otp, "otp_generated_at": datetime.now()}
#     )
#     message = "Your OTP is: " + otp

#     # Send the OTP to the user via SMS
#     if otp_request.phone_number:
#         send_sms_twilio_simple(otp_request.phone_number, message)
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Please provide a valid phone number.",
#         )

#     return OTPResponse(success=True, message="OTP sent successfully.")

# # Endpoint for verifying the OTP and generating a JWT
# @router.post("/otp/verify")
# async def verify_otp(otp: str, form_data: OAuth2PasswordRequestForm = Depends()):
#     # Verify the OTP provided by the user
#     print("Verifying OTP")
#     client = pymongo.MongoClient(Settings.MONGODB_ENDPOINT_URL)
#     db = client[Settings.AUTH_DB]
#     print("Connected to MongoDB!")
#     user = db.users.find_one({"username": form_data.username, "otp": otp})
#     print("Found user")
#     print(user)
#     if (
#         user is not None and "username" in user
#     ):  # Replace with your own validation logic
#         # Generate a JWT token
#         otp = str(randint(100000, 999999))
#         db.users.update_one(
#             {"username": user.get("username")},
#             {"$set": {"otp": otp, "otp_generated_at": datetime.now()}},
#         )
#         access_token_expires = timedelta(minutes=int(Settings.ACCESS_TOKEN_EXPIRE_MINUTES))
#         print("Access token expires")
#         access_token = create_access_token(
#             data={
#                 "sub": user.get("username"),
#                 "email": user.get("email"),
#                 "studies": user.get("studies"),
#                 "uid": user.get("uid"),
#             },
#             expires_delta=access_token_expires,
#         )
#         return {"access_token": access_token, "token_type": "bearer"}
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid OTP."
#         )
