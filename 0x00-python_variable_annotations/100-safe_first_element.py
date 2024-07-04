#!/usr/bin/env python3
'''Task 100 module.
'''


from typing import Sequence, Optional, Any

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None

