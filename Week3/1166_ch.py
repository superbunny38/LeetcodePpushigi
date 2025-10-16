class Node:
    def __init__(self,val=None):
        self.val = val
        self.children = dict()
        
class FileSystem:
    
    def __init__(self):
        self.root = Node()
        
    def createPath(self, path: str, value: int) -> bool:
        if not path or path == "/" or path[-1] == "/":
          return False
        path_list = path.split('/')[1:]
        
        node = self.root
        for path_ in path_list[:-1]:
            if path_ in node.children:
                node = node.children[path_]
            else:
                return False
            
        if path_list[-1] in node.children:
            return False
        else:
            node.children[path_list[-1]] = Node(val=value)
            return True

    def get(self, path: str) -> int:
        path_list = path.split('/')[1:]
        cur = self.root
        for path_ in path_list:
            if path_ not in cur.children:
                return -1
            cur = cur.children[path_]
        return cur.val


# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
param_1 = obj.createPath("/leet",1)
print(param_1)
param_2 = obj.createPath("/leet/code",2)
print(param_2)
param_2 = obj.get("/leet/code")