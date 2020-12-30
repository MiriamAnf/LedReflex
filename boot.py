import network

import utime as time

from credenciales import ssid, password



red = network.WLAN(network.STA_IF)

red.active(True)

red.connect(ssid, password)



while not red.isconnected():

    time.sleep_ms(50)

    if time.ticks_ms() > 10000:  # timeout de 10 segundos

        print("ERROR no se ha podido conectar a la wifi {}".format(ssid))

        break

else:

    print(red.ifconfig())