#immutable_var = 1, 2, 3, True, "Ананас"
#print(immutable_var)
#immutable_var [0] = 200 #нельзя изменить элементы кортежа, не придав значения что именно мы хотим заменить
mutable_list = ([9, 6, 3], True, "Дверь")
print(mutable_list)
mutable_list [0][0] = 2
mutable_list [0][1] = 5
mutable_list [0][2] = 7
mutable_list [0][1] = False
mutable_list [0][2] = "Окно"
print(mutable_list)
