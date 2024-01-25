#!/usr/bin/python3
import sys

def print_statistics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_counts.items()):
        print("{}: {}".format(code, count))

def parse_line(line, total_size, status_counts):
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        total_size += file_size

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

    except (ValueError, IndexError):
        pass

    return total_size, status_counts

def main():
    total_size = 0
    status_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            total_size, status_counts = parse_line(line.strip(), total_size, status_counts)

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()

