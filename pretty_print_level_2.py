class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(A):
        boundary = 2 * A - 1 # -1 because 1 only shows up one time 

        result = [[0 for x in range(width)] for y in range(height)]

        start_x, start_y = 0, 0
        boundary_width, boundary_height = boundary, boundary

        while start_x < boundary_width and start_y < boundary_height:
            i = start_x
            j = start_y

            # traversing the first row
            while j < boundary_width:
                result[i][j] = A
                j +=1
            boundary_width -=1
            j = boundary_width

            # traversing the last column
            while i < boundary_height:
                result[i][j] = A
                i +=1
            boundary_height -=1
            i = boundary_height

            # traversing the last row
            while j > start_y:
                result[i][j] = A
                j -=1
            start_y +=1
            # traversing the first column
            while i > start_x:
                result[i][j] = A
                i -=1
            start_x +=1

            # decrementing A
            A -=1

        return result
