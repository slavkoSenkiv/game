import classes as c

pA = c.Character('A')
pB = c.Character('B')

print(pA.name, pA.hp_current)
print(pB.name, pB.hp_current)
for x in range(12):
    pA.attack(pB)
    print(pB.name, pB.hp_current)
print(pA.name, pA.hp_current)

