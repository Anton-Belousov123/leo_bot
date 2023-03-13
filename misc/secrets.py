import dataclasses
import dotenv
import os

@dataclasses.dataclass
class PgConntection:
    USERNAME: str
    PASSWORD: str
    HOSTNAME: str
    PORT: str
    DATABASE: str


@dataclasses.dataclass
class SecretInfo:
    TELEGRAM_API_TOKEN: str
    POSTGRES: PgConntection

def load_secrets() -> SecretInfo:
    dotenv.load_dotenv()
    return SecretInfo(TELEGRAM_API_TOKEN=os.getenv('TELEGRAM_API_TOKEN'),
                      POSTGRES=PgConntection(
                          USERNAME=os.getenv('USERNAME'),
                          PASSWORD=os.getenv('PASSWORD'),
                          HOSTNAME=os.getenv("HOSTNAME"),
                          PORT=os.getenv('PORT'),
                          DATABASE=os.getenv('DATABASE')
                      ))

secret_info = load_secrets()