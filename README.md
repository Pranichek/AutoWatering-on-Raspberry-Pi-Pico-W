## Automatic watering 
**Учасники проєкту:** 
*TeamLead -* Грінченко Володимир 
*Учасник №1* - [Барило Михайло](https://github.com/Mbarilo). Активно приймав участь у конференціях, допомагав з вирішенням проблем та збирати онлайн-версію схему у додатку Fritzing.
*Учасник №2* - [Артем Ващенко](https://github.com/VashchenkoArtem).Це  активний учасник , який постійно заходив на зустрічі , та допомогав з рішеннями.Постійно відповідав на повідомлення , що допомогало скоріше вирішувати питання.
## Опис  проекту про автополив
Для реалізації проекту нам дали завдання розробити  автоматичний полив рослин для забезпечення автоматизованого поливу рослин за допомогою мікроконтролеру. Спочатку ми з командою вирішили розробляти автоматизовану систему поливу у офлайн-режимі, без потреби в зовнішньому зв'язку. Однак з самого початку виникла проблема з отриманням реального часу, щоб включати світло за фіксованим графіком. Тому що ми думали брати час із модулем time, aле для коректної отримки часу Raspberry Pi Pico потрібно постійне живлення від комп'ютера або ноутбука, що не було можливо з міркувань зручності — кожен день мені був необхідний ноутбук, і віддати його на кілька місяців для схеми по-перше було б не розумно,  а по-друге це дуже не зручно.
![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/photo_2024-06-26_15-48-40.jpg?raw=true)

У певний момент ми вже втратили надію і розглядали можливість використання часу в секундах, але й тут зіткнулися з труднощами. Перевага цього методу полягала у точності, але його реалізація вимагала точного налаштування часу, що виявилося незручним для режиму, актуального в Україні.У пошуках альтернативних рішень ми виявили [RTC](https://www.youtube.com/watch?v=5jylVizMTa8) (годинники реального часу), який може забезпечити точний час без постійного підключення до комп'ютера. Це відкрило нові можливості для автоматизації системи поливу і знизило вимоги до постійного живлення мікроконтролера.
![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B0%D0%B1%D0%B7%D0%B0%D1%86%D0%B0.jpg?raw=true)
Але на жаль, з'явилася проблема з тим, що через приблизно день, час на мікроконтролері перестав зберігатися правильно, що призводило до сбоїв у програмі автоматичного поливу рослин, і доводилось перезапукати схему кожень день.

У другій версії проекту було додане друге реле, та  використано мікроконтролер [Raspberry Pi Pico W](https://evo.net.ua/ru/mikrokontroller-raspberry-pi-pico-w/), що підтримує з'єднання з Інтернетом і забезпечує більш надійну і ефективну роботу системи. Окрім основної функціональності поливу, до проекту було додано можливість надсилання повідомлень про стан системи. Наприклад, система відправляє на пошту повідомлення  про включення освітлення або розпочаток поливу до мобільного пристрою користувача через спеціально налаштовані повідомлення.Але найважливіше це те, що з появою модулю вай фай, ми змогли отримувати час через NTP сервер, що дуже допомогло.![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B0%D0%B1%D0%B7%D0%B0%D1%86%D0%B0%20%281%29.jpg?raw=true)
## Користність Автополиву
Перед тим, як ми дізналися про мікроконтролери та їхні можливості в автоматизації повсякденних справ, ми вважали, що це складний і недосяжний напрямок. Однак, з розвитком нашого проекту автоматичного поливу рослин за допомогою мікроконтролеру, ми зрозуміли, які переваги вони можуть принести новачкам у цьому поляганні.Але я також вважаю що автополив значно полегшує життя людям, забезпечуючи автоматизований і регулярний полив рослин без необхідності постійного контролю. Це особливо корисно для тих, хто має городи або великі сади, де необхідно підтримувати оптимальний рівень вологості для рослин ,або для  людей які постійно подорожують у не можуть постійно наглядати за рослинами. Автополив забезпечує постійний режим поливу, що сприяє здоровому росту і кращому врожаю без потреби в постійній увазі ,крім того, система автополиву також включає освітлення за фіксованим графіком, що додатково сприяє здоровому росту рослин без потреби в постійній увазі та фізичних зусиллях.Як для нас, можна сказати що завдяки цьому проекту ми не лише зрозуміли важливість автоматизації в сільському господарстві, а й отримали цінний досвід у програмуванні мікроконтролерів та роботі у команді. Вивчення функціональних можливостей мікроконтролерів дозволило нам впровадити складні програмні рішення для управління поливом, та розуміння у подальшому розробці більш складних проектів.
