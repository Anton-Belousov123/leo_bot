import dataclasses
import enum

import dotenv
import os


class LoggingMode(enum.Enum):
    CONSOLE = 'CONSOLE'
    FILE = 'FILE'


@dataclasses.dataclass
class PgConnection:
    USERNAME: str
    PASSWORD: str
    HOSTNAME: str
    PORT: str
    DATABASE: str


@dataclasses.dataclass
class SecretInfo:
    TELEGRAM_API_TOKEN: str
    POSTGRES: PgConnection
    LOGGING_MODE: LoggingMode


def load_secrets() -> SecretInfo:
    dotenv.load_dotenv()
    return SecretInfo(TELEGRAM_API_TOKEN=os.getenv('TELEGRAM_API_TOKEN'),
                      POSTGRES=PgConnection(
                          USERNAME=os.getenv('USERNAME'),
                          PASSWORD=os.getenv('PASSWORD'),
                          HOSTNAME=os.getenv("HOSTNAME"),
                          PORT=os.getenv('PORT'),
                          DATABASE=os.getenv('DATABASE')
                      ),
                      LOGGING_MODE=LoggingMode(os.getenv('LOGGING_MODE')))


secret_info = load_secrets()
