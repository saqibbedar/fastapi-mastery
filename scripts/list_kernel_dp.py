# list_kernel_dp.py: list installed dependencies in kernel directory script

import tomllib
from pathlib import Path

ROOT = Path(__file__).parent.parent
pyproject_file_path = (ROOT / "kernel" / "pyproject.toml").resolve()


# read dependencies
def get_dependencies():
    if not pyproject_file_path.exists():
        raise FileNotFoundError("Unable to find pyproject.toml file")

    # read file
    with open(pyproject_file_path, "rb") as file:
        config = tomllib.load(file)

    project_table = config.get("project", {})
    deps = project_table.get("dependencies", [])
    dep_groups = config.get("dependency-groups", {})

    return {"dependencies": deps, "dependency-groups": dep_groups}


def main():
    try:
        print("\n--- kernel Directory ---\n")
        print(f"- A centralized directory to manage dependencies for everyday workflow.\n- Directory location: {(ROOT / "kernel").resolve()}\n\n")

        # current dependencies
        all_deps = get_dependencies()

        # core dependencies
        print("--- [Installed: Core Dependencies] ---\n")
        for dep in all_deps["dependencies"]:
            print(f"- {dep}")

        # dev dependencies
        print("\n--- [Installed: Dev Dependencies] ---\n")
        for group_name, group_deps in all_deps["dependency-groups"].items():
            print(f"[{group_name}]")
            for dep in group_deps:
                print(f"   - {dep}")

    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
