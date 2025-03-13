import random
from collections import Counter

def dobas():
    
    return random.randint(1, 6)

def kiir_eredmeny(dobk1, dobk2, eredmeny, index, f):
    
    print(f'Dobás {index}:')
    print(f'  Az első kocka eredménye: {dobk1}')
    print(f'  A második kocka eredménye: {dobk2}')
    print(f'  A két dobókocka dobási eredménye: {eredmeny}')
    
    # Fájlba írás
    f.write(f'Dobás {index}:\n')
    f.write(f'  Az első kocka eredménye: {dobk1}\n')
    f.write(f'  A második kocka eredménye: {dobk2}\n')
    f.write(f'  A két dobókocka dobási eredménye: {eredmeny}\n\n')

def kiértékel(dobk1, dobk2, eredmeny):
    
    if dobk1 == dobk2:
        print('Ez aztán ritka!')
    elif eredmeny == 12:
        print('Nagyon szerencsés vagy!')  
    else:
        print('Ezek csak sima dobások')

def main():
    
    eredmenyek = [] 
    with open("Eredmenyek.txt", "w", encoding="UTF-8") as f:
        print('Dobókocka projekt:\n')
        
        for i in range(1, 21): 
            dobk1 = dobas()  
            dobk2 = dobas()  
            eredmeny = dobk1 + dobk2 
            
            kiir_eredmeny(dobk1, dobk2, eredmeny, i, f)  
            kiértékel(dobk1, dobk2, eredmeny) 
                        
            eredmenyek.append(eredmeny)
                   
        atlag = sum(eredmenyek) / len(eredmenyek)        
        f.write(f'\nStatisztikai összegzés:\n')
        f.write(f'  Az átlagos dobás eredménye: {atlag:.2f}\n')
        f.write(f'  A legnagyobb dobás: {max(eredmenyek)}\n')
        f.write(f'  A legkisebb dobás: {min(eredmenyek)}\n')
        f.write(f'  A dobások átlaga: {atlag:.2f}\n')

if __name__ == "__main__":
    main()
