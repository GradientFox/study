import telebot, os, datetime, json
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message


TOKEN = os.getenv("TOKEN", False)
if not TOKEN:
    print("Добавьте ключ в переменные окружения.")
    exit(0)
_DT_DISPLAY = "%d.%m.%Y %H:%M:%S"
bot = telebot.TeleBot(TOKEN)
LAST_COMMAND = []
if os.path.exists("data.json"):
    with open("data.json", "r", encoding="utf-8") as f:
        DB = json.load(f)
else:
    DB = {}

def get_commands() -> str:
    return """Список команд:
/sleep - включить таймер сна
/wake - завершить сон
/quality - поставить оценку качеству последнего сна
/notes - сделать заметку для последнего сна
/avg - среднее время сна за все время
/avg_week - среднее время сна за неделю
/check {ДД.ММ.ГГГГ} - узнать информацию по сну за определенную дату"""

def write_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

@bot.message_handler(commands=["start"])
def start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        KeyboardButton("/sleep"),
        KeyboardButton("/wake"),
    ]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id,
f"Привет! Я умею отслеживать время твоего сна.\n{get_commands()}", reply_markup=keyboard)

@bot.message_handler(commands=["help"])
def help(message: Message):
    bot.send_message(message.chat.id, get_commands())


def is_sleeping(user_id):
    if user_id in DB.keys():
        return len(DB[user_id]) > 0 and DB[user_id][-1]["duration"] == 0
    return False


@bot.message_handler(commands=["sleep"])
def go_sleep(message: Message):
    user_id = str(message.from_user.id)
    if not user_id in DB.keys():
        DB[user_id] = list()
    if is_sleeping(user_id):
        bot.send_message(message.chat.id,
                         "Ранее вы уже использовали команду /sleep, пожалуйста, отправьте команду /wake")
        return
    sleep_info = {
        "start_time": datetime.datetime.now().strftime(_DT_DISPLAY),
        "duration": 0,
        "quality": "",
        "notes": ""
    }
    DB[user_id].append(sleep_info)
    bot.send_message(message.chat.id, "Хорошего сна! Как только проснешься напиши /wake.")


@bot.message_handler(commands=["wake"])
def waking(message: Message):
    user_id = str(message.from_user.id)
    if not is_sleeping(user_id):
        bot.send_message(message.chat.id,
                         """Чтобы воспользоваться командой пробуждения /wake,
тебе необходимо сообщить о том, что ты пошел спать /sleep.""")
        return
    time = datetime.datetime.now()
    start_time = datetime.datetime.strptime(DB[user_id][-1]["start_time"], _DT_DISPLAY)
    delta = time - start_time
    hours = round(delta.total_seconds() / 1, 2)
    DB[user_id][-1]["duration"] = hours
    write_json(DB, "data.json")
    bot.send_message(message.chat.id,
                     f"Твой сон длился {hours}. Можешь дать оценку /quality, и добавить заметку /notes.")


@bot.message_handler(commands=["quality"])
def quality(message: Message):
    user_id = str(message.from_user.id)
    if is_sleeping(user_id):
        bot.send_message(message.chat.id, "Для оценки вы должны проснуться /wake")
        return
    global LAST_COMMAND
    LAST_COMMAND = "quality"
    bot.send_message(message.chat.id, "Напишите оценку:")


@bot.message_handler(commands=["notes"])
def notes(message: Message):
    user_id = str(message.from_user.id)
    if is_sleeping(user_id):
        bot.send_message(message.chat.id, "Для заметки вы должны проснуться /wake")
        return
    global LAST_COMMAND
    LAST_COMMAND = "notes"
    bot.send_message(message.chat.id, "Напишите заметку:")


@bot.message_handler(commands=["avg"])
def avg_time(message: Message):
    user_id = str(message.from_user.id)
    if len(DB[user_id]) == 0:
        bot.send_message(message.chat.id, "У меня нет информации о вашем сне, воспользуйтесь командой /sleep")
        return
    if is_sleeping(user_id):
        bot.send_message(message.chat.id, "Для суммирования вы должны проснуться /wake")
        return
    summary_time = 0
    for value in DB[user_id]:
        summary_time += value["duration"]
    avg = round(summary_time / len(DB[user_id]), 2)
    print(DB)
    bot.send_message(message.chat.id, f"Среднее время сна: {avg}")


@bot.message_handler(commands=["avg_week"])
def avg_week_time(message: Message):
    user_id = str(message.from_user.id)
    if len(DB[user_id]) == 0:
        bot.send_message(message.chat.id, "У меня нет информации о вашем сне, воспользуйтесь командой /sleep")
        return
    if is_sleeping(user_id):
        bot.send_message(message.chat.id, "Для суммирования вы должны проснуться /wake")
        return
    summary_time = 0
    last_num = len(DB[user_id])
    rng = [i for i in range(last_num - 7, last_num) if i >= 0]
    for i in rng:
        summary_time += DB[user_id][i]["duration"]
    avg = round(summary_time / len(rng), 1)
    bot.send_message(message.chat.id, f"Среднее время сна за неделю: {avg}")


@bot.message_handler(commands=["check"])
def get_info(message: Message):
    user_id = str(message.from_user.id)
    if len(DB[user_id]) == 0:
        bot.send_message(message.chat.id, "У меня нет информации о вашем сне, воспользуйтесь командой /sleep")
        return
    if is_sleeping(user_id):
        bot.send_message(message.chat.id, "Для проверки вы должны проснуться /wake")
        return
    try:
        info = []
        date = message.text.split()[-1]
        day, month, year = map(int, date.split('.'))
        date = datetime.date(year, month, day)
        for value in DB[user_id]:
            checking_date = datetime.datetime.strptime(value["start_time"], _DT_DISPLAY)
            if checking_date.date() == date:
                info.append(value)
        response = '\n'.join([
f'''- {value["start_time"]}
    Сон: {value["duration"]}
    Оценка: {value["quality"] if value["quality"] != "" else "не указана"}
    Заметка: {value["notes"] if value["notes"] != "" else "не указана"}'''
            for value in info])
        bot.send_message(message.chat.id, f"Информацию по дате:\n{response}")
    except Exception:
        bot.send_message(message.chat.id, "Неверный формат даты")


@bot.message_handler(content_types=["text"])
def non_command(message: Message):
    user_id = str(message.from_user.id)
    global LAST_COMMAND
    if LAST_COMMAND == "notes":
        try:
            DB[user_id][-1]["notes"] = message.text
            write_json(DB, "data.json")
            bot.send_message(message.chat.id, "Заметка добавлена.")
        except Exception:
            bot.send_message(message.chat.id, "Сейчас нельзя добавить заметку.")
    elif LAST_COMMAND == "quality":
        try:
            DB[user_id][-1]["quality"] = message.text
            write_json(DB, "data.json")
            bot.send_message(message.chat.id, "Оценку сна зафиксировал.")
        except Exception:
            bot.send_message(message.chat.id, "Сейчас нельзя дать оценку.")
    else:
        bot.send_message(message.chat.id, "Воспользуйся командами /sleep или /wake.")
    LAST_COMMAND = ""


bot.polling(non_stop=True, interval=0)