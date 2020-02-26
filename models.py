from peewee import *
import hashlib

DATABASE = SqliteDatabase('api_iot.db') 


class Broker(Model):
    id = CharField(unique = True) 
    path = CharField()

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)
    
    @classmethod
    def registerBroker(cls, path):
        try:
            path_hash = hashlib.sha256(path.encode('utf-8')).hexdigest()
            with DATABASE.transaction():
                cls.create(
                    id = path_hash,
                    path = path
                )
        except:
            raise ValueError('Broker already exists')
        return path_hash

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Broker], safe = True)
    DATABASE.close()
