#Импорты
import time

#Отрисовка
def render(sec, min, hour):
    print(str(hour)+' : '+str(min)+' : '+str(sec))

#Тик
def tick(seconds,  multiplayerSeconds):
    seconds = seconds + int(multiplayerSeconds)
    return seconds
#ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ
seconds = float(0)
minuts = float(0)
hours = float(0)
#ЦИКЛ
while True:
    seconds = tick(seconds, 1)
    if seconds > 59:
        seconds = float(0)
        minuts = minuts + int(1)
        if minuts > 59:
            minuts = float(0)
            hours = hours + int(1)
            if hours > 24:
                hours = float(0)
                minuts = float(0)
                seconds = float(0)
    render(int(seconds), int(minuts), int(hours))
    time.sleep(1.0)