from numpy import array
from scipy.sparse import csr_matrix


A = array(
    [
        [1, 0, 0, 1, 0, 0],
        [0, 0, 2, 0, 0, 1],
        [0, 0, 0, 2, 0, 0]
    ]
)

S = csr_matrix(A)
print(S)


