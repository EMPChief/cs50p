def main() -> None:
    """
    Main function: starts the program.
    Does not return anything.
    """
    file_extension()


def file_extension() -> None:
    """
    Prompt the user for a filename and print its MIME type based on the file extension.
    Unknown extensions default to 'application/octet-stream'.

    Returns:
        None
    """
    # Get user input, remove extra spaces, and convert to lowercase
    user_file_type: str = input("File name: ").strip().lower()

    # Split the filename by dots and get the last part as the file extension
    ext: str = user_file_type.split(".")[-1]

    # Dictionary mapping file extensions to MIME types
    mime_types: dict[str, str] = {
        "gif": "image/gif",
        "jpeg": "image/jpeg",
        "jpg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }

    # Print MIME type, defaulting to 'application/octet-stream' if not found
    print(mime_types.get(ext, "application/octet-stream"))


# Run the program
main()
