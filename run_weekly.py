import os
from sync_sheet import *
from analyze_performance import *

print("Starting weekly automation...")

# Step 1: Sync metrics from Google Sheet
print("Syncing sheet...")
os.system("python sync_sheet.py")

# Step 2: Analyze performance
print("Analyzing performance...")
os.system("python analyze_performance.py")

print("Weekly automation complete.")
