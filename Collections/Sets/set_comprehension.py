# Criando
set_1 = {1, 2}
set_2 = {3, 4}

set_comprehension = {i * i for i in range(0,10)}
print(set_comprehension)

set_comprehension_2 = {i for i in set_1.union(set_2)}
print(set_comprehension_2)