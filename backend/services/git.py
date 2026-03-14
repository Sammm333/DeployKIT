import subprocess
import os
import shutil
import stat

def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clone_repo(github_url: str) -> str:
    repo_name = github_url.rstrip("/").split("/")[-1].replace(".git", "")
    repo_path = os.path.join(os.getcwd(), "repos", repo_name)

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path, onerror=remove_readonly)

    os.makedirs(os.path.join(os.getcwd(), "repos"), exist_ok=True)
    subprocess.run(["git", "clone", github_url, repo_path], check=True)

    dockerignore_path = os.path.join(repo_path, '.dockerignore')
    if not os.path.exists(dockerignore_path):
         with open(dockerignore_path, 'w') as f:
            f.write(".git\n")

    return repo_path

