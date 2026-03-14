import os
import re

def detect_stack(repo_path: str) -> str:
    files = os.listdir(repo_path)

    if 'package.json' in files:
        return 'node'
    elif 'requirements.txt' in files:
        return 'python'
    elif 'go.mod' in files:
        return 'go'
    else:
        return 'unknown'


def detect_port(stack: str, repo_path: str) -> str:
    defaults = {
        'node': '3000',
        'python': '8000',
        'go': '8080'
    }

    try:
        for filename in ['app.py', 'main.py', 'index.js', 'server.js']:
            filepath = os.path.join(repo_path, filename)
            if os.path.exists(filepath):
                content = open(filepath).read()
                match = re.search(r'port\s*=\s*(\d+)', content, re.IGNORECASE)
                if match:
                    return match.group(1)
    except:
        pass

    return defaults.get(stack, '3000')