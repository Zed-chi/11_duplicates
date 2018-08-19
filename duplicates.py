import os
import argparse


def get_files_attributes(path):
    files_attrs_list = []
    for root, dirs, files in os.walk(path):
        files_attrs_list += [
            {
                "name": filename,
                "path": os.path.join(root, filename),
                "size": os.path.getsize(os.path.join(root, filename))
            } for filename in files
        ]
    return files_attrs_list


def get_dublicates_attributes(files_attributes_list):
    dublicates_attrs_dict = {}
    for file_attrs in files_attributes_list:
        filename = file_attrs["name"]
        if filename not in dublicates_attrs_dict:
            size = file_attrs["size"]
            similar_files_attributes = [
                file_attrs
                for file_attrs in files_attributes_list
                if file_attrs["name"] == filename
                and file_attrs["size"] == size
            ]
            if len(similar_files_attributes) > 1:
                dublicates_attrs_dict[filename] = similar_files_attributes
    return dublicates_attrs_dict


def print_dublicates_attributes(dublicates_attributes_dict):
    for filename_key, files_atributes in dublicates_attributes_dict.items():
        print("\n {}:\n".format(filename_key))
        paths = [
            file_attributes["path"]
            for file_attributes in files_atributes
        ]
        for file_path in paths:
            print("\t", file_path)


def get_path_from_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", default=".", dest="path")
    args = parser.parse_args()
    return args.path


def main():
    path = get_path_from_args()
    founded_files_attributes = get_files_attributes(r"{}".format(path))
    dublicates_attributes = get_dublicates_attributes(founded_files_attributes)
    print_dublicates_attributes(dublicates_attributes)


if __name__ == "__main__":
    main()
