1. Goal
--------
Take a file name as input and return its MIME type.

2. Input
--------
- File name (string)
Examples: cat.gif, document.PDF, archive, photo.JpG

3. Output
---------
- MIME type (string)
- Default if unknown: application/octet-stream

4. File Extension → MIME Type Mapping
--------------------------------------
.gif   → image/gif
.jpg   → image/jpeg
.jpeg  → image/jpeg
.png   → image/png
.pdf   → application/pdf
.txt   → text/plain
.zip   → application/zip

5. Steps
---------
1. Ask user for file name
2. Convert file name to lowercase and remove spaces
3. Check if there is a dot (.)
   - If no dot → return default
4. Take text after last dot as extension
5. Look up extension in mapping
   - If found → return MIME type
   - If not → return default

6. Examples
------------
File name: cat.gif    → image/gif
File name: cat.JPG    → image/jpeg
File name: archive    → application/octet-stream