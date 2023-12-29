def month_to_season(month):
    if month in (12, 1, 2):
        print ("Зима")
    elif month in (3, 4, 5):
        print ("Весна")
    elif month in (6, 7, 8):
        print ("Лето")
    elif month in (9, 10, 11):
        print ("Осень")
    else:
        print ("Некорректный номер месяца")

month_to_season(12)



#вариант
# def month_to_season(month):
#     if month in (12, 1, 2):
#         return "Зима"
#     elif month in (3, 4, 5):
#         return "Весна"
#     elif month in (6, 7, 8):
#         return "Лето"
#     elif month in (9, 10, 11):
#         return "Осень"
#     else:
#         return "Некорректный номер месяца"

# season = month_to_season(11)
# print(season)