import sys
import os
import pytest

sys.path.insert(0, os.path.abspath('src'))
sys.path.insert(0, os.path.abspath('utilities'))

from src.math import factorial, factorial_rec, fib, fib_rec
from src.sorting import bubble_sort, counting_sort, bucket_sort
from src.data_structures import Stack, MinStack

class TestMath:
    """
    Тесты для factorial, factorial_rec, fib, fib_rec.
    """

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_small(self):
        assert factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_rec_zero(self):
        assert factorial_rec(0) == 1

    def test_factorial_rec_one(self):
        assert factorial_rec(1) == 1

    def test_factorial_rec_small(self):
        assert factorial_rec(5) == 120

    def test_factorial_rec_negative(self):
        with pytest.raises(ValueError):
            factorial_rec(-1)

    def test_fib_zero(self):
        assert fib(0) == 0

    def test_fib_one(self):
        assert fib(1) == 1

    def test_fib_small(self):
        assert fib(5) == 5
        assert fib(10) == 55

    def test_fib_negative(self):
        with pytest.raises(ValueError):
            fib(-1)

    def test_fib_rec_zero(self):
        assert fib_rec(0) == 0

    def test_fib_rec_one(self):
        assert fib_rec(1) == 1

    def test_fib_rec_small(self):
        assert fib_rec(5) == 5
        assert fib_rec(10) == 55

    def test_fib_rec_negative(self):
        with pytest.raises(ValueError):
            fib_rec(-1)



class TestSorting:
    """
    Тесты для bubble_sort, counting_sort, bucket_sort.
    """

    def test_bubble_sort_empty(self):
        assert bubble_sort([]) == []

    def test_bubble_sort_single(self):
        assert bubble_sort([42]) == [42]

    def test_bubble_sort_sorted(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_bubble_sort_reversed(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_bubble_sort_random(self):
        assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_bubble_sort_negative(self):
        assert bubble_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

    def test_bubble_sort_preserves_original(self):
        original = [3, 1, 4]
        sorted_list = bubble_sort(original)
        assert original == [3, 1, 4]
        assert sorted_list == [1, 3, 4]


    def test_counting_sort_empty(self):
        assert counting_sort([]) == []

    def test_counting_sort_single(self):
        assert counting_sort([42]) == [42]

    def test_counting_sort_sorted(self):
        assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_counting_sort_reversed(self):
        assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_counting_sort_random(self):
        assert counting_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_counting_sort_negative(self):
        assert counting_sort([-3, -1, -4, -1, -5]) == [-5, -4, -3, -1, -1]

    def test_counting_sort_preserves_original(self):
        original = [3, 1, 4]
        sorted_list = counting_sort(original)
        assert original == [3, 1, 4]
        assert sorted_list == [1, 3, 4]


    def test_bucket_sort_empty(self):
        assert bucket_sort([]) == []

    def test_bucket_sort_single(self):
        assert bucket_sort([0.5]) == [0.5]

    def test_bucket_sort_sorted(self):
        assert bucket_sort([0.1, 0.2, 0.3, 0.4, 0.5]) == [0.1, 0.2, 0.3, 0.4, 0.5]

    def test_bucket_sort_reversed(self):
        assert bucket_sort([0.5, 0.4, 0.3, 0.2, 0.1]) == [0.1, 0.2, 0.3, 0.4, 0.5]

    def test_bucket_sort_random(self):
        result = bucket_sort([0.3, 0.1, 0.4, 0.1, 0.5, 0.9, 0.2, 0.6, 0.5, 0.3, 0.5])
        expected = [0.1, 0.1, 0.2, 0.3, 0.3, 0.4, 0.5, 0.5, 0.5, 0.6, 0.9]
        assert result == expected

    def test_bucket_sort_preserves_original(self):
        original = [0.3, 0.1, 0.4]
        sorted_list = bucket_sort(original)
        assert original == [0.3, 0.1, 0.4]
        assert sorted_list == [0.1, 0.3, 0.4]


class TestStack:
    """
    Тесты для Stack.
    """
    def test_stack_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_stack_peek(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.peek() == 2
        assert s.peek() == 2
        assert s.pop() == 2

    def test_stack_is_empty(self):
        s = Stack()
        assert s.is_empty() is True
        s.push(1)
        assert s.is_empty() is False
        s.pop()
        assert s.is_empty() is True

    def test_stack_len(self):
        s = Stack()
        assert len(s) == 0
        s.push(1)
        assert len(s) == 1
        s.push(2)
        assert len(s) == 2
        s.pop()
        assert len(s) == 1

    def test_stack_pop_empty(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()

    def test_stack_peek_empty(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.peek()


class TestMinStack:
    """
    Тесты для MinStack.
    """
    def test_min_stack_push_pop_min(self):
        ms = MinStack()
        ms.push(3)
        assert ms.min() == 3
        ms.push(1)
        assert ms.min() == 1
        ms.push(5)
        assert ms.min() == 1
        assert ms.pop() == 5
        assert ms.min() == 1
        assert ms.pop() == 1
        assert ms.min() == 3
        assert ms.pop() == 3

    def test_min_stack_min_after_pop(self):
        ms = MinStack()
        ms.push(1)
        ms.push(2)
        ms.push(3)
        assert ms.min() == 1
        ms.pop()
        assert ms.min() == 1
        ms.pop()
        assert ms.min() == 1
        ms.pop()
        assert ms.is_empty()
        with pytest.raises(ValueError):
            ms.min()

    def test_min_stack_is_empty(self):
        ms = MinStack()
        assert ms.is_empty() is True
        ms.push(1)
        assert ms.is_empty() is False

    def test_min_stack_len(self):
        ms = MinStack()
        assert len(ms) == 0
        ms.push(1)
        assert len(ms) == 1
        ms.push(2)
        assert len(ms) == 2
        ms.pop()
        assert len(ms) == 1

    def test_min_stack_pop_empty(self):
        ms = MinStack()
        with pytest.raises(IndexError):
            ms.pop()

    def test_min_stack_peek_empty(self):
        ms = MinStack()
        with pytest.raises(IndexError):
            ms.peek()

    def test_min_stack_min_empty(self):
        ms = MinStack()
        with pytest.raises(ValueError):
            ms.min()
