import re
import matplotlib.pyplot as plt

file_name = "data_test.txt"

with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 1) Подсчет количества транзакций (не включая заголовок)
transaction_count = len(lines) - 1
print(f'Количество транзакций: {transaction_count}')

# 2) Нахождение общей суммы всех покупок
total_amount = sum(float(line.split(", ")[3]) for line in lines[1:])
print(f'Общая сумма всех покупок: ${total_amount:.2f}')

# 3) Извлечение строк, где категория товара — Electronics
electronics_transactions = [line for line in lines[1:] if 'Electronics' in line]
print('Транзакции в категории Electronics:')
for transaction in electronics_transactions:
    print(transaction.strip())

# 4) Нахождение транзакций, где сумма больше 100 долларов
high_value_transactions = [line for line in lines[1:] if float(line.split(", ")[3]) > 100]
print('Транзакции с суммой больше 100 долларов:')
for transaction in high_value_transactions:
    print(transaction.strip())

# 5) Построение гистограммы количества покупок в каждой категории
categories = {}
for line in lines[1:]:
    category = line.split(", ")[4]
    categories[category] = categories.get(category, 0) + 1

plt.figure(figsize=(10, 6))
plt.bar(categories.keys(), categories.values(), color='b', alpha=0.7, edgecolor='black')
plt.title('Количество покупок в каждой категории', fontsize=16)
plt.xlabel('Категория', fontsize=12)
plt.ylabel('Количество покупок', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

plt.savefig('category_histogram.png')
plt.show()