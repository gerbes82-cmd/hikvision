import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from database import add_user, get_users, bind_user, get_user_by_tg

TOKEN = "8623940567:AAHCouEQsVVFyV-ZnOqfK1SayFZblFH-_mQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# ================= START =================
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🤖 Бот учета\n\n"
        "Команды:\n"
        "/add 101 Ali\n"
        "/list\n"
        "/bind 101\n"
        "/me"
    )


# ================= ADD =================
@dp.message(Command("add"))
async def add_cmd(message: types.Message):
    try:
        _, emp, name = message.text.split(maxsplit=2)

        add_user(emp, name)

        await message.answer(f"✅ Добавлен: {name}")
    except:
        await message.answer("Формат: /add 101 Ali")


# ================= LIST =================
@dp.message(Command("list"))
async def list_cmd(message: types.Message):
    users = get_users()

    if not users:
        await message.answer("Сотрудников нет")
        return

    text = "\n".join([f"{e} - {n}" for e, n in users])
    await message.answer(text)


# ================= BIND =================
@dp.message(Command("bind"))
async def bind_cmd(message: types.Message):
    try:
        emp = message.text.split()[1]

        bind_user(emp, message.from_user.id)

        await message.answer("✅ Привязан")
    except:
        await message.answer("Формат: /bind 101")


# ================= ME =================
@dp.message(Command("me"))
async def me_cmd(message: types.Message):
    user = get_user_by_tg(message.from_user.id)

    if not user:
        await message.answer("❌ Не привязан")
        return

    await message.answer(f"Вы: {user[1]} (ID {user[0]})")


# ================= RUN =================
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
