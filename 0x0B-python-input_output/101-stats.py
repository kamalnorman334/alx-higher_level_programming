#!/usr/bin/python3
import sys
from collections import defaultdict

# Initialize metrics dictionary
metrics = defaultdict(int)
total_size = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Read stdin line by line
for i, line in enumerate(sys.stdin):
    # Parse line
    parts = line.strip().split()
    ip_address, _, date, request, status_code, file_size = parts
    file_size = int(file_size)

    # Update metrics
    total_size += file_size
    metrics[status_code] += 1

    # Print metrics every 10 lines or after a keyboard interruption
    if (i + 1) % 10 == 0 or sys.stdin.channel.closed:
        print(f'Total file size: File size: {total_size}')
        for status_code in status_codes:
            if metrics[status_code] > 0:
                print(f'{status_code}: {metrics[status_code]}')
        print()

        # Reset metrics
        total_size = 0
        metrics = defaultdict(int)
