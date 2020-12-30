import utime as time
import random
from umqtt.simple import MQTTClient
from miscelanea import Button
import json

client = MQTTClient("uehft84ui", "broker.hivemq.com")
client.connect()

start_time = time.ticks_ms()

class Reflex:
    def __init__(self, name):
        self.name = name
        self.button = Button(39)
        self.client = client
        self.client.connect()

    def game_on(self): #empieza el juego, cada vez el led se enciende a un tiempo aleatorio
        random_time = random.randrange(1000, 6000)
        time.sleep_ms(random_time)
   
    def wait_for_button(self): #espera a que el botón esté pulsado
        while self.button.get_pulsado_polling():
            time.sleep_ms(1)

    def game_off(self, start_time): #el juego se acaba al pulsar el botón 
        finish_time = time.ticks_ms() #marca el tiempo total desde inicio al momento de pulsado del botón
        self.score = time.ticks_diff(finish_time, start_time) #función que da como el resultado el tiempo de respuesta
        
    def publish_message(self): #registro, mensaje que aparece y se envía a mqtt
        j = {"score": self.score}
        message = json.dumps(j)
        print(message)
        self.client.publish(b"JUEGOIOT", message)
