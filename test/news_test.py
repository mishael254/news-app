import unnitest
from app.modules import Article


class ArticleTest(unittest.TestCase):
    '''
    Test case to test the behaviour of the article class
    '''
    def setup(self):
        '''
        Setup method that will run before every test
        '''
        self.new_article = Article('bbc','silah koskei','Trump takes on swearing in of kenyan opposition leader'
                                   'www.bbc.com/kenya','www.bbc.com/kenya/image.jpg','28-02-2019')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_article, Article))


    if__name__== '__main__';
    unittest.main()                      