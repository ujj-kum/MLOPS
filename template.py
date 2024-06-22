import os
import logging
from pathlib import Path

list_of_files = [
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluation.py'
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utils/__init__.py'
    'src/utils/utils.py',
    'src/logger/logging.py',
    'src/exception/exception.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    '__init__setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'experiment/experiments.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dirname, filename = os.path.split(filepath)
    if dirname!="":
        os.makedirs(dirname, exist_ok=True)
        logging.info(f"Creating directory: {dirname} for file: {filename}")
    else:
        with open(filename, 'w') as f:
            pass
