## Automatic watering 
**Учасники проєкту:** 


*TeamLead -* Грінченко Володимир 


*Учасник №1* - [Барило Михайло](https://github.com/Mbarilo). Активно приймав участь у конференціях, допомагав з вирішенням проблем та збирати онлайн-версію схему у додатку Fritzing.


*Учасник №2* - [Артем Ващенко](https://github.com/VashchenkoArtem).Це  активний учасник , який постійно заходив на зустрічі , та допомогав з рішеннями.Постійно відповідав на повідомлення , що допомогало скоріше вирішувати питання.
## Опис  проекту про автополив
Для реалізації проекту нам дали завдання розробити  автоматичний полив рослин для забезпечення автоматизованого поливу рослин за допомогою мікроконтролеру. Спочатку ми з командою вирішили розробляти автоматизовану систему поливу у офлайн-режимі, без потреби в зовнішньому зв'язку. Однак з самого початку виникла проблема з отриманням реального часу, щоб включати світло за фіксованим графіком. Тому що ми думали брати час із модулем time, aле для коректної отримки часу Raspberry Pi Pico потрібно постійне живлення від комп'ютера або ноутбука, що не було можливо з міркувань зручності — кожен день мені був необхідний ноутбук, і віддати його на кілька місяців для схеми по-перше було б не розумно,  а по-друге це дуже не зручно.
![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/photo_2024-06-26_15-48-40.jpg?raw=true)

У певний момент ми розглядали можливість використання часу в секундах, але й тут зіткнулися з труднощами. Перевага цього методу полягала у точності, але його реалізація вимагала точного налаштування часу, що виявилося незручним для режиму, актуального в Україні.У пошуках альтернативних рішень ми виявили [RTC](https://www.youtube.com/watch?v=5jylVizMTa8) (годинники реального часу), який може забезпечити точний час без постійного підключення до комп'ютера. Це відкрило нові можливості для автоматизації системи поливу і знизило вимоги до постійного живлення мікроконтролера.
![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B0%D0%B1%D0%B7%D0%B0%D1%86%D0%B0.jpg?raw=true)
Але  з'явилася проблема з тим, що через приблизно день, час на мікроконтролері перестав зберігатися правильно, що призводило до сбоїв у програмі автоматичного поливу рослин, і доводилось перезапукати схему кожень день.

У останній версії проекту було додане друге реле, та  використано мікроконтролер [Raspberry Pi Pico W](https://evo.net.ua/ru/mikrokontroller-raspberry-pi-pico-w/), що підтримує з'єднання з Інтернетом і забезпечує більш надійну і ефективну роботу системи. Окрім основної функціональності поливу, до проекту було додано можливість надсилання повідомлень про стан системи. Наприклад, система відправляє на пошту повідомлення  про включення освітлення або розпочаток поливу до мобільного пристрою користувача через спеціально налаштовані повідомлення.Але найважливіше це те, що з появою модулю вай фай, ми змогли отримувати час через NTP сервер, що значно полегшело створення цієї схеми. ![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B0%D0%B1%D0%B7%D0%B0%D1%86%D0%B0%20%281%29.jpg?raw=true)
## інструкцію по запуску проекту на компьютері
Якщо що вас зацікавив проект автополиву, і ви хочете його запустити на своєму комп'ютері. Ось інструкція, як це зробити:
1) Перше, що вам потрібно зробити, це встановити [Thonny](https://thonny.org/).
Коли ви перейдете за посиланням, ви побачите кнопку "Download version" для вибору версії, яка підтримується трьома операційними системами. Потім оберіть потрібну операційну систему та встановіть версію, яка підходить для вашого пристрою (сайт сам підкаже, яка краще).
![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-06-27%20111010.png?raw=true)


2)Коли ви встановили Thonny, підключіть свій пристрій через micro USB. У верхній частині інтерфейсу ви побачите кнопку виконати(Run). Після натискання на неї відкриється вікно, де вам потрібно буде вибрати "Configure interpreter" та встановити версію MicroPython(Raspberry Pi Pico).
![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B0%D0%B1%D0%B7%D0%B0%D1%86%D0%B0%20%282%29.jpg?raw=true)


3)Та остання деталь перед тим як ми почнемо працювати із кодом, це потрбіно буде вибрати у правому низу екрану install Micropython , та потім Raspberry Pi Pico W.
![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B0%D0%B1%D0%B7%D0%B0%D1%86%D0%B0%20%283%29.jpg?raw=true)
## Завантаження файлів на Raspberry Pi Pico W через Thonny
1)  **Створіть новий пустий файл в Thonny**: В Thonny створіть два  пустих файлів, до якогх ми будемо завантажувати наші файли проекту. ![enter image description here](https://github.com/Pranichek/AutoWatering-on-Raspberry-Pi-Pico-W/blob/main/images/%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B0%D0%B1%D0%B7%D0%B0%D1%86%D0%B0%20%284%29.jpg?raw=true)
    
2) **Копіюйте файли з папки AutoWatering**: Після цього на гіт хабі з папки AutoWatering на вашому комп'ютері скопіюйте файл `umail.py` і файл `main.py`.
 
 
3)**Вставка файлів**:Коли ви натисли кнопку зберегти файли на вашому мікроконтролері , але обов'язково зберіжіть файли під тією назвою що і на гіт хабі.Це дозволить запускати код без вашої допомоги .

 ## Опис коду проекту автоматичного поливу рослин
Тепер давайте розглянемо основні аспекти коду проекту, які відповідають за автоматизований полив рослин:
 - [ ] module `time` - забезпечує функції для роботи з часом. У проекті автоматичного поливу рослин цей модуль використовується для таких цілей як затримки виконання коду, отримання часу та завдяки йому ми робили паузи у підключенню вай фай.
 - [ ] module `network` - завдяки цьому модулю, ми змогли використовувати мережеві функції для підключення до Wi-Fi. 
 - [ ] module `umail` - цей модуль дозволив  надсилати email-повідомлення, але перед тим як його  імпортувати у код , вам доведеться завантажити на ваш мікроконтролер файл під назвою umail.py , його ви зможете знайти і моємо гітхабі у папці під назвою AutoWatering.
 - [ ] module `Pin` - цей модуль допомогає керувати цифровими пінами , у нашому випадку це були Pin1(GP0) та Pin2(GP1)
 - [ ] module `ADC` - допомогав зчитувати аналогові значення з датчика вологості.
 - [ ] module `RTC` - у коді використовується модуль RTC  (Real-Time Clock), який являє собою апаратний компонент або програмну  що дає можливість відстежувати плин часу навіть при вимкненні живлення. У нашому випадку RTC використовується для читання системного часу.У першій версії схеми ми використовували фізичний RTC-модуль, наприклад DS1302, для цієї мети. В коді ж RTC використовується для перетворення часу, отриманого від NTP-сервера, у часовий пояс України.

Подробний опис файлу umail.py  ви можете подивитися за [посиланням](https://youtu.be/tfp-Futa-lw?feature=shared),але від себе скажу що він виконує роль   відправлення email-повідомлень. Він включає методи для підключення до [SMTP-сервера](https://aws.amazon.com/ru/what-is/smtp/), аутентифікації користувача, відправлення повідомлень та закриття з'єднання.

```sender_email = ''
sender_name = 'PiPico'
sender_app_password = ''
recipient_email = ''
email_subject = 'Email from RPi Pico'

sensor = ADC(28)
min = 10000
max = 16000
SSID = ""
PASSWORD = ""
relay_led = Pin(1, Pin.IN)
relay_pump = Pin(0, Pin.IN)
pump_start_time = None
send_off_pump = 0
chek_pump = 0
```
У цій частині кода визначаються змінні для налаштування відправника та отримувача email, параметри Wi-Fi мережі, налаштування сенсора вологості , параметри керування реле (relay_led, relay_pump) та змінні для контролю насоса.

***Функція надсилання email***

    def send_email(subject, message):
    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True)
    smtp.timeout = 10  
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write("From:" + sender_name + "<" + sender_email + ">\n")
    smtp.write("Subject:" + subject + "\n")
    smtp.write(message)
    smtp.send()
    smtp.quit()
    print("Повідомлення надіслано")
>Ця функція  встановлює з'єднання з сервером Gmail через захищене з'єднання, аутентифікується з використанням відправникового email і паролю, тому ви можете не перйматися що якась інформація буде перехоплена.Ще ця функція формує та відправляє email з вказаним заголовком який ви самі можете написати і звусно повідомлення теж. Після відправлення вона завершує з'єднання з SMTP-сервером , та на цьому цей процес завершується.Коли ми із командою це пробували це дуже допомогло розширити функціонал, а самий головний плюс це те що пристрій на якій відправляється повідомлення не повинен бути підключиним до однієї мережи із raspberry pi pico

***Підключення до Wi-Fi***


Як вже раніше було написано ,що для підключення до Wi-Fi мережі використовується модуль `network`

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print(f'Підключення к  {SSID}...')
    
    while not wlan.isconnected():
        time.sleep(1)
        print('Чекайте підключення')
        
    print('Connected to Wi-Fi')
    print(wlan.ifconfig())
    send_email(email_subject, "Встановлено підключення із вай-фай")

>Для підключення до Wi-Fi використовується модуль `network`. Спочатку створюється об'єкт Wi-Fi , що дозволяє підключатися до існуючої мережі. Потім Wi-Fi активується командою `active(True)`. Після цього використовується метод  для підключення до мережі Wi-Fi з вказаними ім'ям мережі (SSID) та паролем. У нескінченому циклі перевіряється, чи підключився мікроконтролер до мережі. Якщо ще ні, програма чекає одну секунду перед повторною перевіркою. Коли підключення відбудеться, на екран виводиться IP-адреса та встановлюється підключення.

***Отримання часу із NTP серверу***


**NTP**- це протокол для синхронізації годинників комп'ютерів через мережу. Він дозволяє отримати точний час з серверів, які спеціалізуються на наданні цієї інформації. 
    def set_time():
	    ntp_servers = ['pool.ntp.org', 'time.nist.gov', 'time.google.com']
	    for server in ntp_servers:
	        print(f'Підключення к: {server}...')
	        ntptime.host = server
	        ntptime.settime()  
	        print('Час отримано')
	        send_email(email_subject, "Час встановлено")
>Спочатку визначаються адреси кількох NTP-серверів, таких як `pool.ntp.org`, `time.nist.gov` та `time.google.com`(Ви можете використовувати будь які). Потім програма по черзі звертається до кожного з цих серверів,щоб якщо один із серверів зайнятий то пробуєм під'єднатися до іншого.Після чого викликається функція , яка синхронізує системний час мікроконтролера з часом NTP. Якщо час успішно встановлено, ящо час отримано, у носолі виводиться про це повідомлення.
>
Але оскільки час із цих серверів ми отримаємо не почасовому поясу як в Україні, то ми всеж таки звернуль до AI, щоб він зробив функцію перетвору часу.

**Основний цикл**
Основний цикл програми забезпечує безперервну роботу системи автоматичного поливу рослин. Спочатку перевіряється підключення до вай-фай. Якщо мікроконтролер підключений до вай-фай, проводиться вимірювання вологості ґрунту за допомогою датчика, а результат виводиться у консолі. Потім отримується поточний час з урахуванням українського часового поясу. Далі програма перевіряє час доби і відповідно включає або вимикає лампу для освітлення рослин, а також керує роботою насоса для поливу залежно від рівня вологості. Якщо вологість висока, насос вимикається, якщо низька - включається, ще ми із командою попрацювали над тим щоб у вашій хаті не було затопу тому у одну годину насос може поливати лише два рази. У випадку відсутності підключення ,через хвилину мікроконтролер передає сигнали о втраті інтернету, та пробує підключитися ще раз.
## Опис схеми

**Компоненти**
*Raspberry Pi Pico W*-мікроконтролер, який керує всією системою. Має вбудований Wi-Fi для підключення до мережі.

*Датчик вологості ґрунту*(версію не пом'ятаю але їх легко знайти у інтернеті)-для вимірювання рівня вологості ґрунту. Видає аналоговий сигнал,  вологості.

*Реле модуль* (2 штуки)-Використовуються для керування  насоса та лампи. Дозволяють включати або вимикати прилади за допомогою сигналів від мікроконтролера.

*Насос*-подає воду для рослин

*Блок живлення* - цей блок живлення перетворює із 220 вольт у 5вольт, що дуже зручно та не треба купувати батарейки коженгь місяць

*Макетна плата*-для зручного з'єднання компонентів без необхідності пайки.

Наша схема автоматичного поливу рослин володіє декількома ключовими перевагами, які роблять її незамінною для догляду за рослинами без постійного контролю з вашого боку.

1)**Автономність:** Схема працює від батарейок, тому навіть при відключенні електроенергії вона продовжить функціонувати. Це особливо важливо в регіонах з частими перебоями в електропостачанні.Єдине що вама може завадити це відсутність вай фаю ,але є рішення або запустити схему без використанння його, або приобрести вай-фай який працює у відключення свтла.
 2)**Безпека:** Наша система виключає ризик затоплення, що часто траплялося з ранніми прототипами. Ми ретельно пропрацювали код, щоб повністю усунути цю проблему.
3)**Простота:** Збирання та підключення схеми не потребують спеціальних знань чи навичок. У комплекті завжди є детальна інструкція, яка допоможе вам розібратися в усіх нюансах.
 4)**Зручність:** Відправляючись у відпустку або виїжджаючи на вихідні, ви можете бути спокійні за свої рослини. Система автоматичного поливу забезпечить їм необхідну вологу, навіть у вашу відсутність.
5)**Освітній аспект:** Крім практичної користі, робота з нашою схемою дозволить вам отримати цінний досвід роботи з мікроконтролерами. Це чудова можливість розширити свої знання та навички в галузі електроніки.

## Висновок по роботі над автополивом
Перед тим, як ми дізналися про мікроконтролери та їхні можливості в автоматизації повсякденних справ, ми вважали, що це складний і недосяжний напрямок. Однак, з розвитком нашого проєкту автоматичного поливу рослин за допомогою мікроконтролеру, ми зрозуміли які переваги вони можуть принести новачкам у цьому поляганні. Але я також вважаю, що автополив значно полегшує життя людям, забезпечуючи автоматизований і регулярний полив рослин без необхідності постійного контролю. Це особливо корисно для тих, хто має городи або великі сади, де необхідно підтримувати оптимальний рівень вологості для рослин, або для людей, які часто подорожують та не можуть постійно наглядати за рослинами. Автополив забезпечує постійний режим поливу, що сприяє здоровому росту і кращому врожаю без потреби в постійній увазі, крім того, система автополиву також включає освітлення за фіксованим графіком, що додатково сприяє здоровому росту рослин без потреби в постійній увазі та фізичних зусиллях. Як для нас, можна сказати що завдяки цьому проєкту ми не лише зрозуміли важливість автоматизації в сільському господарстві, а й отримали цінний досвід у програмуванні мікроконтролерів та роботі у команді. Вивчення функціональних можливостей мікроконтролерів дозволило нам впровадити складні програмні рішення для управління поливом та розуміння надалі, як робити більш складні проєкти.
