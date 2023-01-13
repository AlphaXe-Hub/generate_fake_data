import time


def function(n):
    for i in range(0,n):
        time.sleep(1)
        print(i)


if __name__ == '__main__':
    function(10)
