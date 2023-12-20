from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("6030387829:AAFdS9zioQCjs4N190eaELV316t_XKby1cE")  # Bot toekn
# ADMINS = env.list("2033651030")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

BOT_TOKEN = "6030387829:AAFdS9zioQCjs4N190eaELV316t_XKby1cE"
ADMINS = ["2033651030"]

DATABASE = {
    'NAME': 'evos_bot',
    'USER': 'postgres',
    'PASSWORD': '2928',
    'HOST': 'localhost',
    'PORT': '5433',
}