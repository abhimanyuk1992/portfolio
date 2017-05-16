import os
def populate():
	add_cat('Python')
	add_cat('Machine Learning')
	add_cat('Competition Programming')
	add_blog(name='How to use list in python',url='a.txt')
	add_blog(name='What is neural network',url='b.txt')
	add_blog(name='What is dynamic Programming',url='a.txt')

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

def add_blog(name,url):
	b = Blog.objects.get_or_create(name=name,url=url)[0]
	return b


if __name__=='__main__':
	print "Starting Resume population script"
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abhimanyu_portfolio.settings')
	from resume.models import Category, Blog
	populate()