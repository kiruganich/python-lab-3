class Stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._stack[-1]

    def is_empty(self):
        return len(self._stack) == 0

    def __len__(self):
        return len(self._stack)


class MinStack(Stack):
    def __init__(self):
        super().__init__()

        self._min_stack = []

    def push(self, x):
        super().push(x)

        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)

    def pop(self):
        val = super().pop()
        if val == self._min_stack[-1]:
            self._min_stack.pop()
        return val

    def min(self):
        if self.is_empty():
            raise ValueError("min from empty stack")
        return self._min_stack[-1]
