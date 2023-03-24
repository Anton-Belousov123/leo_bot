from flask import Flask, request
from db import actions
from db.models import Transactions
from misc import messages, secrets
import requests

app = Flask(__name__)

provider_channel_id = -1001815435429
admin_channel_id = -1001751669371


def create_post(chat_id: int, keybaord, m: str):
    print(m)
    url = f"https://api.telegram.org/bot{secrets.secret_info.TELEGRAM_API_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": m,
        "reply_markup": keybaord
    }
    response = requests.post(url, json=data)
    response.raise_for_status()


def get_approve_keyboard(index: int):
    return {
        "inline_keyboard": [
            [
                {
                    "text": messages.SUGGEST,
                    "callback_data": f"approve_{index}"
                }
            ]
        ],
        "resize_keyboard": True
    }


def get_post_keyboard(index: int):
    return {
        "inline_keyboard": [
            [
                {
                    "text": messages.ACCEPT,
                    "callback_data": f"accept_{index}"
                }
            ]
        ],
        "resize_keyboard": True
    }


@app.route('/example', methods=['POST'])
def handle_post_request():
    data = request.get_json()
    for d in data['data']:
        try:
            transaction = Transactions(
                telegram_chat_id=d["TelegramChatId"],
                country=d["Country"],
                operations_id=d["OperationsID"],
                sum_of_trans_in_currency=float(d["SumOfTransInCurrency"]),
                currency_of_trans=d["CurrencyOfTrans"],
                sum_of_tether=float(d["SumOfTether"]),
                currency_exchange_rate_to_tether=float(d["CurrencyEchangeRateToTether"].replace(',', '.'))
            )
            transaction_id = actions.save_new_data(transaction)
            create_post(provider_channel_id, get_post_keyboard(transaction_id),
                        messages.NEW_POST(actions.get_obj_by_id(transaction_id)))
        except Exception as e:
            print(e)
    return ''


@app.route('/example2', methods=['POST'])
def handle_post2_request():
    data = request.get_json()
    print(data)
    for d in data['data']:
        try:
            if d['Status'] == 'Выполнен':
                actions.update_transaction(d)
                transaction_id = actions.get_id_by_transaction_id(d['OperationsID'])
                create_post(admin_channel_id, get_approve_keyboard(transaction_id),
                            messages.NEW_POST(actions.get_obj_by_id_admin(transaction_id)))
        except Exception as e:
            print(e)
    return ''


app.run(debug=True)
