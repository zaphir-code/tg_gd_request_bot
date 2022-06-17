import os

HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY')
HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
BOT_API_TOKEN = os.environ.get('BOT_API_TOKEN')

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_API_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))
