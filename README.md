# LightBridge

A PyBridge extension to manipulate FileSystem locations on any platform

#

## Linux

Use LightBridge to path directories on Linux

## Linux Directories

- Desktop
- Documents
- Downloads
- Music

## Example

The code below shows how to use LightBridge on Linux environments

```
import LightBridge
from LightBridge import Linux

print(Linux.Desktop)
print(Linux.Documents)
```

```
### Output

/home/YOUR_USER/Desktop/
/home/YOUR_USER/Documents/
```

#

## Mac

Use LightBridge to path directories on Mac

## Mac Directories

- Applications
- Desktop
- Documents
- Downloads
- Movies
- Music
- Pictures
- Public

## Example

The code below shows how to use LightBridge on Mac environments

```
import LightBridge
from LightBridge import Mac

print(Mac.Desktop)
print(Mac.Documents)
```

```
### Output

/Users/YOUR_USER/Desktop/
/Users/YOUR_USER/Documents/
```

#

## Windows

Use LightBridge to path directories on Windows

## Windows Directories

- ApplicationData
- Desktop
- Documents
- Downloads
- LocalAppData
- Temp
- Pictures
- Favorites

## Example

The code below shows how to use LightBridge on Windows environments

```
import LightBridge
from LightBridge import Windows

print(Windows.Desktop)
print(Windows.Documents)
```

```
### Output

C:\Users\YOUR_USER/Desktop/
C:\Users\YOUR_USER/Documents/
```
