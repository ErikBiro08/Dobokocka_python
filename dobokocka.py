import random  # Behívjuk a random függvényt


with open("Eredmenyek.txt", "w", encoding="UTF-8") as f:
    print('Dobókocka projekt:')

    # Ciklus, ami 20 alkalommal dob
    for i in range(20):
        dobk1 = random.randint(1, 6)  # Az első kocka dobásának eredménye
        dobk2 = random.randint(1, 6)  # A második kocka dobásának eredménye

        eredmeny = dobk1 + dobk2  # Az eredmény kiszámítása

        # Eredmények kiírása a képernyőre
        print('Az első kocka eredménye: ', dobk1)            
        print('A második kocka eredménye: ', dobk2)           
        print('A két dobókocka dobási eredménye: ', eredmeny)

        # Az eredmények kiírása a fájlba
        f.write(f'Dobás {i + 1}:\n')
        f.write(f'  Az első kocka eredménye: {dobk1}\n')  
        f.write(f'  A második kocka eredménye: {dobk2}\n')  
        f.write(f'  A két dobókocka dobási eredménye: {eredmeny}\n\n')
        
        if dobk1 == dobk2:
            print('Ez aztán ritka!')
        elif eredmeny == 12:
            print('Nagyon szerencsés vagy!')
        else:
            print('Ezek csak sima dobások')
