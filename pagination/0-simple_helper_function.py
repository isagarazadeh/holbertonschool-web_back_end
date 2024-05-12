#!/usr/bin/env python3
"""Simple function"""


def index_range(page, page_size):
    """Index range"""
    beginning = (page - 1) * page_size
    end = page * page_size
    return (beginning, end)
