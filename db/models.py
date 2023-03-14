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


Base.metadata.create_all(engine)
