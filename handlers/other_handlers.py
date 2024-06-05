from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_default

router = Router()


@router.message()
async def process_start_message(message: Message):
    await message.answer(LEXICON_default["unknown_command"])
