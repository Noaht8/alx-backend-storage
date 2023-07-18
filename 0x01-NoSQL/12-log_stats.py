#!/usr/bin/env python3
"""Log stats module"""
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient()
db = client.logs
collection = db.nginx

# Get the total number of logs
total_logs = collection.count_documents({})

# Get the number of logs for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_logs = {}
for method in methods:
    method_logs[method] = collection.count_documents({"method": method})

# Get the number of logs with method=GET and path=/status
status_check_logs = collection.count_documents({"method": "GET", "path": "/status"})

# Print the statistics
print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_logs[method]}")
print(f"{status_check_logs} status check")
