import pytest

class Queue():
    @staticmethod
    def is_empty():
        return True

def test_is_empty():
    queue = Queue()
    assert queue.is_empty()