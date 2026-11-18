import csv

file_path = "sales(in).csv"

def validate_sale(customer, product, amount, cost, line):
    valid = True
    fields = [(customer, "customer"), (product, "product"),
              (amount, "quantity"), (cost, "price")]
    for value, field in fields:
        if not value.strip():
            print(f"Line {line} | Missing {field}")
            valid = False
    for value, field, convert, minimum in [(amount, "quantity", int, 1), (cost, "price", float, 0)]:
        if value.strip():
            try:
                if convert(value) < minimum:
                    raise ValueError
            except ValueError:
                print(f"Line {line} | Invalid {field}")
                valid = False
    return valid

def read_sales():
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        for line, (name, item, qty, price) in enumerate(reader, start=2):
            if not validate_sale(name, item, qty, price, line):
                continue
            qty = int(qty)
            price = float(price)


def main():
    read_sales()


if __name__ == "__main__":
    main()