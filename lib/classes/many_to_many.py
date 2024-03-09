class Article:
    def __init__(self, author, magazine, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception('Invalid title. Title must be between 5 and 50 characters.')    
        self._magazine = magazine
        self._author = author

    @property
    def title(self):
        return self._title
        
    @property
    def author(self):
        return self._author  
      
    @property
    def magazine(self):
        return self._magazine    
        
class Author:
    _all_authors = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception('Invalid name. Name must be at least 1 character long.')        
        self._articles = []
        Author._all_authors.append(self)

    @property
    def name(self):
        return self._name 

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    @property
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set([article.magazine.category for article in self._articles]))

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception('Invalid name. Name must be a string of between 2 and 16 characters.')    
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise Exception('Invalid category. Category must be a string at least 1 character long.')    
        self._articles = []
        Magazine._all_magazines.append(self)
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @property
    def articles(self):
        return self._articles
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
        pass

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        return [author for author in authors if authors.count(authors) > 2]
    
    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        magazine_count = {}
        for magazine in cls._all_magazines:
            magazine_count[magazine] = len(magazine.articles)
        max_count = max(magazine_count.values())
        for magazine, count in magazine_count.items():
            if count == max_count:
                return magazine    