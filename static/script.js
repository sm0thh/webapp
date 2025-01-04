// Получение данных о пользователе
const tg = window.Telegram.WebApp;

// Отображение имени пользователя
tg.ready();
document.getElementById('username').innerText = `Привет, ${tg.initDataUnsafe.user.first_name}!`;

// Функция для закрытия мини-приложения
function closeWebApp() {
    tg.close();
}

