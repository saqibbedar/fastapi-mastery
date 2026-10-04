# To run this Justfile, you need to install Just
# Justfile for automatic scripts

# cq (code quality): run code quality checks on kernel directory
cq:
    uv run --project kernel python scripts/code_quality.py

# list installed dependencies in kernel directory
# kdp (kernel dependencies): list kernel installed dependencies in central dir named kernel
kdp:
    uv run --project kernel python scripts/list_kernel_dp.py