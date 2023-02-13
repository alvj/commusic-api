"""
Import the various model modules in one place and resolve forward refs.
"""

from .post_model import PostReadWithDetails
from .photo_model import PhotoRead
from .user_model import UserReadBasic

PostReadWithDetails.update_forward_refs(
    PhotoRead=PhotoRead, UserReadBasic=UserReadBasic)
