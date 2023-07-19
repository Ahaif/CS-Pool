- Introductory project to web scraping and metadata.
  - First small program to automatically extract information from the web.
  - second program to analyze these files and manipulate the metadata.

- The spider program allow you to extract all the images from a website, recursively, by
providing a url as a parameter.
- program options:
  - ./spider [-rlp] URL
    - Option -r : recursively downloads the images in a URL received as a parameter.
    - Option -r -l [N] : indicates the maximum depth level of the recursive download.
- If not indicated, it will be 5.
    - Option -p [PATH] : indicates the path where the downloaded files will be saved.
- If not specified, ./data/ will be used.
- The program will download the following extensions by default:
  - .jpg/jpeg
  - .png
  - .gif
  - .bmp

- The second scorpion program receive image files as parameters and must be able to
parse them for EXIF and other metadata, displaying them on the screen.
- The program must at least be compatible with the same extensions that spider handles.
It display basic attributes such as the creation date, as well as EXIF data.

  - ./scorpion FILE1 [FILE2 ...]
