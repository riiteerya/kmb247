import telebot
import datetime
import time
import os
import subprocess
import psutil
import sqlite3
import hashlib
import requests
import sys
import socket
import zipfile
import io
import re
import threading
from google_authenticator import GoogleAuthenticator
import speedtest
import types
import pyshorteners
import logging

# Thiết lập cấp độ log và định dạng
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Tạo một đối tượng logger cho bot của bạn
logger = logging.getLogger(__name__)

# Bắt đầu log khi bot được khởi động
logger.info('Bot started successfully.')

bot_token = '6870197479:AAElHTqilYCe7aVIGY881kAbTDll35bBD9A'

bot = telebot.TeleBot(bot_token)
IMGUR_CLIENT_ID = '74f5c858f447bb9'
SHORTENER = pyshorteners.Shortener()

allowed_group_id = -1002042041196

allowed_users = []
processes = []
ADMIN_ID = 6670870530
GROUP_ID = '-4112260455'  # Thay YOUR_GROUP_ID bằng ID của nhóm Telegram bạn muốn thông báo
proxy_update_count = 0
last_proxy_update_time = time.time()
key_dict = {}
cooldown_dict = {}  # Khai báo cooldown_dict ở đây

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT
    )
''')
connection.commit()


def TimeStamp():
  now = str(datetime.date.today())
  return now


def load_users_from_database():
  cursor.execute('SELECT user_id, expiration_time FROM users')
  rows = cursor.fetchall()
  for row in rows:
    user_id = row[0]
    expiration_time = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
    if expiration_time > datetime.datetime.now():
      allowed_users.append(user_id)


def save_user_to_database(connection, user_id, expiration_time):
  cursor = connection.cursor()
  cursor.execute(
      '''
        INSERT OR REPLACE INTO users (user_id, expiration_time)
        VALUES (?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
  connection.commit()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Log khi nhận được một tin nhắn mới
    logger.info(f"Received message: {message.text}")

    # Xử lý tin nhắn như bình thường
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['add'])
def add_user(message):
  admin_id = message.from_user.id
  if admin_id != ADMIN_ID:
    bot.reply_to(message, 'Chi Dành Cho Admin')
    return

  if len(message.text.split()) == 1:
    bot.reply_to(message, 'Nhập Đúng Định Dạng /add + [id]')
    return

  user_id = int(message.text.split()[1])
  allowed_users.append(user_id)
  expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
  connection = sqlite3.connect('user_data.db')
  save_user_to_database(connection, user_id, expiration_time)
  connection.close()

  bot.reply_to(message,
               f'Đã Thêm Người Dùng Có ID Là: {user_id} Sử Dụng Lệnh 30 Ngày')


load_users_from_database()


@bot.message_handler(commands=['getkey'])
def laykey(message):
  bot.reply_to(message, text='Vui Lòng Chờ...')

  with open('key.txt', 'a') as f:
    f.close()

  username = message.from_user.username
  string = f'GL-{username}+{TimeStamp()}'
  hash_object = hashlib.md5(string.encode())
  key = str(hash_object.hexdigest())
  print(key)

  url_key = requests.get(
      f'https://link4m.co/api-shorten/v2?api=64d28035727d3b3e1b7410c3&url=https://card1s.store/key?key!{key}'
  ).json()['shortenedUrl']

  text = f'''
- Cảm Ơn Bạn Đã Getkey -
- Link Lấy Key Hôm Nay Là: {url_key}
- KEY CỦA BẠN {TimeStamp()} LÀ: {key}
- DÙNG LỆNH /key {{key}} ĐỂ TIẾP TỤC
 [Lưu ý: mỗi key chỉ có 1 người dùng]
    '''
  bot.reply_to(message, text)


@bot.message_handler(commands=['key'])
def key(message):
  if len(message.text.split()) == 1:
    bot.reply_to(
        message,
        'Vui Lòng Nhập Key\nVí Dụ /key Khangkmb247\nSử Dụng Lệnh /getkey Để Lấy Key'
    )
    return

  user_id = message.from_user.id

  key = message.text.split()[1]
  username = message.from_user.username
  string = f'GL-{username}+{TimeStamp()}'
  hash_object = hashlib.md5(string.encode())
  expected_key = str(hash_object.hexdigest())
  if key == expected_key:
    allowed_users.append(user_id)
    bot.reply_to(message, 'Nhập Key Thành Công')
  else:
    bot.reply_to(message,
                 'Key Sai Hoặc Hết Hạn\nKhông Sử Dụng Key Của Người Khác!')


@bot.message_handler(commands=['start', 'help'])
def help(message):
  help_text = '''
🌐 Tất Cả Các Lệnh:
1️⃣ Lệnh Lấy Key Và Nhập Key
- /getkey : Để lấy key
- /key + [Key] : Kích Hoạt Key
2️⃣ Lệnh Spam 
- /sms + [Số Điện Thoại]
3️⃣ Lệnh Tiện ích
- /time : Số Thời Gian Bot Hoạt Động
- /2fa + [Mã 2FA] : Lấy mã 2FA
- /code + [link website]
- /anh : Tải ảnh lấy link
4️⃣ Info Admin
- /admin : Info Admin
- /on : On Bot
- /off : Off Bot
'''
  bot.reply_to(message, help_text)


is_bot_active = True


@bot.message_handler(commands=['sms'])
def attack_command(message):
  user_id = message.from_user.id

  if not is_bot_active:
    bot.reply_to(message,
                 'Bot hiện đang tắt. Vui lòng chờ khi nào được bật lại.')
    return

  if user_id not in allowed_users:
    bot.reply_to(message,
                 text='Vui lòng nhập Key\nSử dụng lệnh /getkey để lấy Key')
    return

  if len(message.text.split()) != 3:
    bot.reply_to(message,
                 'Sử dụng lệnh theo định dạng: /sms {số điện thoại} {số lần}')
    return

  phone_number = message.text.split()[1]
  lap = message.text.split()[2]

  if not re.search(
      "^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",
      phone_number):
    bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
    return

  blocked_numbers = ['113', '114', '115', '198', '911', '0376349783']
  if phone_number in blocked_numbers:
    bot.reply_to(message, 'Bạn không được spam số này.')
    return

  cooldown_dict[user_id] = time.time()

  username = message.from_user.username

  bot.reply_to(
      message,
      f'┏━━━━━━━━━━━━━━┓\n┃   Spam Thành Công!!!\n┗━━━━━━━━━━━━━━➤\n┏━━━━━━━━━━━━━━┓\n┣➤ Attack By: @{username} \n┣➤ Số Tấn Công: {phone_number} \n┣➤ Group: t.me/+1CsguhMAhl8yMGRl \n┗━━━━━━━━━━━━━━➤'
  )

  # Chạy file newsms.py sử dụng subprocess
  file_path = os.path.join(os.getcwd(), "newsms.py")
  process = subprocess.Popen(["python", file_path, phone_number, lap])
  processes.append(process)
  # Gửi thông báo vào nhóm
  bot.send_message(
      GROUP_ID,
      f'🔰👮Người dùng @{message.from_user.username} đã thực hiện lệnh /spam \n🔰Số điện thoại {phone_number} \n❌Lặp lại {lap} lần.'
  )
  bot.reply_to(
      message,
      f'┏━━━━━━━━━━━━━━┓\n┃   Spam Thành Công!!!\n┗━━━━━━━━━━━━━━➤\n┏━━━━━━━━━━━━━━┓\n┣➤ Attack By: @{username} \n┣➤ Số Tấn Công: {phone_number} \n┣➤ Group: t.me/+1CsguhMAhl8yMGRl \n┗━━━━━━━━━━━━━━➤'
  )


@bot.message_handler(commands=['off'])
def turn_off(message):
  user_id = message.from_user.id
  if user_id != ADMIN_ID:
    bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
    return

  global is_bot_active
  is_bot_active = False
  bot.reply_to(
      message,
      'Bot đã được tắt. Tất cả người dùng không thể sử dụng lệnh khác.')


@bot.message_handler(commands=['on'])
def turn_on(message):
  user_id = message.from_user.id
  if user_id != ADMIN_ID:
    bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
    return

  global is_bot_active
  is_bot_active = True
  bot.reply_to(
      message,
      'Bot đã được khởi động lại. Tất cả người dùng có thể sử dụng lại lệnh bình thường.'
  )


is_bot_active = True
# Hàm tính thời gian hoạt động của bot
start_time = time.time()

proxy_update_count = 0
proxy_update_interval = 600


@bot.message_handler(commands=['time'])
def show_uptime(message):
  current_time = time.time()
  uptime = current_time - start_time
  hours = int(uptime // 3600)
  minutes = int((uptime % 3600) // 60)
  seconds = int(uptime % 60)
  uptime_str = f'{hours} giờ, {minutes} phút, {seconds} giây'
  bot.reply_to(message, f'Bot Đã Hoạt Động Được: {uptime_str}')


@bot.message_handler(commands=['2fa'])
def handle_2fa(message):
  try:
    # Lấy text sau lệnh /2fa và loại bỏ khoảng trắng
    args = message.text.split()[1:]
    if not args:
      bot.reply_to(message,
                   'Vui lòng gửi lệnh theo định dạng: /2fa <mã_bí_mật>')
      return

    # Gộp các phần tử trong args thành một chuỗi mã bí mật
    secret = ''.join(args).upper()  # Chuyển đổi mã bí mật thành chữ hoa
    ga = GoogleAuthenticator()
    code = ga.get_code(secret)
    bot.reply_to(message, f'Mã 2FA của bạn là: {code}')
  except Exception as e:
    bot.reply_to(
        message,
        'Đã có lỗi xảy ra khi tạo mã 2FA. Vui lòng kiểm tra mã bí mật và thử lại.'
    )


@bot.message_handler(commands=['code'])
def code(message):
  user_id = message.from_user.id
  if not is_bot_active:
    bot.reply_to(message,
                 'Bot hiện đang tắt. Vui lòng chờ khi nào được bật lại.')
    return

  if user_id not in allowed_users:
    bot.reply_to(message,
                 text='Vui lòng nhập Key\nSử dụng lệnh /getkey để lấy Key')
    return
  if len(message.text.split()) != 2:
    bot.reply_to(message,
                 'Vui lòng nhập đúng cú pháp.\nVí dụ: /code + [link website]')
    return

  url = message.text.split()[1]

  try:
    response = requests.get(url)
    if response.status_code != 200:
      bot.reply_to(
          message,
          'Không thể lấy mã nguồn từ trang web này. Vui lòng kiểm tra lại URL.'
      )
      return

    content_type = response.headers.get('content-type', '').split(';')[0]
    if content_type not in ['text/html', 'application/x-php', 'text/plain']:
      bot.reply_to(
          message,
          'Trang web không phải là HTML hoặc PHP. Vui lòng thử với URL trang web chứa file HTML hoặc PHP.'
      )
      return

    source_code = response.text

    zip_file = io.BytesIO()
    with zipfile.ZipFile(zip_file, 'w') as zipf:
      zipf.writestr("source_code.txt", source_code)

    zip_file.seek(0)
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_document(message.chat.id, zip_file)

  except Exception as e:
    bot.reply_to(message, f'Có lỗi xảy ra: {str(e)}')


@bot.message_handler(commands=['admin'])
def help(message):
  help_text = '''
👉 Telegram : @Khangmb247
👉 Zalo : zalo.me/khangmbb
👉 Link nhóm : t.me/+1CsguhMAhl8yMGRl
👉 Kênh list : https://t.me/liststkmbbank
'''
  bot.reply_to(message, help_text)


is_bot_active = True

# Dictionary để lưu trạng thái yêu cầu ảnh cho mỗi người dùng
requesting_photo = {}


@bot.message_handler(commands=['anh'])
def request_photo(message):
  # Kiểm tra xem người gửi đã được yêu cầu gửi ảnh chưa
  if message.chat.type == "private" or message.chat.type == "supergroup":
    # Nếu là chat riêng hoặc nhóm, gửi yêu cầu gửi ảnh
    bot.reply_to(message, "Gửi ảnh bạn muốn tải lên lấy link.")
    # Đặt trạng thái yêu cầu ảnh cho người dùng
    requesting_photo[message.from_user.id] = True
  else:
    bot.reply_to(message, "Gửi lệnh /anh trong chat riêng hoặc nhóm với bot.")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
  try:
    # Kiểm tra xem người gửi đã được yêu cầu gửi ảnh chưa
    if message.from_user.id in requesting_photo and requesting_photo[
        message.from_user.id]:
      # Đánh dấu là không yêu cầu nữa
      requesting_photo[message.from_user.id] = False

      # Lấy thông tin ảnh và tải lên, sau đó gửi lại link
      file_info = bot.get_file(message.photo[-1].file_id)
      file = requests.get(
          f'https://api.telegram.org/file/bot{bot_token}/{file_info.file_path}',
          stream=True)

      headers = {'Authorization': f'Client-ID {IMGUR_CLIENT_ID}'}
      response = requests.post("https://api.imgur.com/3/image",
                               files={"image": file.content},
                               headers=headers)
      response_data = response.json()

      if response_data['success']:
        imgur_url = response_data['data']['link']
        short_url = SHORTENER.tinyurl.short(imgur_url)
        bot.reply_to(message, f'Đường link của ảnh: {short_url}')

        # Gửi tin nhắn với link ảnh vào nhóm
        bot.send_message(
            GROUP_ID,
            f'Link ảnh từ {message.from_user.first_name} (@{message.from_user.username}): {short_url}'
        )
      else:
        bot.reply_to(message, "Có lỗi xảy ra khi tải ảnh lên.")
    else:
      bot.reply_to(
          message,
          "Bạn không được yêu cầu gửi ảnh. Sử dụng lệnh /anh trong chat riêng hoặc nhóm với bot."
      )

  except Exception as e:
    bot.reply_to(message, f'Có lỗi xảy ra: {e}')


@bot.message_handler(func=lambda message: message.text.startswith('/'))
def invalid_command(message):
  bot.reply_to(
      message,
      'Lệnh không hợp lệ. Vui lòng sử dụng lệnh /help để xem danh sách lệnh.')


bot.infinity_polling(timeout=60, long_polling_timeout=1)
