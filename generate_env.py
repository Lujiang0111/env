import subprocess
from pathlib import Path


def git_clone_if_missing(repo_url, target_dir):
    if not Path(target_dir).exists():
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)


# 创建目录结构
Path("source/lib").mkdir(parents=True, exist_ok=True)
Path("source/program").mkdir(parents=True, exist_ok=True)
Path("version/lib").mkdir(parents=True, exist_ok=True)

# source/lib
git_clone_if_missing("https://github.com/Lujiang0111/lccl.git", "source/lib/lccl")
git_clone_if_missing(
    "https://github.com/Lujiang0111/pcap_dump.git", "source/lib/pcap_dump"
)
git_clone_if_missing(
    "https://github.com/Lujiang0111/ts_transmit.git", "source/lib/ts_transmit"
)

# source/program
git_clone_if_missing(
    "https://github.com/Lujiang0111/pcap_recorder2.git", "source/program/pcap_recorder2"
)

print("done.")
