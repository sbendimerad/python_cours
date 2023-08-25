import unittest
from solution import Queue, QueueError, SuperQueue 

class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        que = SuperQueue()
        que.put(1)
        que.put("dog")
        que.put(False)

        self.assertEqual(que.get(), 1)
        self.assertEqual(que.get(), "dog")
        self.assertEqual(que.get(), False)

        with self.assertRaises(QueueError):
            que.get()

        self.assertTrue(que.isempty())

if __name__ == '__main__':
    unittest.main()
