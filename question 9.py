lb_kg_conversion = 0.45359237

N = int(input('enter the number of students'))

L1 = []

for i in range(N):
    L1.append(int(input('enter the element ')))

output = [lb_kg_conversion * i for i in L1]

print(output)
