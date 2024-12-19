"""
This type stub file was generated by pyright.
"""

from enum import Flag
from typing import Optional
from pytgcalls.types.update import Update

class RawCallUpdate(Update):
    class Type(Flag):
        ACCEPTED = ...
        CONFIRMED = ...
        REQUESTED = ...
        SIGNALING_DATA = ...
        UPDATED_CALL = ...
    
    
    def __init__(self, chat_id: int, status: Type, g_a_or_b: Optional[bytes] = ..., protocol=..., fingerprint: int = ..., signaling_data: Optional[bytes] = ...) -> None:
        ...
    


