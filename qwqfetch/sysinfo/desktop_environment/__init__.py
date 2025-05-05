from __future__ import annotations
from ... import global_vars

platform_info = global_vars.get(["platform"])[0]
sys_name = platform_info["name"]
sys_arch = platform_info["arch"]


def get() -> dict[str, str]:
    if sys_name == "Windows":
        de_name = "Windows Shell"
    elif sys_name == "Darwin" and "iPhone" in sys_arch:
        de_name = ""
    elif sys_name == "Darwin":
        de_name = "Aqua"
    elif sys_name == "Linux":
        from os import getenv

        de_name = getenv("DESKTOP_SESSION")
        if not de_name:
            de_name = ""
    else:
        de_name = ""

    if de_name == "plasma":
        from .plasma import get as getplasma

        de_name = getplasma()
    return {"DE": de_name}
