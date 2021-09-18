class arraushuffle:
    def shuffle(self):
        m = [1, 3, 5, 7, 2, 4, 6, 8]
        n = 4
        result = []
        for i in range(n):

            result.append(m[i])
            result.append(m[n+i])
        return result

ar = arraushuffle()

print(ar.shuffle())



