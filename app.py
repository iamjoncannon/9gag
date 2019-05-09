import feedparser
import ssl
from flask import Flask, url_for, render_template, request, session
from flask_caching import Cache
app = Flask(__name__)
ssl._create_default_https_context=ssl._create_unverified_context

# caching that stores each feed 
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

channels = ('Awesome', 
			'Awesome No Gif', 
			'Comic', 
			'Comic No Gif',
			'Dark Humor',
			'Dark Humor No Gif',
			'Fresh',
			'Fresh No Gif',
			'Funny',
			'Funny No Gif',
			'Gif',
			'Hot',
			'Hot No Gif',
			'NSFW',
			'NSFW No Gif',
			'Trending',
			'Trending No Gif',
			)

# feedparser to retrieve RSS data
@cache.cached(timeout=120) # feeds are refreshed every 2 minutes
def feeder(channel):
	print('not cached') # verify caching with serverlogs
	channel = channel.replace('Trending', '')
	url = 'https://9gag-rss.com/api/rss/get?code=9GAG' + channel + '&format=2'
	d = feedparser.parse(url)
	return d

# rest service 
@app.route("/", methods=['GET'])
def index():
	return render_template('index.html', channels=channels)

@app.route('/feed/<channel>')
def showFeed(channel):

	data = []
	for key, value in feeder(channel).items():
		data.append([key, value]) 
	return render_template('feed.html', feed=data)

if __name__ == '__main__':
    app.run()