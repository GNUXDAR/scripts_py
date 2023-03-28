import psutil
import time
from plyer import notification # asegúrate de tener instalada la biblioteca plyer
def batery():
    LOW_BATTERY_THRESHOLD = 20  # porcentaje de batería por debajo del cual se considera que la batería está baja
    SLEEP_INTERVAL = 5 * 60  # tiempo en segundos entre las verificaciones de la batería, 5 minutos

    while True:
        battery = psutil.sensors_battery()
        if battery.percent < LOW_BATTERY_THRESHOLD: # and not battery.power_plugged:
            notification_title = "X_X Batería Baja X_X"
            notification_text = f"Nivel de batería: {battery.percent}%"
            notification.notify(notification_title, notification_text)
        time.sleep(SLEEP_INTERVAL)

batery()