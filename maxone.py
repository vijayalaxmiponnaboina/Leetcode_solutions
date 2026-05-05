class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_one=-1
        row_index=-1
        for i in range(len(mat)):
            count=mat[i].count(1)
            if count>max_one:
                max_one=count
                row_index=i
        return [row_index,max_one]