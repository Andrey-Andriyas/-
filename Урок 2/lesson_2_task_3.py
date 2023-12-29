
import math

def square(side):
    area = side*side
    print (math.ceil(area))

square(2.05)


# #вариант
# import math

# def square(side):
#     area = side * side
#     if not isinstance(side, int):
#         area = math.ceil(area)
#     print (area)

# square(2.05)