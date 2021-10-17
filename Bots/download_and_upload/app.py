import urllib.request
from pytube import YouTube

#downloading any picture by url 
def dl_hpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter image url: ')
file_name = input('Enter the file name to save: ')

dl_hpg(url, '', file_name)

#further we can upload these pictures to Instagram or 
# to Website created with Django and Templates


