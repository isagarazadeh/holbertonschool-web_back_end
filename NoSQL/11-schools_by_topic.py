#!/usr/bin/env python3
"""Search by Topic"""


def schools_by_topic(mongo_collection, topic):
    """School by topic"""
    return mongo_collection.find({"topics": topic})
