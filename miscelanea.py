import neopixel
import machine
from random import randrange

class LedRGB: 
    def __init__(self):
        self.np = neopixel.NeoPixel(machine.Pin(27), 1)
        self.temporizador = machine.Timer(-1) # utilizamos un timer para programar el apagado

    def encender(self):
        self.np[0] = (255, 255, 255)
        self.np.write()

    def apagar(self):
        self.np[0] = (0, 0, 0)
        self.np.write()
    
    def color(self, r, g, b):
        self.np[0] = (r, g, b)
        self.np.write()

class Button:
    def __init__(self, pinNumber):   #(self, pinNumero)
        self.flag = False
        self.button = machine.Pin(pinNumber, machine.Pin.IN)    #39 = pinNumero
        self.button.irq(self.cb, machine.Pin.IRQ_FALLING)

    def cb(self, inst):
        self.flag = True

    def get_pulsado(self):
        if not self.flag:
            return False
        self.flag = False
        return True    
    
    def get_pulsado_polling(self):
        return self.button.value()
