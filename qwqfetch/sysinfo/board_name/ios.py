from ...tools.command import RunCommand
from ...tools.parse_info import parser


model_name = RunCommand(f"/usr/sbin/sysctl -n hw.model").readline()
info = f"Apple {model_name}"
