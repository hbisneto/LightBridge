## FileSystem - Android
## This file contains some default directories of your system

import os

## Current Directory
CurrentPath = os.getcwd()

## Access your internal storage
def InternalStorage():
    InternalStorage.Home = '/storage/emulated/0/'
    InternalStorage.Android = '/storage/emulated/0/Android/'
    InternalStorage.Documents = '/storage/emulated/0/Documents/'
    InternalStorage.Downloads = '/storage/emulated/0/Download/'
    InternalStorage.Movies = '/storage/emulated/0/Movies/'
    InternalStorage.Pictures = '/storage/emulated/0/Pictures/'
    
InternalStorage()
