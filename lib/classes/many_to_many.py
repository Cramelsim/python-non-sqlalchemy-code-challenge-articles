class Article:
    all =[]
    def __init__(self, author, magazine, title):
        if isinstance(author,Author):
            self.author = author
        else:
            raise Exception("Author must be an instance of the Author class.")
        if isinstance(magazine,Magazine):
            self.magazine = magazine
        else:
            raise Exception("Magazine must be an instance of the Magazine class.")
        
        if isinstance(title,str) and 5 <= len(title) <=50: 
            self._title = title
        else:
            raise Exception("Titles must be strings of between 5 and 50 characters")
        Article.all.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,value):
        if hasattr(self,'_title'):
            raise Exception("Article title cannot be changed once it is set")
        
class Author:
    all =[]
    def __init__(self, name):
        if isinstance(name,str) and len(name) > 0:
            self._name = name
        else: 
            raise Exception("Name must not be an empty string")
        Author.all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name (self,value):
        if hasattr(self,'_name'):
            raise Exception("Cannot change author name once it is set")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in Article.all if article.author == self})

    def add_article(self, magazine, title):
        if isinstance(magazine,Magazine) and isinstance(title,str):
            new_article = Article(self,magazine,title)
            return new_article
        else: 
            raise Exception("Invalid magazine or title")

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})

class Magazine:
    def __init__(self, name, category):
        if isinstance(name,str) and 2<= len(name) <=16:
            self.name = name
        else:
            raise Exception("Magazine names must be between 2 and 16 characters")
        if isinstance(category,str) and len(category) >0:
            self._category = category
        else:
            raise Exception("Categories must be longer than 0 characters")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value,str) and 2<= len(value) <=16:
            self._name = value
        else:
            raise Exception("Magazine names must be between 2 and 16 characters")
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,value):
        if isinstance(value,str) and len(value) >0:
            self._category = value
        else:
            raise Exception("Categories must be longer than 0 characters")

    def articles(self):
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine ==self})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        authors_with_more_than_two_articles = [author for author, count in author_count.items() if count > 2]
        return authors_with_more_than_two_articles if authors_with_more_than_two_articles else None
