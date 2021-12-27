## FileSystem - Android
## This file contains some default directories of your system

import os

## Current Directory
CurrentPath = os.getcwd()

## Access your internal storage
def InternalStorage():
    ## Home location on Android
    InternalStorage.Home = '/storage/emulated/0'
    ## Alarms
    InternalStorage.Alarms = f'{InternalStorage.Home}/Alarms/'
    ## Android
    InternalStorage.Android = f'{InternalStorage.Home}/Android/'
    ## DCIM
    InternalStorage.DCIM = f'{InternalStorage.Home}/DCIM/'
    ## Documents
    InternalStorage.Documents = f'{InternalStorage.Home}/Documents/'
    ## Download
    InternalStorage.Downloads = f'{InternalStorage.Home}/Download/'
    ## Movies
    InternalStorage.Movies = f'{InternalStorage.Home}/Movies/'
    ## Music
    InternalStorage.Music = f'{InternalStorage.Home}/Music/'
    ## Notifications
    InternalStorage.Notifications = f'{InternalStorage.Home}/Notifications/'
    ## Pictures
    InternalStorage.Pictures = f'{InternalStorage.Home}/Pictures/'
    ## Podcasts
    InternalStorage.Podcasts = f'{InternalStorage.Home}/Podcasts/'
    ## Ringtones
    InternalStorage.Ringtones = f'{InternalStorage.Home}/Ringtones/'
    
InternalStorage()

def ExternalStorage():
    print(">> This method is not callable yet")
    print(">> Future update...")
    
