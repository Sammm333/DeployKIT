# 🚀 DeployKit

> Paste a GitHub URL → get a live Docker container in seconds.

DeployKit is a self-hosted deployment platform that automatically clones a GitHub repository, detects the tech stack, generates a Dockerfile if needed, and deploys it as a running Docker container — inspired by Heroku and Railway.

> 💡 **Live Demo available** — DM me on LinkedIn for access. Or clone and run it yourself (see below).

---

## ✨ Features

- **Auto stack detection** — detects Python, Node.js, Go from repo files
- **Dockerfile generation** — auto-generates Dockerfile if not present
- **Port detection** — reads port from `app.py`, `main.py`, `server.js` automatically
- **One-click deploy** — paste a GitHub URL and get a live container
- **Dockerfile download** — download the generated Dockerfile after deploy
- **Automatic cleanup** — repo folder deleted after deploy, image stays
- **Concurrency protection** — semaphore prevents server overload
- **CI/CD** — GitHub Actions auto-deploys on every push to main
- **CloudWatch monitoring** — CPU, RAM, logs monitored on AWS EC2

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, Python 3.11 |
| Containerization | Docker, Docker Compose |
| Cloud | AWS EC2 (t3.small) |
| Monitoring | AWS CloudWatch |
| CI/CD | GitHub Actions |
| Frontend | HTML, CSS, Vanilla JS |
| Web Server | Uvicorn |

---

## 🏗 Architecture
```
User pastes GitHub URL
          ↓
    FastAPI Backend
          ↓
     git clone repo
          ↓
  detect stack (Python/Node/Go)
          ↓
  detect port from source code
          ↓
  generate Dockerfile (if missing)
          ↓
  docker build + docker run
          ↓
  cleanup repo folder
          ↓
  return live URL + Dockerfile ✅
```

---

## 🚀 Run It Yourself

### Requirements

- Docker
- Docker Compose
- Git

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/Sammm333/DeployKIT.git
cd DeployKIT

# 2. Build and run
docker compose up --build

# 3. Open in browser
# http://YOUR_SERVER_IP:8000
```

> ⚠️ DeployKit needs access to Docker socket to build and run containers.
> The `docker-compose.yml` mounts `/var/run/docker.sock` automatically.

---

## 📋 How It Works

1. User pastes a GitHub repository URL into the web UI
2. DeployKit clones the repository onto the server
3. Detects the stack by checking files:
   - `package.json` → Node.js
   - `requirements.txt` → Python
   - `go.mod` → Go
4. Reads the port from source files (`app.py`, `main.py`, `index.js`)
5. Generates a Dockerfile if one doesn't exist
6. Runs `docker build` + `docker run` with the correct port
7. Cleans up the cloned repo folder
8. Returns a live URL and the generated Dockerfile for download

---

## ☁️ AWS Infrastructure

- **EC2 t3.small** — hosts DeployKit and all deployed containers
- **Elastic IP** — fixed public IP that doesn't change on restart
- **Security Groups** — ports 8000 (DeployKit) and app ports open
- **CloudWatch Agent** — monitors CPU, RAM, and Docker container logs

---

## 🔄 CI/CD Pipeline

Every push to `main` branch triggers GitHub Actions:
```
git push
    ↓
GitHub Actions runner
    ↓
SSH into EC2
    ↓
git pull + docker compose up --build -d
    ↓
DeployKit updated on server ✅
```

---

## 📁 Project Structure
```
DeployKIT/
├── Dockerfile
├── docker-compose.yml
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── routes/
│   │   └── deploy.py
│   └── services/
│       ├── git.py
│       ├── detector.py
│       ├── generator.py
│       └── docker.py
└── frontend/
    ├── index.html
    └── script.js
```

---

## 🗺 Roadmap

- [ ] Nginx reverse proxy + SSL (HTTPS)
- [ ] Custom domain support
- [ ] Deploy history dashboard
- [ ] GitHub webhook — auto redeploy on push
- [ ] Support for more stacks (Ruby, PHP, Rust)
- [ ] Kubernetes deployment option

---

## 📄 License

MIT License

---

## 👤 Author

**Samvel Khachatryan** — Backend & DevOps Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)]www.linkedin.com/in/samvel-khachatryan-04b9b3371
[![GitHub](https://img.shields.io/badge/GitHub-Sammm333-black)](https://github.com/Sammm333)