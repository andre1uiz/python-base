#!/app/python-base/.venv/bin/python

#numbers = [1, 2, 3, 4, 5, 6, ]

numbers = range(1, 11) #start, stop, step

#Iterable for loop - laço for
# for number in numbers:
#     if number % 2 == 0:
#         print(number)
#     else:    
#         continue
#     #   break


#     print("mais numeros impressos")


# original = [1, 2, 3]
# dobrada = []
# Com laço

# for n in original:
#     dobrada.append(n * 2)

# print(dobrada)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# List comprehension
# dobrada = [n * 2 for n in original]

# print(dobrada)

# Dict comprehension
# dados = {
#     line.split(",")[0] : line.split(",")[1].strip()
#     for line.split(",") in open("emails.txt")
# }
# print(dados)

#laço while também pode ser utilizado com break e continue 