import yaml


def read(filename):

    with open(filename, "r", encoding="utf-8") as file:

        return yaml.safe_load(file)


def write(data, filename):

    with open(filename, "w", encoding="utf-8") as file:

        yaml.safe_dump(
            data,
            file,
            sort_keys=False
        )