"""
API Gateway entry point

"""
from fastapi import FastAPI
from versioned_fastapi import FastApiVersioner

from routes import router


app = FastAPI(
  title="IRON Store",
  summary="IRON Store API gateway"
)

app.include_router(router)

versions = FastApiVersioner(app)

versions.prefix_format = "/api/v{version}"
versions.default_version = 1
versions.version_fastapi()
