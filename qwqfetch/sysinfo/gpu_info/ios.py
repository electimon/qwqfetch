from ...tools.command import RunCommand
from .ios_gpus import hw_model_gpu_map

model_name = RunCommand(f"/usr/sbin/sysctl -n hw.model").readline()

gpu_info = hw_model_gpu_map[model_name]
