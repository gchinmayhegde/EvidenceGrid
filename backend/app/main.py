from fastapi import FastAPI

app = FastAPI(
    title="EvidenceGrid API",
    description="Evidence-first research RAG workbench",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "evidencegrid-backend",
    }