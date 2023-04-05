import os
import time

import keyboard as keyboard


class TrafficLight:
    # атрибуты класса
    __color = ['red', 'yellow', 'green']

    def running(self):
        __index = 0
        while True:
            if keyboard.is_pressed('esc'):
                return
            match self.__color[__index]:
                case 'red':
                    print(end='\r')
                    print(f'{self.__color[__index]}', end=' ')
                    time.sleep(2)
                case 'yellow':
                    print(end='\r')
                    print(f'{self.__color[__index]}', end=' ')
                    time.sleep(2)
                case 'green':
                    print(end='\r')
                    print(f'{self.__color[__index]}', end=' ')
                    time.sleep(2)
            if __index < 2:
                __index += 1
            else:
                __index = 0


print('Светофор. Авто переключение по времени. Для завершения удерживате ESC')
a = TrafficLight()
a.running()
