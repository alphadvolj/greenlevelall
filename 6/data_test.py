file_name = "data_test.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("TransactionID, Date, Customer, Amount, Category, Email\n")
    file.write("TX1001, 2023-01-15, Alice Johnson, 120.50, Electronics, alice@gmail.com\n")
    file.write("TX1002, 2023-01-16, Bob Smith, 75.00, Groceries, bob_smith@gmail.com\n")
    file.write("TX1003, 2023-01-17, Charlie Davis, 200.00, Furniture, charlie_d@gmail.com\n")
    file.write("TX1004, 2023-01-18, Diana Brown, 50.25, Groceries, diana.b@gmail.com\n")
    file.write("TX1005, 2023-01-19, Eve Taylor, 300.99, Electronics, eve@gmail.net\n")
    file.write("TX1006, 2023-01-20, Frank Wilson, 90.00, Clothing, frank_wilson@gmail.org\n")

print(f"Файл {file_name} создан.")