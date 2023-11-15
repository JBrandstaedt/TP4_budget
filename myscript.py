import os
os.system('git bisect start c0509c5acef90386f59d729cfcb4c1c3ae03e3d0 a9f20e8a511665d81967342e7829e737395944d3')
os.system('git bisect run python manage.py test')