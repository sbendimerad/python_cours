from solution import CountingStack

def test_counting_stack():
    stk = CountingStack()
    for i in range(100):
        stk.push(i)
        stk.pop()
    assert stk.get_counter() == 100

if __name__ == '__main__':
    test_counting_stack()
    print("All tests passed!")
