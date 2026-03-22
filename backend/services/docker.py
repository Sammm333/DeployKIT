import os
import subprocess

DOCKER = "docker"

def build_and_run(repo_path: str, app_name: str, port: str) -> str:
    print(f"repo_path: {repo_path}")
    print(f"Dockerfile exists: {os.path.exists(os.path.join(repo_path, 'Dockerfile'))}")

    subprocess.run(
        [DOCKER, "build", "-t", app_name, "."],
        cwd=repo_path,
        check=True
    )

    subprocess.run([DOCKER, "rm", "-f", app_name])

    subprocess.run([
        DOCKER, "run", "-d",
        "--name", app_name,
        "-p", f"{port}:{port}",
        app_name
    ], check=True)

    return port