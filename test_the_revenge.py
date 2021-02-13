from typing import Any

import pytest

class Queue():
    empty = True

    def is_empty(self) -> bool:
        return self.empty

    def push(self, item: Any) -> None:
        self.empty = False

def test_is_empty():
    queue = Queue()
    assert queue.is_empty()

def test_push():
    queue = Queue()
    assert queue.is_empty()
    
    queue.push(0)
    assert not queue.is_empty()