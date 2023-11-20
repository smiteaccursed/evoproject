from pydantic_settings import BaseSettings, PydanticBaseSettingsSource
from typing import Tuple, Type
from pydantic import Field, MongoDsn, SecretStr, AmqpDsn

class Config(BaseSettings):
    mongo_dsn: MongoDsn = Field(
        default='mongodb://user:pass@host:27017/complaint',
    )
    RABBITMQ_DSN: AmqpDsn = Field(alias="RABBITMQ_DSN")

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