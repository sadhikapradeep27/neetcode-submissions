class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for i in range(1, numRows):
            prev_row = result[-1]
            new_row = [1]  # every row starts with 1
            
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            
            new_row.append(1)  # every row ends with 1
            result.append(new_row)
        
        return result