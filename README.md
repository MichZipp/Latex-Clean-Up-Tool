# Latex-Clean-Up-Tool
## Discription
This tool was created to clean up a latex project. I had the problem, that sometimes "pdflatex.exe" didn't regenerate all necessary files and so, the content in the generated pdf wasn't up to date. By running this Tool before running "pdflatex.exe", all generated files are deleted and "pdflatex.exe" has to regenerate all files.

Furthermore, this tool can be used to delete specified file extensions in a directory recursively. 

## Configuration 
The `CleanUpConfig.json` defines the file extension to delete and the path to the directory.
```json
{
    "extensions":
    [
      "extension1",
      "extension2"
    ],
    "path":"path_to_directory"
}
```

## Running
Make sure that the `CleanUp.py` and `CleanUpConfig.json` are in the same directory. If not, change the path in the `CleanUp.py` to the `CleanUpConfig.json`. To run the tool just type in the console:
```console
python CleanUp.py
```


