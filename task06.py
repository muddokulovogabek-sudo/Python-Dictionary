data = {"name": "Ali", "age": 25, "city": "Tashkent"}
key = input("Kalit nomini kiriting: ")

if key in data:
    print(data[key])
else:
    print("Topilmadi")