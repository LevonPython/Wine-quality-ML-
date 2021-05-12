"""
action - train (fit)
action - predict

n - datapoints count
k - feature count

y = b0 * 1 + b1 * x1 + b2 * x2

y -> (n, 1)
X -> (n, k + 1)
params -> (k+1, 1)

y_hat = X @ beta

       (k+1, n)   n, (k+1)| (k+1, k+1)    (k+1, n)  (n, 1)
beta = (X.T     @ X       )      ^-1    @ X.T      @ y
beta = (X.T @ X) ^ -1 @ X.T @ y

Check inversibility

if linalg.cond(x) < 1 / sys.float_info.epsilon:
    i = linalg.inv(x)
"""
import numpy as np
from numpy.linalg.linalg import LinAlgError
import matplotlib.pyplot as plt
import pickle


class Model:
    """
     This class implements linear regression computing OLS coefs.
    """

    def __init__(self):
        self.fitted = False
        self.params = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Estimates params based on this function
        params = (X.T @ X) ^ -1 @ X.T @ y
        :param X: (n, k)
        :param y: (n, 1)
        """
        # X = np.hstack([np.ones(len(X))[:, np.newaxis], X])
        X = np.hstack([np.ones((X.shape[0], 1)), X])

        try:
            self.params = np.linalg.inv(X.T @ X) @ X.T @ y
            self.fitted = True
        except LinAlgError("Non Invertible Matrix") as e:
            print(e)

    def gradientDescent(self, X, y, alpha=0.1, num_iters=100):
        theta = np.array([[0], [0]])
        X = np.hstack([np.ones((X.shape[0], 1)), X])
        m = y.size  # number of training examples
        for i in range(num_iters):
            y_hat = np.dot(X, theta)
            theta = theta - alpha * (1.0 / m) * np.dot(X.T, y_hat - y)
        return theta

    def fit_gradient(self, X, y, epochs=500, learning_rate=0.1):
        b = 10
        m = 10
        n = X.shape[0]
        for _ in range(epochs):
            b_gradient = -2 * np.sum(y - (m * X + b)) / n
            m_gradient = -2 * np.sum(X * (y - (m * X + b))) / n

            # Updating the previous values
            b = b - (learning_rate * b_gradient)
            m = m - (learning_rate * m_gradient)
        return b, m

    def predict(self, X: np.ndarray) -> np.ndarray:
        X = np.hstack([np.ones((X.shape[0], 1)), X])
        y_hat = X @ self.params
        return y_hat

    def plot_predictions(self, X: np.ndarray, y: np.ndarray, y_hat: np.ndarray = None):
        """
        Plots the line and the actual points.
        :param X: features
        :param y: true value
        :param y_hat: predicted value
        :return:
        """
        if y_hat is None:
            y_hat = self.predict(X)

        plt.scatter(X, y, c='blue', label="Observed values.")
        plt.legend()
        plt.plot(X, y_hat, c="r", label="Predicted values")
        plt.legend()

        plt.title(f"Fitted Regression. intercept_{self.params[0][0]} coefs_{self.params[1:]}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    def save(self):
        pass

    def load(self):
        pass


if __name__ == '__main__':
    np.random.seed(1)
    X = np.arange(50)[:, np.newaxis]
    noise = np.random.randint(5, size=(50, 1))
    # to model
    y = 3 + 2 * X + noise
    ols_model = Model()
    ols_model.fit(X, y)
    print(X)
    # modeled
    print(f"y = {ols_model.params[0][0]} + {ols_model.params[1][0]} * x")
    # X_new = np.arange(60, 61)[:, np.newaxis]
    # X_new = np.array([[60]])
    y_hat = ols_model.predict(X)
    ols_model.plot_predictions(X, y, y_hat)
    pickle.dump(ols_model, open("model.pkl", "wb"))
