from __future__ import annotations
from ... import global_vars

platform_info = global_vars.get(["platform"])[0]
sys_name = platform_info["name"]
sys_arch = platform_info["arch"]

def get() -> dict[str, str]:
    if sys_name == "Linux":
        from .linux import info
    elif sys_name == "Windows":
        from .windows import info
    elif sys_name == "Darwin" and "iPhone" in sys_arch:
        from .ios import info
    elif sys_name == "Darwin":
        from .macos import info
    else:
        info = ""
    return {"Host": info}
