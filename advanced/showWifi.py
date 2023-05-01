'''
Este código escanea las redes WiFi disponibles y muestra su SSID (nombre de la red) 
y BSSID (dirección MAC del punto de acceso).
'''
import wifi

wifi_scanner = wifi.WiFiScan()
networks = wifi_scanner.scan()

for network in networks:
    print(f"SSID: {network.ssid}, BSSID: {network.bssid}")