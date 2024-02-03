from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.lifespan import lifespan
from app.routes.bots import router

# Initialize FastAPI app (similar to Flask)
app = FastAPI(lifespan=lifespan)

# setup static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Register routes
app.include_router(router, prefix="/telegram")
