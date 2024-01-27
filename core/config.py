from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings
from typing import Optional, List

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# REFERENCE
# https://docs.pydantic.dev/latest/concepts/pydantic_settings/

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

class AppSettings(BaseSettings):
    debug_mode: bool = Field(..., env="DEBUG_MODE")
    param_uid_length: int = Field(..., env="PARAM_UID_LENGTH")

    app_name: str = Field(..., env="APP_NAME")
    app_description: str = Field(..., env="APP_DESCRIPTION")
    app_version: str = Field(..., env="APP_VERSION")
    app_deployment: str = Field(..., env="APP_DEPLOYMENT")
    app_website: str = Field(..., env="APP_WEBSITE")
    app_author_name: str = Field(..., env="APP_AUTHOR_NAME")
    app_author_email: str = Field(..., env="APP_AUTHOR_EMAIL")

    mongodb_cluster_id: SecretStr = Field(..., env="MONGODB_CLUSTER_ID")
    mongodb_db_name: str = Field(..., env="MONGODB_DB_NAME")
    mongodb_username: str = Field(..., env="MONGODB_USERNAME")
    mongodb_password: SecretStr = Field(..., env="MONGODB_PASSWORD")

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# instantiate the AppSettings class
config = AppSettings()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
