import time


def count(fn):
    def counted(*args):
        counted.count += 1
        return fn(*args)

    counted.count = 0
    return counted


def timer(fn):
    def timed(*args):
        start = time.time()
        timed.times += 1
        this_time = timed.times
        r = fn(*args)
        print(f"Call time {this_time}, takes {(time.time() - start) * 1000} ms.")
        return r

    timed.times = 0
    return lambda *args: timed(*args)
