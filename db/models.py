from sqlalchemy import Column, Integer, String, Float, BigInteger
from db.connection import Base, engine


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
    provider_id = Column(BigInteger)
    provider_photo = Column(String)
    admin_photo = Column(String)
    chat_id = Column(BigInteger)
    reply_to_message_id = Column(BigInteger)
    provider_api_id = Column(BigInteger)
    crypto_wallet_number = Column(String)
    status_api = Column(String)
    sum_api = Column(Float)


Base.metadata.create_all(engine)
