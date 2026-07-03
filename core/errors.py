class AllkitpyError(Exception):
    """Base error for all Allkitpy modules."""
    pass


class FileError(AllkitpyError):
    """Errors related to file operations."""
    pass


class ImageError(AllkitpyError):
    """Errors related to image operations."""
    pass


class TextError(AllkitpyError):
    """Errors related to text operations."""
    pass

class AllkitpyError(Exception):
    """Base exception for Allkitpy."""


class ValidationError(AllkitpyError):
    """Invalid user input."""


class FileError(AllkitpyError):
    """File operation failed."""


class ImageError(AllkitpyError):
    """Image operation failed."""


class PDFError(AllkitpyError):
    """PDF operation failed."""


class AudioError(AllkitpyError):
    """Audio operation failed."""


class VideoError(AllkitpyError):
    """Video operation failed."""


class WebError(AllkitpyError):
    """Web operation failed."""


class AIError(AllkitpyError):
    """AI operation failed."""