from pathlib import Path
import os


def get_workspace():

    workspace = os.environ.get(
        "KREA_WORKSPACE",
        "/workspace"
    )

    return Path(workspace)


WORKSPACE = get_workspace()

MODELS = WORKSPACE / "models"

LORAS = WORKSPACE / "loras"

DATASETS = WORKSPACE / "datasets"

OUTPUTS = WORKSPACE / "outputs"

CACHE = WORKSPACE / "cache"

CONFIG = WORKSPACE / "config"

LOGS = WORKSPACE / "logs"


def create_directories():

    dirs = [

        MODELS,
        LORAS,
        DATASETS,
        OUTPUTS,
        CACHE,
        CONFIG,
        LOGS,

    ]

    for folder in dirs:
        folder.mkdir(
            parents=True,
            exist_ok=True,
        )
