class Article:
    all = [] # a cls variable to hold all the instances of Article

    def __init__(self,author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
      
        Article.all.append(self)  # Append the instance to the class-level list

        magazine._articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an Author instance")
        self._author = new_author #allow author to be changed
    
    @property
    def magazine(self):
        return self._magazine
    #setter prop
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        self._magazine = new_magazine #allows magazine to be changed
        
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
   
    def articles(self):
        return [article for article in Article.all if article.author == self] #scope???

    def magazines(self):
        return list(set(article.magazine for article in self.articles())) #comprehension

    def add_article(self, magazine, title):
         return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set(article.magazine.category for article in articles))

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
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
           raise ValueError("Magazine name must be a string between 2 and 16 characters")
        self._name = new_name
    
    @property
    def category(self):
        return self._category
    
    #setter

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or not new_category.strip():
           raise ValueError("Category must be a non-empty string")
        self._category = new_category
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # def contributors(self):
    #     if not hasattr(self, '_contributors'):
    #         self._contributors = [] #lets initialize here
    #     return self._contributors
    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    # def contributing_authors(self):
    #     author_count = {} #unique list for aunthoors in type author
    #     for article in self._articles:
    #         #increment author count logic
    #         author_count[article.author] = author_count.get(article.author, 0) + 1
    #     return [author for author, count in author_count.items() if count > 2]

    def contributing_authors(self):
        from collections import Counter
    # get all articles for this magazine
        articles = [article for article in Article.all if article.magazine == self]
    # count how many articles each author has written for this magazine
        author_counts = Counter(article.author for article in articles)
    # filter authors who have written more than 2 articles
        result = [author for author, count in author_counts.items() if count > 2]
    # if none, return None
        return result if result else None

    
    #DO WE NEED A CLASS METHOD?

    # Create Author and Magazine instances
author = Author("Carry Bradshaw")
magazine = Magazine("Vogue", "Fashion")

# Add articles through the author
author.add_article(magazine, "How to wear a tutu with style")
author.add_article(magazine, "Dating life in NYC")

# Verify the articles
print(len(author.articles()))  # Outputs: 2