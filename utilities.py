"""
Functions required:
    read_sales() - read and process source records
    validate_sale() - validate required fields and values
    update_summary() - accumulate item totals
    log_error() - record invalid data and error details
    save_summary() - write grouped sales CSV
    display_totals() - print final totals
    main() - coordinate the program
"""
import csv

file_path = "sales(in).csv"

def validate_sale(customer, product, amount, cost, line):
    if customer.strip() == "" or product.strip() == "" or amount.strip() == "" or cost.strip() == "":
        print(f"Line {line} | ")

def read_sales():
    with open(file_path, "r", newline = "") as file:
        reader = csv.reader(file)
        next(reader)
        for name, item, qty, price in reader:
            pass


def main():
    pass

if __name__ == "__main__":
    main()