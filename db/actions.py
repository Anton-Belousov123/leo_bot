from db.models import Transactions
from db.connection import session


def save_new_data(transaction: Transactions) -> int:
    """Return saved transaction id"""
    session.add(transaction)
    session.flush()
    transaction_id = transaction.id
    session.commit()
    return transaction_id


def set_private_user_id(user_id: int, transaction_id: int):
    """Set provider_id to user_id"""
    transaction = session.query(Transactions).filter_by(id=transaction_id).first()
    transaction.provider_id = user_id
    session.commit()


def get_id_by_transaction_id(operations_id: int) -> int:
    """Return transaction id by operation id"""
    transaction = session.query(Transactions).filter_by(operations_id=operations_id).first()
    return transaction.id


def set_private_photo(filename: str, provider_id: int):
    """Set provider photo by provider id"""
    transaction = session.query(Transactions).filter_by(provider_id=provider_id).first()
    transaction.provider_photo = filename
    session.commit()


def set_admin_photo(filename: str, provider_id: int):
    """Set admin photo by provider id"""
    transaction = session.query(Transactions).filter_by(provider_id=provider_id).first()
    transaction.admin_photo = filename
    session.commit()

def set_reply(filename: str, provider_id: int):
    """Set admin photo by provider id"""
    transaction = session.query(Transactions).filter_by(provider_id=provider_id).first()
    transaction.admin_photo = filename
    session.commit()




def get_obj_by_id(transaction_id: int):
    """Return __str__ obj of transaction by id"""
    transaction = session.query(Transactions).filter_by(id=transaction_id).first()
    return f"{transaction.country}\n" \
           f"Номер: {transaction.operations_id}\n" \
           f"Перевод: {transaction.sum_of_trans_in_currency}\n" \
           f"Обеспечение: {transaction.currency_exchange_rate_to_tether} ({transaction.currency_of_trans})\n" \
           f"Курс: 1 = {transaction.sum_of_tether}\n"



def get_obj_by_id_to_private(transaction_id: int):
    """Return __str__ obj of transaction by id to private message"""
    transaction = get_obj_by_id(transaction_id=transaction_id)
    return transaction + '\nНомер карты: 4000 0012 3456 7899'


def get_obj_by_id_admin(transaction_id: int):
    transaction = session.query(Transactions).filter_by(id=transaction_id).first()
    return f'Номер: {transaction.operations_id}\nОбеспечение: {transaction.sum_api}\n' \
           f'Номер кошелька: {transaction.crypto_wallet_number}' 


def update_transaction(d):
    print(d)
    transaction = session.query(Transactions).filter_by(operations_id=d['OperationsID']).first()
    print(transaction)
    transaction.status_api = d['Status']
    transaction.crypto_wallet_number = d['CryptoWalletNumber']
    transaction.provider_api_id = d['ProviderID']
    transaction.sum_api = float(d['SumOfTether'].replace(',', '.'))
    session.commit()


def update_thread_id(operations_id, reply_to_message_id):
    transaction = session.query(Transactions).filter_by(operations_id=operations_id).first()
    transaction.reply_to_message_id = reply_to_message_id
    session.commit()


def update_admin_photo(thread_id, filename):
    transaction = session.query(Transactions).filter_by(reply_to_message_id=thread_id).first()
    transaction.admin_photo = filename
    session.commit()
