import os
import argparse
from datetime import datetime, timedelta
from logs_file import tracker_logs_file, read


def calculate_total_work_time(logs, since):
    time_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.now()
    filter_time = datetime.min  # Default to all time

    if since == 'day':
        filter_time = now - timedelta(days=1)
    elif since == 'midnight':
        filter_time = datetime(now.year, now.month, now.day)
    elif since:
        try:
            filter_time = datetime.strptime(since, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print(f"Error parsing date: {since}. Calculating for the entire time.")

    print(f"Filtering logs from: {filter_time}")

    start_time = None
    afk_start = None
    total_time = 0
    afk_time = 0
    session_active = False

    for log in logs.split('\n'):
        log = log.strip()
        if not log:
            continue

        try:
            time_stamp = datetime.strptime(log[:19], time_format)
        except ValueError:
            print(f"Error parsing log timestamp: '{log[:19]}'")
            continue

        print(f"Log Timestamp: {time_stamp}, Entry: {log}")

        if time_stamp < filter_time:
            print('Skipping log')
            continue

        if "Starting time_tracker" in log:
            start_time = time_stamp
            session_active = True
            print(f"Session started at: {start_time}")
        elif "afk start" in log:
            afk_start = time_stamp
            print(f"AFK started at: {afk_start}")
        elif "afk stop" in log and afk_start is not None:
            afk_time += (time_stamp - afk_start).total_seconds()
            print(f"AFK stopped at: {time_stamp}, Total AFK Time: {afk_time} seconds")
            afk_start = None
        elif log.lower().endswith('stop') and session_active:
            if start_time is not None:
                session_time = (time_stamp - start_time).total_seconds() - afk_time
                total_time += session_time
                print(f"Session stopped at: {time_stamp}, Session Time: {session_time} seconds, Total Time: {total_time} seconds")
                start_time = None
                afk_time = 0
                session_active = False

    total_hours = total_time / 3600
    print(f'\u001b[30m\u001b[42mFull working time: {total_hours:.2f} hours\u001b[0m')
    return total_hours


def get_args():
    parser = argparse.ArgumentParser(description='Track work time for projects.')
    parser.add_argument('--since', type=str,
                        help='Calculate time since a specific point (day, midnight, or "YYYY-MM-DD HH:MM:SS")',
                        nargs='?', const='all', default='all')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    file_logs = read(tracker_logs_file)
    calculate_total_work_time(file_logs, get_args().since)
