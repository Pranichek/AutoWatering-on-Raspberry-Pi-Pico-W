import network
import ntptime
import umail
import time
from machine import RTC, Pin, ADC

sender_email = ''
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
    


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
print(f'Підключенння к  {SSID}...')

while not wlan.isconnected():
    time.sleep(1)
    print('Триває підключення')
    
print('Connected to Wi-Fi')
print(wlan.ifconfig())
send_email(email_subject, "Встановлено підключення із вай-фай")



def set_time():
    ntp_servers = ['pool.ntp.org',  'time.google.com']
    for server in ntp_servers:
        print(f'Підключення к: {server}...')
        ntptime.host = server
        ntptime.settime()  
        print('Час отримано')
        send_email(email_subject, "Час встановлено")
    

def get_ukraine_time():
    rtc = RTC()
    current_time = rtc.datetime()
    
    current_time = year, month, day, weekday, hours, minutes, seconds, subseconds 
    hours += 3
    
    if hours >= 24:
        hours -= 24
        day += 1
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))):
        days_in_month[1] = 29  

    if day > days_in_month[month - 1]:
        day = 1
        month += 1
    
    if month > 12:
        month = 1
        year += 1
    
    return year, month, day, hours, minutes, seconds


set_time()

while True:
    if wlan.isconnected():
        wet = round(100 - ((sensor.read_u16() - min) / ((max - min) / 100)))
        print(wet, "%")
        year, month, day, hours, minutes, seconds = get_ukraine_time()

        hour = int(hours)
        minuty = int(minutes)
        sek = int(seconds)

        print(hour, "часов")
        print(minuty, "минут")
        print(sek, "секунд")

        if hour == 20 and minuty == 1 and sek == 1:
            send_email(email_subject, f"Лампа ввімкнулась,час {hour}")
            relay_led = Pin(1, Pin.OUT)
        if hour == 4 and minuty == 1 and sek == 1:
            relay_led = Pin(1, Pin.OUT)   
        elif hour == 7 and minuty == 1 and sek == 1:
            send_email(email_subject, f"Лампа вимкнулась,час {hour}")
            relay_led = Pin(1, Pin.IN)
        elif hour == 10 and minuty == 1 and sek == 1:
            relay_led = Pin(1, Pin.IN)
            
        if wet >= 69:
            relay_pump = Pin(0, Pin.IN)
            if send_off_pump is None:
                send_email(email_subject, f"Насос вимкнувся, вологісті {wet}")
                send_off_pump = 0
        elif minuty != 1:
            if wet <= 68:
                chek_pump += 1
                if chek_pump >= 3:
                    relay_pump = Pin(0, Pin.IN)
                    send_off_pump = 0
                    if pump_start_time is None:
                        pump_start_time = time.time()
                        send_email(email_subject, f"Насос вже проработав два рази, тому чекайте годину щоб вім міг поливати ще {wet}")
                else:
                    print("зашло")
                    relay_pump = Pin(0, Pin.OUT)
                    send_email(email_subject, f"Насос ввімкнувся, вологість {wet}")
                    time.sleep(4)
                    send_off_pump = None
        if pump_start_time is not None:
            if time.time() - pump_start_time >= 3600:
                chek_pump = 0
                pump_start_time = None
        print(chek_pump)
        time.sleep(1)
    else:
        relay_pump = Pin(0, Pin.IN)
        time.sleep(10)
        for i in range(10):
            relay_led = Pin(1, Pin.OUT)
            time.sleep(1)
            relay_led = Pin(1, Pin.IN)
            time.sleep(1)
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(SSID, PASSWORD)
        print(f'Підключенння к  {SSID}...')
        
        while not wlan.isconnected():
            time.sleep(1)
            print('Триває підключення')
            
        print('Connected to Wi-Fi')
        print(wlan.ifconfig())
        send_email(email_subject, "Встановлено підключення із вай-фай")
        set_time()
