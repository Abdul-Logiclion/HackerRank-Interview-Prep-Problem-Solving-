class Editor:
    def __init__(self):
        self.S = ""
        self.states = []

    def print_k(self, k):
        if 1 <= k <= len(self.S):
            print(self.S[k - 1])

    def append(self, s):
        self.states.append(self.S)
        self.S += s

    def delete(self, k):
        if k > 0:
            self.states.append(self.S)
            self.S = self.S[:-k]

    def undo(self):
        if self.states:
            self.S = self.states.pop()

if __name__ == "__main__":
    Q = int(input())
    editor = Editor()
    for _ in range(Q):
        query = input().split()
        operation = int(query[0])
        if operation == 1:
            editor.append(query[1])
        elif operation == 2:
            editor.delete(int(query[1]))
        elif operation == 3:
            editor.print_k(int(query[1]))
        elif operation == 4:
            editor.undo()