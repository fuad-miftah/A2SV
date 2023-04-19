class ThroneInheritance:

    def __init__(self, kingName: str):
        self.adl = defaultdict(list)
        self.dead = set()
        self.adl[kingName] = []
        self.kingName = kingName
        

    def birth(self, parentName: str, childName: str) -> None:
        self.adl[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        res = []
        
        def dfs(node):
            if node not in self.dead:
                res.append(node)
            for neighbour in self.adl[node]:
                dfs(neighbour)
        
        dfs(self.kingName)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()