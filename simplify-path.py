class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        val = path.split("/")
        
        for i in range(len(val)):
            if val[i] != "":
                if stack and val[i] == "..":
                    stack.pop()
                elif val[i] == ".." and not stack:
                    stack.append("/")
                elif val[i] == ".":
                    continue
                else:
                    if not stack:
                        v = "/"+val[i]
                        stack.append(v)
                    elif stack [-1] != "/":
                        v = "/"+val[i]
                        stack.append(v)
                    else:
                        stack.append(val[i])

        return "".join(stack) if stack else "/"