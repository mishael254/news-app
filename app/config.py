class Config:
    '''
    parent configuration class
    '''
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
