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
bth_database_administrator = types.InlineKeyboardButton(text="Администратор баз данных", callback_data="btn_1")
btn_business_architect = types.InlineKeyboardButton(text="Бизнес-архитектор", callback_data="btn_2")
btn_development_team_leader = types.InlineKeyboardButton(text="Руководитель группы разработки", callback_data="btn_3")
btn_personnel_evaluator = types.InlineKeyboardButton(text="Специалист по оценке персонала", callback_data="btn_4")
btn_system_architect = types.InlineKeyboardButton(text="Системный архитектор", callback_data="btn_5")
btn_devops_engineer = types.InlineKeyboardButton(text="DevOps-инженер", callback_data="btn_6")
btn_project_manager = types.InlineKeyboardButton(text="Руководитель проектов", callback_data="btn_7")
btn_presale_manager = types.InlineKeyboardButton(text="Pre-Sale менеджер", callback_data="btn_8")
vacancy_selection_keyboard = types.InlineKeyboardMarkup(row_width=1).add(
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
