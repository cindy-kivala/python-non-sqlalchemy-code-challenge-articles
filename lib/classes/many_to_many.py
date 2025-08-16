class Article:
    def __init__(self, title, author, magazine):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        self.name = name
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name =name
        self._articles = []

    #prop to return author name
    @property
    def name(self):#getter
        return self._name #fulfills the prop requirements
    @name.setter
    def name(self, value):
        self._name = value #confirm if this is needed

    def articles(self):
        return self._articles #scope???

    def magazines(self):
        return list(set(article.magazine for article in self._articles)) #comprehension

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass