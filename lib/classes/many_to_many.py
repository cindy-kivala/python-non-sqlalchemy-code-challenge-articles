class Article:
    def __init__(self, title, author, magazine):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        # self.name = name
        # if not isinstance(name, str) or len(name) == 0:
        #     raise ValueError("Name must be a non-empty string")
        # self._name =name
        # self._articles = []
        self._validate_name(name)
        self._name = name
        self._articles = []
    
    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")

    #prop to return author name
    @property
    def name(self):#getter
        return self._name #fulfills the prop requirements
    # @name.setter
    # def name(self, value):
    #     self._name = value #confirm if this is needed

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
    #class variable to keep track of all instances of magazine
    _magazine = []

    def __init__(self, name, category):
        #conditionals
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine nme must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        self._articles = []
        Magazine._magazine.append(self)

    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    def articles(self):
        return self._articles

    def contributors(self):
        return self._contributors #CONFIRM HOW TO RESOLEV

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_count = {} #unique list for aunthoors in type author
        for article in self._articles:
            #increment author count logic
            author_count[article.author] = author_count.get(article.author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]