from stopwatch import Stopwatch
from timer import Timer

def main():
    stopwatch = Stopwatch()
    timer = Timer(10)

    stopwatch.start()
    time.sleep(2)
    print(f"Elapsed time: {stopwatch.elapsed()} seconds")
    stopwatch.stop()

    timer.start()
    while timer.remaining_time() > 0:
        print(f"Time remaining: {timer.remaining_time()} seconds")
        time.sleep(1)
    timer.stop()

if __name__ == "__main__":
    main()
