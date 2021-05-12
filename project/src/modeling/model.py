import pandas as pd
from sklearn.tree import DecisionTreeClassifier


class ModelWrapper:
    """Special Class for classifying."""

    def __init__(self):
        self.model = DecisionTreeClassifier()

    def fit(self, data: str or pd.DataFrame, labels: str or pd.DataFrame):
        self.model.fit(data, labels)
        return self

    def predict(self, data: str or pd.DataFrame) -> pd.DataFrame:
        """Builds sentiment data."""
        print('Prediction is started.')
        prediction = self.model.predict(data)
        print('Prediction is finished.')
        return prediction
