import os
import time

import keyboard as keyboard


class TrafficLight:
    # атрибуты класса
    __color = ['red', 'yellow', 'green']

    def running(self, time_r=2, time_y=2, time_g=2):
        __index = 0
        while True:
            if keyboard.is_pressed('esc'):
                return
            match self.__color[__index]:
                case 'red':
                    print(end='\r')
                    print(f'{self.__color[__index]}', end=' ')
                    time.sleep(time_r)
                case 'yellow':
                    print(end='\r')
                    print(f'{self.__color[__index]}', end=' ')
                    time.sleep(time_y)
                case 'green':
                    print(end='\r')
                    print(f'{self.__color[__index]}', end=' ')
                    time.sleep(time_g)
            if __index < 2:
                __index += 1
            else:
                __index = 0


time_red = 7
time_yellow = 2
time_green = 10
print('Светофор. Авто переключение по времени. Для завершения удерживате ESC')
a = TrafficLight()
a.running(time_red, time_yellow, time_green)
