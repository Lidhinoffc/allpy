from pathlib import Path

from .errors import ValidationError


def file_exists(filename):

    if not Path(filename).exists():
        raise ValidationError(
            f"File not found: {filename}"
        )


def positive(value, name="value"):

    if value <= 0:
        raise ValidationError(
            f"{name} must be positive."
        )


def not_empty(text, name="text"):

    if not text:
        raise ValidationError(
            f"{name} cannot be empty."
        )