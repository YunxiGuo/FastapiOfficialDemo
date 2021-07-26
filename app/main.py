from fastapi import FastAPI
from routers import users


app = FastAPI()
app.include_router(users.router)

# app.api_route(api_route)


@app.on_event("startup")
async def startup():
    pass
    # await database.connect()


@app.on_event("shutdown")
async def shutdown():
    pass
    # await database.disconnect()
