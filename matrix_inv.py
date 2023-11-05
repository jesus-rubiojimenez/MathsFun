import numpy as np

def gaussian_inverse(matrix):
    n = matrix.shape[0]
    augmented_matrix = np.hstack((matrix, np.eye(n)))
    
    # Forward elimination
    for i in range(n):
        pivot = augmented_matrix[i, i]
        augmented_matrix[i, :] /= pivot
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
    
    # Backward substitution
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
    
    inverse_matrix = augmented_matrix[:, n:]
    return inverse_matrix

# Example usage
matrix = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]], dtype = float)
print("Original matrix:")
print(matrix)

inverse = gaussian_inverse(matrix)
print("Inverse matrix:")
print(inverse)