# script de notificaciones, para cuando mi bateria baje el porcentaje de carga
# pip install psutil
# pip install notify-py
# Created by @gnuxdar
import psutil
import time
from os import path
from notifypy import Notify


def battery_low():
    # porcentaje de batería por debajo del cual se considera que la batería está baja
    LOW_BATTERY_THRESHOLD = 20
    # tiempo en segundos entre las verificaciones de la batería, 5 minutos
    SLEEP_INTERVAL = 5 * 60

    while True:
        battery = psutil.sensors_battery()
        if battery.percent < LOW_BATTERY_THRESHOLD:  # and not battery.power_plugged:
            notification = Notify()
            notification.title = "Battery Low!"
            notification.message = "it's time to connect the machine!!!"
            # notification.icon = "/home/gnuxdar/scripts_py/img/ACTECNOLOGY.png" #con rutas absolutas
            # notification.audio = "/home/gnuxdar/scripts_py/sound/3014.wav"
            icono = "../img/ACTECNOLOGY.png"
            audio = "../sound/3014.wav"
            direccion = path.abspath(path.dirname(__file__))
            notification.icon = path.join(direccion, icono)
            notification.audio = path.join(direccion, audio)

            notification.send()
        time.sleep(SLEEP_INTERVAL)


battery_low()