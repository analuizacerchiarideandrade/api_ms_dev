import os
from dotenv import load_dotenv
#TODO
from pathlib import Path


# app\db\.env
#vai no file env e armazena numa variável
caminho = Path('app\db') / '.env'
print(caminho)
load_dotenv(dotenv_path=caminho)

class Settings:
    PROJECT_NAME:str = "Luiza Board"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str= os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", )
    POSTGRES_PORT : int = os.getenv("POSTGRES_PORT") # --------------------alterado o tipo conforme doc
    POSTGRES_DB : str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
settings = Settings()