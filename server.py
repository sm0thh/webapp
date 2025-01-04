from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "7896861090:AAE_KmXaUjib9KrDJ2ESivy8TWmw8xH5T_o"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

# Роут для обработки данных от мини-приложения
@app.route("/send-data", methods=["POST"])
def send_data():
    data = request.json
    user_message = data.get("message", "")
    chat_id = data.get("chat_id")  # Получаем chat_id из запроса

    # Отправляем сообщение боту
    url = TELEGRAM_API_URL + "sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"Новое сообщение: {user_message}"
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return jsonify({"status": "Сообщение отправлено"})
    else:
        return jsonify({"status": "Ошибка при отправке"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
