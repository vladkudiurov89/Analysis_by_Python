from sklearn.metrics.pairwise import manhattan_distances

a = [[1, 1, 0]]
b = [[0, 2, -1]]
c = [[2, 3, 1]]
d = [[1, 0, 4]]


ab = manhattan_distances(a, b)
ac = manhattan_distances(a, c)
ad = manhattan_distances(a, d)

bc = manhattan_distances(b, c)
bd = manhattan_distances(b, d)

dc = manhattan_distances(d, c)
print('A: ', ab + ac + ad)
print('B: ', ab + bc + bd)
print('C: ', ac + bc + dc)
print("D: ", ad + bd + dc)


