import pandas as pd
import os
import csv
import time
import psutil

t0 = time.time()


def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))

        return result

    return wrapper


@profile
def func():
    os.mkdir('Output')
    file = "./input.csv"
    total_columns = 50
    header_values = ["deal_id"]
    for i in range(2, total_columns + 1):
        header_values.append(f"col_{i}")

    header = ",".join(header_values)
    header_list = list(header.split(","))

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        df = pd.DataFrame(csv_reader)
        df = df.iloc[1:, :]
        df.columns = header_list
        write_file = lambda x: x.to_csv(os.getcwd() + "/Output/{}.csv".format(x.name.lower()), index=False)
        df.groupby('deal_id').apply(write_file)


func()

t1 = time.time()

total = t1 - t0
print(total)
