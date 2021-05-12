from typing import List, Tuple

import dill
from sklearn.pipeline import Pipeline as SkPipe

from src.features import FeatureBuilder
from src.modeling import ModelWrapper


class Pipeline(SkPipe):
    """Class for defining pipeline that encapsulates workflow."""
    def __init__(self, steps: List[Tuple[str, object]]):
        super().__init__(self.__parse_steps(steps))

    @staticmethod
    def __parse_steps(steps):
        return steps

    def save(self, path: str):
        with open(path, 'wb') as f:
            dill.dump(self, f)

    @staticmethod
    def load(path: str):
        with open(path, 'rb') as f:
            pipe = dill.load(f)
        return pipe


def define_steps():
    """Here you define the steps of the main pipeline of the project"""
    transformer = FeatureBuilder()
    model = ModelWrapper()
    steps = [
        ("transformer", transformer),
        ("model", model)
    ]
    return steps
