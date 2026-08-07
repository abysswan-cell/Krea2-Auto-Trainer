"""
Configuration Manager

Generate AI Toolkit YAML automatically.
"""

from pathlib import Path
import yaml

from .logger import logger


class ConfigManager:

    def __init__(self):

        self.config = {}

    # ---------------------------------------------------

    def load_template(self, template_path):

        template_path = Path(template_path)

        with open(template_path, "r", encoding="utf-8") as f:

            self.config = yaml.safe_load(f)

        logger.info(f"Template loaded: {template_path}")

    # ---------------------------------------------------

    def set_dataset(self, dataset_path):

        self.config["dataset"] = {

            "path": str(dataset_path)

        }

    # ---------------------------------------------------

    def set_output(self, output_path, output_name):

        self.config["output"] = {

            "path": str(output_path),

            "name": output_name,

        }

    # ---------------------------------------------------

    def set_model(self, model_path):

        self.config["model"] = {

            "path": model_path

        }

    # ---------------------------------------------------

    def apply_training_parameters(self, params):

        self.config["training"] = {

            "batch_size": params.batch_size,

            "epochs": params.epochs,

            "repeat": params.repeat,

            "steps": params.steps,

            "network_dim": params.network_dim,

            "network_alpha": params.network_alpha,

            "learning_rate": params.learning_rate,

            "optimizer": params.optimizer,

            "scheduler": params.scheduler,

        }

    # ---------------------------------------------------

    def save(self, save_path):

        save_path = Path(save_path)

        with open(save_path, "w", encoding="utf-8") as f:

            yaml.dump(

                self.config,

                f,

                sort_keys=False,

                allow_unicode=True,

            )

        logger.info(f"Config saved: {save_path}")
