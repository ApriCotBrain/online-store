"""A module containing custom validators for Django model fields."""

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from PIL.Image import Image


@deconstructible
class ImageWidthHeightValidator:
    """Validate width and height of image in pixels."""

    size_error_message = (
        "Maximum allowed image size: "
        "{max_width} x {max_height} pixels."
        "Current size: {width} x {height} pixels."
    )

    def __init__(self, max_width: int, max_height: int) -> None:
        self.max_width = max_width
        self.max_height = max_height

    def __call__(self, image: Image) -> None:
        if image.width > self.max_width or image.height > self.max_height:
            raise ValidationError(
                self.size_error_message.format(
                    max_width=self.max_width,
                    max_height=self.max_height,
                    width=image.width,
                    height=image.height,
                )
            )

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, ImageWidthHeightValidator)
            and self.max_width == other.max_width
            and self.max_height == other.max_height
            and self.size_error_message == other.size_error_message
        )
