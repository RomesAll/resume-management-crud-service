from pydantic_settings import BaseSettings, SettingsConfigDict
from src import BASE_DIR

class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f'{BASE_DIR}/.env.postgresql',
        env_prefix='POSTGRES_',
        env_file_encoding='utf-8',
        extra='ignore'
    )
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DB: str

    @property
    def database_url(self):
        return f'postgresql+psycopg2://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB}'

class Settings(BaseSettings):
    postgres: PostgresSettings = PostgresSettings()

settings = Settings()