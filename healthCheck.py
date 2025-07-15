#!/usr/bin/env python3

import shutil
import psutil

def check_cpu():
    usage = psutil.cpu_percent(1)
    return usage < 75


def check_disk(disk):
    du= shutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free > 20

if not check_disk("/") or not check_cpu():
    print("ERROR!")
else:
    print("Every thing ok!!")