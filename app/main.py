#!/usr/bin/env python
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
