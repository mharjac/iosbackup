from netmiko import Netmiko


class IOSDevice():
    def __init__(self, host, username, password, enable, secret):
        self.device = {
            'device_type': 'cisco_ios',
            'host':   host,
            'username': username,
            'password': password,
            'secret': secret
        }
        self.enable = enable
        self.dev_connection = Netmiko(**self.device)

    def get_config(self):
        if self.enable:
            self.dev_connection.enable()

        return self.dev_connection.send_command('show runn')


