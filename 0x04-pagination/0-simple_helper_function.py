#!/usr/bin/env python3
"""
Exercise:
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Simple helper"""

    start = (page - 1) * page_size
    end = page * page_size

    return start, end
