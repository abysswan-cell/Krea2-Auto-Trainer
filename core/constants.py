"""
Krea2 Auto Trainer
Global Constants
"""

from pathlib import Path

# ==========================================================
# Project
# ==========================================================

PROJECT_NAME = "Krea2 Auto Trainer"
VERSION = "1.0.0"

# ==========================================================
# Supported Models
# ==========================================================

SUPPORTED_MODELS = {
    "krea2": "krea/Krea-2-Raw",
}

# ==========================================================
# Training Defaults
# ==========================================================

DEFAULTS = {

    # image
    "resolution": 1024,

    # network
    "network_dim": 32,
    "network_alpha": 16,

    # optimizer
    "optimizer": "adamw8bit",

    # scheduler
    "lr_scheduler": "cosine",

    # learning rate
    "learning_rate": 1e-4,

    # batch
    "batch_size": 1,

    # save
    "save_every_n_epochs": 1,

    # workers
    "num_workers": 4,

    # precision
    "mixed_precision": "bf16",

    # cache
    "cache_latents": True,

    # shuffle
    "shuffle_caption": True,

    # bucketing
    "bucket": True,

    "bucket_step": 64,

    "bucket_min": 512,

    "bucket_max": 2048,
}

# ==========================================================
# Image Extensions
# ==========================================================

IMAGE_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
)

# ==========================================================
# Caption Extensions
# ==========================================================

CAPTION_EXTENSIONS = (
    ".txt",
)

# ==========================================================
# Output
# ==========================================================

OUTPUT_EXTENSION = ".safetensors"
