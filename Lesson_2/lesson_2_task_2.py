def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

year = 2020

leap = is_year_leap(year)

print("год", year, ":", leap)



#вариант
# is_year_leap = input("Введите год (число): ")
# if (int(is_year_leap) % 4 == 0):
#     print("год", is_year_leap, ": True")
# else:
#     print("год", is_year_leap, ": False")