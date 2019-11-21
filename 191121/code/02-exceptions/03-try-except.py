#!/usr/bin/env python3
from typing import Optional
def try_parse_int(x: str) -> Optional[int]:
    try: 
        return int(x)
    except ValueError:
        return None


print(try_parse_int('123'))
print(try_parse_int('123x'))
