from pip_api.engines.base import ResearchEngine
from pip_api.models import Evidence

class WebSearchEngine(ResearchEngine):
    name = "web"
    async def research(self, query: str, max_sources: int) -> list[Evidence]:
        # Provider implementation belongs here; workers stay provider-neutral.
        return []