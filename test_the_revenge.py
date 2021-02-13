from typing import Any
from _pytest.python_api import raises

import pytest

class Queue():
    data = None

    def is_empty(self) -> bool:
        return self.data is None

    def push(self, item: Any) -> None:
        self.data = item

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Can't pop from empty queue")
        temp = self.data
        self.data = None
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
