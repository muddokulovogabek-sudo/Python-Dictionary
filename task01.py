products = [
    {
        "id": 1,
        "name": "s22",
        "price": 450,
        "quantity": 3,
    },
    {
        "id": 2,
        "name": "s23",
        "price": 550,
        "quantity": 2,
    },
    {
        "id": 3,
        "name": "s24",
        "price": 650,
        "quantity": 8,
    }
]

jami = 0
for p in products:
    jami += p["price"] * p["quantity"]

eng_qimmat = products[0]
for p in products:
    if p["price"] > eng_qimmat["price"]:
        eng_qimmat = p


print("jami: ", jami)
