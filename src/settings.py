from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr
    deta_project_key: SecretStr
    admin_id: int
    deta_space_app_hostname: str | None = None
    webhook_secret_token: SecretStr | None = None

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
