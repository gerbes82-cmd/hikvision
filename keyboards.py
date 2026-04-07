from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👥 Сотрудники", callback_data="staff")]
    ])


def staff_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ Добавить", callback_data="add")],
        [InlineKeyboardButton(text="❌ Удалить", callback_data="delete")],
        [InlineKeyboardButton(text="📋 Список", callback_data="list")]
    ])


def users_kb(users):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"{name} ({emp})", callback_data=f"user_{emp}")]
            for emp, name in users
        ]
    )
