# This script file is verification file for data directory
# You can completely ignore this and verify json and csv files directly /data dir.

from pathlib import Path

# get absolute path of current file's directory
curr_file_path_dir = Path(__file__).resolve().parent

# go one level up to project's root dir
project_root = curr_file_path_dir.parent

# get data directory path
data_dir = (project_root / "data").resolve()

# collect json & csv files
json_files: list = []
csv_files: list = []


# ls: list dir and files and generate useful info of data dir
def metadata_data_generator():
    if data_dir.is_dir():
        print(f"\n> ls {data_dir}\n")
        # .iterdir() yields Path objects one by one
        for item in data_dir.iterdir():
            type_indicator = "📁" if item.is_dir() else "📄"
            print(f"{type_indicator} {item.name}")

            if item.is_file():
                if item.suffix == ".json":
                    json_files.append(item.name)
                if item.suffix == ".csv":
                    csv_files.append(item.name)

        # print json and csv files collected in lists
        if len(json_files) > 0 and len(csv_files) > 0:
            print(f"Json files: {json_files}")
            print(f"CSV files: {csv_files}")

        else:
            # If no working files i.e., json/csv are found then show message
            print(f"No Json or CSV files were found at {data_dir}")

    else:
        # display error in-case if its not a directory
        print(f"Error: No data directory found at {data_dir}\nFix: check core/data.py to fix the error")


metadata_data_generator()


"""
Expected output:

> ls ${dynamic_path}

📄 data_generation_guide.md
📄 data.json
📄 data.csv
Json files: ['data.json']
CSV files: ['data.csv']
"""
