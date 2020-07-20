import unittest
from models import news-source
Newssource = newssource.Newssource

class NewsTest(unittest.TestCase):
    '''
    a test class to test the behaviour of News class
    '''
    def setUp(self):
        '''
        a setup method that will run before every test
        '''
        self.new_newssource = Newssource('Mishael Stark', 'Gangster ages', 'a group of gangsters attacked nividia', 'https://finance.yahoo.com/news/britain-signs-deals-pfizer-biontech-060801083.html',
        "https://s.yimg.com/uu/api/res/1.2/CkL43B3HFBeB8CLIKniKZw--~B/aD01MTQ7dz04MDA7c209MTthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en-US/reuters.com/2b8920c26de3de46d30cb1e48fa3b1a0",
        "2020-07-20T06:09:26Z",'those gangsters lived by the age of rules'
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newssource,Newssource))

if __name__ == "__main__":
    unittest.main()
