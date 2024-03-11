class stack(object):
    def __init__(self):
        self.top = -1
        self.array = [None]*10000
 
    def push(self, data: int) -> None:
        if self.top != 9999:
            self.top += 1
            self.array[self.top] = data
            return

        raise Exception("Stack is Full")
    
    def pop(self) -> int:
        if self.top != -1:
            v = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            return v
        raise Exception("stack is empty")
    

if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.pop()) 


        