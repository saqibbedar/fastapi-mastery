from pathlib import Path

curr_file_dir = Path(__file__).parent

# go two level up (to access data dir)
Json_Data_File_Path = (curr_file_dir.parent.parent / "data" / "data.json").resolve()

JSON_DATA_FILE_PATH: Path | None = (
    Json_Data_File_Path
    if (Json_Data_File_Path.exists() and Json_Data_File_Path.is_file() and Json_Data_File_Path.suffix == ".json")
    else None
)
