from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


from typing import Tuple, Type

from pydantic import Field, PostgresDsn, SecretStr

class Config(BaseSettings):
    PG_DSN: PostgresDsn = Field(
        default='postgresql+asyncpg://book:book@127.0.0.1:5432/library',
        env='POSTGRES_DSN',
        alias='POSTGRES_DSN'
    )

    jwt_secret: SecretStr = Field(
        default='JWT_SECRET',
        env='JWT_SECRET',
        alias='JWT_SECRET'
    )

    reset_password_token_secret: SecretStr = Field(
        default='RESET_PASSWORD_TOKEN_SECRET',
        env='RESET_PASSWORD_TOKEN_SECRET',
        alias='RESET_PASSWORD_TOKEN_SECRET'
    )

    verification_token_secret: SecretStr = Field(
        default='VERIFICATION_TOKEN_SECRET',
        env='VERIFICATION_TOKEN_SECRET',
        alias='VERIFICATION_TOKEN_SECRET'        
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return dotenv_settings, env_settings, init_settings

def load_config(*arg, **vararg) -> Config:
    return Config(*arg, **vararg)