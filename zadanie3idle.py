# Импортируем модуль serial для работы с последовательным портом
import serial
# Импортируем модуль time для работы с временем
import time
# Импортируем модуль serial.tools.list_ports для получения списка доступных последовательных портов
import serial.tools.list_ports

# Список скоростей передачи данных
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']
# Получаем список доступных портов
ports = [p.device for p in serial.tools.list_ports.comports()]
# Выбираем первый порт из списка
port_name = ports[0]
# Устанавливаем скорость передачи данных для порта
port_speed = int(speeds[-1])
# Устанавливаем таймаут для порта
port_timeout = 10
# Открываем соединение с портом
ard = serial.Serial(port_name, port_speed, timeout=port_timeout)
# Задержка на 1 секунду
time.sleep(1)
# Очищаем буфер входных данных порта
ard.flushInput()

try:
    # Считываем данные из порта и объединяем их в одну строку
    msg_bin = ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    # Декодируем полученные данные в строку
    msg_str_ = msg_bin.decode()
    # Выводим длину полученной строки
    print(len(msg_bin))
except Exception as e:
    # В случае ошибки выводим сообщение об ошибке
    print('Error!')

# Закрываем соединение с портом
ard.close()
# Задержка на 1 секунду
time.sleep(1)
# Выводим полученную строку
print(msg_str_)
