from datetime import datetime, timedelta


class NewsArticle:
    def __init__(self, title, description, url, publishedAt, author, source):
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.author = author
        self.source = source

    # def get_news_info(self):
    #      data=fetch_news()
    #      if(data):
    #         if data.get("status")=="ok" and data.get("articles"):
    #             print("News Articles:")
    #             for article in data["articles"]:
    #                 self.title=article["title"]
    #                 self.description=article["description"]
    #                 self.url=(article["url"])
    #                 self.publishedAt=(article["publishedAt"])
    #                 self.author=(article["author"])
    #                 self.source=(article["source"]["name"])
    # print("-" * 30)
    # print("title:\n ",self.title,"description:\n",self.description,"url:\n",self.url,"pulishdedAt:\n",self.publishedAt,"author:\n",self.author,"source:\n",self.source)
    #     else:
    #         print("No articles found")
    #  else:
    #     print("No data found")

    def summary(self):
        # return short descriptiom of the article
        return self.description

    def is_recent(self):
        # return true if the article is recent (within last 24 hours)
        try:
            pub_date = datetime.strptime(self.publishedAt, "%Y-%m-%dT%H:%M:%SZ")
            return pub_date > datetime.utcnow() - timedelta(days=1)
        except (ValueError, TypeError):
            return False

    def __str__(self):
        return f"{self.title}\n{self.author}\n{self.source}\n{self.url}"


class ProcessedNews(NewsArticle):
    def __init__(self, title, description, url, publishedAt, author, source, category):
        super().__init__(title, description, url, publishedAt, author, source)
        self.category = category
        self.importance_score = self.calculate_importance()

    def calculate_importance(self):
        # return importance score of the article
        score = 0
        if self.author:
            score += 10
        if self.description and len(self.description) > 200:
            score += 10
        if self.title and (
            "important" in self.title.lower() or "urgent" in self.title.lower()
        ):
            score += 10
        return score

    def __str__(self):
        return f"{self.title}\n{self.author}\n{self.source}\n{self.url}"
