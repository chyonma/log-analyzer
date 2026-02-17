import argparse
import os
from collections import Counter
import datetime

error_lines = []
parser = argparse.ArgumentParser(description="Simple Log Analyzer")
parser.add_argument("--file", required=True, help="Path to log file")
parser.add_argument("--level", help="Filter by log level (INFO, WARNING, ERROR)")

args = parser.parse_args()

filter_level = args.level

log_file = args.file
print(f"Analyzing file: {log_file}")

if not os.path.exists(log_file):
    print("Error: Log file not found.")
    exit()
with open(log_file, "r") as f:
    lines = f.readlines()
print(f"Total lines found: {len(lines)}")

error_count = 0
warning_count = 0
info_count = 0
consecutive_errors = 0
max_consecutive_errors = 0
for line in lines:
    if filter_level and filter_level not in line:
        continue

    if "ERROR" in line:
        error_count += 1
        error_lines.append(line.strip())

        consecutive_errors +=1
        if consecutive_errors > max_consecutive_errors:
            max_consecutive_errors = consecutive_errors
    
    else:
        consecutive_errors = 0

    if "WARNING" in line:
        warning_count += 1
    elif "INFO" in line:
        info_count += 1

top_errors = Counter(error_lines).most_common(3)

print("\n===== Log Summary =====")
print(f"INFO: {info_count}")
print(f"WARNING: {warning_count}")
print(f"ERROR: {error_count}")

if max_consecutive_errors >= 2:
    print("\n⚠️ Possible error spike detected!")
    print(f"Max consecutive errors: {max_consecutive_errors}")

print("\n===== Top Errors =====")
for err, count in top_errors:
    print(f"{count}x - {err}")

now = datetime.datetime.now()
with open("report.txt", "w") as r:
    r.write(f"Report generated at: {now}\n")
    r.write(f"INFO: {info_count}\n")
    r.write(f"WARNING: {warning_count}\n")
    r.write(f"ERROR: {error_count}\n")

    r.write("\nTop Errors: \n")
    for err, count in top_errors:
        r.write(f"{count}x - {err}\n")


