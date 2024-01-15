sequence = input("Enter a sequence of comma-separated numbers: ")

list = sequence.split(',')
list = [int(num) for num in list] 

tuple = tuple(list)

print("List: ", list)
print("Tuple: ", tuple)
