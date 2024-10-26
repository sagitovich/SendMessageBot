import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

admin_id_str = os.getenv('ADMIN_ID', '')
ADMIN_ID = list(map(int, admin_id_str.split(',')))
