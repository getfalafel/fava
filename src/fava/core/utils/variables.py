import os
import toml
from shutil import copy2


def get_app_dir():
    """
    :return :str
    """
    return os.getcwd()


def load_file(file_name):
    try:
        return toml.load(get_app_dir() + file_name)
    except OSError:
        print("Cannot open variables file", file_name)
        return None


def load_env_file():
    """
    :return:
    """
    variables = {"default": {}}
    with open(get_app_dir() + "/.env", "r") as f:
        for line in f.readlines():
            if "=" in line:
                key, value = (
                    line.replace("\n", "").replace(" ", "").replace("'", "").split("=")
                )
                variables["default"][key] = value
    return variables["default"]


def project_variables():
    """
    :return:
    """
    variables = {}
    if os.path.isfile(get_app_dir() + "/settings.toml"):
        variables = load_file("/settings.toml")
    if os.path.isfile(get_app_dir() + "/.env"):
        variables["default"] = {**variables["default"], **load_env_file()}

    return variables


global_variables_from_file = load_file("/app/config/variables.toml")
database_variables_from_file = load_file("/app/config/database.toml")
project_variables_from_file = project_variables()


def get(name):
    """
    :param name:
    :return:
    """

    if global_variables_from_file.get("default").get(name) is not None:
        return global_variables_from_file.get("default").get(name)

    if database_variables_from_file.get("default").get(name) is not None:
        return global_variables_from_file.get("default").get(name)

    if project_variables_from_file.get("default").get(name) is not None:
        return project_variables_from_file.get("default").get(name)

    return None


def get_database_uri():
    """
    :return:
    """
    if get("DB_CONNECTION") == "sqlite":
        return get("DB_CONNECTION") + ":///" + get_app_dir() + "/" + get("DB_NAME")

    return (
        f"{get('DB_CONNECTION')}://{get('DB_USERNAME')}:{get('DB_PASSWORD')}"
        f"@{get('DB_HOST')}:{get('DB_PORT')}/{get('DB_NAME')}"
    )
