from pip_api.models import ResearchJobRequest, ResearchPlan

class Planner:
    def create_plan(self, request: ResearchJobRequest, permitted_engines: set[str]) -> ResearchPlan:
        invalid = set(request.engines) - permitted_engines
        if invalid:
            raise ValueError(f"unsupported engines: {', '.join(sorted(invalid))}")
        return ResearchPlan(
            objectives=[f"Investigate: {request.query}", "Collect attributable evidence", "Produce a cited brief"],
            engines=request.engines,
            max_sources=request.max_sources,
        )