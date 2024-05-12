import random

if __name__ == "__main__":
    filename = "./input.csv"
    total_lines = 1_000_000
    total_columns = 50
    min_deal_id = 1
    max_deal_id = 1000  # this can be upto 10000

    header_values = ["deal_id"]
    for i in range(2, total_columns + 1):
        header_values.append(f"col_{i}")

    header = ",".join(header_values)

    with open(filename, "w") as f:
        f.write(f"{header}\n")

        for i in range(total_lines):
            deal_id = str(random.randint(min_deal_id, max_deal_id))
            entry_values = [deal_id]
            for j in range(2, total_columns + 1):
                entry_values.append(f"col_{j}_value_{i}")

            entry = ",".join(entry_values)
            f.write(f"{entry}\n")


