"""
This type stub file was generated by pyright.
"""

from ...scaffold import Scaffold

class CallHolder(Scaffold):
    def __init__(self) -> None:
        ...
    
    @property
    async def calls(self): # -> Dict:
        ...
    
    @property
    async def group_calls(self): # -> Dict:
        ...
    
    @property
    async def private_calls(self): # -> Dict:
        ...
    


