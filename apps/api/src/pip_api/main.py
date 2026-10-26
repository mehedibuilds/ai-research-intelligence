from fastapi import FastAPI, HTTPException, status
from pip_api.workers.factory import build_worker
from pip_api.models import JobStatus, ResearchJob, ResearchJobRequest
from pip_api.services.jobs import JobStore
from pip_api.services.planner import Planner

store = JobStore()
planner = Planner()
worker = build_worker()
PERMITTED_ENGINES = {"web", "product", "b2b_leads", "website_analysis"}
app = FastAPI(title="Personal Intelligence Platform", version="0.1.0")

@app.get("/healthz")
async def healthz() -> dict:
    return {"status": "ok"}

@app.post("/v1/research-jobs", response_model=ResearchJob, status_code=status.HTTP_201_CREATED)
async def create_research_job(request: ResearchJobRequest) -> ResearchJob:
    try:
        plan = planner.create_plan(request, PERMITTED_ENGINES)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    job = store.create(ResearchJob(request=request, plan=plan, status=JobStatus.QUEUED))
    return job

@app.get("/v1/research-jobs/{job_id}", response_model=ResearchJob)
async def get_research_job(job_id: str) -> ResearchJob:
    from uuid import UUID
    job = store.get(UUID(job_id))
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")
    return job

@app.post("/v1/research-jobs/{job_id}/run", response_model=ResearchJob)
async def run_research_job(job_id: str) -> ResearchJob:
    from uuid import UUID
    job = store.get(UUID(job_id))
    if job is None:
        raise HTTPException(status_code=404, detail="job not found")
    return store.save(await worker.execute(job))