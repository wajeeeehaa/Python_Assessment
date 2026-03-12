from datetime import datetime, timedelta
import time
from models import ProcessedNews


# no of articles from each source
def get_source_summary(articles):
    source_articles = {}
    for article in articles:
        source_name = article.source
        if source_name in source_articles:
            #  if it already exists in dictionary then add the value in count
            #    source_articles[sourcename]=article.source[name]
            source_articles[source_name] += 1
        else:
            source_articles[source_name] = 1
    return source_articles


def recent_articles_generator(articles):
    # this is the date format in api response 2022-05-05T06:09:12Z

    # Calculate exactly 24 hours ago dynamically when the generator is called
    # We use utcnow() since the API times end in 'Z' (UTC timezone)
    twenty_four_hours_ago = datetime.utcnow() - timedelta(hours=24)

    for article in articles:
        if type(article.publishedAt) is str:
            article.publishedAt = datetime.strptime(
                article.publishedAt, "%Y-%m-%dT%H:%M:%SZ"
            )
        if article.publishedAt > twenty_four_hours_ago:
            yield article


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start

        print(f"{func.__name__} executed in {execution_time:.4f} seconds")

        return result

    return wrapper


@measure_time
def process_articles(data):
    if not data or "articles" not in data:
        return []

    articles = []
    # Using a list comprehension to store articles in a list of objects
    articles = [
        ProcessedNews(
            title=item.get("title"),
            description=item.get("description", ""),
            url=item.get("url"),
            publishedAt=item.get("publishedAt"),
            author=item.get("author"),
            source=item.get("source", {}).get("name"),
            category="technology",
        )
        for item in data["articles"]
    ]

    filtered_articles = [a for a in articles if a.author]

    filtered_articles.sort(key=lambda x: x.publishedAt, reverse=True)

    return filtered_articles
