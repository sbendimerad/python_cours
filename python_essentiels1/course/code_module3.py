## Module 3 : Les opérateurs de comparaison

#1
2 == 2    
2 == 2.
1 == 2
                     
var=2
var == 0

1 > 2
1 >= 2
1 != 2
answer = 5 != 2 

## Module 3 : Les conditions

#1
reponse = "B"

if reponse == "B": #Si condition renvoie True
    print("hello") #J'affiche Hello, sinon rien

if reponse == "B": #Si condition renvoie True
    print("hello") #action1 soumise à condition
    print("hey")   #action2 soumise à condition

if reponse == "B": #Si condition renvoie True
    print("hello") #action1 soumise à condition
    print("hey")   #action2 soumise à condition
print("hi") #action non soumise à condition


#2
if reponse == "B": #Si condition renvoie True
    print("hello") #J'affiche Hello
else:			   #Si condition renvoie False
    print("hi")	   #J'affiche hi


if reponse == "B":
    print("hello")
elif reponse == "C":
    print("hi")
elif reponse == "D":
    print("hey")
else:
    print("end")


## Module 3 : Les boucles (While)

#1
user_answer = "A"

while user_answer = "A":
    print("Hello") 

#2
odd_numbers = 0
even_numbers = 0

# read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number != 0:
    # check if the number is odd
    if number % 2 == 1:
        # increase the odd_numbers counter
        odd_numbers += 1
    else:
        # increase the even_numbers counter
        even_numbers += 1
    # read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


#3
#Version 1
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#Version simplifiée
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)



## Module 3 : Les boucles (For)

#1
"""
for element in sequence:
    action1"""

#2
chaine = "Bonjour les ZER0S"
for lettre in chaine:
    print(lettre)

#2
for i in range(10):
    print("The value of i is currently", i)


for i in range(2, 8):
    print("The value of i is currently", i)


for i in range(0, 10,2 ):
    print("The value of i is currently", i)


## Module 3 : Les boucles (Le mot clé break)

#1
while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break


## Module 3 : Les boucles (break et continue)

#1
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

nt("The continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

## Module 3 : Les boucles (Avec else)

#1
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


for i in range(5):
    print(i)
else:
    print("else:", i)


## Module 3 : Les opérateurs de logique 

#1
a = 5
b= 10

if a>=2 and b<=8:
    print("a et b respectent la condition")
else:
    print("condition non respectée")



if a>0 or b>0:
    print("a ou b ou les 2 sont valide")
else:
    print("condition non respectée")


## Module 3 : Les listes 

#1

ma_liste = list() 

#On crée une liste vide V2
ma_liste = [] 

#Liste avec types différents
ma_liste = [1, 3.5, "une chaine", []]

# On crée une liste avec des entiers
ma_liste = [1, 2, 3, 4, 5] 
print(ma_liste)

#On accede au 1er element de la iste
print(ma_liste[0]) 

#Assigner 111 au 1er element de la liste
ma_liste[0] = 111
print(ma_liste) 

#Assigner la valeur de l'element 5 à 2
ma_liste[1] = ma_liste[4] 
print(ma_liste) 

## Module 3 : Les listes (Fonctions/Méthodes) 

#1
len(ma_liste)
del ma_liste[1]

numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])

#2
numbers.append(56) # On ajoute 56 en fin de la liste
numbers

chaine1 = "une petite phrase"
chaine2 = chaine1.upper() # On met en majuscules chaine1
chaine1  # pas été modifiée par la méthode upper
chaine2  # modifiée par la méthode upper

#3
numbers = [111, 7, 2, 1]
###
numbers.append(4)
numbers2 = numbers.append(-15)
print(numbers) # modifiée
print(numbers2) # Rien ! Retourne None
###
numbers.insert(0, 222)
print(len(numbers))
print(numbers)


## Module 3 : Les listes (Itérations) 

#1
myList = ["white", "purple", "blue"]
for color in myList: 
	print(color) 

#Liste vide
myList = [] 

#range()
for i in range(5):
    myList.append(i + 1)
print(myList) 	



#len()
myList = [10, 1, 8, 3, 5]
total = 0
for i in range(len(myList)):
    total += myList[i]
print(total)

#i comme copie de valeurs
for i in myList: 
	total += i 
print(total)


## Module 3 : Les listes (Permutations) 

#1
#Exemple 1
variable1 = 1
variable2 = 2
variable2 = variable1
variable1 = variable2

#Variable intermediaure
variable1 = 1
variable2 = 2
auxiliary = variable1
variable1 = variable2
variable2 = auxiliary

#A la manière python
variable1 = 1
variable2 = 2
variable1, variable2 = variable2, variable1


#2
#Permutation simple avec liste
myList = [10, 1, 8, 3, 5]

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print(myList)

#Permutation complexe avec liste
myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)



## Module 3 : Algorithmes de tri(Tri à bulles) 

#bubble sort en pseudo code
Je recommence jusqua trier ma liste :
	pour i de 1 à taille(ma_liste -1)
       si T[i + 1] < T[i]
           echanger_(T[i + 1], T[i])


#bubble sort en python
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # a little fake, need it to enter the while loop

while swapped:
    swapped = False # no swaps
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)

#bubble sort interactif en python
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("Sorted:")
print(myList)



## Module 3 : Les listes

lst = [5, 3, 1, 2, 4]
lst.reverse()
print(lst) 
lst.sort()
print(lst)

lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)

ma_liste1 = [1, 2, 3]
ma_liste2 = ma_liste1
ma_liste2.append(4)
print(ma_liste2)
print(ma_liste1)

#Copier toute la liste
ma_liste1 = [1, 2, 3]
ma_liste2 = ma_liste1[:]
ma_liste2.append(4)
print(ma_liste2)
print(ma_liste1)

#Copier une partie de la listee
ma_liste1 = [10, 8, 6, 4, 2]
ma_liste2 = ma_liste1[1:3]
print(ma_liste1)
print(ma_liste2)


#On peut omettre le 0 au debut du slice
myList = [10, 8, 6, 4, 2]
newList = myList[0:3]
newList = myList[:3]
print(newList)

#On peut omettre la fin du slice
myList[start:]
myList[start:len(myList)]

myList = [10, 8, 6, 4, 2]
newList = myList[3:]
newList = myList[3:len(myList)]
print(newList)

#Del sur plusieurs elements
myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

#Del sur tous les elements
myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)

#Les operateurs in et not in
myList = [0, 3, 12, 8, 2]
print(5 in myList)
print(5 not in myList)
print(12 in myList)


## Module 3 : Les listes (list comprehension)

"""
nouvelle_squence = [expression for element in ancienne_squence if condition]

for element in ancienne_squence:
    if condition:
        expression

"""


liste_origine = [0, 1, 2, 3, 4, 5]

#Boucle for classique
resultat=[]
for nb in liste_origine :
	resultat.append(nb**2)
print(resultat)

#List comprehesion
resultat = [nb**2 for nb in liste_origine]
print(resultat)

#List comprehension avec condition
liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = [nb for nb in liste_origine if nb % 2 == 0]
print(resultat)

L = [[1, 2,4], [3, 4, 5]]
len(L)
L[0][1]

#Afficher les elements avec for
for i in L:
    for j in i:
        print(j)

#Afficher les elements avec list comprehensions
resultat = [[j for j in i] for i in L]



# Syntaxe d'une fonction
def nom_de_la_fonction(paramètres):
	instructions
