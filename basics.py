import os
from datetime import datetime

os.chdir('C:/Users/User/Desktop/')

print(dir(os))

# os.mkdir('python-projects-test/sub-dir')
# os.removedirs('python-projects-test/sub-dir')
# os.rename('python_projects', 'python-project')

# for dirpath, dirnames, filenames in os.walk('C:/Users/User/'):
#     print('Current Path:', dirpath)
#     print('Directories Path:', dirnames)
#     print('Files:', filenames)
#     print()

# print(os.environ.get('USERPROFILE'))

file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')

print(file_path)

print(os.path.split('/tmp/test.txt'))  #get both
print(os.path.dirname('/tmp/test.txt'))  #get the path of a dir
print(os.path.basename('/tmp/test.txt'))  # get the path of the file
print(os.path.exists('/tmp/test.txt'))  # checks if the dir is real
print(os.path.isdir('/tmp/test.txt'))  # checks if the dir is real
print(os.path.isfile('/tmp/test.txt'))  # checks if the file is real
print(os.path.splitext('/tmp/test.txt'))  # 

# mod_times = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_times))