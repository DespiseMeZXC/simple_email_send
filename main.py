import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import dotenv

dotenv.load_dotenv()

def send_email(sender_email, sender_password, recipient_email, subject, body, attachments=None, 
               host="smtp.gmail.com", port=465, use_ssl=True, use_tls=False):
    """
    Функция для отправки электронных писем
    
    Параметры:
    sender_email (str): Email отправителя
    sender_password (str): Пароль от почты отправителя (или app password)
    recipient_email (str): Email получателя
    subject (str): Тема письма
    body (str): Текст письма
    attachments (list): Список путей к файлам для прикрепления (опционально)
    host (str): SMTP-сервер (по умолчанию smtp.gmail.com)
    port (int): Порт SMTP-сервера (по умолчанию 465 для SSL)
    use_ssl (bool): Использовать SSL-соединение (по умолчанию True)
    use_tls (bool): Использовать TLS-соединение (по умолчанию False)
    """
    # Создаем объект сообщения
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    
    # Добавляем текст письма
    message.attach(MIMEText(body, 'plain'))
    
    # Добавляем вложения, если они есть
    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    attachment = MIMEApplication(file.read(), Name=os.path.basename(file_path))
                    attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                    message.attach(attachment)
    
    try:
        # Подключаемся к SMTP-серверу в зависимости от настроек
        if use_ssl:
            server = smtplib.SMTP_SSL(host, port)
        else:
            server = smtplib.SMTP(host, port)
            if use_tls:
                server.starttls()  # Включаем шифрование TLS
        
        # Логинимся на сервере
        server.login(sender_email, sender_password)
        
        # Отправляем письмо
        server.send_message(message)
        
        # Закрываем соединение
        server.quit()
        
        print("Письмо успешно отправлено!")
        return True
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
        return False

# Пример использования
if __name__ == "__main__":
    # Настройки из предоставленной конфигурации
    recipient = "2003lesha2003@mail.ru"
    subject = "Тестовое письмо"
    body = "Привет! Это тестовое письмо, отправленное с помощью Python."
    
    # Отправка письма с настройками SSL
    send_email(
        sender_email=os.getenv("SENDER_EMAIL"), 
        sender_password=os.getenv("SENDER_PASSWORD"), 
        recipient_email=recipient, 
        subject=subject, 
        body=body,
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        use_ssl=os.getenv("USE_SSL"),
        use_tls=os.getenv("USE_TLS")
    )
    
    # Пример отправки письма с вложениями
    # attachments = ["path/to/file1.pdf", "path/to/file2.jpg"]
    # send_email(sender, password, recipient, subject, body)
