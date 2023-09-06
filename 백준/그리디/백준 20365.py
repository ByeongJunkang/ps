N = int(input())
colors = list(input())
c = {'B':0, 'R':0}
num = 1
prev = ''
for color in colors:
    if color != prev:
        c[color] +=1
    prev = color

count = c['R']+1 if c['B']>c['R'] else c['B']+1
print(count)