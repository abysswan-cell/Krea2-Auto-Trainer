"""
Dataset Analyzer
"""

from pathlib import Path
import hashlib

from PIL import Image

from .dataset import Dataset
from .logger import logger


class DatasetAnalyzer:

    def __init__(self, dataset):

        if isinstance(dataset, str):

            dataset = Dataset(dataset).load()

        self.dataset = dataset

    # ------------------------------------

    def image_count(self):

        return len(self.dataset)

    # ------------------------------------

    def caption_count(self):

        count = 0

        for txt in self.dataset.captions:

            if txt.exists():

                count += 1

        return count

    # ------------------------------------

    def missing_caption(self):

        missing = []

        for txt in self.dataset.captions:

            if not txt.exists():

                missing.append(txt)

        return missing

    # ------------------------------------

    def broken_images(self):

        broken = []

        for image in self.dataset.images:

            try:

                img = Image.open(image)

                img.verify()

            except Exception:

                broken.append(image)

        return broken

    # ------------------------------------

    def resolutions(self):

        result = []

        for image in self.dataset.images:

            img = Image.open(image)

            result.append(img.size)

        return result

    # ------------------------------------

    def average_resolution(self):

        sizes = self.resolutions()

        if not sizes:

            return (0, 0)

        w = sum(x for x, y in sizes) // len(sizes)

        h = sum(y for x, y in sizes) // len(sizes)

        return (w, h)

    # ------------------------------------

    def duplicate_images(self):

        hashes = {}

        duplicate = []

        for image in self.dataset.images:

            md5 = hashlib.md5(image.read_bytes()).hexdigest()

            if md5 in hashes:

                duplicate.append(image)

            else:

                hashes[md5] = image

        return duplicate

    # ------------------------------------

    def summary(self):

        logger.info("Dataset Summary")

        logger.info("--------------------------")

        logger.info(f"Images : {self.image_count()}")

        logger.info(f"Captions : {self.caption_count()}")

        logger.info(f"Missing Caption : {len(self.missing_caption())}")

        logger.info(f"Broken Images : {len(self.broken_images())}")

        logger.info(f"Duplicate Images : {len(self.duplicate_images())}")

        logger.info(
            f"Average Resolution : {self.average_resolution()}"
        )
