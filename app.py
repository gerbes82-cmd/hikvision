import asyncio
from aiogram import Bot, Dispatcher, types
from datetime import date

from config import BOT_TOKEN
from database import *
from logic import calculate
from scheduler import run

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def msg(message: types.Message):
    if message.text == "/start":
        await message.answer("ERP система готова")

    elif message.text.startswith("/bind"):
        emp = message.text.split()[1]
        bind_user(emp, message.from_user.id)
        await message.answer("OK")

    elif len(message.text.split()) == 2:
        emp, name = message.text.split()
        add_user(emp, name)
        await message.answer("Добавлен")


@dp.message()
async def today(message: types.Message):
    if message.text == "today":
        emp = get_emp(message.from_user.id)
        if not emp:
            await message.answer("Сначала /bind")
            return

        events = get_events(emp, str(date.today()))
        schedule = get_schedule(emp)

        h, l, o, s = calculate(events, schedule)

        await message.answer(f"{h} ч\nОпоздание: {l}\n{s}")


async def main():
    asyncio.create_task(run())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
