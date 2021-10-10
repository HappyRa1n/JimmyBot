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


@dp.message_handler(text=["Где находится офис?",
                          "Расскажи о компании",
                          "Расскажи о доступных вакансиях",
                          "Хочу записаться на собеседование"])
async def handling(message: types.Message):
    if message.text == "Где находится офис?":
        await message.answer(
            "Адрес офиса в Перми : ул. Ленина, 77a"
        )
    elif message.text == "Расскажи о компании":
        await message.answer(
            "Группа компаний <b>PARMA Technologies Group</b> основана в 2016 году. "
            "Главным направлением деятельности является разработка заказного программного обеспечения.\n\n "
            "У нас собрана профессиональная команда, чей опыт работы на рынке информационных технологий составляет"
            "более 12 лет. Решениями, разработанными нашими специалистами, пользуются многие федеральные,"
            "региональные и муниципальные органы государственной власти.\n\n "
            'Подробности по <a href="https://www.parma.ru/">ссылке</a>',
            disable_web_page_preview=True
        )
    elif message.text == "Расскажи о доступных вакансиях":
        await message.answer(
            "О какой вакансии ты бы хотел узнать?\n"
            "1 - Администратор баз данных\n"
            "2 - Бизнес-архитектор\n"
            "3 - Руководитель группы разработки\n"
            "4 - Специалист по оценке персонала\n"
            "5 - Системный архитектор\n"
            "6 - DevOps-инженер\n"
            "7 - Руководитель проектов\n"
            "8 - Pre-Sale менеджер\n",
            reply_markup=kb.vacancy_selection_keyboard
        )
    else:
        await message.answer(
            "Отправьте своё резюме в этот чат, мы рассмотрим Вашу заявку и свяжемся с вами"
        )


@dp.callback_query_handler(text_startswith="btn_")
async def callbacks_num(call: types.CallbackQuery):
    vacancy_num = call.data.split("_")[1]
    if vacancy_num == "1":
        await call.message.answer("Администратор баз данных")
    elif vacancy_num == "2":
        await call.message.answer("Бизнес-архитектор")
    elif vacancy_num == "3":
        await call.message.answer("Руководитель группы разработки")
    elif vacancy_num == "4":
        await call.message.answer("Специалист по оценке персонала")
    elif vacancy_num == "5":
        await call.message.answer("Системный архитектор")
    elif vacancy_num == "6":
        await call.message.answer("DevOps-инженер")
    elif vacancy_num == "7":
        await call.message.answer("Руководитель проектов")
    elif vacancy_num == "8":
        await call.message.answer("Pre-Sale менеджер")
    await call.answer()


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
