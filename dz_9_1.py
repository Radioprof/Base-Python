from time import sleep
import turtle

def sq(color):
    square = turtle.Turtle()
    # square.shape("turtle")
    square.color(color, color)
    square.begin_fill()
    for i in range(4):
        square.forward(100)
        square.right(90)
    square.end_fill()
    return

class TrafficLight:
    __color = 'red'

    def running(self):
        # print(self.__color)
        sq(self.__color)
        sleep(7)
        sq('yellow')
        sleep(2)
        sq('green')
        sleep(10)


a = TrafficLight()
a.running()
