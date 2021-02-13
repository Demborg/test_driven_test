from dataclasses import dataclass
from typing import Any, Optional
from _pytest.python_api import raises

import pytest

@dataclass
class LinkItem():
    data: Any 
    next_item: "LinkItem"

class Queue():
    first: Optional[LinkItem]
    last: Optional[LinkItem]

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def is_empty(self) -> bool:
        return self.first is None

    def push(self, item: Any) -> None:
        if self.is_empty():
            self.first = LinkItem(item, None)
            self.last = self.first
            return
        temp = LinkItem(item, None)
        self.last.next_item = temp
        self.last = temp

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Can't pop from empty queue")        
        else:
            temp = self.first
            self.first = self.first.next_item
        return temp.data

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

def test_push_push_pop_pop_return():
    queue = Queue()
    queue.push(0)
    queue.push(1)
    assert queue.pop() == 0
    queue.push(2)
    assert queue.pop() == 1
    