# import os
from pathlib import Path
from itertools import chain

if __name__ == "__main__":
    # for dir_path, dir_names, files in os.walk("."):
    #     for file in files:
    #         if not (file.endswith(".py") or file.endswith(".sql")):
    #             continue
    #         problem_num, _, problem_name = file.partition("_")
    #         new_filename = f"{problem_num.zfill(5)}_{problem_name}"
    #         print(f"source: {os.path.join(dir_path, file)} -> destination: {os.path.join(dir_path, new_filename)}")
    #         os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_filename))

    for source in chain(Path.cwd().rglob("*.py"), Path.cwd().rglob("*.sql")):
        problem_num, _, problem_name = source.name.partition("_")
        new_name = problem_num.zfill(5) + "_" + problem_name
        source.rename(source.with_name(new_name))
        print(f"source: {source} -> destination: {source.with_name(new_name)}")
