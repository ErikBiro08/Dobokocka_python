import random  #Behívjuk a random függvényt

print('Dobókocka projekt:')

for i in range(20):
    dobk1 = random.randint(1,6)     
    dobk2 = random.randint(1,6)     

eredmeny = dobk1 + dobk2

print('Az első kocka eredménye: ', dobk1)               #első dobás eredménye
print('A másokdik kocka eredménye: ', dobk2)            #második dobás eredménye
print('A két dobókocka dobási eredménye: ', eredmeny)   #A két kocka eredménye

