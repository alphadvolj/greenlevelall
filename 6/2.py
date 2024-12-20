import re
import matplotlib.pyplot as plt

file_path = 'data.txt'

temperatures = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        match = re.search(r'(\d{4}-\d{2}-\d{2}): Temperature = (\d+)°C', line)
        if match:
            temperatures.append(int(match.group(2)))

plt.figure(figsize=(10, 6))
plt.hist(temperatures, bins=5, color='b', alpha=0.7, edgecolor='black')
plt.title('Гистограмма температур', fontsize=16)
plt.xlabel('Температура (°C)', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

plt.savefig('temperature_histogram.png')
plt.show()