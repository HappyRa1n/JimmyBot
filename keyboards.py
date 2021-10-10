from aiogram import types

# ------------------------ToComeBackToTheBeginning-----------------------------
# btn_back_begin = types.InlineKeyboardButton(text="Вернуться в начало", callback_data="btn_back")

# ------------------------------StartButtons-----------------------------------
btn_where_is_the_office = types.KeyboardButton("Где находится офис?")
bth_about_company = types.KeyboardButton("Расскажи о компании")
btn_available_vacancies = types.KeyboardButton("Расскажи о доступных вакансиях")
btn_interview = types.KeyboardButton("Хочу записаться на собеседование")
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    btn_where_is_the_office,
    bth_about_company,
    btn_available_vacancies,
    btn_interview
)

# ------------------------ButtonsForChoosingProfession--------------------------
bth_database_administrator = types.InlineKeyboardButton(text="1️⃣", callback_data="btn_1")
btn_business_architect = types.InlineKeyboardButton(text="2️⃣", callback_data="btn_2")
btn_development_team_leader = types.InlineKeyboardButton(text="3️⃣", callback_data="btn_3")
btn_personnel_evaluator = types.InlineKeyboardButton(text="4️⃣", callback_data="btn_4")
btn_system_architect = types.InlineKeyboardButton(text="5️⃣", callback_data="btn_5")
btn_devops_engineer = types.InlineKeyboardButton(text="6️⃣", callback_data="btn_6")
btn_project_manager = types.InlineKeyboardButton(text="7️⃣", callback_data="btn_7")
btn_presale_manager = types.InlineKeyboardButton(text="8️⃣", callback_data="btn_8")
vacancy_selection_keyboard = types.InlineKeyboardMarkup(row_width=4).add(
    bth_database_administrator,
    btn_business_architect,
    btn_development_team_leader,
    btn_personnel_evaluator,
    btn_system_architect,
    btn_devops_engineer,
    btn_project_manager,
    btn_presale_manager
    # btn_back_begin
)
