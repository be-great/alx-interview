#!/usr/bin/python3
"""
Log parsing script that computes and prints metrics:
- Total file size
- Number of occurrences of specific status codes
"""
import sys


if __name__ == '__main__':
    # Initialize total file size and line counter
    filesize, count = 0, 0
    # Define possible status codes and initialize their counters
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Prints accumulated metrics:
        total file size and status code counts.
        """
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        # Read each line from stdin
        for line in sys.stdin:
            count += 1
            data = line.split()

            # Update status code counts
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except (IndexError, ValueError):
                pass

            # Update total file size
            try:
                filesize += int(data[-1])
            except (IndexError, ValueError):
                pass

            # Print stats every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)

        # Print final stats after processing all lines
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        # Print stats on keyboard interruption (CTRL + C)
        print_stats(stats, filesize)
        raise
