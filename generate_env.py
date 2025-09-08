import os
import pathlib
import subprocess


def git_sync(repo_url, target_dir):
    if pathlib.Path(target_dir).exists():
        subprocess.run(["git", "-C", target_dir, "pull", "origin", "main"], check=True)
    else:
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)


if __name__ == "__main__":
    env_path = pathlib.Path(__file__).resolve().parent
    os.chdir(env_path)

    # 更新env自身
    git_sync("https://github.com/Lujiang0111/env.git", ".")

    # 创建目录结构
    pathlib.Path("source/lib").mkdir(parents=True, exist_ok=True)
    pathlib.Path("source/program").mkdir(parents=True, exist_ok=True)
    pathlib.Path("version/lib").mkdir(parents=True, exist_ok=True)

    # source/lib
    git_sync("https://github.com/Lujiang0111/lccl.git", "source/lib/lccl")
    git_sync("https://github.com/Lujiang0111/pcap_dump.git", "source/lib/pcap_dump")
    git_sync("https://github.com/Lujiang0111/ts_transmit.git", "source/lib/ts_transmit")

    # source/program
    git_sync(
        "https://github.com/Lujiang0111/pcap_recorder2.git",
        "source/program/pcap_recorder2",
    )
    git_sync(
        "https://github.com/Lujiang0111/udp_recorder.git", "source/program/udp_recorder"
    )

    print("generate done.")
