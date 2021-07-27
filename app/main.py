from fastapi import FastAPI, Request
from routers import users, items
from schemas.models import StaticResponse

app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)


# app.api_route(api_route)


@app.middleware("http")
async def add_process_response(request: Request, call_next):
    response = await call_next(request)
    static_response = StaticResponse(code=200, result="success", data=response)
    return static_response


@app.on_event("startup")
async def startup():
    pass
    # await database.connect()


@app.on_event("shutdown")
async def shutdown():
    pass
    # await database.disconnect()
