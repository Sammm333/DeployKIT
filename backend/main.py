
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.deploy import router as deploy_router



app = FastAPI(title="DeployKit", description="Automated deployment service for web applications")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deploy_router, prefix="/api")


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")