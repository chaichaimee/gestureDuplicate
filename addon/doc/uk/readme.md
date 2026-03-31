<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>gestureDuplicate NVDA Add-on</title>
<style>
body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background-color: #f4f4f4; }
.container { max-width: 800px; margin: auto; background: #fff; padding: 20px 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
h1, h2, h3 { text-align: center; }
b { font-weight: bold; }
.section { margin-bottom: 30px; }
.nvda-logo { display: block; margin: 0 auto 20px; width: 120px; height: auto; }
.hotkey { background: #f8f9fa; border-left: 4px solid #3498db; padding: 15px; margin: 15px 0; border-radius: 0 4px 4px 0; }
.feature-item { margin: 15px 0; padding-left: 10px; }
.note { background: #fff3cd; border-left: 4px solid #ffc107; padding: 12px; margin: 15px 0; border-radius: 0 4px 4px 0; }
a { color: #3498db; text-decoration: none; }
a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="container">
    <div class="section">
        <img src="https://www.nvaccess.org/files/nvda/documentation/userGuide/images/nvda.ico" alt="NVDA Logo" class="nvda-logo">
        <h1>gestureDuplicate</h1>
        <br>
        <p style="text-align: center;">Виявляє конфлікти гарячих клавіш та очищує конфігурацію NVDA.</p>
    </div>
    <br>
    <div class="section">
        <p style="text-align: center;"><b>Автор:</b> Chai Chaimee</p>
        <p style="text-align: center;"><b>URL:</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>
    </div>
    <hr>
    <div class="section">
        <h2>Опис</h2>
        <p><b>gestureDuplicate</b> — це професійний додаток для NVDA, розроблений для підтримки стабільності та ефективності вашого екранного читця. Він допомагає виявляти конфліктні жести введення (дублікати клавіш), керувати користувацькими призначеннями та виконувати глибоке очищення залишків конфігурації від видалених додатків.</p>
        <p>Додаток надає три основні інструменти обслуговування:</p>
        <ul>
            <li><strong>Перевірка дублікатів жестів</strong> — знаходить і виводить список усіх жестів, що дублюються, у всіх контекстах (глобальні, модулі додатків тощо).</li>
            <li><strong>Керування моїми жестами</strong> — дозволяє переглядати та безпечно видаляти жести, призначені додаткам, які більше не встановлені.</li>
            <li><strong>Очищення конфігурації (nvda.ini)</strong> — виявляє та видаляє застарілі розділи видалених додатків, які все ще зберігаються у вашому основному файлі <em>nvda.ini</em>.</li>
        </ul>
        <div class="note">
            <strong>Важливо:</strong> З часом після видалення додатків у <em>nvda.ini</em> та <em>gestures.ini</em> залишаються «фантомні» налаштування. Це може призвести до конфліктів або уповільнення роботи. Цей інструмент зберігає вашу NVDA чистою та стабільною.
        </div>
    </div>
    <br>
    <div class="section">
        <h2>Гарячі клавіші</h2>
        <div class="hotkey">
            <strong>Windows + Shift + G</strong><br>
            • <b>Одне натискання:</b> Відкрити діалог <strong>Перевірка дублікатів жестів</strong><br>
            • <b>Подвійне натискання:</b> Відкрити діалог <strong>Керування моїми жестами</strong><br>
            • <b>Потрійне натискання:</b> Відкрити діалог <strong>Очищення конфігурації</strong>
        </div>
        <br>
        <p style="padding-left: 20px;">
            <strong>Доступ через меню: Меню NVDA → Інструменти → gestureDuplicate →</strong><br>
                • Перевірка дублікатів жестів...<br>
                • Керування користувацькими жестами...<br>
                • Очищення конфігурації...
        </p>
    </div>
    <br>
    <div class="section">
        <h2>Особливості</h2>
        <ul>
            <li class="feature-item"><strong>Детектор дублікатів:</strong> Сканує всі завантажені призначення (Ядро + Додатки) для пошуку конфліктів.</li>
            <li class="feature-item"><strong>Розумна навігація:</strong> Перехід одним кліком у стандартний діалог NVDA «Жести вводу» з попередньо встановленим фільтром скрипта.</li>
            <li class="feature-item"><strong>Видалення фантомних жестів:</strong> Знаходить записи у <em>gestures.ini</em>, пов'язані з відсутніми додатками (виділені сірим).</li>
            <li class="feature-item"><strong>Глибоке очищення nvda.ini:</strong> Сканує основний файл налаштувань на наявність залишків видалених додатків для їх безпечного видалення.</li>
            <li class="feature-item"><strong>Масові дії:</strong> Видалення окремих елементів або всіх жестів конкретного додатка за один раз.</li>
            <li class="feature-item"><strong>Повна доступність:</strong> Усі діалоги повністю керуються з клавіатури (Enter, Пробіл, Delete, Escape).</li>
        </ul>
    </div>
    <br>
    <div class="section">
        <h2>Як очистити конфігурацію</h2>
        <ol>
            <li>Відкрийте інструмент <strong>Очищення конфігурації</strong> (Потрійне натискання <b>Windows+Shift+G</b>).</li>
            <li>Перегляньте список розділів, знайдених у вашому <em>nvda.ini</em>.</li>
            <li>Позначте прапорцями додатки, які ви вже видалили.</li>
            <li>Натисніть <strong>Видалити вибране</strong> для безпечного видалення цих розділів.</li>
        </ol>
    </div>

<br><br>
<h2 style="text-align: center;">Підтримати проєкт</h2>
    <p style="text-align: center;">Якщо <b>gestureDuplicate</b> допоміг вам у керуванні NVDA, будь ласка, підтримайте його подальшу розробку.</p>
    <p style="text-align: center;">
        <strong><a href="https://github.com/chaichaimee/gestureDuplicate">Відвідати репозиторій на GitHub</a></strong>
    </p>
    <br>
    <p style="text-align: center; font-size: 0.8em; color: #7f8c8d;">&copy; 2026 Chai Chaimee • Ліцензія GNU GPL v2+</p>
</div>
</body>
</html>