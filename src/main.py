from fastapi import FastAPI
from src.settings import settings
from src.api.v1.payment import payment_router
from fastapi.middleware.cors import CORSMiddleware
from src.infra.database.modelbase import model_init
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute


# Core Application Instance
def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.API_VERSION,
        debug=settings.DEBUG,
    )

    # Add middleware cors
    origins = ["http://localhost:8000" "https://localhost:8000"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add Health Checks
    _healthChecks = HealthCheckFactory()
    app.add_api_route(
        "/health",
        endpoint=healthCheckRoute(factory=_healthChecks),
        tags=["health"],
        name="health_check",
        description="Rota para validar o funcionamento da API.",
    )

    # Add Routers
    app.include_router(payment_router, prefix=settings.API_PREFIX)

    # Initialise Data Model
    model_init()

    return app


app = create_app()
