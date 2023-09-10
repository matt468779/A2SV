class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split = path.split('/')
        res = []
        for file in path_split:
            if file == '' or file == '.':
                continue
            elif file == '..':
                if res:
                    res.pop()
            else:
                res.append(file)
        
        return '/' + '/'.join(res)