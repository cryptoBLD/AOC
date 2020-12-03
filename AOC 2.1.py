read = open("passwords.txt", "r")
read1 = read.read()
amountyes = 0
num1 = 0
line1 = 0
amopasswd = 1000
while num1 < amopasswd:
    line1 = read1.splitlines()[num1]
    char = line1.split()[1]
    finalchar = char.replace(':', '')
    passwd = line1.split()[2]
    amount = passwd.count(finalchar)
    minmax = line1.split()[0]
    small = minmax.split('-')[0]
    big = minmax.split('-')[1]
    if int(small) <= int(amount) and int(big) >= int(amount):
        amountyes = amountyes + 1
        num1 = num1 + 1
    else:
        num1 = num1 + 1
print(amountyes)

