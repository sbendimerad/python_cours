# Estimated time
15-30 minutes

# Level of difficulty
Easy/Medium

# Scenario
Your task is to slightly extend the Queue class' capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

* Complete the code provided.
* Run it to check whether it outputs a similar result to ours.

Below you can copy the code we used in the previous lab:
```

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

class SuperQueue(Queue):
    #
    # Write new code here.
    #
```

