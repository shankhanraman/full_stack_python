# You 're creatig a monthly report for a cafe's sales.
# Instead of putig all login on one plac , break it down.
# Task:
# . Write a function generate_report() that calls:
# . fetch_sales()
# .fiter_valid_orders()
# .summarize_data()

def fetch_sales():
    print("Fetching the sales data")

def filter_valid_sales():
    print("Filterning valid sales data")

def summarize_data():
    print("Summarize the sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")

generate_report()