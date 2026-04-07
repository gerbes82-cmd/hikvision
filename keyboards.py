from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# 🔹 Главное меню
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👥 Сотрудники", callback_data="staff")],
        [InlineKeyboardButton(text="📊 Учет времени", callback_data="time")]
    ])


# 🔹 Меню сотрудников
def staff_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ Добавить", callback_data="add")],
        [InlineKeyboardButton(text="❌ Удалить", callback_data="delete")],
        [InlineKeyboardButton(text="📋 Список", callback_data="list")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ])


# 🔹 Список сотрудников
def users_kb(users):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=f"{name} ({emp})",
                callback_data=f"user_{emp}"
            )]
            for emp, name in users
        ] + [[InlineKeyboardButton(text="⬅️ Назад", callback_data="staff")]]
    )
