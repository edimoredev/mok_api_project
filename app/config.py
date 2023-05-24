# POSTGRES_URL = "127.0.0.1:5432"
# POSTGRES_USER = "postgres"
# POSTGRES_PW = ""
# POSTGRES_DB = "apimok"

# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
#     user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
# SQLALCHEMY_TRACK_MODIFICATIONS = False


import os


class Config:
    DEBUG = False
    # Resto de las configuraciones...


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db/apimok'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
