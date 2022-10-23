

from datetime import datetime

# create the txt file
filename = 'Newsfeed_Deineha.txt'

# create the main class
class NewsFeed:

    def __init__(self, news, city):
        self.news = news
        self.city = city

# create the subclass for getting today date
class PubDate(NewsFeed):

    def __init__(self, today_date):
        self.today_date = ()


today_date = datetime.today()

# create the subclass for PrivateAd , where the today date is used
class PrivateAd(PubDate):
    def __init__(self, goal, actual_date):
        self.goal = goal
        self.actual_date = (datetime.strptime(actual_date, '%d/%m/%Y') )
        PubDate.__init__(self, today_date)


# create the subclass for unique publish
class FreePost(NewsFeed):
    def __init__(self, post_title, post_text):
        self.post_title = post_title
        self.post_text = post_text


# the input function for user, where the data type he wants to add shoul be selected

inp = input('What kind of information do you want to post now: \nenter \033[1m1\033[0m for \x1B[3m"News"\x1B[0m, \nenter \033[1m2\033[0m for \x1B[3m"Private advertising"\x1B[0m, '
            '\nenter \033[1m3\033[0m for \x1B[3m"My own publication (on a free topic)"\x1B[0m? - ');
if inp =='1':
     # call the fucnction for News
     first_news = NewsFeed(input('Enter your news:'), input('Enter the city:'))
     # adding the text to Newsfeed.txt file
     with open(filename, 'a') as file_object:
         file_object.write(f"NEWS----------------------------\n{first_news.news} \n{first_news.city},  {today_date.strftime('%d/%m/%Y %H:%M')}\n--------------------------------\n\n\n")
elif inp =='2':
    # call the fucnction for PrivateAd
     my_adv = PrivateAd(input('Enter your advertising goal:'),  input('Enter the expiration date (\x1B[3mdd/mm/yyyy\x1B[0m format):'))
    # adding the text to Newsfeed.txt file
     with open(filename, 'a') as file_object:
         file_object.write(f"Private advertising-------------\n{my_adv.goal} \nActual until:  {my_adv.actual_date.strftime('%d/%m/%Y')}, {(my_adv.actual_date - today_date).days} days left\n--------------------------------\n\n\n")
elif inp =='3':
    # call the fucnction for FreePost
     free_post = FreePost(input ('Enter your own publication title:'), input ('Enter your own publication text:'))
    # adding the text to Newsfeed.txt file
     with open(filename, 'a') as file_object:
         file_object.write(f"{free_post.post_title}----------------------------\n{free_post.post_text}\n--------------------------------\n\n\n")
else: print("Unknown result")


