import os
os.system('git bisect start 9c611f83bf13ece1ce57195d0e8f63f70fef46af e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c')
os.system('git bisect run python manage.py test')