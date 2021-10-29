## FileSystem - Linux
## This file contains some default directories of your system

import os

## Special Directories
CurrentPath = os.getcwd()
User = f'/home/{os.environ["USER"]}/'

Desktop = f'{User}Desktop/'
Documents = f'{User}Documents/'
Downloads = f'{User}Downloads/'
Music = f'{User}Music/'
