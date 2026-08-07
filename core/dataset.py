"""
Dataset Loader

Only responsible for reading datasets.
"""

from pathlib import Path
from PIL import Image

from .constants import IMAGE_EXTENSIONS


class Dataset:

    def __init__(self, root):

        self.root = Path(root)

        self.images = []

        self.captions = []

    # -----------------------------------------

    def load(self):

        self.images.clear()

        self.captions.clear()

        for ext in IMAGE_EXTENSIONS:

            self.images.extend(
                sorted(self.root.rglob(f"*{ext}"))
            )

        for image in self.images:

            txt = image.with_suffix(".txt")

            self.captions.append(txt)

        return self

    # -----------------------------------------

    def __len__(self):

        return len(self.images)

    # -----------------------------------------

    def image(self, index):

        return self.images[index]

    # -----------------------------------------

    def caption(self, index):

        return self.captions[index]

    # -----------------------------------------

    def open(self, index):

        return Image.open(self.images[index])
