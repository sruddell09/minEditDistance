import sys
def med(source, target):
    m = len(source) + 1
    n = len(target) + 1

    matrix = [[0 for i in range(0,m)]for j in range(0,n)]

    for i in range(0,m):
        matrix[0][i] = i
    for j in range(0,n):
        matrix[j][0] = j

    for j in range(1,n):
        for i in range(1,m):
            if source[i - 1] == target[j - 1]:
                matrix[j][i] = matrix[j - 1][i - 1]
            else:
                matrix[j][i] = min(matrix[j - 1][i - 1], matrix[j][i - 1], matrix[j - 1][i]) + 1

    return matrix[n - 1][m - 1]

if __name__ == '__main__':

    source = 'test'
    target = 'testt'

    ones = 0
    twos = 0

    lines = sys.stdin.readlines()

    for line in lines:
        target, source = line.strip().split('\t')
        dist = med(source, target)
        if dist == 1:
            ones += 1
        if dist == 2:
            twos += 2

    print "ones: " + str(ones)
    print "twos: " + str(twos)
        
    
