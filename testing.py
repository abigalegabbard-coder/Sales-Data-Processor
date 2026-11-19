import csv

file_path = "sales.csv"

def log_error(person, product, qty, cost, error, mistake, row):
    """Opens the errors.log file and appends the incorrect information"""
    with open("errors.log", "a") as file:
        file.write(f"Line {row} | Invalid {error}: {mistake} | {person},{product},{qty},{cost}\n")

def validate_sale(customer, product, amount, cost, line):
    """Checks to see if any of the information is left blank, then checks if the qty and cost 
    data types are correct and in the correct range"""
    valid = True
    fields = [(customer, "customer"), (product, "product"), (amount, "quantity"), (cost, "price")]
    for value, field in fields:
        if not value.strip():
            log_error(customer, product, amount, cost, field, value, line)
            valid = False
    for value, field, convert, minimum in [(amount, "quantity", int, 1), (cost, "price", float, 0)]:
        if value.strip():
            try:
                if convert(value) < minimum:
                    raise ValueError
            except ValueError:
                log_error(customer, product, amount, cost, field, value, line)
                valid = False
    return valid

def update_summary():
    totals = {}
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            item = row[1]
            qty = int(row[2])
            price = float(row[3])
            if item in totals:
                totals[item][0] += qty
                totals[item][1] += price
            else:
                totals[item] = [qty, price]
    with open("sales_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item", "Qty", "Price Total"])
        for item, values in totals.items():
            writer.writerow([item, values[0], round(values[1], 2)])

def read_sales():
    """Reads through the sales(in).csv file and processes the information"""
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        for line, (name, item, qty, price) in enumerate(reader, start=2):
            if not validate_sale(name, item, qty, price, line):
                continue
            qty = int(qty)
            price = float(price)


def display_totals():
    print("Sales Processing Complete")
    print("-------------------------")


def main():
    read_sales()


if __name__ == "__main__":
    main()