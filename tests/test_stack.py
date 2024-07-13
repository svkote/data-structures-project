import pytest
from src.stack import Node, Stack


def test_node():
    n1 = Node(5)
    assert n1.data == 5
    assert n1.next_node is None

    n2 = Node('a', n1)
    assert n2.data == 'a'
    assert n2.next_node == n1


def test_stack_push():
    stack = Stack()
    stack.push('data1')
    assert stack.top.data == 'data1'

    stack.push('data2')
    assert stack.top.data == 'data2'
    assert stack.top.next_node.data == 'data1'


def test_stack_pop():
    stack = Stack()
    stack.push('data1')
    stack.push('data2')

    data = stack.pop()
    assert data == 'data2'
    assert stack.top.data == 'data1'

    data = stack.pop()
    assert data == 'data1'
    assert stack.top is None

    with pytest.raises(IndexError):
        stack.pop()
