def Калькулятор (
    #Импорты
    import sys, math
    from colorama import init, Fore, AnsiToWin32
    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream
    #Функция расчёта
    def mathematic(firstValue, argument, secondValue):
        result = str('Вы ввели некорректное действие')
        if argument=='*':
            result = int(firstValue * secondValue)
        if argument=='/':
            if secondValue == 0:
                while secondValue == 0:
                    print('Делитель равен нулю!')
                    secondValue = int(input("Введите  второе число: "))           
            if secondValue != 0:
                result = firstValue / secondValue
            if result > int(result):
                result = float(result)
            if result == int(result):
                result = int(result)
        if argument=='+':
            result = int(firstValue + secondValue)
        if argument=='-':
            result = int(firstValue - secondValue)
        if argument=='%':
            result = str(int(firstValue * secondValue / 100)) + '%'
        if argument=='**':
            result = int(firstValue ** secondValue)
        if argument=='^':
            result = 'Корень из первого числа:  ' + str(math.sqrt(firstValue)) + '     Корень из второго числа:  ' + str(math.sqrt(secondValue))
        return result
    #Цикл
    while True:
        print(Fore.YELLOW + '', file=stream)
        a = int(input("Введите первое число: "))
        print(Fore.GREEN + '', file=stream)
        b = str(input("Введите действие: "))
        print(Fore.BLUE + '', file=stream)
        c = int(input("Введите второе число: "))
        print(Fore.RED + '', file=stream)
        print('Ответ: ' + str(mathematic(a, b, c)))
        print(Fore.RESET + '', file=stream)
        if str.lower(str(input("Выйти?(N/n)"))) == "n":
            break
    )
def Таймер (
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
    )