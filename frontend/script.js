const API_URL = `${window.location.origin}/api/deploy`;

const messages = [
  "Cloning repository...",
  "Detecting stack...",
  "Generating Dockerfile...",
  "Building Docker image...",
  "Starting container...",
];

let msgInterval;

function showStatus(text) {
  const status = document.getElementById("status");
  const statusText = document.getElementById("statusText");
  status.classList.add("visible");
  statusText.textContent = text;
}

function cycleMessages() {
  let i = 0;
  showStatus(messages[i]);
  msgInterval = setInterval(() => {
    i = (i + 1) % messages.length;
    document.getElementById("statusText").textContent = messages[i];
  }, 2500);
}

function stopMessages() {
  clearInterval(msgInterval);
  document.getElementById("status").classList.remove("visible");
}

function showResult(data) {
  const host = window.location.hostname;
  const url = `http://${host}:${data.url}`;

  document.getElementById("resStack").textContent = data.stack;
  document.getElementById("resPort").textContent = data.url;
  document.getElementById("resUrl").textContent = url;
  document.getElementById("resUrl").href = url;
  document.getElementById("result").classList.add("visible");

  const btn = document.getElementById("downloadBtn");
  btn.style.display = "block";
  btn.onclick = () => {
    const blob = new Blob([data.dockerfile], { type: "text/plain" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "Dockerfile";
    a.click();
  };
}

function showError(msg) {
  const errorBox = document.getElementById("errorBox");
  errorBox.textContent = "Error: " + msg;
  errorBox.classList.add("visible");
}

function reset() {
  document.getElementById("result").classList.remove("visible");
  document.getElementById("errorBox").classList.remove("visible");
  document.getElementById("status").classList.remove("visible");
  document.getElementById("downloadBtn").style.display = "none";
}

async function deploy() {
  const repoUrl = document.getElementById("repoUrl").value.trim();
  const btn = document.getElementById("deployBtn");

  if (!repoUrl) {
    showError("Please enter a GitHub URL");
    return;
  }

  reset();
  btn.disabled = true;
  cycleMessages();

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ repo_url: repoUrl }),
    });

    const data = await response.json();
    stopMessages();

    if (!response.ok) {
      showError(data.detail || "Something went wrong");
    } else {
      showResult(data);
    }
  } catch (err) {
    stopMessages();
    showError("Cannot connect to backend. Is it running?");
  } finally {
    btn.disabled = false;
  }
}

document.getElementById("repoUrl").addEventListener("keydown", (e) => {
  if (e.key === "Enter") deploy();
});