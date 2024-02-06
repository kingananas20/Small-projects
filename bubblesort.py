import random, time

print("Making list")
daten = [random.randint(1000, 10000) for _ in range(100000)]

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

print("Starting bubble sort")
startTime = time.time()
sorted = bubblesort(daten)
duration = time.time() - startTime

for i in range(len(daten)):
    print(f"{daten[i]} : {sorted[i]}")

print(f"Duration: {round(duration / 60)}m {duration % 60}s") if duration > 60 else print(f"Duration: {duration}")