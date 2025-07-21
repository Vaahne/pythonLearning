#!/usr/bin/env python3
import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    # If result is  None ,  it should return empty string
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
