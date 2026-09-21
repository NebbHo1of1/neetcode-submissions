from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {}
        seen = set()
        count = 0
        queue = deque()
    
        for i in range(n):
            adjlist[i] = []

        for j, k in edges:
            adjlist[j].append(k)
            adjlist[k].append(j)

        for node in adjlist:
            if node not in seen:
                seen.add(node)
                count += 1
                queue.append(node)

            while queue:
                node = queue.popleft()

                for curr in adjlist[node]:
                    if curr not in seen:
                        seen.add(curr)
                        queue.append(curr)
        return count 



            
        
        




            
        
        
