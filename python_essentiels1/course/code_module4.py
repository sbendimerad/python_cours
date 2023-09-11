## Module 4 :  Les fonctions

print("Enter a value :")
a = int(input())
print("Enter a value :")
b = int(input())
print("Enter a value :")
c = int(input())


def message():  #définition de la fonction                   
    print("Enter a value: ")    #corps

message() #invocation de la fonction
a = int(input())
message() #invocation de la fonction
b = int(input())
message() #invocation de la fonction
c = int(input())


## Module 4 : Les fonctions (Paramètres)

def hello(name):    #définition de la fonction
    print("Hello,", name)    #corps

name_user = input("Enter your name: ")
hello(name_user)    #invocation

#invocation de hello
hello()


def hello(a):    #définition de la fonction
    print("Hello,", a)    #corps

hello("sabrine")    #invocation


def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)


## Module 4 : Les fonctions (Arguments positionnels)

def message(text, value):
    print("Enter", text, "value", value)


message("telephone", 0102030405)
message("price", 5)
message("number1", "number2")


## Module 4 : Les fonctions (Arguments mots clés)

def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)


introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke")


## Module 4 : Les fonctions (Arguments mixtes)

def adding(a, b, c):
    print("la somme de",a,b,c,"est", a + b + c)

adding(3, c = 1, b = 2) 
adding(3, a = 1, b = 2) #Erreur1
adding(a = 1, b = 2,3)  #Erreur2

## Module 4 : Les fonctions (Paramètres par défaut)

def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)


introduction() #Erreur 

#invocation par argument positionnel ou mot clé
introduction("JOE") 
introduction(firstName="Joe") 

#possible d'écraser la valeur du parmaètre par défaut
introduction("JOE","Williams")
introduction("JOE",lastName="Williams")



def introduction(firstName="John", lastName="Smith"):
    print("Hello, my name is", firstName, lastName)
    
introduction()
introduction(lastName="Hopkins")


## Module 4 : Les fonctions (return)
fonctions 
#Ne renvoie rien
x = print("hello")
print(x)


## Module 4 : Les fonctions (Les listes)

#Renvoie le type de liste1
liste1 = []
x= type(liste1)
print(x)


#La fonction retourne None
def carre(valeur):
    valeur * valeur

x = carre(5)
print(x)

#La fonction retourne un résultat
def carre(valeur):
    return valeur * valeur

x = carre(5)
print(x)


#Return stop l'exécution
def happy_new_year(wishes = True):
    print("Hey...")
    if wishes == False:
        return
    
    print("Happy New Year!")

happy_new_year()
happy_new_year(False)


## Module 4 : Les fonctions (Les listes)

#Liste comme argument
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s

list_sum([5, 4, 3])
list_sum(5) #Erreur car objet non itérable


#Liste comme résultat
def strangeListFunction(n):
    strangeList = []
    for i in range(0, n):
        strangeList.insert(0, i)
    return strangeList

strangeListFunction(5)


## Module 4 : Les fonctions (Le scope)

#Exemple1
def scopeTest():
    x = 123
scopeTest()
print(x)

#Exemple2
def myFunction():
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

#Exemple3
def myFunction():
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

def myFunction():
    global var
    var = 2
    print("Do I know that variable?", var)
var = 1
myFunction()
print(var)

## Module 4 : Les types (Tuple)
myTuple = (1, 10, 100, 1000)

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])
print(myTuple[:-2])

"""
for elem in myTuple:
    print(elem)"""


myTuple = (1, 10, 100)
print(len(myTuple))

t1 = myTuple + (1000, 10000)
t2 = myTuple * 3
print(t1)
print(t2)

print(10 in myTuple)
print(-10 not in myTuple)


## Module 4 : Les types (Dictionnaire)

dictionary = {"cat" : "chat", "dog" : "chien"}
phone_numbers = {'boss' : 55512, 'Suzy' : 22657}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['cat'])
print(phone_numbers['Suzy'])

len(dictionary)


dictionary = {"cat" : "chat", "dog" : "chien"}
words = ['cat', 'lion', 'horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")



dictionary = {"cat" : "chat", "dog" : "chien"}
for key in dictionary.keys():
    print(key, "->", dictionary[key]


dictionary = {"cat" : "chat", "dog" : "chien"}
for french in dictionary.values():
    print(french)


dictionary = {"cat" : "chat", "dog" : "chien"}
for english, french in dictionary.items():
    print(english, "->", french)


#modifier un dictionnaire
dictionary = {"cat" : "chat", "dog" : "chien"}
dictionary['cat'] = 'minou'
print(dictionary)

#ajouter une valeur à un dictionnaire
dictionary = {"cat" : "chat", "dog" : "chien"}
dictionary['swan'] = 'cygne'
print(dictionary)

#ajouter une valeur à la fin du dictionnaire
dictionary = {"cat" : "chat", "dog" : "chien"}
dictionary.update({"duck" : "canard"})
print(dictionary)


#supprimer une valeur d'un dictionnaire
dictionary = {"cat" : "chat", "dog" : "chien"}
del dictionary['dog']
print(dictionary)

#supprimer la derni_re valeur d'un dictionnaire
dictionary.popitem()
print(dictionary)    

#supprimer un dictionnaire
del dictionary

for key in sorted(dictionary.keys()):

## Module 4 : Les exceptions
#
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
#
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 
#
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')

