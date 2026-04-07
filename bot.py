import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from database import add_user, get_users, delete_user
from keyboards import main_menu, staff_menu, users_kb

TOKEN = "PASTE_YOUR_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# временное хранилище состояния
user_state = {}


# ================= START =================
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Меню:", reply_markup=main_menu())


# ================= КНОПКИ =================
@dp.callback_query()
async def callbacks(call: types.CallbackQuery):
    data = call.data

    # открыть меню сотрудников
    if data == "staff":
        await call.message.answer("Управление:", reply_markup=staff_menu())

    # добавить
    elif data == "add":
        user_state[call.from_user.id] = "add"
        await call.message.answer("Введите: ID Имя\nпример: 101 Ali")

    # удалить
    elif data == "delete":
        users = get_users()
        if not users:
            await call.message.answer("Нет сотрудников")
            return

        await call.message.answer("Выберите кого удалить:", reply_markup=users_kb(users))

    # список
    elif data == "list":
        users = get_users()
        if not users:
            await call.message.answer("Нет сотрудников")
            return

        text = "\n".join([f"{e} - {n}" for e, n in users])
        await call.message.answer(text)

    # удаление конкретного
    elif data.startswith("user_"):
        emp = data.split("_")[1]
        delete_user(emp)
        await call.message.answer(f"❌ Удалён {emp}")


# ================= ТЕКСТ =================
@dp.message()
async def handle_text(message: types.Message):
    uid = message.from_user.id

    # режим добавления
    if user_state.get(uid) == "add":
        try:
            emp, name = message.text.split(maxsplit=1)
            add_user(emp, name)

            await message.answer(f"✅ Добавлен {name}")
            user_state.pop(uid)

        except:
            await message.answer("Ошибка. Формат: 101 Ali")


# ================= RUN =================
async def main():
    print("Бот с UI запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
