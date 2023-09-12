## Module 3 : Classes et objets

#
class This_Is_A_Class:
     pass

this_is_an_object = This_Is_A_Class()

#
stack = []
def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

Module 3 : L’encapsulation 
#
class Stack:
    def __init__(self):
        self.stack_list = []

stack_object1 = Stack()
stack_object3 = Stack()
print(len(stack_object1.stack_list))
print(len(stack_object2.stack_list))


#
class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object1 = Stack()
stack_object3 = Stack()
print(len(stack_object1.stack_list))
print(len(stack_object2.stack_list))

#
class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())


#
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop())


## Module 3 : L'héritage

#
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

#
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())


## Module 3 : Variables d'instance

#
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val

object_1 = ExampleClass()
object_2 = ExampleClass(2)

object_2.set_second(3)

object_3 = ExampleClass(4)
object_3.third = 5

print(object_1.__dict__)
print(object_2.__dict__)
print(object_3.__dict__)


#
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

object_1 = ExampleClass()
object_2 = ExampleClass(2)

print(object_1._ExampleClass__first)


# Variables de classe
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


object_1 = ExampleClass()
object_2 = ExampleClass(2)
object_3 = ExampleClass(4)

print(object_1.__dict__, object_1.counter)
print(object_2.__dict__, object_2.counter)
print(object_3.__dict__, object_3.counter)

## Module 3 : Méthodes

#
class MyClass:
    def regular_method(self, parameter):
        print("regular method", parameter)
        
    
    def __init__(self, value):
        self.initial_value = value
        print("Constructor called with value", value)

obj = MyClass(5)
obj.regular_method("Hello")


## Module 3 : Méthodes spéciales

#
class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

print(Sub.__name__)
print(Sub.__module__)
print(Sub.__bases__)



## Module 3 : Méthodes spéciales (__str__)

#
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

sun = Star("Sun", "Milky Way")
print(sun)

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


sun = Star("Sun", "Milky Way")
print(sun)

## Module 3 : L’héritage

#
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

## Module 3 : Gestion des propriétés et méthodes

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)
        Super.__init__(self, name)

obj = Sub("Andy")
print(obj)

## Module 3 : Propriétés et méthodes

#
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102

class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202

class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302
         
obj = Level3()
print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())

#
