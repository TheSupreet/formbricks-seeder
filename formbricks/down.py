import subprocess

def down():
    print("🧹 Stopping Formbricks...")
    subprocess.run(["docker-compose", "down", "-v"], check=True)
    print("✅ Clean shutdown complete")
