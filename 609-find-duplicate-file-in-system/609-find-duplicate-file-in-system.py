class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dirDic = {}
        for path in paths:
            files = path.split()
            for file in files[1:]:
                content = file.split('(')
                if content[1] in dirDic:
                    dirDic[content[1]].append(files[0] + '/' + content[0])
                else:
                    dirDic[content[1]] = [files[0] + '/' + content[0]]
        
        res = []
        for key in dirDic:
            if len(dirDic[key]) > 1:
                res.append(dirDic[key])
        
        return res
            