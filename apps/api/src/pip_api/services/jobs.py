from uuid import UUID
from pip_api.models import ResearchJob

class JobStore:
    def __init__(self) -> None:
        self._jobs: dict[UUID, ResearchJob] = {}
    def create(self, job: ResearchJob) -> ResearchJob:
        self._jobs[job.id] = job
        return job
    def get(self, job_id: UUID) -> ResearchJob | None:
        return self._jobs.get(job_id)
    def save(self, job: ResearchJob) -> ResearchJob:
        self._jobs[job.id] = job
        return job