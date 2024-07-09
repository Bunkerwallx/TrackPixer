# Proyecto de Seguimiento con Envío de SMS

Este proyecto utiliza Flask para implementar un píxel de seguimiento y Twilio para enviar SMS cuando se activa el píxel.

## Requisitos

- Python 3.8+
- Flask
- Twilio
- Requests
- BeautifulSoup4
- Python-dotenv

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/tracking_project.git
    cd tracking_project
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
    ```plaintext
    LOG_FILENAME=logs/tracking.log
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    RECIPIENT_PHONE_NUMBER=recipient_phone_number
    ```

4. Ejecuta la aplicación Flask:
    ```bash
    python -m app.main
    ```

## Uso

- Visita `http://localhost:5000/tracking-pixel?user_id=123&campaign_id=456` para activar el píxel de seguimiento y enviar un SMS.
- Los registros se almacenarán en `logs/tracking.log`.


pip install -r requirements.txt
python -m app.main

http://localhost:5000/tracking-pixel?user_id=123&campaign_id=456&send_sms=true

http://localhost:5000/tracking-pixel?user_id=123&campaign_id=456&send_sms=false


POST /send-link
{
    "user_id": "123",
    "campaign_id": "456",
    "contact_method": "sms",  // o "email"
    "contact_info": "recipient_phone_number"  // o "recipient_email"
}


## Contribuciones

Si deseas contribuir, por favor abre un issue o una pull request en el repositorio.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).