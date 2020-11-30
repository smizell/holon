from enum import Enum
from holon.ietf.rfc2119 import Keyword
from holon.principles import Principle
from holon.writing import autocomplete
from pydantic import BaseModel
from typing import List


@autocomplete
class PrincipleRule(BaseModel):
    keyword: Keyword
    principle: Principle


@autocomplete
class DesignSystem(BaseModel):
    principles: List[PrincipleRule]
