#!/usr/bin/env python3
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


def get_hash(file):
     # Function to calculate the hash of a file using SHA256.
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read the file in small chunks to handle large files.
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def monitor_critical_area(path, initial_hashes):
    print("Monitoring critical area: %s", path)
    logging.info("Monitoring critical area: %s", path)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file  in initial_hashes:
                file_hash = get_hash(file)
                if file_hash != initial_hashes[file]:
                    logging.warning("File %s has been modified", file)
            else:
                logging.info("File %s has been added", file)
                initial_hashes[file] = get_hash(file)
def main():
    check_root()
    log_file = "/home/abdel/Documents/CS-Pool/day06/log/irondome.log"
    set_up(log_file)

    inital_hashes = {}
    paths_to_monitor = []

    if len(sys.argv) > 1:
        path_to_monitor = [sys.argv[1]]
    else:
        paths_to_monitor = ["/default1", "~/default2"]
    try:
        while True:
            for path in paths_to_monitor:
                monitor_critical_area(path, initial_hashes)
                break
            time.sleep(5)
    except KeyboardInterrupt:
        logging.info("Exiting IronDome")

if __name__ == "__main__":
    main()