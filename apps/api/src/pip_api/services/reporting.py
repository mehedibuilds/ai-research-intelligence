from pip_api.models import Evidence

def cited_report(query: str, evidence: list[Evidence]) -> str:
    if not evidence:
        return f"Research brief: {query}\n\nNo validated evidence was returned."
    citations = "\n".join(f"- [{item.title}]({item.url}) — {item.excerpt}" for item in evidence)
    return f"# Research brief\n\n## Question\n{query}\n\n## Evidence\n{citations}"