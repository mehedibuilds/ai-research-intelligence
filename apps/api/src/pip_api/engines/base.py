from abc import ABC, abstractmethod
from pip_api.models import Evidence

class ResearchEngine(ABC):
    name: str
    @abstractmethod
    async def research(self, query: str, max_sources: int) -> list[Evidence]: ...