from google_images_download import google_images_download   # importing the library
import sys

# * pega os argumentos 1 e 2 do console
busca = sys.argv[1]     
limit = sys.argv[2]

response = google_images_download.googleimagesdownload()   #class instantiation

# * creating list of arguments
arguments = {"keywords":busca,"limit":limit,"print_urls":True, "delay":1,
             "output_directory":"train", "prefix":busca}
paths = response.download(arguments)    #passing the arguments to the function
print(paths)

'''Code from --> https://github.com/joaoreiis/PythonGoogleImagesDownload/blob/master/get_images.py'''
  