read = open("passwords.txt", "r")
read1 = read.read()
amountyes = 0
num = 0
line1 = 0
amopasswd = 1000
while num < amopasswd:
    line1 = read1.splitlines()[num]
    char = line1.split()[1]
    finalchar = char.replace(':', '')
    passwd = line1.split()[2]
    amount = passwd.count(finalchar)
    wholelengh = len(passwd)
    nbr = line1.split()[0]
    num1 = nbr.split('-')[0]
    num1 = int(num1) - 1
    num2 = nbr.split('-')[1]
    num2 = int(num2) -1
    if int(num1) > int(wholelengh) or int(num2) > int(wholelengh):
        num = num + 1
    else:
        cha1 = passwd[int(num1)]
        cha2 = passwd[int(num2)]
        if int(num1) > int(wholelengh) or int(num2) > int(wholelengh):
            num = num + 1
        elif finalchar == cha1 or finalchar == cha2:
            if finalchar == cha1 and finalchar == cha2:
                num = num + 1
            else:
                num = num +1
                amountyes = amountyes +1
        else:
            num = num + 1
print(amountyes)
