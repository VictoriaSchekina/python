from time import sleep

class TrafficLight:
    # атрибуты класса
    __color1 = "Black"

    # методы класса
    def running(self):
        while True:
            #print("Red")
            print('\x1b[0;30;41m' + 'Red' + '\x1b[0m')
            sleep(5)
            print('\x1b[1;33;47m' + 'Yellow' + '\x1b[0m')
            sleep(2)
            print('\x1b[6;30;42m' + 'Green' + '\x1b[0m')
            sleep(5)
            print('\x1b[1;33;47m' + 'Yellow' + '\x1b[0m')
            sleep(2)

trafficlight = TrafficLight()
trafficlight.running()

