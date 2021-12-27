## FileSystem - Mac
## This file contains some default directories of your system

import os

## Current Directory
CurrentPath = os.getcwd()

## User directory
User = f'/Users/{os.environ["USER"]}/'

## Special Directories
Applications = f'{User}Applications/'
Desktop = f'{User}Desktop/'
Documents = f'{User}Documents/'
Downloads = f'{User}Downloads/'
Movies = f'{User}Movies/'
Music = f'{User}Music/'
Pictures = f'{User}Pictures/'
Public = f'{User}Public/'
