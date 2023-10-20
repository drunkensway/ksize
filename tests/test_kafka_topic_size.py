import unittest
from unittest.mock import MagicMock, patch
from ksize.kafka_topic_size import get_kafka_all_topics, describe_kafka_topics

class TestKafkaTopicSize(unittest.TestCase):

    @patch('subprocess.check_output')
    def test_get_kafka_all_topics(self, mock_check_output):
        # Mock subprocess.check_output
        mock_check_output.return_value = "topic1"

        bootstrap_server = "localhost:9092"
        result = get_kafka_all_topics(bootstrap_server)

        self.assertEqual(result, ["topic1"])

    @patch('subprocess.check_output')
    def test_describe_kafka_topics(self, mock_check_output):
        # Mock subprocess.check_output
        mock_check_output.return_value = '1.024'

        bootstrap_server = "localhost:9092"
        all_topics = ["topic1"]
        result = describe_kafka_topics(bootstrap_server, all_topics)

        expected_result = ["topic1: 1.02 MB\n"]

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
