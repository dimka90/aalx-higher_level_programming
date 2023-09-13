#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Define the status codes we want to track
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0


# Function to print the statistics
def print_statistics(signal, frame):
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_codes):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")
    sys.exit(0)


# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, print_statistics)

# Read input line by line
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) == 7:
            ip_address, _, _, _, _, status_code_str, file_size_str = parts
            status_code = int(status_code_str)
            file_size = int(file_size_str)

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
            # Check if 10 lines have been processed
            if line_count % 10 == 0:
                print_statistics(None, None)
    except ValueError:
        pass  # Ignore lines with incorrect format
