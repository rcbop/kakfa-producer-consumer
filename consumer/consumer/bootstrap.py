from kink import di
from argparse import ArgumentParser, FileType
from configparser import ConfigParser


def bootstrap():
    """Bootstrap the application."""
    print("Bootstrapping application...")

    parser = ArgumentParser()
    parser.add_argument("config_file", type=FileType("r"))
    args = parser.parse_args()

    config_parser = ConfigParser()
    config_parser.read_string(args.config_file.read())

    topic_name = config_parser["topic"]["name"]
    di["topic"] = topic_name

    consumer_config = dict(config_parser["default"])
    consumer_config.update(config_parser["consumer"])
    di["consumer_config"] = consumer_config
    print(f"Consumer config: {consumer_config}")
    print("Bootstrapping complete.")
