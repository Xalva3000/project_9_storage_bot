from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from gspread import Spreadsheet, Worksheet

from lexicon.lexicon import LEXICON_user
from gdrive.gdrive_config import get_google_spreadsheet, fishstorage_table_id
from gdrive.query import get_fishstorage_total
from states.bot_states import FSMStates


router = Router()


@router.message(Command(commands=['остатки']))
async def process_start_message(message: Message):
    df = get_fishstorage_total()
    lst_temp = []
    for row in df.values:
        lst_temp.append(f"{row[0]}: {row[2]}шт X {row[1]}кг = {row[3]}кг")
    await message.answer(text='\n'.join(lst_temp))


@router.message(Command(commands=['остаток']))
async def process_start_message(message: Message):
    sh: Spreadsheet = get_google_spreadsheet(fishstorage_table_id)
    ws: Worksheet = sh.worksheet('total')
    lst_temp = []
    for row in ws.get_all_values()[1::]:
        if row[0] != '---':
            lst_temp.append(f"{row[0]}: {row[2]}шт X {row[1]}кг = {row[3]}кг")
    await message.answer(text='\n'.join(lst_temp))


@router.message(Command(commands=['транзакция', 'тр']))
async def process_start_message(message: Message, state: FSMContext):
    await state.set_state(FSMStates.adding_transaction)
    await message.answer(text=LEXICON_user['add_transaction'])


@router.message(StateFilter(FSMStates.adding_transaction))
async def process_start_message(message: Message, state: FSMContext):
    if message.text == '/cancel' or message.text == '/cancel@fishstorage_bot':
        await message.answer(text=LEXICON_user['cancel_transaction'])
        await state.clear()
    else:
        sh: Spreadsheet = get_google_spreadsheet(fishstorage_table_id)
        ws: Worksheet = sh.worksheet('transactions')
        ws.append_row(message.text.split(':') + [message.from_user.first_name])
        await message.answer(text=LEXICON_user['transaction_added'])
        await state.clear()
