import os
import argparse


def get_files(path):
    files_list = []
    for root, dirs, files in os.walk(path):
        files_list += [
            {
                "name": filename,
                "path": os.path.join(root, filename),
                "size": os.path.getsize(os.path.join(root, filename))
                }
            for filename in files
            ]
    return files_list


def get_dublicates(files_list):
    dublicates_dict = {}
    for file in files_list:
        name = file["name"]
        if name not in dublicates_dict:
            size = file["size"]
            similar_files = [
                dublicate
                for dublicate in files_list
                if dublicate["name"] == name and
                dublicate["size"] == size
                ]
            if len(similar_files) > 1:
                dublicates_dict[name] = similar_files
    return dublicates_dict


def print_dublicates(dublicates):
    for name, files in dublicates.items():
        print("\n {}:\n".format(name))
        for path in [file["path"] for file in files]:
            print("\t", path)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", default=".", dest="path")
    args = parser.parse_args()
    return args.path


def main():
    path = get_arguments()
    founded_files = get_files(r"{}".format(path))
    dublicates = get_dublicates(founded_files)
    print_dublicates(dublicates)


if __name__ == "__main__":
    main()

