import snscrape.modules.twitter as sntwitter
import pandas as pd

# The scraper class, which uses SNscrape to scrape tweets from Twitter for now, but will be expanded to include other social media platforms in the future.
class Scraper():

    def __init__(self, text, start_date, end_date, num_tweets, return_values):
        self.text = text
        self.start_date = start_date
        self.end_date = end_date
        self.num_tweets = num_tweets

        # The values to be returned
        self.return_values = return_values

    def scrape(self):
        # The dataframe of tweets to be returned
        tweets = pd.DataFrame(columns = self.return_values)

        # The actual scraping
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{} since:{} until:{} lang:en'.format(self.query, self.start_date, self.end_date)).get_items()):
            if i>self.num_tweets:
                break
            tweets.append([tweet.date, tweet.content])
        return tweets