import telebot
from telebot import types
import sqlite3


bot_token = '5485655874:AAGmSSSPacvPSGNG7r3CfhZC0V8RtNOTRtU'
bot = telebot.TeleBot(bot_token, parse_mode=None)

connection = sqlite3.connect('base.db', check_same_thread=False)
cursor = connection.cursor()

database = """CREATE TABLE "Log" (
	"id"	INTEGER,
	"names"	TEXT,
	"kontact" INTEGER,
	"bosilgan_tugma"  TEXT,
	"user_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT) 
);"""

try:
    cursor.execute(database)
except sqlite3.OperationalError:
    pass

def get_user(user_id):
    sql = f'select * from Log where user_id={user_id}'
    return cursor.execute(sql).fetchone()


def save_information(contact=None, names=None, pressed_btn=None, userr_id=None):
    sql = ''
    if pressed_btn:
        sql = f"""Insert into Log(user_id, bosilgan_tugma) Values({userr_id}, "{pressed_btn}")"""
    elif names:
        sql = f"""Update Log set names="{names}" where user_id={userr_id}"""
    elif contact:
        sql = f"""Update Log set kontact="{contact}" where user_id={userr_id}"""

    cursor.execute(sql)
    connection.commit()


def start_button_markup():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )
    reply_markup.row(
        telebot.types.KeyboardButton(text="📩Green Cardga ariza qoldirish")
    )
    buttons = [
        "📝Biz haqimizda",
        "🇱🇷Green Card haqida umumiy ma'lumot"
    ]
    reply_markup.add(*[
       telebot.types.KeyboardButton(text) for text in buttons
    ])
    return reply_markup


def familiy_button():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )
    reply_markup.row(
        telebot.types.KeyboardButton(text="🙍🏻‍♂️Bo'ydoq/🙍🏻‍♀️Turmushga chiqmagan")
    )
    buttons = [
        "👫Uylangan/Turmushga chiqgan",
        "💰To'lov Tizimi",
        "↩️Orqaga qaytish",
    ]
    reply_markup.add(*[
       telebot.types.KeyboardButton(text) for text in buttons
    ])
    return reply_markup



def order_markups():
    inline_buttons = [
        telebot.types.InlineKeyboardButton(
            text="Green Card haqida ma'lumot", url="https://telegra.ph/Green-Card-haqida-malumot-10-03"
        )
    ]
    reply_markup = telebot.types.InlineKeyboardMarkup(row_width=True)
    reply_markup.add(*inline_buttons)
    return reply_markup


@bot.message_handler(commands=['start'])
def start_message(message):
    user_first_name = str(message.from_user.first_name)
    bot.reply_to(message, f"🤝Assalomu alaykum! {user_first_name} \n🇺🇸Green Card 2023-yil botiga xush kelibsiz", reply_markup=start_button_markup())


def all_phone(message):
    save_information(userr_id=message.from_user.id, names=message.text)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="☎️Telefon nomer jo'natish", request_contact=True)
    keyboard.add(button_phone)
    msg3 = bot.send_message(message.chat.id, '📞Telefon nomer kiriting', reply_markup=keyboard)
    bot.register_next_step_handler(msg3, all_registration)



@bot.message_handler(func=lambda m: True)
def echo_message(message):
    if message.text == "🇱🇷Green Card haqida umumiy ma'lumot":
        text ="👉Biz bilan AMERIKAga GREEN CARD yutib oling!\n" \
               "👉Biz orqali Green Card lotareyasida ro'yxatdan o'tishingiz avfzallik tomonlari👇. \n" \
               "1️⃣-CONFIRMATION kodi o'zizga beriladi. \n" \
               "2️⃣-Shaxsiy email pochtangiz kiritiladi. \n" \
               "3️⃣-Barcha kerakli maslahatlar beriladi.\n" \
               "4️⃣-Vaqtingiz tejaladi. \n" \
               "5️⃣-Eng asosiysi bularning barchasi 4️⃣0️⃣ming so'm \n" \
               "⏰Vaqt - bu oliy ne'mat. \n" \
              "🇱🇷Hozirgi vaqtda GREEN CARDni 🔴Yashil pasport, 🔴Qizil Pasport va ⚪️Id karta orqali ham o'ynash mumkin! \n" \
               "👉Green Card haqida umumiy malumot bilan tanishish uchun pastdagi knopkani boshing👇 <a href='https://telegra.ph/Green-Card-haqida-malumot-10-03'>.</a>"
        bot.send_message(message.from_user.id, text, parse_mode='HTML', reply_markup=order_markups())

    elif message.text == "📩Green Cardga ariza qoldirish":
        text = "👨‍👩‍👦Oilaviy holatingiz"
        msg2 = bot.send_message(message.from_user.id, text, reply_markup=familiy_button())
        bot.register_next_step_handler(msg2, all_family)
    elif message.text == "📝Biz haqimizda":
        text = "👥Biz Fenix Team jamoasi \n" \
               "🟢O'z xizmatlarini: arzon narxlardagi yuqori sifatni taklif qiladi \n" \
               "Fenix team sizlarga quyidagi xizmatlarni taklif qiladi👇: \n" \
               " 💻Kompyuter xizmatlari: \n" \
               "    🔴Windows 7, vesta, 8.1, 10, 11 o'rnatish \n" \
               "    🔴Linux kali, ubuntu, mint, garuda, arch o'rnatish \n" \
               "    🔴MacOS ni  kompyuterga o'rnatish \n" \
               "    🔴Kompyuterga ikkita operatsion tizim o’rnatish \n" \
               "    🔴Formatlangan HDD, SDD, Fleshka malumotlarni qayta tiklash \n" \
               "    🔴Driver va Antiviruslar o'rnatish \n" \
               " 🔷Telegram Bot yasash \n" \
               " 🔷Taqdimot va mustaqil ishlar tayyorlab berish \n" \
               " 🇺🇸GREEN CARD da ro'yxatdan o'tkazish" \
               "$$ FENIX TEAM $$ \n" \
               "☎️Hoziroq biz bilan bog'laning va arzon va sifatli xizmatlarimizdan foydalanib qoling: \n" \
               "    💌Telegram: @djabborov_diyorbek \n" \
               "    💌Telegram: @Fenix_Team \n" \
               "    💌Telegram kanal: @Fenixteam_servis \n" \
               "    Telegram Guruh: " \
               "    📞: 9️⃣9️⃣8️⃣9️⃣1️⃣2️⃣1️⃣6️⃣8️⃣0️⃣8️⃣7️⃣ \n" \
               "    📞: 9️⃣9️⃣8️⃣9️⃣1️⃣2️⃣2️⃣3️⃣6️⃣1️⃣6️⃣3️⃣"

        bot.send_message(message.from_user.id, text)


def all_family(message):
    user = get_user(message.from_user.id)
    if user is None:
        save_information(pressed_btn=message.text, userr_id=message.from_user.id)
    if message.text == "🙍🏻‍♂️Bo'ydoq/🙍🏻‍♀️Turmushga chiqmagan":
        text = "👤Iltimos Ismingiz va Familyangizni kiriting"
        msg1 = bot.send_message(message.from_user.id, text, reply_markup=start_button_markup())
        bot.register_next_step_handler(msg1, all_phone)
    elif message.text == "👫Uylangan/Turmushga chiqgan":
        text = "👤Iltimos Ismingiz va Familyangizni kiriting"
        msg1 = bot.send_message(message.from_user.id, text, reply_markup=start_button_markup())
        bot.register_next_step_handler(msg1, all_phone)
    elif message.text == "💰To'lov Tizimi":
        text = "💳To'lov tizimiga o'tish uchun QR CODE ni skaner qiling. \n" \
               "💰Biz orqali eng arzon narxda GREEN CARD ga ro'yxatdan o'tish imkoniga egasiz. \n" \
               "    🟡Bir kishi uchun 3️⃣9️⃣0️⃣0️⃣0️⃣ so'm \n" \
               "    🟡Oilaviy 6️⃣9️⃣0️⃣0️⃣0️⃣ so'm \n" \
               "💣Bunaqasi hali bo'lmagan \n" \
               "🧨Bundan tashqari biz mijozlarimizni o'ylagan holda \n" \
               "Sizning nomingizdan kelgan va biz orqali ro'yxatdan o'tgan har bir odam uchun sizga 2️⃣0️⃣0️⃣0️⃣ so'mdan pul kartangizga qaytariladi. \n" \
               "🎉Bu shunchaki VAUUU bunaqa imkoniyatdan foydalanib qolish kerak xolos \n" \
               "👥Hoziroq do'stlaringizni taklif qiling va bizning xizmatlarimizdan foydalanib qoling." \

        ping = open("cr_code.jpg", 'rb')
        bot.send_photo(message.from_user.id, ping, text, reply_markup=start_button_markup())

    elif message.text == "↩️Orqaga qaytish":
        text = "Siz orqaga qaytdingiz"
        bot.send_message(message.from_user.id, text, reply_markup=start_button_markup())



def all_registration(message):
    home = str(message.from_user.first_name)
    try:
        save_information(contact=message.contact.phone_number, userr_id=message.from_user.id)
    except:
        save_information(contact=message.text, userr_id=message.from_user.id)
    bot.send_message(message.from_user.id, f"Siz ro'yxatga o'tdingiz biz siz bilan tez orada bog'lanamiz! \n"
                                           f"Ro'yxatdan o'tganingiz uchun tashakkur {home}",
                     reply_markup=start_button_markup())

bot.polling(none_stop=True)


