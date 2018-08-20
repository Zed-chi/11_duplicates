import os
import argparse
from collections import defaultdict


def get_files_paths(path):
    files_paths = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            size = os.path.getsize(os.path.join(dirpath, filename))
            path = os.path.join(dirpath, filename)
            files_paths[(filename, size)].append(path)
    return files_paths


def get_duplicates_paths(files_paths):
    duplicates_paths = {}
    for identificator, paths in files_paths.items():
        if len(paths) > 1:
            duplicates_paths[identificator] = paths
    return duplicates_paths


def print_duplicates_paths(duplicates_paths):
    for (filename, size), paths in duplicates_paths.items():
        print("\n {} - {} bytes:\n".format(filename, size))
        print("\n\t".join(paths))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", default=".", dest="path")
    args = parser.parse_args()
    return args


def main():
    path = get_args().path
    founded_files_paths = get_files_paths(path)
    duplicates_paths = get_duplicates_paths(founded_files_paths)
    print_duplicates_paths(duplicates_paths)


if __name__ == "__main__":
    main()
