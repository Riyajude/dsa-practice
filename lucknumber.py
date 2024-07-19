class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        N=len(matrix)
        M=len(matrix[0])

        rowmin=[]
        for i in range(N):
            rmin=99999
            for j in range(M):
                rmin=min(rmin,matrix[i][j])
            rowmin.append(rmin)

        colmax=[]
        for i in range(M):
            cmax=-99999
            for j in range(N):
                cmax=max(cmax,matrix[j][i])
            colmax.append(cmax)

        lucky=[]
        for i in range(N):
            for j in range(M):
                if matrix[i][j]==rowmin[i] and matrix[i][j]==colmax[j]:
                    lucky.append(matrix[i][j])
        return lucky

