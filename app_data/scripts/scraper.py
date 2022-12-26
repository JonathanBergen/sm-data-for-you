import snscrape.modules.twitter as sntwitter

# The scraper class, which uses SNscrape to scrape tweets from Twitter for now, but will be expanded to include other social media platforms in the future.
class Scraper():

    def __init__(self, query, start_date, end_date, num_tweets):
        self.query = query
        self.start_date = start_date
        self.end_date = end_date
        self.num_tweets = num_tweets

    def scrape(self):
        # The list of tweets to be returned
        tweets = []

        # The actual scraping
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{} since:{} until:{} lang:en'.format(self.query, self.start_date, self.end_date)).get_items()):
            if i>self.num_tweets:
                break
            tweets.append([tweet.date, tweet.content])
        return tweets