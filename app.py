import os
import logging
import argparse
from time_calculator import calculate_total_work_time, get_args
from logs_file import tracker_logs_file, read


def start(logger, project):
    logger.info(f'{project}. Starting time_tracker')


def stop(logger, project):
    logger.info(f'{project}. Stop')


def info(logger, project, msg):
    logger.info(f'{project}. {msg}')


def main():
    logging.basicConfig(
        filename=tracker_logs_file,
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)-s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logger = logging.getLogger('time_tracker')

    project = input('Enter project name: ').strip()
    start(logger, project)
    while True:
        msg = input('Enter completed task: ').strip()

        if msg.lower() == 'stop':
            stop(logger, project)
            break
        elif msg.lower() == 'change project':
            new_project = input('Enter project name: ').strip()
            stop(logger, project)
            project = new_project
            start(logger, project)
        elif msg:
            info(logger, project, msg)

    logs = read(tracker_logs_file)
    calculate_total_work_time(logs, get_args().since)


if __name__ == '__main__':
    main()
