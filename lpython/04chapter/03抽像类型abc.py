

class CacheBase():
    def get(self,key):
        raise NotImplementedError
    def set(self,key,value):
        raise NotImplementedError


class RedisCache(CacheBase):
    def set(self,key,value):
        pass


redis_cache = RedisCache()
redis_cache.set("key","value")
