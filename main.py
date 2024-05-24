number = int(input("Enter a number: "))
print(number)
while number > 9:
    temp_number = str(number)
    number = 1
    for num in temp_number:
        number *= int(num)
    print(number)