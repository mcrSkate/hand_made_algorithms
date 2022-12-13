class MinNode:
    def __init__(self, val = None) -> None:
        self.val = val
        self.min = self
        self.next = None