from enum import Enum
from holon.ietf.rfc2119 import Keyword
from holon.headers import Header
from holon.principles import Principle
from holon.writing import autocomplete
from pydantic import BaseModel
from typing import List, Optional


@autocomplete
class PrincipleRule(BaseModel):
    keyword: Keyword
    principle: Principle


@autocomplete
class HeaderRule(BaseModel):
    keyword: Keyword
    header: Header


@autocomplete
class APIDesignSystem(BaseModel):
    principles: Optional[List[PrincipleRule]] = []
    headers: Optional[List[HeaderRule]] = []
