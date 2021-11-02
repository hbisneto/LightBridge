## FileSystem - Windows
## This file contains some default directories of your system

import os

## Current Directory
CurrentPath = os.getcwd()
## User directory
User = os.environ['USERPROFILE']

## Special Directories
ApplicationData = f'{User}/AppData/Roaming/'
Desktop = f'{User}/Desktop/'
Documents = f'{User}/Documents/'
Downloads = f'{User}/Downloads/'
LocalAppData = f'{User}/AppData/Local/'
Temp = f'{LocalAppData}Temp'
Pictures = f'{User}/Pictures/'
Favorites = f'{User}/Favorites/'
