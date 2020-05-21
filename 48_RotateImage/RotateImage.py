class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        element_count = len(matrix)
        hash_mapping = {}
        for row in range(element_count):
            for col in range(element_count):
                hash_mapping[row*element_count+col] = matrix[row][col]
                if ((element_count-1-col)*element_count + row) not in hash_mapping.keys():
                    matrix[row][col] = matrix[element_count-col-1][row]
                else:
                    matrix[row][col] = hash_mapping[(
                        element_count-1-col)*element_count + row]

        # print(matrix)
        return matrix
