import requests

BOT_TOKEN = "7896861090:AAE_KmXaUjib9KrDJ2ESivy8TWmw8xH5T_o"  
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

# Функция для отправки сообщения от имени бота
def send_message(chat_id, text):
    url = TELEGRAM_API_URL + "sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.json()

# Пример использования: отправляем сообщение пользователю
if __name__ == "__main__":
    chat_id = "123456789"  # Вставь сюда ID чата пользователя
    text = "Привет! Это сообщение от бота."
    result = send_message(chat_id, text)
    print(result)
