"""FastAPI application factory for the simulator service."""

import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .routes import get_home, router


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):  # pylint: disable=unused-argument
    """Manage the simulator lifecycle when the API starts and stops."""

    get_home().start_simulation()
    logger.info("SmartHome simulation started")
    try:
        yield
    finally:
        get_home().stop_simulation()
        logger.info("SmartHome simulation stopped")


def create_app() -> FastAPI:
    """Instantiate and configure the FastAPI application."""

    application = FastAPI(
        title="Virtual Smart Home", version="1.0.0", lifespan=lifespan
    )
    application.include_router(router)
    return application


app = create_app()


def main() -> None:
    """Entry point used by ``python -m src.simulator.api.app``."""

    import uvicorn

    port = int(os.getenv("SERVER_PORT", 8000))
    uvicorn.run("src.simulator.api.app:app", host="0.0.0.0", port=port, reload=False)


if __name__ == "__main__":
    main()
