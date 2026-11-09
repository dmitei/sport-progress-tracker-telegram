import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)

TOKEN = os.environ["BOT_TOKEN"]        # токен от @BotFather
WEBAPP_URL = os.environ["WEBAPP_URL"]  # ссылка на GitHub Pages (https://...)

dp = Dispatcher()


def open_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="Открыть трекер", web_app=WebAppInfo(url=WEBAPP_URL))
        ]]
    )


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Это трекер прогресса: замеры тела и подсчёт КБЖУ.\n"
        "Нажми кнопку ниже или используй кнопку меню слева от поля ввода.",
        reply_markup=open_kb(),
    )


@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "/start — открыть трекер\n"
        "Данные хранятся в твоём Telegram-аккаунте и доступны на всех устройствах."
    )


async def main():
    bot = Bot(TOKEN)
    # постоянная кнопка меню рядом с полем ввода
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Прогресс", web_app=WebAppInfo(url=WEBAPP_URL))
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
