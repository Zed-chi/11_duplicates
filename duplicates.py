import os
import argparse


def get_all_files(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        file_list += [
            {
                "name": filename,
                "path": os.path.join(root, filename),
                "size": os.path.getsize(os.path.join(root, filename))
                }
            for filename in files
            ]
    return file_list


def get_dublicates_set(file_list):
    dubl_dict = {}
    for file_info in file_list:
        name = file_info["name"]
        if name not in dubl_dict:
            size = file_info["size"]
            dublicates = [
                i
                for i in file_list
                if i["name"] == name and
                i["size"] == size
                ]
            if len(dublicates) > 1:
                dubl_dict[name] = dublicates
    return dubl_dict


def print_dublicates(dublicates_container):
    for name, dublicates in dublicates_container.items():
        print(f"\n {name}:\n")
        for i in [x["path"] for x in dublicates]:
            print("\t", i)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", action="store", dest="path")
    args = parser.parse_args()
    path = args.path if args.path else "."
    file_list = get_all_files(path)
    dublicates_set = get_dublicates_set(file_list)
    print_dublicates(dublicates_set)


if __name__ == "__main__":
    main()
