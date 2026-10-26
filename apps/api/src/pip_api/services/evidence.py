from collections.abc import Iterable
from pip_api.models import Evidence

def deduplicate(evidence: Iterable[Evidence]) -> list[Evidence]:
    retained: dict[str, Evidence] = {}
    for item in evidence:
        key = str(item.url).rstrip("/").lower()
        current = retained.get(key)
        if current is None or item.credibility > current.credibility:
            retained[key] = item
    return list(retained.values())

def validate_sources(evidence: Iterable[Evidence], threshold: float = 0.5) -> list[Evidence]:
    return [item for item in evidence if item.credibility >= threshold]

def score(evidence: Iterable[Evidence]) -> float:
    values = [item.credibility for item in evidence]
    return round(sum(values) / len(values), 2) if values else 0.0