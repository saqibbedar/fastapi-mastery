from pathlib import Path

# Get absolute path *this file
core_dir = Path(__file__).resolve().parent

# Go two level up to read data/data.json file
project_root = core_dir.parent.parent

# Get the data dir
data_dir = (project_root / "data" / "data.json").resolve()

# resolve path for /data/data.json
DATA_DIR: Path | None = data_dir if data_dir.exists() and data_dir.is_file and data_dir.suffix == ".json" else None
