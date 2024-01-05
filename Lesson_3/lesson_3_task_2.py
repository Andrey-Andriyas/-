from smartphone import Smartphone


phone1 = Smartphone("Huawei - ", "P 60 Pro - ", "+7 913 111-11-11")
phone2 = Smartphone("Samsung - ", "Galaxy S23 - ", "+7 914 222-22-22")
phone3 = Smartphone("Google - ", "Pixel 7 - ", "+7 915 333-33-33")
phone4 = Smartphone("Xiaomi - ", "Mi 13 - ", "+7 916 444-44-44")
phone5 = Smartphone("Apple - ", "iPhone 14 Pro  - ", "+7 917 555-55-55")

catalog = [phone1, phone2, phone3, phone4, phone5]


for phone in catalog:
    print(phone.brand, phone.model, phone.number)
