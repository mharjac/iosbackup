"""Tool for creating Cisco IOS configuration backup

It can be used as an interactive tool from CLI or for unattended backups in 
containers, in which case it uses following environment variables:

IOS_HOST: for storing Ip address or hostname (e.g., 192.168.1.1)
IOS_USER: username for making backups
IOS_PASS: password for provided username
IOS_ENABLE: set to True if privileged mode is required
IOS_SECRET: privileged mode password

When used in CLI, it will prompt for password if -p (--password) flag
not provided. Config will be printed to the stdout if -f (--file) omitted. 
"""


import os
import sys
import getpass
import argparse
import datetime
import iosbackup


def main():
    parser = argparse.ArgumentParser(prog="iosbackup")
    parser.add_argument("-H", "--host", help="IP address of the switch")
    parser.add_argument("-u", "--user", help="username for executing backup")
    parser.add_argument("-p", "--password", help="password for provided username; prompts if not provided")
    parser.add_argument("-e", "--enable", action="store_true", help="use privileged mode")
    parser.add_argument("-s", "--secret", help="privileged mode password")
    parser.add_argument("-f", "--filename", default="/dev/stdout", metavar="FILE", help="FILE to write backup; stdout if not provided")
    parser.add_argument("-v", "--version", action="store_true", help="show version")
    options = parser.parse_args()

    time_stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    if options.version:
        print(iosbackup.__version__)
        sys.exit(0)
    elif options.host and options.user:
        username = options.user
        if options.password:
            password = options.password
        else:
            password = getpass.getpass("Input password: ")
        host = options.host
        filename = options.filename
        
        if options.enable:
            enable = options.enable
            if options.secret:
                secret = options.secret
            else:
                secret = getpass.getpass("Input secret: ")
    else:
        try:
            username = os.environ['IOS_USER']
            password = os.environ['IOS_PASS']
            host = os.environ['IOS_HOST']
            enable = (False, True)[os.environ['IOS_ENABLE'].upper() == "TRUE"]
            secret = os.environ['IOS_SECRET']
            filename = f"config-{time_stamp}.cfg"
        except KeyError as err:
            sys.stderr.write(f"ERROR: Missing {err} environment variable.\n")
            sys.exit(1)

    sw = iosbackup.IOSDevice(host, username, password, enable, secret)
    config = sw.get_config()

    with open(filename, "w") as f:
        f.write(config)


if __name__ == "__main__":
    main()