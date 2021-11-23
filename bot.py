import asyncio
import logging
import keyboards as kb
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from os import getenv
from sys import exit


bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

# Объект бота
bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)

# Логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)
    await message.reply("Вы заблокированы")


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, <b>{message.from_user.first_name}</b>\nЧем могу помочь?",
        reply_markup=kb.start_keyboard
    )


@dp.callback_query_handler(text_startswith="btn_")
async def callbacks_num(call: types.CallbackQuery):
    btn_number = call.data.split("_")[1]
    if btn_number == "1":
        await call.message.answer(
            "В каком городе ты находишься?",
            reply_markup=kb.city_selection_keyboard
        )
    elif btn_number == "2":
        await call.message.answer(
            "Группа компаний <b>PARMA Technologies Group</b> основана в 2016 году. "
            "Главным направлением деятельности является разработка заказного программного обеспечения.\n\n "
            "У нас собрана профессиональная команда, чей опыт работы на рынке информационных технологий составляет"
            "более 12 лет. Решениями, разработанными нашими специалистами, пользуются многие федеральные,"
            "региональные и муниципальные органы государственной власти.\n\n "
            'Подробности по <a href="https://www.parma.ru/">ссылке</a>',
            disable_web_page_preview=True
        )
    elif btn_number == "3":
        await call.message.answer(
            "О какой вакансии ты бы хотел узнать?",
            reply_markup=kb.vacancy_selection_keyboard
        )
    elif btn_number == "4":
        await call.message.answer(
            "Отправьте своё резюме в этот чат, мы рассмотрим Вашу заявку и свяжемся с вами"
        )
    elif btn_number == "5":
        await call.message.answer("Администратор баз данных")
    elif btn_number == "6":
        await call.message.answer("Бизнес-архитектор")
    elif btn_number == "7":
        await call.message.answer("Руководитель группы разработки")
    elif btn_number == "8":
        await call.message.answer("Специалист по оценке персонала")
    elif btn_number == "9":
        await call.message.answer("Системный архитектор")
    elif btn_number == "10":
        await call.message.answer("DevOps-инженер")
    elif btn_number == "11":
        await call.message.answer("Руководитель проектов")
    elif btn_number == "12":
        await call.message.answer("Pre-Sale менеджер")
    elif btn_number == "13":
        await call.message.answer_venue(
            58.00525208845205,
            56.2002500830642,
            "Адрес и геометка офиса компании:",
            "ул. Ленина, 77a"
        )
    elif btn_number == "14":
        await call.message.answer_venue(
            45.039152997105475,
            38.986183413655006,
            "Адрес и геометка офиса компании:",
            "ул. Северная, 327"
        )
    elif btn_number == "15":
        await call.message.answer_venue(
            55.713253622991715,
            37.62032107134292,
            "Адрес и геометка офиса компании:",
            "ул. Мытная, 66"
        )
    elif btn_number == "16":
        await call.message.answer(
            "Извините, но офисы нашей компании находятся только в указанных выше городах"
        )
    await call.answer()


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
