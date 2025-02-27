import os
import subprocess

# GitHub Repository Details
GITHUB_REPO = "https://github.com/rishhongit/ClouVix.git"

def push_code():
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial Commit"])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "remote", "add", "origin", GITHUB_REPO])
    subprocess.run(["git", "push", "-u", "origin", "main"])

if __name__ == "__main__":
    push_code()
