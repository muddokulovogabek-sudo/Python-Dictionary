data = {"name": "Ali", "age": 25, "city": "Tashkent"}
key = input("O‘chiriladigan kalitni kiriting: ")

if key in data:
    del data[key]
else:
    print("Bunday kalit yo‘q")

print(data)