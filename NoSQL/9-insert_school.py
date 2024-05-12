#!/usr/bin/env python3
"""Inserting item to mongodb"""


def insert_school(mongo_collection, **kwargs):
    """Inserts an item"""
    return mongo_collection.insert(kwargs)
