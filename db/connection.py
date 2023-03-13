from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from misc import secrets

pg_secrets = secrets.SecretInfo.POSTGRES
engine = create_engine(f'postgresql://{pg_secrets.USERNAME}'
                       f':{pg_secrets.PASSWORD}'
                       f'@{pg_secrets.HOSTNAME}'
                       f':{pg_secrets.PORT}'
                       f'/{pg_secrets.DATABASE}')
Base = declarative_base()
