## FileSystem - Linux
## This file contains some default directories of your system

import os

## Current Directory
CurrentPath = os.getcwd()

## User directory
User = f'/home/{os.environ["USER"]}/'

## Special Directories
Desktop = f'{User}Desktop/'
Documents = f'{User}Documents/'
Downloads = f'{User}Downloads/'
Music = f'{User}Music/'
