import configparser
import os


class ConfigurationManager(object):

    def __init__(self, path):
        if not os.path.exists(path):
            raise Exception('Configuration Path does not exist')
        else:
            self._path = path


    def get_redis_configuration(self):
        config_dic = {}
        enviroment_file = self._path
        config = configparser.ConfigParser()
        config.read(enviroment_file)
        if config.has_section("redis"):
            if config.has_option('redis', 'host'):
                config_dic["redis-host"] = config.get('redis', 'host')
            if config.has_option('redis', 'port'):
                config_dic["redis-port"] = config.get('redis', 'port')
            if config.has_option('redis', 'password'):
                config_dic["redis-password"] = config.get('redis', 'password')
        return config_dic