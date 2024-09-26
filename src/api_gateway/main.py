import asyncio

from fastapi import FastAPI
from versioned_fastapi import FastApiVersioner

from hypercorn.asyncio import serve
from hypercorn.config import Config

from .routers import router




app = FastAPI(
  title="API Gateway [ IRON Store ]"
)


def start():
  config = Config()
  config.bind = "127.0.0.1:9000"

  app.include_router(router)

  versions = FastApiVersioner(app)

  versions.prefix_format = "/api/v{version}"
  versions.default_version = 1
  versions.version_fastapi()

  asyncio.run(
    serve(versions.app, config)
  )
