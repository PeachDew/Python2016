pastfile = open("PASTRY.txt", 'r')
pastlines = pastfile.readlines()
pastfile.close()

arrayclean = []
arraypast = []

for i in pastlines:
    arrayclean.append(i.rstrip())

for i in range(0, len(pastlines), 3):
    arraypast.append([arrayclean[i][16:-1], arrayclean[i+1][15:], arrayclean[i+2][15:]])
print(arraypast)    

def soldOut():
    answer = input("Enter pastry name: ")
    for i in range(0, len(arraypast)):
        if arraypast[i][0] == answer:
            if arraypast[i][2] == '0':
                print("Sold out!")
            else:
                print("Available.")
#soldOut()

def budgetSpending():
    budget = float(input("Enter budget($): "))
    if budget < 0.8:
        return "Not enough!"
    elif budget < 0.9:
        return 'Red Bean: 1 \nAmount spent($): 0.80'
    elif budget < 1:
        return 'Peanut Butter: 1 \nAmount spent($): 0.90'
    

print(budgetSpending())
