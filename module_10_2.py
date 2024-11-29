# Задача "За честь и отвагу!":
import time
from threading import Thread
class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name  # имя рыцаря (str)
        self.power = power # сила рыцаря (int)
    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100  # количество врагов
        days = 0  # количество дней
        while enemies > 0:
            time.sleep(1)  # задержка в 1 секунду
            days += 1 # количество дней сражения
            enemies -= self.power # В процессе сражения количество врагов уменьшается на power текущего рыцаря
            print(f"{self.name} сражается {days} дней(дня), осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')







