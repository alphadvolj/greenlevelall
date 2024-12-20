import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [20, 21, 22, 20, 23],
    "Department": ["Math", "Physics", "CS", "Math", "CS"],
    "GPA": [3.9, 3.5, 3.8, 3.7, 3.6],
    "Credits": [30, 28, 32, 30, 26]
}

df = pd.DataFrame(data)

gpa_above_3_7 = df[df['GPA'] > 3.7]
print("Студенты с GPA выше 3.7:")
print(gpa_above_3_7)

math_students = df[df['Department'] == "Math"]
print("\nСтуденты с кафедры 'Math':")
print(math_students)

sorted_by_age = df.sort_values(by='Age')
print("\nСтуденты, отсортированные по возрасту:")
print(sorted_by_age)

sorted_by_gpa = df.sort_values(by='GPA', ascending=False)
print("\nСтуденты, отсортированные по GPA в порядке убывания:")
print(sorted_by_gpa)

average_gpa_by_department = df.groupby('Department')['GPA'].mean()
print("\nСредний GPA студентов по кафедрам:")
print(average_gpa_by_department)

student_count_by_department = df['Department'].value_counts()
print("\nКоличество студентов в каждой кафедре:")
print(student_count_by_department)

df['Internship'] = [True, False, np.nan, True, False]
print("\nТаблица с новым столбцом Internship:")
print(df)

missing_internship = df[df['Internship'].isna()]
print("\nСтуденты с пропущенными значениями в Internship:")
print(missing_internship)

df['Internship'].fillna(False, inplace=True)

df['Final Credits'] = df['Credits'] * df['GPA']
print("\nОбновленная таблица с новым столбцом Final Credits:")
print(df)

second_student = df.iloc[1]
print("\nДанные о втором студенте:")
print(second_student)

first_three_names_gpa = df.iloc[:3, [0, 3]]
print("\nИмена и GPA первых трёх студентов:")
print(first_three_names_gpa)

df.at[3, 'GPA'] = 3.95
print("\nОбновленная таблица после изменения GPA у четвёртого студента:")
print(df)

last_two_columns = df.iloc[:, -2:]
print("\nПоследние два столбца для всех студентов:")
print(last_two_columns)