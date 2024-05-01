import os
import configparser
from datetime import datetime
import logging

def setup_folders():
    config = configparser.ConfigParser()
    config.read('config.properties')
    logs_folder = config.get('folders', 'logs_folder', fallback='Logs')
    reports_folder = config.get('folders', 'reports_folder', fallback='Reports')
    features_folder = config.get('folders', 'features_folder')
    steps_folder = config.get('folders', 'steps_folder', fallback='steps')
    return logs_folder, reports_folder, features_folder, steps_folder

def setup_logging(logs_folder):
    # # Configure Logs
    logs_file_path = os.path.join(logs_folder, "Batch Logs", "project.log")
    # # Ensure logs directory exists
    os.makedirs(os.path.dirname(logs_file_path), exist_ok=True)
    logging.basicConfig(filename=logs_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_reports(reports_folder):
    # # Configure Reports
    os.makedirs(reports_folder, exist_ok=True)
    report_file_path = os.path.join(reports_folder, f"execution_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
    return report_file_path


