import utilities as ut

file_path = "sales.csv"

def main():
    ut.read_sales()
    ut.save_summary(file_path)
    ut.display_totals()

if __name__ == "__main__":
    main()