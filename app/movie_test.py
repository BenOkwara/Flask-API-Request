import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every TestCase
        '''
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

    def test_init(self):
        '''
        A function to test that the method has been instastiated correctly
        '''
        self.assertEqual(self.new_movie.id,1234)


if __name__ == '__main__':
    unittest.main()
