from ...tools.command import RunCommand

memory_all = int(RunCommand("sysctl -n hw.memsize").read()) / 1024
free_pages = int(RunCommand("sysctl -n vm.page_free_count").read())
page_size = int(RunCommand("sysctl -n hw.pagesize").read())
memory_free = free_pages * page_size / 1024
memory_used = memory_all - memory_free
