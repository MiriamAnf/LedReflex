import utime as time
from miniproyecto import Reflex
from miscelanea import LedRGB, Button
from umqtt.simple import MQTTClient

client = MQTTClient("uehft84ui", "broker.hivemq.com")
client.connect()

project = Reflex("miniproyecto")
start_time = time.ticks_ms()

led = LedRGB()

while True:   #bucle infinito
    led.apagar() #empezamos con el led apagado
    print("Cuando el led se encienda, pulsalo lo mas rapido que puedas")
    project.game_on() # el juego empieza
    led.encender() # el led se enciende
    if project.wait_for_button():   # momento en el que se pulsa el botón (necesita lógica inversa)
        project.game_off(start_time)  # el juego acaba 
    led.apagar() # el led se apaga
    finish_time = time.ticks_ms() # marca el tiempo total del juego
    project.score = time.ticks_diff(finish_time, start_time)  #función para calcular el tiempo de respuesta
    print("Tu tiempo de respuesta ha sido de {} ms".format(project.score))
    project.publish_message() #publicamos en mqtt nuestro score