from typing import Any
from _pytest.python_api import raises

import pytest

class Queue():
    data1 = None
    data2 = None

    def is_empty(self) -> bool:
        return self.data1 is None

    def push(self, item: Any) -> None:
        if self.is_empty():
            self.data1 = item
            return
        self.data2 = item

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Can't pop from empty queue")
        if self.data2 is not None:
            temp = self.data2
            self.data2 = None
        else:
            temp = self.data1
            self.data1 = None
        return temp

def test_is_empty():
    queue = Queue()
    assert queue.is_empty()

def test_push():
    queue = Queue()
    assert queue.is_empty()
    
    queue.push(0)
    assert not queue.is_empty()

def test_push_pop():
    queue = Queue()
    queue.push(0)
    queue.pop()
    assert queue.is_empty()

def test_push_pop_return():
    queue = Queue()
    queue.push(0)
    assert queue.pop() == 0

def test_pop_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.pop()

def test_push_push_pop_pop():
    queue = Queue()
    queue.push(0)
    queue.push(1)
    queue.pop()
    queue.pop()
    assert queue.is_empty()