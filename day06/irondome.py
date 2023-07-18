#!/usr/bin/env python3
import os
import sys
import argparse
import time
import logging
from cryptography.fernet import Fernet
import hashlib


def check_root():
    if os.geteuid() != 0:
        print("You need to be root to run this script")
        sys.exit(1)


def set_up(log_file):
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')


def get_hash(file):
     # Function to calculate the hash of a file using SHA256.
    sha256_hash = hashlib.sha256()
    with open(file, "rb") as f:
        # Read the file in small chunks to handle large files.
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def monitor_critical_area(path, initial_hashes):
    if not os.path.exists(path):
        print(f"The directory '{path}' does not exist.")
        return

    print(f"Monitoring critical area: {path}")
    logging.info("monitoring file changes based on their hashes : %s", path)
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "test.txt":
                full_file_path = os.path.join(root, file)  # Join the root and file to get the full path

                read_count = initial_hashes.get(full_file_path, 0)
                read_count += 1
                initial_hashes[full_file_path] = read_count

                if read_count > 3:
                    logging.warning("Potential disk read abuse detected for file: %s", full_file_path)

                
                if file in initial_hashes:
                    file_hash = get_hash(full_file_path)
                    if file_hash != initial_hashes[file]:
                        logging.warning("File %s has been modified", full_file_path)
                else:
                    logging.info("File %s has been added", full_file_path)
                    initial_hashes[file] = get_hash(full_file_path)

    print(f"Monitoring critical area: {path}")
    logging.info("Monitoring critical area Cryptography part : %s", path)        


initial_hashes = {}


def main():
    check_root()
    log_file = "/home/abdel/Documents/CS-Pool/day06/log/irondome.log"
    set_up(log_file)

    
    paths_to_monitor = []

    if len(sys.argv) > 1:
        paths_to_monitor = [sys.argv[1]]
    else:
        paths_to_monitor = ["/default1", "~/default2"]
    try:
        while True:
            for path in paths_to_monitor:
                monitor_critical_area(path, initial_hashes)
            time.sleep(2)
    except KeyboardInterrupt:
        logging.info("Exiting IronDome")

if __name__ == "__main__":
    main()