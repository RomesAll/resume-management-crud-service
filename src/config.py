from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from src import BASE_DIR

class PostgresSettings(BaseModel):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    DB: str

    @property
    def database_url(self):
        return f'postgresql+psycopg2://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB}'

class Settings(BaseSettings):
    postgres: PostgresSettings

    app_name: str = "ResumesManagerApp"
    debug: bool = False

    model_config = SettingsConfigDict(
        env_prefix='APP_',
        env_file=f'{BASE_DIR}/.env.postgresql',
        env_file_encoding='utf-8',
        env_nested_delimiter='__'
    )

settings = Settings()
print(settings)