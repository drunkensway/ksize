from .kafka_topic_size import get_kafka_all_topics, describe_kafka_topics

import click
import os

def require_topic_definition(ctx, param, value):
    if not value and not ctx.params.get('topic') and not ctx.params.get('all'):
        raise click.UsageError('Either --topic or --all is required.')
    return value

@click.command()
@click.option('-b', '--bootstrap-server', type=str, required=True, help='The Kafka Cluster to Connect to.')
@click.option('-c', '--config', type=str, help='The Kafka config file path location.')
@click.option('-t', '--topic', type=str, required=False, callback=require_topic_definition, help="Topic or list of topics to get the size for.")
@click.option('-a', '--all', required=False, is_flag=True, callback=require_topic_definition, help="Gets the size for all topics.")
@click.option('-o', '--output', type=(str), help='Send output to a file')

def ksize(bootstrap_server, config, topic, all, output):
    if config and all:
        all_topics = get_kafka_all_topics(bootstrap_server=bootstrap_server, config_file_path=config)
        final_result = describe_kafka_topics(bootstrap_server=bootstrap_server, all_topics=all_topics)
    elif config and topic:
        all_topics = get_kafka_all_topics(bootstrap_server=bootstrap_server, config_file_path=config)
        final_result = describe_kafka_topics(bootstrap_server=bootstrap_server, user_topic=topic)
    elif all:
        all_topics = get_kafka_all_topics(bootstrap_server=bootstrap_server)
        final_result = describe_kafka_topics(bootstrap_server=bootstrap_server, all_topics=all_topics)
    elif topic:
        final_result = describe_kafka_topics(bootstrap_server=bootstrap_server, user_topic=topic)

    if output:
        with open(output, 'w') as file:
            for topic in final_result:
                file.write(topic)
