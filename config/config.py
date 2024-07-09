import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env

class Config:
    LOG_FILENAME = os.getenv('LOG_FILENAME', 'logs/tracking.log')
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
    RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER')
