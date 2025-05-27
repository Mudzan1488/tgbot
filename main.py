import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Укажи сюда свой токен
TOKEN = "7810573588:AAHE5IXuJ9t6a6cIEujqtfkl8J84N50qj3o"

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

# Главное меню
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Заказать"), KeyboardButton(text="Оставить отзыв")]
    ],
    resize_keyboard=True
)

# Подменю для заказа
order_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Логотипы"), KeyboardButton(text="Сайты")],
        [KeyboardButton(text="Телеграмм боты")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Хендлер /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Ассаламу алейкум! Добро пожаловать в бота.", reply_markup=main_kb)

# Заказ
@dp.message(lambda message: message.text == "Заказать")
async def order_menu(message: types.Message):
    await message.answer("Выберите, что хотите заказать:", reply_markup=order_kb)

# Назад
@dp.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=main_kb)

# Логотипы
@dp.message(lambda message: message.text == "Логотипы")
async def logos_info(message: types.Message):
    await message.answer(
        "Для заказа логотипа свяжитесь со мной:\n"
        "+7 777 123 45 67\n"
        "Telegram: @Abdusaliam"
    )

# Сайты
@dp.message(lambda message: message.text == "Сайты")
async def sites_info(message: types.Message):
    await message.answer(
        "Для заказа сайта свяжитесь со мной:\n"
        "+7 777 123 45 67\n"
        "Telegram: @Abdusaliam"
    )

# Телеграмм боты
@dp.message(lambda message: message.text == "Телеграмм боты")
async def bots_info(message: types.Message):
    await message.answer(
        "Для заказа Telegram-бота свяжитесь со мной:\n"
        "+7 777 123 45 67\n"
        "Telegram: @Abdusaliam"
    )

# Отзывы
@dp.message(lambda message: message.text == "Оставить отзыв")
async def feedback_link(message: types.Message):
    await message.answer("Оставить отзыв можно в нашем канале: https://t.me/ahiworks")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
