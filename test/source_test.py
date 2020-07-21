import unittest
from app.modules import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source clss
    '''
    def setup(self):
        '''
        set up method that will run before every test
        '''
        self.new_source = Source('abcnews','abc','News that keeps you up to date','https:abc.org')

    def test_instance(self):
            self.assertTrue(isinstance(self.new_source,Source))


    if__name__== '__main__';
    unittest.main()           