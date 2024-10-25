#!/usr/bin/python3
"""
Log parsing module
"""
import re
import sys
from collections import defaultdict


# Regex paatern for Apache log entries
log_pattern = (
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/\d\.\d" (\d{3}) (\d+)'
        )

# initialization of metrics
total_file_size = 0
status_count = defaultdict(int)
line_count = 0


def print_metrics(total_size, status_count):
    """Prints the total file size and status code counts."""
    print(f"Total file size: {total_size}")
    for code in sorted(status_count.keys()):
        print(f"{code}: {status_count[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(log_pattern, line)

        if match:
            # Parse the log entry using regex
            status_code = match.group(3)
            file_size = int(match.group(4))

            # Update metrics
            total_file_size += file_size
            status_count[status_code] += 1
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_file_size, status_count)

except KeyboardInterrupt:
    print_metrics(total_file_size, status_count)
