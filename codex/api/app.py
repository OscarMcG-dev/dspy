import uvicorn
from fastapi import FastAPI
from api.services.tracing import init_tracing
from api.routes.health import router as health_router
from api.routes.experiments import router as experiments_router


def create_app() -> FastAPI:
    init_tracing()
    app = FastAPI(title="Codex API")
    app.include_router(health_router, prefix="/healthz", tags=["health"])
    app.include_router(experiments_router, prefix="/experiments", tags=["experiments"])
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
