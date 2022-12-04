from newspaper import Article

url = 'https://www.bbc.com/news/world-europe-63323263'

test_article = Article(url, language='en')
test_article.download()
test_article.parse()
# test_article.nlp()

print(test_article.title)
print(test_article.text)
print(test_article.keywords)
