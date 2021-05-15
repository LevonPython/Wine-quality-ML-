from src.pipelines.pipeline import define_steps, Pipeline
import pandas as pd


def run_training(data, labels, pipe_path: str):
    """The function which runs training and saves the results and the pipe."""
    steps = define_steps()
    pipe = Pipeline(steps)
    pipe.fit(data, labels)
    pipe.save(pipe_path)
