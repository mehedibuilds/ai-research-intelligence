from pip_api.engines.deferred import DeferredEngine
from pip_api.engines.web import WebSearchEngine
from pip_api.workers.research import ResearchWorker

def build_worker() -> ResearchWorker:
    return ResearchWorker({
        "web": WebSearchEngine(),
        "product": DeferredEngine("product"),
        "b2b_leads": DeferredEngine("b2b_leads"),
        "website_analysis": DeferredEngine("website_analysis"),
    })