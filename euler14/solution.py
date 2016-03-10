
def numberofnumbers(i, numbers):
    if i == 1:
        return len(numbers)
    
    elif i % 2 == 0:
        # Even, /= 2
        i  = i // 2
        numbers.append(i)
        return numberofnumbers(i, numbers)
    
    else:
        # Odd, *3 + 1
        i = i * 3 + 1
        numbers.append(i)
        return numberofnumbers(i, numbers)


longestseries = 0
numberlong = 0
for i in range(1, 1000000):
    a = []
    a.append(i)
    serie = numberofnumbers(i, a)
    if serie > longestseries:
        longestseries = serie
        numberlong = i
        

print(numberlong, longestseries)
    
