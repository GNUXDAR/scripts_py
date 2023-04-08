# script de notificaciones, para cuando mi bateria baje el porcentaje de carga
# pip install notify-py
# Created by @gnuxdar
from os import path
from notifypy import Notify


notification = Notify()
notification.title = "Battery Low!"
notification. message = "it's time to connect the machine!!!"
# notification.icon = "/home/gnuxdar/scripts_py/img/ACTECNOLOGY.png" #con rutas absolutas
# notification.audio = "/home/gnuxdar/scripts_py/sound/3014.wav"
icono = "../img/ACTECNOLOGY.png"
audio = "../sound/3014.wav"
direccion = path.abspath(path.dirname(__file__))
notification.icon = path.join(direccion, icono)
notification.audio = path.join(direccion, audio)

notification.send()
