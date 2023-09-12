## Module 1 : Classes et objets

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
