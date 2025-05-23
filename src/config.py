from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    URL_AUTH: str
    GRANT_TYPE: str
    USER_NAME: str
    CLEAR_TEXT_PWD: str
    PASSWORD: str
    IDENTITY_TYPE: str
    CLIENT_ID: str
    ACW_TC_KEY: str

    URL_DATA: str
    BEARER_TOKEN: str

    IP_ZABBIX: str

    model_config = SettingsConfigDict(env_file='../.env_prod')


settings = Settings()
