"""
Import the various model modules in one place and resolve forward refs.
"""

from .post_model import PostReadWithPhotos
from .photo_model import PhotoRead

PostReadWithPhotos.update_forward_refs(PhotoRead=PhotoRead)
