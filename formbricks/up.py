import subprocess

def up():
    print("🚀 Starting Formbricks...")
    subprocess.run(["docker-compose", "up", "-d"], check=True)
    print("✅ Formbricks running at http://localhost:3000")
