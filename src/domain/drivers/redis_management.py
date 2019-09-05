import redis
from redis.sentinel import Sentinel, SentinelConnectionPool

class RedisManagement():

    def __init__(self, config):
        self.config = config
        self._init_redis_db_pool()

    def _init_redis_db_pool(self):

        self._db_pool = redis.ConnectionPool(host=self.config['redis-host'], port=self.config['redis-port'],
                                             db='0', password=self.config['redis-password'])
    def ping(self):
        redis_conecc = redis.Redis(connection_pool=self._db_pool)
        return redis_conecc.ping()
