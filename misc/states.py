from aiogram.dispatcher.filters.state import State, StatesGroup


class Report(StatesGroup):
    set_file = State()


class Approve(StatesGroup):
    set_file = State()
