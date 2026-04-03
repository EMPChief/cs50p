Goal:
    Determine the MIME type of a file based on its extension.

Input:
    - File name (string)
      Examples: cat.gif, document.PDF, archive, photo.JpG

Output:
    - MIME type (string)
    - Default: application/octet-stream

Process / Steps:
    1. Receive file name from user
    2. Normalize input:
        - Remove leading/trailing spaces
        - Convert to lowercase
    3. Check if file contains a dot (.)
        - If not → return default MIME type
    4. Extract extension:
        - Take substring after the last dot
    5. Match extension using mapping:
        gif   → image/gif
        jpg   → image/jpeg
        jpeg  → image/jpeg
        png   → image/png
        pdf   → application/pdf
        txt   → text/plain
        zip   → application/zip
    6. Return result:
        - If match found → return MIME type
        - Otherwise → return default

Example:
    cat.gif   → image/gif
    cat.JPG   → image/jpeg
    archive   → application/octet-stream