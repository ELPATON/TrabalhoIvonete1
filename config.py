import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('SUPABASE_URL')
KEY = os.getenv('SUPABASE_KEY')

HEADERS = {
    'apikey': KEY,
    'Authorization': f'Bearer {KEY}',
    'Content-Type': 'application/json'
}