# Created by @gnuxdar 
# Modify by Root-FTW 21/04/23
import psutil
import time
from os import path
from notifypy import Notify
from datetime import timedelta

# Personalización
LOW_BATTERY_THRESHOLD = 20
SLEEP_INTERVAL = 5 * 60
ICON_PATH = '../img/ACTECNOLOGY.png'
AUDIO_PATH = '../sound/3014.wav'


def convert_time(seconds):
    return str(timedelta(seconds=seconds))


def battery_low(icon_path=ICON_PATH, audio_path=AUDIO_PATH):
    while True:
        try:
            battery = psutil.sensors_battery()
            connected = battery.power_plugged
            actually_time = time.strftime('%H:%M:%S')
            is_connected = 'Connected' if connected else 'Disconnected'

            if battery.percent < LOW_BATTERY_THRESHOLD and not connected:
                time.sleep(SLEEP_INTERVAL)
                notification = Notify()
                notification.title = 'Battery Low!'
                notification.message = "it's time to connect the machine!!!"
                
                directory = path.abspath(path.dirname(__file__))
                notification.icon = path.join(directory, icon_path)
                notification.audio = path.join(directory, audio_path)

                notification.send()

            print(psutil.sensors_battery())
            print('Time NOW: ', actually_time)
            print('Battery Percent: ', battery.percent)
            print('Connected to charger: ', is_connected)
            print('Battery remaining: ', convert_time(battery.secsleft), '\n')

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(SLEEP_INTERVAL)


battery_low()
