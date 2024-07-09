


from flask import request, send_file, abort, url_for
import logging
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
from app import app

# Configurar el logger
log_filename = os.getenv('LOG_FILENAME', 'logs/tracking.log')
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

# ConfiguraciÃ³n de Twilio
twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(twilio_account_sid, twilio_auth_token)

# ConfiguraciÃ³n de correo electrÃ³nico
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT', 587))
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')
from_email = os.getenv('FROM_EMAIL')

def send_sms(user_id, campaign_id, link, recipient_phone_number):
    message_body = f"Click the link to track: {link}"
    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        logging.info(f"SMS sent: {message.sid}")
    except Exception as e:
        logging.error(f"Error sending SMS: {e}")

def send_email(user_id, campaign_id, link, recipient_email):
    message_body = f"Click the link to track: {link}"
    msg = MIMEText(message_body)
    msg['Subject'] = f'Tracking Link for Campaign {campaign_id}'
    msg['From'] = from_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, [recipient_email], msg.as_string())
        logging.info(f"Email sent to {recipient_email}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

@app.route('/send-link', methods=['POST'])
def send_link():
    user_id = request.form.get('user_id')
    campaign_id = request.form.get('campaign_id')
    contact_method = request.form.get('contact_method')  # 'email' or 'sms'
    contact_info = request.form.get('contact_info')

    if not user_id or not campaign_id or not contact_method or not contact_info:
        abort(400, description="Missing required parameters")

    # Generar enlace de seguimiento
    tracking_link = url_for('tracking_pixel', user_id=user_id, campaign_id=campaign_id, _external=True)

    if contact_method == 'sms':
        send_sms(user_id, campaign_id, tracking_link, contact_info)
    elif contact_method == 'email':
        send_email(user_id, campaign_id, tracking_link, contact_info)
    else:
        abort(400, description="Invalid contact method")

    return "Link sent successfully", 200

@app.route('/tracking-pixel')
def tracking_pixel():
    user_id = request.args.get('user_id')
    campaign_id = request.args.get('campaign_id')
    if not user_id or not campaign_id:
        abort(400, description="Missing required parameters: user_id or campaign_id")

    # Detalles de la solicitud
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    referer = request.headers.get('Referer', 'Unknown')

    # Registro de la actividad
    logging.info(f"User ID: {user_id}, Campaign ID: {campaign_id}, IP: {ip}, User-Agent: {user_agent}, Referer: {referer}")

    # Enviar una imagen de 1x1 pÃ­xel
    try:
        return send_file('static/pixel.png', mimetype='image/png')
    except FileNotFoundError:
        abort(404, description="Pixel image not found")

if __name__ == '__main__':
    app.run()#!/usr/bin/env python
## 
##
##
#
#
#  Se cargan las bibliotecas python

from flask import requests, send_file, about, url_for
import loggin
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMETEXT
from twilio.rest import Client
from app import app


# Se realiza la configuracion de logger

log_filename = os.getenv('LOG_FILENAME', 'logs/trackimg.log')
logging.basicConfig(filename=log_filename, level=logging.INFO, format)
