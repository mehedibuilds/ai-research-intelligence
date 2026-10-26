from pip_api.engines.base import ResearchEngine
from pip_api.models import Evidence

class DeferredEngine(ResearchEngine):
    def __init__(self, name: str) -> None:
        self.name = name
    async def research(self, query: str, max_sources: int) -> list[Evidence]:
        # A capability is enabled only when its provider adapter is configured.
        return []