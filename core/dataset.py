"""
Dataset Analyzer
Krea2 Auto Trainer
"""

from pathlib import Path
from PIL import Image

from .logger import logger
from .constants import IMAGE_EXTENSIONS


class DatasetAnalyzer:

    def __init__(self, dataset_path):

        self.dataset_path = Path(dataset_path)

        self.images = []

        self.captions = []

    # ----------------------------------------

    def scan_images(self):

        self.images.clear()

        for ext in IMAGE_EXTENSIONS:

            self.images.extend(
                self.dataset_path.rglob(f"*{ext}")
            )

        self.images = sorted(self.images)

        logger.info(f"Found {len(self.images)} images.")

        return self.images

    # ----------------------------------------

    def scan_captions(self):

        self.captions.clear()

        missing = []

        for image in self.images:

            txt = image.with_suffix(".txt")

            if txt.exists():

                self.captions.append(txt)

            else:

                missing.append(image)

        logger.info(f"Found {len(self.captions)} captions.")

        return missing

    # ----------------------------------------

    def verify_images(self):

        broken = []

        for image in self.images:

            try:

                img = Image.open(image)

                img.verify()

            except Exception:

                broken.append(image)

        logger.info(f"Broken images: {len(broken)}")

        return broken

    # ----------------------------------------

    def image_sizes(self):

        sizes = []

        for image in self.images:

            img = Image.open(image)

            sizes.append(img.size)

        return sizes

    # ----------------------------------------

    def count(self):

        return len(self.images)

    # ----------------------------------------

    def summary(self):

        self.scan_images()

        missing = self.scan_captions()

        broken = self.verify_images()

        return {

            "images": len(self.images),

            "captions": len(self.captions),

            "missing_caption": len(missing),

            "broken_images": len(broken),

        }
