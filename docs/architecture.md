# Design decisions

## ADR-001: Jobs are the unit of work

The API creates durable job records before a worker performs external research. This lets clients inspect status, cancel queued work, receive notifications, and reproduce a report from the same input and evidence set.

## ADR-002: Evidence precedes synthesis

The pipeline normalizes, deduplicates, validates, and scores sources before report assembly. Generated prose must reference retained evidence IDs rather than relying on model memory.

## ADR-003: Engines are replaceable adapters

Search, commerce, lead, and website analysis modules share a narrow contract. Provider-specific rate limits, authentication, and parsing live inside the adapter.