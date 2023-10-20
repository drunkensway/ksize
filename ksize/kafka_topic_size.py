import os
import sys
import subprocess

def get_kafka_all_topics(bootstrap_server, config_file_path=None):
    try:
        command = ["kafka-topics", "--bootstrap-server", bootstrap_server]
        if config_file_path:
            command.extend(["--command-config", config_file_path])
        
        all_topics = subprocess.check_output(
            command + ["--list"],
            stderr=subprocess.PIPE,
            text=True,
        ).split("\n")
    except subprocess.CalledProcessError as e:
        print("Error running kafka-topics command:", e)
        print("Command stderr:", e.stderr)
        exit(1)
    return all_topics


def describe_kafka_topics(bootstrap_server, all_topics=None, user_topic=None, config_file_path=None):
    if user_topic:
        topics_to_describe = [user_topic]
    elif all_topics:
        topics_to_describe = all_topics

    final_result = []
    for topic in topics_to_describe:
        command = [ "kafka-log-dirs", "--bootstrap-server", bootstrap_server]
        if config_file_path:
            command.extend(["--command-config", config_file_path,])
        
        command.extend(["--topic-list", topic, "--describe"])
        try:
            output = subprocess.check_output(command, shell=False, stderr=subprocess.PIPE, text=True)
        except subprocess.CalledProcessError as e:
            print("Error running the command:", e)
            print("Command stderr:", e.stderr)
            exit(1)

        filtered_lines = [line for line in output.split('\n') if line.strip().startswith('{')]

        combined_json = "[" + ",".join(filtered_lines) + "]"

        try:
            result = subprocess.check_output(["jq", '[ ..|.size? | numbers / (1024 * 1024)] | add'], input=combined_json, text=True)
        except subprocess.CalledProcessError as e:
            print("Error running jq:", e)
            exit(1)
        
        print(topic + ": " + str(round(float(result.strip()), 2)) + " MB")
        final_result.append(topic + ": " + str(round(float(result.strip()), 2)) + " MB\n")
    return final_result
