# yt_vid_downloader
A gui application for downloading yoututbe videos using only link.


**Libraries used
- tkinter
- pytube

**Troubleshoots
- if you're having problem running the code or getting errors like this "AttributeError: 'NoneType' object has no attribute 'span'" Use this command to install pytube "pip install git+https://github.com/baxterisme/pytube". This is a fork of pytube with some change in parser.py
you can also do this by yourself like, in C:\Python38\lib\site-packages\pytube\parser.py

Change this line:

152: func_regex = re.compile(r"function\([^)]+\)")

to this:

152: func_regex = re.compile(r"function\([^)]?\)")