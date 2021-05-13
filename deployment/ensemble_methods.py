
import numpy as np
from scipy import stats
import pickle

# if you want to use your own Decision Tree implementation for Random Forest
from decision_tree import DTClassifier  

# something useful for tracking algorithm's iterations
import progressbar

widgets = ['Model Training: ', progressbar.Percentage(), ' ',
            progressbar.Bar(marker="-", left="[", right="]"),
            ' ', progressbar.ETA()]


def get_bootstrap_samples(X, y, nr_bootstraps, nr_samples=None):
    # this function is for getting bootstrap samples with replacement
    # from the initial dataset (X, y)
    # nr_bootstraps is the number of bootstraps needed
    # nr_samples is the number of data points to sample each time
    # it should be the size of X, if nr_samples is not provided
    # Hint: you may need np.random.choice function somewhere in this function
    if nr_samples == None:
      nr_samples = X.shape[0]
    bootstrap_samples = np.zeros((nr_bootstraps, X.shape[0], X.shape[1] + 1))

    for i in range(nr_bootstraps):
      idx = np.random.choice(range(nr_samples), size=nr_samples, replace=True)
      bootstrap_samples[i][:, :-1] = X[idx, :]
      bootstrap_samples[i][:, -1] = y[idx]
    return bootstrap_samples


class Bagging:

    def __init__(self, base_estimator, nr_estimators=10):
        # number of models in the ensemble
        self.nr_estimators = nr_estimators
        self.progressbar = progressbar.ProgressBar(widgets=widgets)
        # this can be any object that has 'fit', 'predict' methods
        self.base_estimator = base_estimator

    def fit(self, X, y):
        # this method will fit a separate model (self.base_estimator)
        # on each bootstrap sample and each model should be stored
        # in order to use it in 'predict' method
        X = np.array(X)
        y = np.array(y)
        bootstrap_samples = get_bootstrap_samples(X, y,
                                                  nr_bootstraps=self.nr_estimators)
        self.models = []
        for i in self.progressbar(range(self.nr_estimators)):
          model = self.base_estimator
          X_boot, y_boot = bootstrap_samples[i][:, :-1],  bootstrap_samples[i][:, -1]
          model.fit(X_boot, y_boot)
          self.models.append(model)
        return self.models

    def predict(self, X):
        # this method will predict the labels for a given test dataset
        # get the majority 'vote' for each test instance from the ensemble
        # Hint: you may want to use 'mode' method from scipy.stats
        y_pred = np.zeros((X.shape[0], self.nr_estimators))

        for i in range(self.nr_estimators):
            y_pred[:, i] = (self.models[i].predict(X))
        return stats.mode(y_pred, axis=1)[0]


class RandomForest:

    def __init__(self, nr_estimators=10, max_features=None, min_samples_split=2,
                  min_gain=0, max_depth=float("inf")):
        # number of trees in the forest
        self.nr_estimators = nr_estimators
        # this is the number of features to use for each tree
        # if not specified this should be set to sqrt(initial number of features)
        self.max_features = max_features
        # the rest is for decision tree
        self.min_samples_split = min_samples_split
        self.min_gain = min_gain
        self.max_depth = max_depth
        self.progressbar = progressbar.ProgressBar(widgets=widgets)

    def fit(self, X, y):
        # this method will fit a separate tree
        # on each bootstrap sample and subset of features
        # each tree should be stored
        # in order to use it in 'predict' method
        X = np.array(X)
        y = np.array(y)
        if self.max_features == None:
            self.max_features = int(np.sqrt(X.shape[1]).round(0))
        bootstrap_samples = get_bootstrap_samples(X, y,
                                                  self.nr_estimators
        self.trees = []
        for i in self.progressbar(range(self.nr_estimators)):
          # you can modify the code to use sklearn's decision tree
          # if you don't want to use your implementation
          tree = DTClassifier(
                    min_samples_split=self.min_samples_split,
                    min_impurity=self.min_gain,
                    max_depth=self.max_depth)
          X_boot, y_boot = bootstrap_samples[i][:, :-1], bootstrap_samples[i][:, -1]
          idx = np.random.choice(range(X_boot.shape[1]), self.max_features, replace=False)
          # we need to keep the indices of the features used for this tree
          tree.feature_indices = idx
          tree.fit(X_boot[:, idx], y_boot)
          self.trees.append(tree)

    def predict(self, X):
        # this method will predict the labels for a given test dataset
        # get the majority 'vote' for each test instance from the forest
        # Hint: you may want to use 'mode' method from scipy.stats
        # besides the individual trees, you will also need the feature indices
        # it was trained on
        print("Predict execution started!")
        y_pred = np.zeros((X.shape[0], self.nr_estimators))
        for i, tree in enumerate(self.trees):
            idx = tree.feature_indices
            y_pred[:, i] = tree.predict(X[:, idx])
        return stats.mode(y_pred, axis=1)[0]

    def load(self, pk_file):
        print("Load executed")
        with open(pk_file, 'rb') as f:
            print(f"f: {f}")
            res = pickle.load(f)
            print(f"res {res}")
            return res

# Adaboost starts from here

# Instead of using a Decision Tree with one level
# we can create another object for Decision Stump
# which will work faster since it will not compute impurity
# to decide on which feature to make a split

# after implementing this version, create a different Adaboost
# that uses decision trees with one level and check that it is 
# more inefficient compared to the below implementation.


class DecisionStump:

    def __init__(self):
        # we will use this attribute to convert the predictions
        # in case the error > 50%
        self.flip = 1
        # the feature index on which the split was made
        self.feature_index = None
        # the threshold based on which the split was made
        self.threshold = None
        # the confidence of the model (see the pseudocode from the lecture slides)
        self.alpha = None

class Adaboost:

    # this implementation supports only -1,1 label encoding
    def __init__(self, nr_estimators=5):
        # number of weak learners (Decision Stumps) to use
        self.nr_estimators = nr_estimators
        self.progressbar = progressbar.ProgressBar(widgets=widgets)

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        nr_samples, nr_features = np.shape(X)
        # initialize the uniform weights for each training instance
        w = np.ones(nr_samples) / nr_samples


        self.models = []
        for i in self.progressbar(range(self.nr_estimators)):

            model = DecisionStump()
            # we set the initial error very high in order to select
            # the model with lower error
            min_error = 1
            # we go over each feature as in case of decision tree
            # to decide which split leads to a smaller error
            # note that here we don't care about the impurity
            # even if we find a model with 90% error, we will flip the
            # sign of the predictions and will make it a model with 10% error
            for feature_id in range(nr_features):

                unique_values = np.unique(X[:, feature_id])
                thresholds = (unique_values[1:] + unique_values[:-1]) / 2
                for threshold in thresholds:
                  # setting an intial value for the flip
                  flip = 1
                  # setting all the predictions as 1
                  prediction = np.ones(nr_samples)
                  # if the feature has values less than the fixed threshold
                  # then it's prediction should be manually put as -1
                  prediction[X[:, feature_id] < threshold] = -1
                  # compute the weighted error (epsilon_t) for the resulting prediction
                  error = np.sum(w * (prediction != y))

                  # if the model is worse than random guessing
                  # then we need to set the flip variable to -1
                  # so that we can use it later, we also modify the error
                  # accordingly
                  if error > 0.5:
                    error = 1 - error
                    flip = -1
                  # if this feature and threshold were the one giving
                  # the smallest error, then we store it's info in the 'model' object
                  if error < min_error:
                    model.flip = flip
                    model.threshold = threshold
                    model.feature_index = feature_id
                    min_error = error

            # compute alpha based on the error of the 'best' decision stump
            model.alphas = 0.5 * np.log((1 - min_error) / min_error + 1e-10)
            predictions = np.ones(nr_samples)
            negative_idx = ((model.flip * X[:, model.feature_index]) < (model.flip * model.threshold))
            predictions[negative_idx] = -1
            # obtain the predictions from the chosen decision stump
            # using the info stored in the 'model' object
            # don't forget about the flip if necessary

            # compute the weights and normalize them
            w *= np.exp(- model.alphas * y * predictions)
            w /= np.sum(w)
            # store the decision stump of the current iteration for later
            self.models.append(model)

    def predict(self, X):
        X = np.array(X)
        nr_samples = np.shape(X)[0]
        y_pred = np.zeros(nr_samples)
        for model in self.models:
            prediction = np.ones(nr_samples)
            negative_idx = ((model.flip * X[:, model.feature_index]) < (model.flip * model.threshold))
            prediction[negative_idx] = -1
            y_pred += model.alphas * prediction
        return np.sign(y_pred)
        # for each instance in X you should obtain the 'prediction'
        # from each decision stump (not forgetting about the flip variable)
        # then take the sum of
        # all the individual predictions times their weights (alpha)
        # if the resulting amount is bigger than 0 then predict 1, otherwise -1