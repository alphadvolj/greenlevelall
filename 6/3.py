import re
import matplotlib.pyplot as plt

file_path = 'data.txt'

dates = []
temperatures = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        match = re.search(r'(\d{4}-\d{2}-\d{2}): Temperature = (\d+)°C', line)
        if match:
            date = match.group(1)
            temp = int(match.group(2))
            if temp >= 13:
                dates.append(date)
                temperatures.append(temp)

max_temp_index = temperatures.index(max(temperatures))
max_temp_date = dates[max_temp_index]
max_temp_value = temperatures[max_temp_index]

print(f'Дата с самой высокой температурой: {max_temp_date}, Температура: {max_temp_value}°C')

plt.figure(figsize=(10, 6))
plt.plot(dates, temperatures, marker='o', linestyle='-', color='b', label='Temperature')
plt.title('Температура по дням (отфильтровано)', fontsize=16)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Температура (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('filtered_temperature_plot.png')
plt.show()