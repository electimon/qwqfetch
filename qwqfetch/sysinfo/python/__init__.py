import platform

def get() -> dict[str, str]:
    return {"Python": platform.python_version()}
