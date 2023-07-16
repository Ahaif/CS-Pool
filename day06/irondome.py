import os
import sys
import argparse
import time
import logging
from cryptography.fernet import Fernet


def check_root():
    if os.geteuid() != 0:
        print("You need to be root to run this script")
        sys.exit(1)


def set_up(log_file):
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')



def monitor_critical_area(path):
    logging.info("Monitoring critical area: %s", path)
    for root, dirs, files in os.walk(path):
        for file in files:
            

def main():
    check_root()
    log_file = "/var/log/irondome.log"
    set_up(log_file)

    if len(sys.argv) > 1:
        path_to_monitor = sys.argv[1]
    else:
        paths_to_monitor = ["~/default1", "~/default2"]
    try:
        while True:
            for path in paths_to_monitor:
                monitor_critical_area(path)
            time.sleep(5)

    