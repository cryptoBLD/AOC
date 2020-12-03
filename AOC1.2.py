read = open("numbers.txt", "r")
read1 = read.read()
result = 0
needed = 2020
num1 = 0
num2 = 0
num3 = 0
max = 199
line1 = 0
line2 = 0
line3 = 0
while result != needed:
    line1 = read1.splitlines()[num1]
    line2 = read1.splitlines()[num2]
    line3 = read1.splitlines()[num3]
    if int(line1) + int(line2) + int(line3) != needed and num2 != max and num3 != max:
        num3 = num3 + 1
        result = int(line1) + int(line2) + int(line3)
    elif num2 == max and int(line1) + int(line2) + int(line3) != needed:
        num1 = num1 + 1
        num2 = 0
    elif num3 == max and int(line1) + int(line2) + int(line3) != needed:
        num2 = num2 + 1
        num3 = 0
    else:
        result = int(line1) + int(line2) + int(line3)
print(line1)
print(line2)
print(line3)
print(int(line1)*int(line2)*int(line3))