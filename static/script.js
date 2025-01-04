const tg = window.Telegram.WebApp;

// Telegram готов к работе
tg.ready();

// Динамически получаем chat_id
const chatId = tg.initDataUnsafe.user.id;

// Отправляем данные вместе с chat_id
document.getElementById("data-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const userData = document.getElementById("user-data").value;

    // Отправляем данные на сервер
    const response = await fetch("/send-data", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            message: userData,
            chat_id: chatId // Отправляем chat_id
        })
    });

    const result = await response.json();
    alert(result.status);
});
