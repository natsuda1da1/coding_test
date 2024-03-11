from __future__ import annotations

class Node(object):
    def __init__(self, data: int = None, next_node: Node = None):
        self.data = data
        self.next_node = next_node
    
class LinkedList(object):
    def __init__(self, head: Node = Node()):
        self.head = head
    
    def append(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node 
        current.next_node = new_node
    
    def delete(self, data: int):
        if self.head.data == data:
            self.head = self.head.next_node
            return

        current = self.head
        while current.next_node:
            if current.next_node.data == data:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node
        
        print(f"Node with data {data} not found")
        
    def obprint(self):
        current = self.head
        string = ""
        while current:
            string += str(current.data) + " -> "
            current = current.next_node
        string += "None"
        print(string)

if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.obprint()
    l.delete(1)
    l.obprint()
    l.delete(2)
    l.obprint()
    l.delete(3)
