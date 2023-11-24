import subprocess
import os
import shutil
import urllib.request
import tarfile
import sys

def kafka_install():
    # Check if Kafka is already installed
    if os.path.exists('/usr/local/Cellar/kafka'):
        print("Kafka is already installed.")
        return

    # Check the operating system
    if os.name == 'posix':
        # Running on Linux or MacOS
        if sys.platform == 'linux':
            # Linux: Update and install required packages
            subprocess.run(['sudo', 'apt-get', 'update'])
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'openjdk-8-jdk'])
            # Download Kafka
            url = 'https://downloads.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz'
            filename = 'kafka_2.13-3.0.0.tgz'
            urllib.request.urlretrieve(url, filename)

            # Extract Kafka
            with tarfile.open(filename, 'r:gz') as tar:
                tar.extractall()

            # Move Kafka to /usr/local/kafka
            shutil.move('kafka_2.13-3.0.0', '/usr/local/kafka')

            # Clean up downloaded files
            os.remove(filename)

            # Add Kafka's bin directory to PATH
            with open(os.path.expanduser('~/.bashrc'), 'a') as file:
                file.write('export PATH=$PATH:/usr/local/kafka/bin\n')

            # Refresh environment
            subprocess.run(['source', os.path.expanduser('~/.bashrc')])
        elif sys.platform == 'darwin':
            # MacOS: Install using Homebrew
            subprocess.run(['brew', 'install', 'kafka'])
        else:
            print("Unsupported operating system.")
            return
    else:
        print("Unsupported operating system.")
        return
    # Refresh environment
    os.system('source ~/.bashrc')


# Call the function to execute the installation
kafka_install()
