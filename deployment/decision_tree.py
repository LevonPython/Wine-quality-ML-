import pandas as pd
from sklearn.utils import resample
from sklearn.tree import DecisionTreeClassifier
from scipy import stats
import pickle


class RandomForest:

    def __init__(self,
                 n_trees: int,
                 max_depth: int = 3,
                 min_samples_split: int = 5,
                 leavout_feature_ratio: float = 0.8):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.leavout_feature_ratio = leavout_feature_ratio
        self.trees = []

    def fit(self, X, y):
        for i in range(self.n_trees):
            X_new, y_new = resample(X, y, replace=True, n_samples=int(len(y) * 1.2), random_state=i)
            X_new = X_new.sample(int(X_new.shape[1] * self.leavout_feature_ratio), axis=1)
            clf = DecisionTreeClassifier(max_depth=self.max_depth,
                                         min_samples_split=self.min_samples_split).fit(X_new, y_new)
            self.trees.append(clf)
        return self

    def predict(self, X):
        predictions = []
        print("start")
        print(f"self.trees: {self.trees}")
        for tree in self.trees:
            predictions.append(tree.predict(X))
        print("middle")
        predictions = np.array(predictions)

        # final_predictions = []
        mode, counts = stats.mode(predictions)
        return mode.reshape(-1)

    def score(self, X, y):
        y_pred = self.predict(X)
        return np.sum(y == y_pred) / len(y_pred)

    def load(self, pk_file):
        print(f"Load started: {pk_file}")
        with open(pk_file, 'rb') as f:
            print(f"f: {f}")
            loaded_model = pickle.load(f)
            print(f"loaded_model {loaded_model}")
            return loaded_model

#
# if __name__ == '__main__':
#     model = RandomForest()
