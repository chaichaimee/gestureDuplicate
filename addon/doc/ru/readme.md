<!DOCTYPE html>
<html lang="ru">
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
        <p style="text-align: center;">Выявляет конфликты горячих клавиш и очищает конфигурацию NVDA.</p>
    </div>
    <br>
    <div class="section">
        <p style="text-align: center;"><b>Автор:</b> Chai Chaimee</p>
        <p style="text-align: center;"><b>URL:</b> <a href="https://github.com/chaichaimee/gestureDuplicate">https://github.com/chaichaimee/gestureDuplicate</a></p>
    </div>
    <hr>
    <div class="section">
        <h2>Описание</h2>
        <p><b>gestureDuplicate</b> — это профессиональное дополнение для NVDA, предназначенное для поддержания стабильности и эффективности вашего экранного диктора. Оно помогает выявлять конфликтующие жесты ввода (дубликаты клавиш), управлять пользовательскими назначениями и выполнять глубокую очистку остатков конфигурации от удаленных дополнений.</p>
        <p>Дополнение предоставляет три основных инструмента обслуживания:</p>
        <ul>
            <li><strong>Проверка дубликатов жестов</strong> — находит и выводит список всех дублирующихся жестов во всех контекстах (глобальные, модули приложений и т.д.).</li>
            <li><strong>Управление моими жестами</strong> — позволяет просматривать и безопасно удалять жесты, назначенные дополнениям, которые больше не установлены.</li>
            <li><strong>Очистка конфигурации (nvda.ini)</strong> — выявляет и удаляет устаревшие разделы удаленных дополнений, которые все еще хранятся в вашем основном файле <em>nvda.ini</em>.</li>
        </ul>
        <div class="note">
            <strong>Важно:</strong> Со временем после удаления дополнений в <em>nvda.ini</em> и <em>gestures.ini</em> остаются «фантомные» настройки. Это может привести к конфликтам или замедлению работы. Этот инструмент сохраняет вашу NVDA чистой и стабильной.
        </div>
    </div>
    <br>
    <div class="section">
        <h2>Горячие клавиши</h2>
        <div class="hotkey">
            <strong>Windows + Shift + G</strong><br>
            • <b>Одинарное нажатие:</b> Открыть диалог <strong>Проверка дубликатов жестов</strong><br>
            • <b>Двойное нажатие:</b> Открыть диалог <strong>Управление моими жестами</strong><br>
            • <b>Тройное нажатие:</b> Открыть диалог <strong>Очистка конфигурации</strong>
        </div>
        <br>
        <p style="padding-left: 20px;">
            <strong>Доступ через меню: Меню NVDA → Сервис → gestureDuplicate →</strong><br>
                • Проверка дубликатов жестов...<br>
                • Управление пользовательскими жестами...<br>
                • Очистка конфигурации...
        </p>
    </div>
    <br>
    <div class="section">
        <h2>Особенности</h2>
        <ul>
            <li class="feature-item"><strong>Детектор дубликатов:</strong> Сканирует все загруженные назначения (Ядро + Дополнения) для поиска конфликтов.</li>
            <li class="feature-item"><strong>Умная навигация:</strong> Переход одним кликом в стандартный диалог NVDA «Жесты ввода» с предустановленным фильтром скрипта.</li>
            <li class="feature-item"><strong>Удаление фантомных жестов:</strong> Находит записи в <em>gestures.ini</em>, связанные с отсутствующими дополнениями (выделены серым).</li>
            <li class="feature-item"><strong>Глубокая очистка nvda.ini:</strong> Сканирует основной файл настроек на наличие остатков удаленных дополнений для их безопасного удаления.</li>
            <li class="feature-item"><strong>Массовые действия:</strong> Удаление отдельных элементов или всех жестов конкретного дополнения за один раз.</li>
            <li class="feature-item"><strong>Полная доступность:</strong> Все диалоги полностью управляются с клавиатуры (Enter, Пробел, Delete, Escape).</li>
        </ul>
    </div>
    <br>
    <div class="section">
        <h2>Как очистить конфигурацию</h2>
        <ol>
            <li>Откройте инструмент <strong>Очистка конфигурации</strong> (Тройное нажатие <b>Windows+Shift+G</b>).</li>
            <li>Просмотрите список разделов, найденных в вашем <em>nvda.ini</em>.</li>
            <li>Отметьте флажками дополнения, которые вы уже удалили.</li>
            <li>Нажмите <strong>Удалить выбранное</strong> для безопасного удаления этих разделов.</li>
        </ol>
    </div>

<br><br>
<h2 style="text-align: center;">Поддержать проект</h2>
    <p style="text-align: center;">Если <b>gestureDuplicate</b> помог вам в управлении NVDA, пожалуйста, поддержите его дальнейшую разработку.</p>
    <p style="text-align: center;">
        <strong><a href="https://github.com/chaichaimee/gestureDuplicate">Посетить репозиторий на GitHub</a></strong>
    </p>
    <br>
    <p style="text-align: center; font-size: 0.8em; color: #7f8c8d;">&copy; 2026 Chai Chaimee • Лицензия GNU GPL v2+</p>
</div>
</body>
</html>