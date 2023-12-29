def bank(X, Y):
    amount = X  
    for n in range(Y):
        percent = amount * 0.1 
        amount += percent  
    return amount

X = 2000  #начальный вклад
Y = 10  #количество лет
result = bank(X, Y)
print("Сумма на счету спустя", Y, "лет будет составлять", result, "рублей.")