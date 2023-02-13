"""
Import the various model modules in one place and resolve forward refs.
"""

from .post_model import PostRead, PostReadWithDetails
from .photo_model import PhotoRead
from .user_model import UserReadBasic, UserReadWithDetails

PostReadWithDetails.update_forward_refs(
    PhotoRead=PhotoRead, UserReadBasic=UserReadBasic)

UserReadWithDetails.update_forward_refs(
    PostRead=PostRead)
