from fastapi import FastAPI
from app.core.config import get_app_settings
from app.api.v1.api import router as api_router

settings = get_app_settings()

app = FastAPI(
    title=settings.title, openapi_url=f"{settings.openapi_prefix}{settings.openapi_url}"
)


# Routers
app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


# def print_routes(application: FastAPI):
#     print("Routes:")
#     for route in application.routes:
#         if isinstance(route, APIRoute):
#             print(
#                 f"* Path: {route.path} | Methods: {', '.join(route.methods)} | Name: {route.name}"
#             )

# if __name__ == "__main__":


# print_routes(app)
