from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.git import clone_repo
from services.detector import detect_stack, detect_port
from services.generator import generate_dockerfile
from services.docker import build_and_run
import os

router = APIRouter()

class DeployRequest(BaseModel):
    repo_url: str

@router.post("/deploy")
async def deploy(request: DeployRequest):
    try:
        repo_path = clone_repo(request.repo_url)
        print(f"1. repo_path: {repo_path}")
        
        stack = detect_stack(repo_path)
        print(f"2. stack: {stack}")
        
        port = detect_port(stack, repo_path)
        print(f"3. port: {port}")

        dockerfile = os.path.join(repo_path, 'Dockerfile')
        print(f"4. Dockerfile exists: {os.path.exists(dockerfile)}")
        print(f"5. Dockerfile path: {dockerfile}")

        if not os.path.exists(dockerfile):
            generate_dockerfile(stack, port, repo_path)

        app_name = request.repo_url.rstrip('/').split('/')[-1].replace('.git', '')
        print(f"6. app_name: {app_name}")
        
        url = build_and_run(repo_path, app_name, port)
        return {"success": True, "url": url, "stack": stack}
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))