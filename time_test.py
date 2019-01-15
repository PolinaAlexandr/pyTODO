from datetime import datetime
import time


def start():
    dat_time = input("Чтоза время:")

    print("Время:", dat_time, "Не верно, сейчас", datetime.now())


def calculations():
    dat_time = input("Чтоза время:")
    real_time = datetime.strptime(dat_time, '%b %d %Y %I:%M%p')
    print("Сейчас", real_time)


if __name__ == "__main__":
    calculations()
