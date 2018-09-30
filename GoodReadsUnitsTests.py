import unittest
from GoodReadsScrapper import GoodReads

class TestGoodReadsScrapper(unittest.TestCase):    
    
    #Invalid empty input
    def testAuthenticateUser_emptyInput_returnsFalse(self):
        expected_output = False
        goodreads = GoodReads()
        result=goodreads.authenticate_user("","")
        assert result==expected_output

    #Invalid non empty input
    def testAuthenticateUser_nonEmptyInvalidInput_returnsFalse(self):
        expected_output = False
        goodreads = GoodReads()
        result=goodreads.authenticate_user("sush@gmail.com","temp23")
        assert result==expected_output
     
    #Valid Input value
    def testAuthenticateUser_validInput_returnsTrue(self):
        expected_output = True
        goodreads = GoodReads() 
        result=goodreads.authenticate_user("sushantg93@gmail.com","12345678") 
        # could have again passed an environment variable but will just add some more steps for the reviewer of my code
        assert result==expected_output
         
    #Verify that only 10 quotes are generated
    def testQuotes_count_isTen(self):
        expected_output = 10
        goodreads = GoodReads()
        result=len(goodreads.get_top_ten_quotes())
        assert result==expected_output
        
if __name__ == '__main__':
   unittest.main()