import psutil
import time

br = psutil.net_io_counters().bytes_recv
bs = psutil.net_io_counters().bytes_sent

while True:
    time.sleep(1)
    speedbr = (psutil.net_io_counters().bytes_recv - br)
    speedbs = (psutil.net_io_counters().bytes_sent - bs)
    br = psutil.net_io_counters().bytes_recv
    bs = psutil.net_io_counters().bytes_sent
    total = (psutil.net_io_counters().bytes_recv) + (psutil.net_io_counters().bytes_sent)
    print(f"↑{float('{:.2f}'.format(speedbs/1000000))}/s ↓{float('{:.2f}'.format(speedbr/1000000))}/s | {float('{:.2f}'.format(total/1000000))}MB")
