# Week 3 CIS162 Mike Audi Queue Assignment
# I did it with queues and .put instead of append and del my_list[0] its the same difference but I wanted to use fun module

from queue import Queue
from pathlib import Path

premium_queue = Queue()
standard_queue = Queue()
economy_queue = Queue()

with open(f"{Path(__file__).parent}/packetqueue.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(maxsplit=1)
        priority = parts[0]
        packet = line

        if priority == "P":
            premium_queue.put(packet)
        elif priority == "S":
            standard_queue.put(packet)
        elif priority == "E":
            economy_queue.put(packet)

while not premium_queue.empty():
    prembatch = []
    for i in range(3):

        if not premium_queue.empty():
            prembatch.append(premium_queue.get_nowait())
    print(prembatch)

while not standard_queue.empty():
    standbatch = []
    for i in range(2):

        if not standard_queue.empty():
            standbatch.append(standard_queue.get_nowait())
    print(standbatch)

while not economy_queue.empty():
    print(economy_queue.get_nowait())
