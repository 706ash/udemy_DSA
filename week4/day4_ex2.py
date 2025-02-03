import numpy as np

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]

#SGD
def SGD(X, y, theta, learning_rate, n_epochs):
    m = len(y)
    for _ in range(n_epochs):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = X[random_index:random_index+1]
            yi = y[random_index:random_index+1]
            gradients = 2 * xi.T @ (xi @ theta - yi)
            theta = theta - learning_rate * gradients
    return theta

theta = np.random.randn(2, 1)
learning_rate = 0.01
n_epochs = 50

theta_opt = SGD(X_b, y, theta, learning_rate, n_epochs)
print(theta_opt)