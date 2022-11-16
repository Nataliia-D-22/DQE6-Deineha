

from datetime import datetime

# create the txt file
filename = 'Newsfeed_Deineha3.txt'

# create the main class
class NewsFeed:
    # the input function for user, where the data type he wants to add should be selected
    def __init__(self, inputtxt):
        self.inputtxt = inputtxt

inputtxt = NewsFeed( input(
        'What kind of information do you want to post now: \nenter \033[1m1\033[0m for \x1B[3m"News"\x1B[0m, \nenter \033[1m2\033[0m for \x1B[3m"Private advertising"\x1B[0m, '
        '\nenter \033[1m3\033[0m for \x1B[3m"My own publication (on a free topic)"\x1B[0m? - '))

class News(NewsFeed):
    def __init__(self, news, city ):
        NewsFeed.__init__(self, inputtxt=inputtxt)
        self.news = news
        self.city = city

    if inputtxt == '1':
        # call the function for News
        first_news = News(input('Enter your news:'), input('Enter the city:'))
        # adding the text to Newsfeed.txt file
        with open(filename, 'a') as file_object:
            file_object.write(
                f"NEWS----------------------------\n{News.news} \n{News.city},  {today_date.strftime('%d/%m/%Y %H:%M')}\n--------------------------------\n\n\n")
nws= News(input('Enter your news:'), input('Enter the city:'))
nws.news()


# create the subclass for getting today date
class PubDate(NewsFeed):
    def __init__(self, today_date):
         self.today_date = ()

today_date = datetime.today()

# create the subclass for PrivateAd , where the today date is used

class PrivateAd(PubDate):
    def __init__(self, goal, actual_date):
        NewsFeed.__init__(self, inputtxt=inputtxt)
        self.goal = goal
        self.actual_date = (datetime.strptime(actual_date, '%d/%m/%Y') )
        PubDate.__init__(self, today_date)

    def first_Ad (self):
        if self.inputtxt == '2':
            # call the fucnction for PrivateAd
            my_adv = PrivateAd(input('Enter your advertising goal:'),
                               input('Enter the expiration date (\x1B[3mdd/mm/yyyy\x1B[0m format):'))
            # adding the text to Newsfeed.txt file
            with open(filename, 'a') as file_object:
                file_object.write(
                f"Private advertising-------------\n{my_adv.goal} \nActual until:  {my_adv.actual_date.strftime('%d/%m/%Y')}, {(my_adv.actual_date - today_date).days} days left\n--------------------------------\n\n\n")



# create the subclass for unique publish
class FreePost(NewsFeed):
    def __init__(self, post_title, post_text):
        NewsFeed.__init__(self, inputtxt=inputtxt)
        self.post_title = post_title
        self.post_text = post_text

    def first_post(self):
        if self.inputtxt == '3':
             # call the fucnction for FreePost
            free_post = FreePost(input('Enter your own publication title:'), input('Enter your own publication text:'))
            # adding the text to Newsfeed.txt file
            with open(filename, 'a') as file_object:
                file_object.write(
                f"{free_post.post_title}----------------------------\n{free_post.post_text}\n--------------------------------\n\n\n")
        else: print("Unknown result")