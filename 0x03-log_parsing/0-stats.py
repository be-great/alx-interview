#!/usr/bin/python3
import sys
"""import file names"""

# Initialize total file size and status code counters
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """
    Prints the accumulated metrics:
    total file size and status code counts
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


try:
    # Process each line from stdin
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        try:
            # Extract status code and file size from each log line
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size and status code counts
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except (IndexError, ValueError):
            # Skip the line if there's a format error
            continue

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interruption (CTRL + C)
    print_stats()
    raise

# Print final stats after reading all lines (if script ends normally)
print_stats()
