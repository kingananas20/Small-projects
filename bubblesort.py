import random, time
from colorama import Fore, init
init(autoreset=True)

print(f"{Fore.WHITE}Making list")
daten = [random.randint(1000, 10000) for _ in range(10000)]

def bubblesort(lst: list) -> list:
    lst = lst.copy()

    for i in range(len(lst)):
        checks = 0
        for i in range(len(lst) - i - 1):
            no1, no2 = lst[i], lst[i + 1]

            if no1 > no2:
                lst[i] = no2
                lst[i + 1] = no1
                checks += 1

        if checks == 0:
            break

    return lst

print(f"{Fore.WHITE}Starting bubble sort")
startTime = time.time()
sorted = bubblesort(daten)
duration = time.time() - startTime

for i in range(len(daten)):
    print(f"{Fore.RED}{daten[i]} {Fore.WHITE}: {Fore.GREEN}{sorted[i]}") if daten[i] != sorted[i] else print(f"{Fore.GREEN}{daten[i]} {Fore.WHITE}: {Fore.GREEN}{sorted[i]}")

print(f"{Fore.WHITE}Duration: {round(duration / 60)}m {duration % 60}s") if duration > 60 else print(f"{Fore.WHITE}Duration: {duration}s")