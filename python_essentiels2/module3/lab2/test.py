import unittest
from solution import Queue, QueueError 

class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        que = Queue()
        que.put(1)
        que.put("dog")
        que.put(False)

        # Check if elements are retrieved correctly
        self.assertEqual(que.get(), 1)
        self.assertEqual(que.get(), "dog")
        self.assertEqual(que.get(), False)

        # Check if QueueError is raised when trying to get from an empty queue
        with self.assertRaises(QueueError):
            que.get()

if __name__ == '__main__':
    unittest.main()
    print("All tests passed!")

