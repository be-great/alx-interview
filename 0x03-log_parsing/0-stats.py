#!/usr/bin/python3
"""
Log parsing script that reads log data from stdin and computes metrics.
- Calculates the total file size.
- Tracks the number of occurrences of specific HTTP status codes.
"""

import sys
import re


def display_stats(log_data: dict) -> None:
    """
    Helper function to display the current log statistics.
    This function prints the total file size and the count of each status code
    if it has been encountered.

    Args:
        log_data (dict): A dictionary containing the accumulated file size
                         and status code frequency.
    """
    print("File size: {}".format(log_data["total_size"]))
    for status_code in sorted(log_data["status_counts"]):
        if log_data["status_counts"][status_code]:
            print("{}: {}".format(
                status_code,
                log_data["status_counts"][status_code]
            ))


if __name__ == "__main__":
    # Regular expression to match log
    # format (IP, date, request, status code, file size)
    log_pattern = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        + ' - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
        r'"GET /projects/260 HTTP/1.1" (.{3}) (\d+)'  # noqa: E501
    )

    # Initialize variables to store log data and line count
    line_counter = 0
    log_data = {
        "total_size": 0,
        "status_counts": {
            str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]
        }
    }

    try:
        # Read each line from standard input (e.g., piped log file)
        for line in sys.stdin:
            line = line.strip()

            # Check if the line matches the log pattern
            match = log_pattern.fullmatch(line)
            if match:
                line_counter += 1
                status_code = match.group(1)
                file_size = int(match.group(2))

                # Update total file size
                log_data["total_size"] += file_size

                # Update status code frequency if the status code is a number
                if status_code.isdecimal():
                    log_data["status_counts"][status_code] += 1

                # Display stats after every 10 lines of input
                if line_counter % 10 == 0:
                    display_stats(log_data)

    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        display_stats(log_data)
        raise

    # Always display final stats at the end
    display_stats(log_data)
