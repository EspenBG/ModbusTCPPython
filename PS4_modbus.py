from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
import pygame

pygame.init()
pygame.joystick.init()
t = pygame.joystick.get_count()
controller = pygame.joystick.Joystick(0)
controller.init()
axis_data = {0: 0.0, 2: 0.0, 3: 0.9, 4: 0, 1: 0.0}
button_data = {0: False, 1: False, 2: False, 3: False, 9: False, 10: False}
x = 0
y = 0

            
# Create an instance of ModbusServer
#server = ModbusServer("158.38.140.10", 502, no_block=True)
server = ModbusServer("10.0.1.92", 502, no_block=True)
print("Start server...")
server.start()
print("Server is online")
state = [0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            axis_data[event.axis] = round(event.value*100,1)
            x = axis_data[0]
            y = axis_data[1]*-1
        elif event.type == pygame.JOYBUTTONDOWN:
            button_data[event.button] = True
        elif event.type == pygame.JOYBUTTONUP:
            button_data[event.button] = False
    buzzer=button_data[0] # Square button
    Stop = button_data[9] # Options button
    #print(button_data)
    if buzzer:
        DataBank.set_words(4, "1")
    else:
        DataBank.set_words(4, "0")

    if Stop:
        DataBank.set_words(3, "1")
    else:
        DataBank.set_words(3, "0")
    DataBank.set_words(0, [x])
    DataBank.set_words(1, [y])
    sleep(0.2)