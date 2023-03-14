from sqlalchemy.orm import sessionmaker

from db.connection import engine
from db.models import Transactions


def save_new_data(data) -> int:
    session = sessionmaker(bind=engine)
    session = session()
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
    session.flush()
    inserted_id = transaction.id
    session.commit()
    session.close()
    return inserted_id


def set_private_user_id(user_id: int, transaction_id: int):
    Session = sessionmaker(bind=engine)
    session = Session()
    transaction = session.query(Transactions).filter_by(id=transaction_id).first()
    transaction.provider_id = user_id
    session.commit()
    session.close()


def get_id_by_transaction_id(trans):
    Session = sessionmaker(bind=engine)
    session = Session()
    transaction = session.query(Transactions).filter_by(operations_id=trans).first()
    session.close()
    return transaction.id


def set_private_photo(filename: str, provider_id: int):
    Session = sessionmaker(bind=engine)
    session = Session()
    transaction = session.query(Transactions).filter_by(provider_id=provider_id).first()
    transaction.provider_photo = filename
    session.commit()
    session.close()


def set_admin_photo(filename: str, provider_id: int):
    Session = sessionmaker(bind=engine)
    session = Session()
    transaction = session.query(Transactions).filter_by(provider_id=provider_id).first()
    transaction.admin_photo = filename
    session.commit()
    session.close()


def get_obj_by_id(trans):
    Session = sessionmaker(bind=engine)
    session = Session()
    print(trans)
    transaction = session.query(Transactions).filter_by(id=trans).first()
    session.close()
    message = f"{transaction.id=}\n" \
              f"{transaction.operations_id=}\n" \
              f"{transaction.country=}\n" \
              f"{transaction.currency_exchange_rate_to_tether=}\n" \
              f"{transaction.sum_of_tether=}\n"
    return message