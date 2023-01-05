#input

def and_gate(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0

def or_gate(a,b):
    if a==0 and b==0:
        return 0
    else:
        return 1

def xor_gate(a,b):
    if a==b:
        return 0
    else:
        return 1
print('A\tB\tA & B')
for i in range(2):
    for j in range(2):
        a=i
        b=j
        print(f'{a}\t{b}\t{and_gate(a,b)}')

print("")

print('A\tB\tA | B')
for i in range(2):
    for j in range(2):
        a=i
        b=j
        print(f'{a}\t{b}\t{or_gate(a,b)}')
print("")

print('A\tB\tA ^ B')
for i in range(2):
    for j in range(2):
        a=i
        b=j
        print(f'{a}\t{b}\t{xor_gate(a,b)}')
print("")

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

print("A & B =",and_gate(a,b))
print("A | B =",or_gate(a,b))
print("A ^ B =",xor_gate(a,b))

#theory for all gates

#1. AND gate:  A AND B = 1 if A = 1 and B = 1, otherwise 0
#2. OR gate:  A OR B = 1 if A = 1 or B = 1, otherwise 0
#3. XOR gate:  A XOR B = 1 if A ≠ B, otherwise 0