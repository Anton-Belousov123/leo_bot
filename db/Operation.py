from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float
from db.connection import Base, engine


# Define the schema for the table
class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    telegram_chat_id = Column(String)
    country = Column(String)
    operations_id = Column(String)
    sum_of_trans_in_currency = Column(Float)
    currency_of_trans = Column(String)
    sum_of_tether = Column(Float)
    currency_exchange_rate_to_tether = Column(Float)


Base.metadata.create_all(engine)


def save_new_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    data = {
        "TelegramChatId": "981655201",
        "Country": "Турция",
        "OperationsID": "AA001",
        "SumOfTransInCurrency": "1000",
        "CurrencyOfTrans": "Турецкая лира",
        "SumOfTether": "52",
        "CurrencyEchangeRateToTether": "19,12"
    }
    transaction = Transactions(
        telegram_chat_id=data["TelegramChatId"],
        country=data["Country"],
        operations_id=data["OperationsID"],
        sum_of_trans_in_currency=float(data["SumOfTransInCurrency"]),
        currency_of_trans=data["CurrencyOfTrans"],
        sum_of_tether=float(data["SumOfTether"]),
        currency_exchange_rate_to_tether=float(data["CurrencyEchangeRateToTether"].replace(',', '.'))
    )
    session.add(transaction)
    session.commit()
    session.close()
