# как-то получить от пользователя оценку
rate_as_str = input("Оцените работу оператора от 1 до 5: ") #str
rate = int(rate_as_str) #int

# проверить, что оценка от 1 до 5
if(rate<1):
    rate = 1

if(rate > 5):
    rate = 5

# в зависимости от оценки предложить дать обратную связь
feedback = ""

if rate == 1:
    feedback = input("Расскажимите, что нам улучшить: ")
elif rate == 2:
    feedback = input("Расскажимите, что вас смутило: ")
elif rate == 3:
    feedback = input("Расскажимите, как нам стать лучше: ")
elif rate == 4:
    feedback = input("Расскажимите, почему не 5: ")
else:
    feedback = input("Расскажимите, за что похвалить оператора: ")

print(feedback)