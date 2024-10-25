import telebot
from telebot import types
import os

bot = telebot.TeleBot('7898992706:AAF5Dp9QPM4-0yDfAikv3Yxg06Iv66KorSU')
photo_folder = os.path.abspath('E:\\telega_bot\\bot_bot\\photoCringe')

# В список дописывать id пользователей
allowed_ids = [959633736, #Андрей
                751997349,
                5690909942,
                998654872,
                826468586
               ]  # Замените на реальные ID

# Словарь для хранения фотографий пользователей
saved_photos = {}

@bot.message_handler(commands=['start', 'START', 'info', 'INFO', 'help'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton('more info', callback_data='inf')
    user_id = message.chat.id
    if user_id not in allowed_ids:
        btn1 = types.InlineKeyboardButton('ID', callback_data='ID')
        markup.add(btn1, btn2)
    else: markup.add(btn2)
    bot.send_message(message.chat.id,
                'Нажмите на <b>ID</b>, чтобы получить свой уникальный <b>ID</b> для дальнейшего использования бота',
                     parse_mode='html',
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_ID(callback):
    if callback.data == 'ID':
        bot.send_message(callback.message.chat.id, f'Ваш ID: {callback.message.chat.id}')
    elif callback.data == 'inf':
        bot.send_message(callback.message.chat.id,
                    f'Этот бот создан для совместной разработки группой <i>БПИЭ-221, ВГТУ, ВОРОНЕЖ, 2024г</i>\n'
                        f'<b>Цель бота</b> - определить студента из группы по фотографии и вывести его имя/фамилию',
                         parse_mode='html')


# Обработчик для фотографий
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.chat.id
    if user_id in allowed_ids:
        # Получаем фотографию с наибольшим размером
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Сохраняем фотографию в словарь с ключом user_id
        saved_photos[user_id] = downloaded_file

        # Сохраняем фотографию на диск
        photo_path = os.path.join(photo_folder, f'photo_{user_id}.jpg')
        with open(photo_path, 'wb') as photo_file:
            photo_file.write(downloaded_file)

        bot.send_message(user_id, 'Фотография успешно сохранена.')
    else:
        bot.send_message(user_id, 'У вас нет доступа к отправке фотографий.')



# Обработчик для фотографий
# @bot.message_handler(content_types=['photo'])
# def handle_photo(message):
#     user_id = message.chat.id
#     if user_id in allowed_ids:
#         # Получаем фотографию с наибольшим размером
#         file_id = message.photo[-1].file_id
#         file_info = bot.get_file(file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#
#         # Сохраняем фотографию в словарь с ключом user_id
#         saved_photos[user_id] = downloaded_file
#
#         bot.send_message(user_id, 'Фотография успешно сохранена.')
#     else:
#         bot.send_message(user_id, 'У вас нет доступа к отправке фотографий.')

# Команда для отправки сохраненной фотографии
@bot.message_handler(commands=['testSend'])
def send_photo(message):
    user_id = message.chat.id
    if user_id in allowed_ids:
        if user_id in saved_photos:
            # Отправляем сохраненную фотографию
            bot.send_photo(user_id, saved_photos[user_id])
        else:
            bot.send_message(user_id, 'У вас нет сохраненных фотографий.')
    else:
        bot.send_message(user_id, 'У вас нет доступа к этой команде.')

bot.polling(none_stop=True)

# @bot.message_handler(content_types=['photo'])
# def ger_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     # Создаем кнопки
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.google.com/')
#     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     # Добавляем первую кнопку отдельно
#     markup.add(btn1)
#     # Добавляем две последние кнопки в одну строку
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Какое некрасивое фото!', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete' :
#         bot.delete_message(
#             callback.message.chat.id,
#             callback.message.message_id - 1
#         )
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text',
#             callback.message.chat.id,
#             callback.message.message_id
#             )




#
# @bot.message_handler(commands=['site'])
# def site(message):
#     webbrowser.open('https://discord.ru')
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, message.from_user.first_name + ' ' + message.from_user.last_name)
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')
#     else: bot.reply_to(message, 'ИДИ ОТСЮДА, ТУТ ЕЩЁ ДЕЛАЕТСЯ ВСЁ!!!')
#




# @bot.message_handler(commands=['site'])
# def site(message):
#     webbrowser.open('https://discord.ru')

# @bot.message_handler(commands=['start', 'main', 'hello'])
# def main(message):
#     bot.send_message(message.chat.id, message.from_user.first_name + ' ДАРОУ')
#
# @bot.message_handler(commands=['face'])
# def main(message):
#     bot.send_message(message.chat.id, message)
#
#
# @bot.message_handler(commands=['info'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>info information</b>', parse_mode='html')
