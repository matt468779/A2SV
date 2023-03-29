class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        word1_dict = {}
        word2_dict = {}
        for w in word1:
            word1_dict[w] = word1_dict.get(w, 0) + 1
        for w in word2:
            word2_dict[w] = word2_dict.get(w, 0) + 1

        distinct1 = temp1 = len(word1_dict)
        distinct2 = temp2 = len(word2_dict)

        for char1 in word1_dict:
            temp1, temp2 = distinct1, distinct2
            if word1_dict[char1] == 1:
                temp1 = distinct1 - 1
            if char1 not in word2_dict:
                temp2 = distinct2 + 1
            for char2 in word2_dict:
                t1, t2 = temp1, temp2

                if char2 not in word1_dict or (word1_dict[char1] == 1 and char1 == char2):
                    temp1 += 1
                if word2_dict[char2] == 1 and char1 != char2:
                    temp2 -= 1
                
                if temp1 == temp2:
                    return True
                temp1, temp2 = t1, t2
        return False