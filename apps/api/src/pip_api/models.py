from enum import StrEnum
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, HttpUrl

class JobStatus(StrEnum):
    PLANNED = "planned"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class ResearchJobRequest(BaseModel):
    query: str = Field(min_length=3, max_length=2000)
    engines: list[str] = Field(default_factory=lambda: ["web"])
    region: str = Field(default="BD", min_length=2, max_length=5)
    max_sources: int = Field(default=10, ge=1, le=30)

class ResearchPlan(BaseModel):
    objectives: list[str]
    engines: list[str]
    max_sources: int

class Evidence(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    url: HttpUrl
    title: str
    excerpt: str
    source_type: str
    credibility: float = Field(ge=0, le=1)

class ResearchJob(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    status: JobStatus = JobStatus.PLANNED
    request: ResearchJobRequest
    plan: ResearchPlan | None = None
    evidence: list[Evidence] = Field(default_factory=list)
    report: str | None = None