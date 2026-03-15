import os

def detect_main_file(repo_path: str) -> str:
    for filename in ['app.py', 'main.py', 'server.py', 'run.py']:
        if os.path.exists(os.path.join(repo_path, filename)):
            return filename
    return 'app.py'

def generate_dockerfile(stack: str, port: str, repo_path: str):
    main_file = detect_main_file(repo_path)

    templates = {
        "node": f"""FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE {port}
CMD ["npm", "start"]""",

        "python": f"""FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE {port}
CMD ["python", "{main_file}"]""",

        "go": f"""FROM golang:1.21-alpine
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o main .
EXPOSE {port}
CMD ["./main"]"""
    }

    content = templates.get(stack, templates["node"])

    with open(os.path.join(repo_path, "Dockerfile"), "w") as f:
        f.write(content)