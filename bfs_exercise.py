def bfs(Data, start, end, visited=[]):
    queue = [start]
    
    while queue:
        currentnode = queue.pop(0)
        if currentnode==end:
            print("Path exists!")
            print("Path : " + "->".join(visited) + "->"+end)
            return
        visited.append(currentnode)
        
        for i in Data[currentnode] - set(visited):
            queue.append(i)
    print("Path does not exist!")    
    return
        
        

        
if __name__ == '__main__':
  Data = {'A': {'B'},
        'B': {'C', 'D'},
        'C': {'E'},
        'D': {'E'},
        'E': {'F'},
        'F': set()}
  bfs(Data, 'A', 'D')

