class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.root = None

    def push(self, value) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            root_node = self.root
            self.root = Node(value)
            self.root.next = root_node

    def pop(self):
        if self.root is None:
            return
        pop_data = self.root.data
        self.root = self.root.next
        return pop_data

    def top(self):
        if self.root is not None:
            return self.root.data
        return -1

    def is_empty(self) -> bool:
        if self.root is None:
            return True
        return False


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_in = "[{("
        bracket_out = "]})"

        bracket_stack = Stack()

        for i in s:
            if i in bracket_in:
                bracket_stack.push(bracket_in.index(i))
            elif i in bracket_out:
                if bracket_stack.top() == bracket_out.index(i):
                    bracket_stack.pop()
                else:
                    return False

        if bracket_stack.is_empty():
            return True
        return False


if __name__ == '__main__':
    print(Solution().isValid("{}(())"))
    print(Solution().isValid("{}(())]"))
