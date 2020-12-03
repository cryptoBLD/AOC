count = 0
line = 0
y = -3
ground = []
with open('map.txt', 'r') as file
  for i in file
    line +=1
    y += 3
    if i[y%31] == '#'
      count += 1
print(count)