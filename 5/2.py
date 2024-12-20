def mean_squared_error(y_true, y_pred):

    if len(y_true) != len(y_pred):
        raise ValueError("Длины списков y_true и y_pred должны быть равны.")

    mse = sum((true - pred) ** 2 for true, pred in zip(y_true, y_pred)) / len(y_true)
    return mse

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

mse = mean_squared_error(y_true, y_pred)
print(f"Средняя квадратичная ошибка: {mse}")