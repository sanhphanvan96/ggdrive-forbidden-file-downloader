Download file does not allow downloading from Google Drive

# Prerequisites
- python 3
- geckodriver (browser driver for selenium) [https://github.com/mozilla/geckodriver](https://github.com/mozilla/geckodriver)

# Installing

```
pip install -r requirements.txt
```

# How to run?

```
python get-video.py -h
```

```
usage: get-video.py [-h] [--filename FILENAME] videourl

positional arguments:
  videourl

optional arguments:
  -h, --help           show this help message and exit
  --filename FILENAME
```

```
python get-video.py https://drive.google.com/file/d/1uOTsAdwYRSLvdpYNPkvrxiCr4SHsx86p/view --filename=ggdrive.mp4
```
