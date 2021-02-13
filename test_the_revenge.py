from typing import Any

import pytest

class Queue():
    data = None

    def is_empty(self) -> bool:
        return self.data is None

    def push(self, item: Any) -> None:
        self.data = item

    def pop(self) -> Any:
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
    