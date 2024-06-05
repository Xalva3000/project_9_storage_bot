from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from lexicon.lexicon import LEXICON_default

router = Router()


@router.message(Command(commands=["start"]))
async def process_start_message(message: Message):
    await message.answer(text=LEXICON_default["start"])
