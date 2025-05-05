from __future__ import annotations
from ...tools.command import RunCommand
from .ios_cpus import cpu_freq_map

def run_sysctl(key: str) -> str:
    return RunCommand(f"/usr/sbin/sysctl -n {key}").readline()


def get_cpu_info() -> dict[str, str]:
    total_cores = run_sysctl("hw.physicalcpu_max")
    try:
        name = run_sysctl("kern.version").split("/")[1].split("_")[-1]
        freq = cpu_freq_map[name]
    except:
        name = ""
        freq = 0
    info = {
        "name": name,
        "core": int(total_cores),
        "freq": freq,
    }

    return info
