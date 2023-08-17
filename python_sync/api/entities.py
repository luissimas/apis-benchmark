from dataclasses import dataclass
from datetime import date
from typing import Optional
from uuid import UUID


@dataclass
class Movie:
    id: UUID
    name: str
    release_date: date
    director: str
    description: Optional[str] = None
    duration: Optional[int] = None
    budget: Optional[int] = None
