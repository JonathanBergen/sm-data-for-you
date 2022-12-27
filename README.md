# SocialMedia-data-for-you (or just Some-data-for-you)
While working on a project regarding the relationship between Twitter and the stock market, I discovered two things: a lack of on-demand social media data, and a beatiful tool called [SNScrape](https://github.com/JustAnotherArchivist/snscrape). This Flask app uses SNScrape to serve up on-demand data from social media channels (just Twitter for now, but I'm planning to expand the functionality to utilize all of SNScrape's capability)

### Tweet Parameters: (specify as many as you want)
- Standard plaintext
- Date range of tweet
- Language
- From: Username
- Number of likes
- Number of retweets

### Returned data points
- url
- date
- rawContent
- renderedContent
- id
- user
- replyCount
- retweetCount
- likeCount
- quoteCount
- conversationId
- lang
- source
- sourceUrl
- sourceLabe
- links
- media
- retweetedTweet
- quotedTweet
- inReplyToTweetId
- inReplyToUser
- mentionedUsers
- coordinates
- place
- hashtags
- cashtags
- card
- username
- outlinks
- content
