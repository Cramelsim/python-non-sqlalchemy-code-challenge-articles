class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be changed after initialization")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine_list = []
        for article in self.articles():
            if article.magazine not in magazine_list:
                magazine_list.append(article.magazine)
        return magazine_list

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = []
        for magazine in self.magazines():
            if magazine.category not in categories:
                categories.append(magazine.category)
        return categories if categories else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if not category.strip():
            raise ValueError("Category must not be empty")
            
        self._name = name
        self._category = category
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
        
    @property
    def category(self):
        return self._category
        
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if not value.strip():
            raise ValueError("Category must not be empty")
        self._category = value
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        
    def contributors(self):
        author_list = []
        for article in self.articles():
            if article.author not in author_list:
                author_list.append(article.author)
        return author_list
        
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
        
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1
                
        frequent_authors = [author for author, count in author_count.items() if count > 2]
        return frequent_authors if frequent_authors else None

class Article:
    all = []  # Class variable to store all articles

    def __init__(self, author, magazine, title):
        # Type checking for author
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        
        # Type checking for magazine
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        
        # Validate title
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")

        # Set attributes
        self._title = title
        self._author = author
        self._magazine = magazine

        # Add to all articles list
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed after initialization")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = value

    @classmethod
    def all_articles(cls):
        """Alias for the all list to maintain compatibility"""
        return cls.all