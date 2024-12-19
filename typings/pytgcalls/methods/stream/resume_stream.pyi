"""
This type stub file was generated by pyright.
"""

from typing import Union
from ...mtproto_required import mtproto_required
from ...scaffold import Scaffold
from ...statictypes import statictypes

class ResumeStream(Scaffold):
    @statictypes
    @mtproto_required
    async def resume_stream(self, chat_id: Union[int, str]):
        ...
    


