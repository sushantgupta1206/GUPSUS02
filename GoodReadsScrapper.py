'''
Author : Sushant Gupta
Exercise 02. 

A script to authenticate into the goodreads website and then get top 10 quotes from Mark Twain
'''
# importing libraries
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import requests

class GoodReads:
# function to check for user authentication
    def authenticate_user(self, user_email, password):

        # Set the users input values and read the home page
        webpage = RoboBrowser()
        goodreads_page = 'http://www.goodreads.com' # best practice: page can be changed whenever needed
        webpage.open(goodreads_page)

        # load and submit the login form using the get_form function
        login_form = webpage.get_form(id='sign_in')
        login_form['user[email]'].value = user_email
        login_form['user[password]'].value = password
        
        webpage.submit_form(login_form)
        
        # read the web page again and check for certain tags only visible after login to verify the user
        # another method could be hitting the database for verifying using dynamic querry building
        home_page = str(webpage.parsed())
        
        if "Currently Reading" in home_page:
            print("User Authenticated")
            return True
        else:
            print("Invalid user creditentials")
            return False

    # function to get top 10 quotes of Mark Twain
    def get_top_ten_quotes(self):
        # list to store all quotes
        top_ten_quotes=[]

        #PS: Goodreades.com displays quotes without any authentication also. Using the URL directly of the quotes page 
        response=requests.get("https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=Mark+Twain&commit=Search")
        
        #read and parse the html_doc page for all quotes and authors 
        html_doc=BeautifulSoup(response.content,"html.parser")
        all_quotes=[]
        all_authors=[]
        
        # traverse the page and take out the texts we need
        for tag in html_doc.findAll('div', attrs = { "class" : "quoteText" }): # read the source files for specific tags
            all_quotes.append(tag.contents[0].strip())
            all_authors.append(tag.find('span', attrs = { "class" : "authorOrTitle" }).text.strip())
        #Filter quotes for a specific author
        count=10
        author = "Mark Twain" # can just change the author for someone else as well
        for i in range(len(all_quotes)):
            if(count>0):
                if(all_authors[i]=="Mark Twain"):
                    count-=1
                    top_ten_quotes.append(all_quotes[i])
            else:
                    break
        return top_ten_quotes


def main():    
    
    obj = GoodReads()
    user_email = raw_input("Enter the user name/ email : ") 
    password=raw_input("Enter the password : ") 
    
    if user_email=="" or password=="":
        print("User name or password can not be empty")
    else:
            # call to authenticate user and get quotes
            if (obj.authenticate_user(user_email,password)):
                
                # call to get top ten quotes
                top_ten_quotes = obj.get_top_ten_quotes()
                
                #writing quotes to an external file
                with open("Top10_Quotes.txt","wb") as file :
                    for each_quote in top_ten_quotes:
                        file.write(each_quote.encode(encoding='utf-8') + "\n" )
                file.close
                print("Quotes stored in Top10_Quotes file")
            else:
                #Print Faulty Message for wrong credentials
                print("Invalid User! Please enter valid credentials")

if __name__ == '__main__':
    main()