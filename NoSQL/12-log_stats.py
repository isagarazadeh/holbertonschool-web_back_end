#!/usr/bin/env python3
"""Example"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    find = {"method": "GET", "path": "/status"}
    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        dictionary = {"method": method}
        print(f'\tmethod {method}: {nginx.count_documents(dictionary)}')
    print(f'{nginx.count_documents(find)} status check')
