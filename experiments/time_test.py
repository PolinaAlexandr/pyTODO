from datetime import datetime
import time


def start():
    dat_time = input("Чтоза время:")

    print("Время:", dat_time, "Не верно, сейчас", datetime.now())


def calculations():
    real_time = datetime.strptime(time.localtime, '%b %d %Y %I:%M%p')
    print("Сейчас", real_time)


def local_time():
    now_time = time.asctime( time.localtime(time.time()))
    print("Current time:", now_time)


if __name__ == "__main__":
    # print(time.localtime())
    local_time()


