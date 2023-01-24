#Importing pyshorteners library
import pyshorteners 

#Function to shorten the url
def shorten(url):
    short_url = pyshorteners.Shortener()
    print("\nThe shortened url is : \n"+short_url.tinyurl.short(url))

#Taking the url as input
url = input("Enter your url:")
#Calling the function
shorten(url)
