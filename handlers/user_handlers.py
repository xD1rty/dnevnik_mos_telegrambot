import os
from datetime import datetime, timedelta
from aiogram import Router, F
from aiogram.types import Message
from dnevniklib import Student, Homeworks, Marks
from dnevniklib.utils import Utils
from aiogram.filters import CommandStart, Command

user_router = Router()
user = Student(token=os.getenv("DNEVNIK_MOS_TOKEN"))
homeworks = Homeworks(user)
marks = Marks(user)


@user_router.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(f"Привет, {user.first_name}!")

@user_router.message(Command("homeworks"))
async def homeworks_bot(message: Message):
    text = "Домашнее задание на завтра:\n\n"
    _datetime = datetime.now() + timedelta(days=1)
    date = Utils.get_normal_date(_datetime.year, _datetime.month, _datetime.day)
    homework = homeworks.get_homework_by_date(date)

    for hw in homework:
        text += f"Предмет: {hw.subject_name}\n"
        text += f"Описание: {hw.description}\n"
        text += f"Выполнение: {'сделано' if hw.is_done else 'не сделано'}\n\n"

    await message.answer(text) # TODO: добавить обработку


@user_router.message(Command("marks"))
async def marks_bot(message: Message):
    text = "Оценки за сегодня:\n\n"
    _datetime = datetime.now()
    date = Utils.get_normal_date(_datetime.year, _datetime.month, _datetime.day)
    marks_today = marks.get_marks_by_date(date, date)

    for mark in marks_today:
        text += f"Предмет: {mark.subject_name}\n"
        text += f"Оценка: {mark.value}\n\n"

    await message.answer(text) # TODO: добавить обработку
