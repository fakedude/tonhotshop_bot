"""
This type stub file was generated by pyright.
"""

from ...statictypes import statictypes
from ..py_object import PyObject

class VideoParameters(PyObject):
    @statictypes
    def __init__(self, width: int = ..., height: int = ..., frame_rate: int = ..., adjust_by_height: bool = ...) -> None:
        ...
    


