import os


def tracker_logs_file_default():
    script = os.path.abspath(__file__)
    project_dir = os.path.dirname(script)
    logs_path = os.path.join(project_dir, 'time_tracking.logs')
    return logs_path


def read(logs_path):
    with open(logs_path, 'r') as f:
        return f.read()


tracker_logs_file = os.environ.get('TIME_TRACKING_LOGS', tracker_logs_file_default())
