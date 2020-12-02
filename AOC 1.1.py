read = open("test.txt", "r")
read1 = read.read()
result = 0
needed = 2020
num1 = 0
num2 = 1
max = 199
line1 = 0
line2 = 0
while result != needed:
    line1 = read1.splitlines()[num1]
    line2 = read1.splitlines()[num2]
    if int(line1) + int(line2) != needed and num2 != max:
        num2 = num2 + 1
        result = int(line1) + int(line2)
    elif num2 == max and int(line1) + int(line2) != needed:
        num1 = num1 + 1
        num2 = 0
    else:
        result = int(line1) + int(line2)
print(line1)
print(line2)
print(int(line1)*int(line2))