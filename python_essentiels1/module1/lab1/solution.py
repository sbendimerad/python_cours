class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        # Call the parent class constructor
        Stack.__init__(self)
        # Initialize the counter to zero
        self.__counter = 0

    def get_counter(self):
        # Return the current value of the counter
        return self.__counter

    def pop(self):
        # Update the counter
        self.__counter += 1
        # Call the parent class pop method
        return Stack.pop(self)

	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
