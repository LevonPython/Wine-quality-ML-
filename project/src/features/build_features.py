import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.preprocessing import StandardScaler


class FeatureBuilder(TransformerMixin):
    """Special Class for cleaning data and building features."""

    def __init__(self):
        self.st = StandardScaler()
        pass

    @staticmethod
    def _clean_content(df: pd.DataFrame) -> pd.DataFrame:
        """Clear and lemmatize review content"""
        df["review_clean"] = df["single_content"] + df["multiple_content"]
        print(f"Got clean review data...")
        return df

    def fit(self, X=None, y=None):
        self.st = self.st.fit(X)
        return self

    def transform(self, X: str or pd.DataFrame, y=None) -> pd.DataFrame:
        """Builds features and saves data.
        Args:
            data: data pandas DataFrame
        """
        self.st.transform(X)
        df = self._clean_content(X)

        print(f"Features are successfully built.")
        return df

    def fit_transform(self, X: pd.DataFrame, y=None):
        self.fit(X, y)
        return self.transform(X, y)


def build_features(raw_data):
    """Returns the data in the form of pandas DataFrame."""
    obj = FeatureBuilder()
    return obj.transform(raw_data)
