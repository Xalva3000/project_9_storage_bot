from aiogram.fsm.state import State, StatesGroup


class FSMStates(StatesGroup):
    adding_transaction = State()