from .celery import app


@app.task
def heavy_cpu_task(num=1):
    factorial = 1

    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
        return 0
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial * i

    return factorial



