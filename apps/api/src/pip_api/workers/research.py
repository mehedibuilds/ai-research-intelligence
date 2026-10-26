from pip_api.engines.base import ResearchEngine
from pip_api.models import JobStatus, ResearchJob
from pip_api.services.evidence import deduplicate, validate_sources
from pip_api.services.reporting import cited_report

class ResearchWorker:
    def __init__(self, engines: dict[str, ResearchEngine]) -> None:
        self.engines = engines
    async def execute(self, job: ResearchJob) -> ResearchJob:
        if job.plan is None:
            raise ValueError("a job requires an approved plan")
        job.status = JobStatus.RUNNING
        collected = []
        for engine_name in job.plan.engines:
            engine = self.engines[engine_name]
            collected.extend(await engine.research(job.request.query, job.plan.max_sources))
        job.evidence = validate_sources(deduplicate(collected))
        job.report = cited_report(job.request.query, job.evidence)
        job.status = JobStatus.COMPLETED
        return job