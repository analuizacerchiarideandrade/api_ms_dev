
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# import os
# from dotenv import load_dotenv
# from pathlib import Path

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

# class Settings:
#     PROJECT_NAME:str = "Luiza Board"
#     PROJECT_VERSION: str = "1.0.0"
#     POSTGRES_USER : str = os.getenv("POSTGRES_USER")
#     POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
#     POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER")
#     POSTGRES_PORT : str = os.getenv("POSTGRES_PORT") # default postgres port is 5432
#     POSTGRES_DB : str = os.getenv("POSTGRES_DB")
#     DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# settings = Settings()


# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# print("Database URL is ",SQLALCHEMY_DATABASE_URL)
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Session = sessionmaker(bind=engine)
