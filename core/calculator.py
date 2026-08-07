"""
Training Parameter Calculator
"""

from dataclasses import dataclass


@dataclass
class TrainingParameters:

    repeat: int

    epochs: int

    steps: int

    batch_size: int

    network_dim: int

    network_alpha: int

    learning_rate: float

    optimizer: str

    scheduler: str


class TrainingCalculator:

    def __init__(

        self,

        image_count,

        batch_size=1,

        model="krea2",

        vram=24,

    ):

        self.image_count = image_count

        self.batch_size = batch_size

        self.model = model

        self.vram = vram

    # ------------------------------------------------

    def recommend_repeat(self):

        n = self.image_count

        if n <= 20:
            return 20

        elif n <= 40:
            return 10

        elif n <= 80:
            return 5

        elif n <= 150:
            return 3

        return 1

    # ------------------------------------------------

    def recommend_epoch(self):

        n = self.image_count

        if n <= 20:
            return 10

        elif n <= 40:
            return 8

        elif n <= 80:
            return 6

        elif n <= 150:
            return 5

        return 4

    # ------------------------------------------------

    def recommend_rank(self):

        if self.model == "flux":

            return 16

        if self.model == "anima":

            return 32

        return 32

    # ------------------------------------------------

    def recommend_alpha(self):

        return self.recommend_rank() // 2

    # ------------------------------------------------

    def recommend_learning_rate(self):

        if self.model == "flux":

            return 8e-5

        return 1e-4

    # ------------------------------------------------

    def recommend_optimizer(self):

        return "adamw8bit"

    # ------------------------------------------------

    def recommend_scheduler(self):

        return "cosine"

    # ------------------------------------------------

    def calculate_steps(self):

        repeat = self.recommend_repeat()

        epochs = self.recommend_epoch()

        return (

            self.image_count
            * repeat
            * epochs
        ) // self.batch_size

    # ------------------------------------------------

    def build(self):

        return TrainingParameters(

            repeat=self.recommend_repeat(),

            epochs=self.recommend_epoch(),

            steps=self.calculate_steps(),

            batch_size=self.batch_size,

            network_dim=self.recommend_rank(),

            network_alpha=self.recommend_alpha(),

            learning_rate=self.recommend_learning_rate(),

            optimizer=self.recommend_optimizer(),

            scheduler=self.recommend_scheduler(),

        )
