import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8623940567:AAHCouEQsVVFyV-ZnOqfK1SayFZblFH-_mQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "🤖 Бот запущен!\n\n"
        "Доступные команды:\n"
        "/start\n"
        "/ping"
    )


@dp.message(commands=["ping"])
async def ping(message: types.Message):
    await message.answer("🏓 Pong!")


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
