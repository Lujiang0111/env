import subprocess
from pathlib import Path


def git_clone_if_missing(repo_url, target_dir):
    if not Path(target_dir).exists():
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)


# 创建目录结构
Path("source/lib").mkdir(parents=True, exist_ok=True)
Path("source/program").mkdir(parents=True, exist_ok=True)
Path("version/lib").mkdir(parents=True, exist_ok=True)

# 克隆库
git_clone_if_missing("https://github.com/Lujiang0111/lccl.git", "source/lib/lccl")
git_clone_if_missing(
    "https://github.com/Lujiang0111/libpcap_dump.git", "source/lib/libpcap_dump"
)
git_clone_if_missing(
    "https://github.com/Lujiang0111/pcap_recorder2.git", "source/program/pcap_recorder2"
)

print("done.")
