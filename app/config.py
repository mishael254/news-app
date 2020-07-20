class Config:
    '''
    parent configuration class
    '''
    NEWS-API-URL = 'http://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    pass

class ProdConfig(Config):
    '''
    a child production class and passed in the parent class
    '''
    pass
class DevConfig(Config):
    '''
    a child development class and passed in the parent class
    '''
    pass

DEBUG = True
