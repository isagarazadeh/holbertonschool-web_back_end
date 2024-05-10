#!/usr/bin/env python3
"""listing"""
def list_all(mongo_collection):
    """function"""
    return mongo_collection.find()
