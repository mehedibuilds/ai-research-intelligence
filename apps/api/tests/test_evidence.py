from pip_api.models import Evidence
from pip_api.services.evidence import deduplicate

def test_deduplication_prefers_more_credible_source() -> None:
    weak = Evidence(url="https://example.com/page", title="First", excerpt="a", source_type="web", credibility=0.4)
    strong = Evidence(url="https://example.com/page/", title="Second", excerpt="b", source_type="web", credibility=0.9)
    result = deduplicate([weak, strong])
    assert len(result) == 1
    assert result[0].title == "Second"