# ksize
## A Tool for Kafka Topic Size

The Kafka Topic Size Tool is a command-line utility that provides information about the size of topics in a Kafka cluster. It utilizes the Kafka command-line tools `kafka-topics` and `kafka-log-dirs` to retrieve and analyze the size information.

## Installation

You can install the Kafka Topic Size Tool from [PyPI](https://pypi.org/project/kafka-topic-size/) using `pip`:

`pip install ksize`

## Usage

### Command Syntax

`ksize -b <bootstrap-server> [-c <config>] (-t <topic> | -a) [-o <output>]`

### Options

- `-b`, `--bootstrap-server`: The Kafka cluster to connect to (e.g., `localhost:9092`).
- `-c`, `--config`: The path to the Kafka config file.
- `-t`, `--topic`: The topic or list of topics to get the size for.
- `-a`, `--all`: Get the size for all topics.
- `-o`, `--output`: Send output to a file.

### Examples

1. Get the size of a specific topic:

`ksize -b localhost:9092 -c /path/to/config/file.conf -t my_topic -o output.txt`

2. Get the size of all topics:

`ksize -b localhost:9092 -c /path/to/config/file.conf -a -o output.txt`

## Important Notes

- Either `--topic` or `--all` is required.
- Make sure you have the Kafka command-line tools (`kafka-topics` and `kafka-log-dirs`) installed and available in your system's PATH.
- The tool calculates the size of topics in megabytes (MB).
- If an error occurs during the process, it will be displayed in the console output.

## License

This tool is provided under the MIT License. Feel free to use, modify, and distribute it according to the terms of the license.
