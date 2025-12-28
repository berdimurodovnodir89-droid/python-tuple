orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
order = []

for ord in orders:
    if ord[0] % 2 == 0:
        order.append(ord)
print(order)