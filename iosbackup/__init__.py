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


from iosbackup.iosdevice import IOSDevice


__version__ = '1.0.0'
__all__ = ('IOSDevice')