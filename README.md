# Latex-Clean-Up-Tool
## Discription
Just a simple tool to clean up a latex project. I had the problem, that sometimes "pdflatex.exe" didn't regenerate all necessary files and so, the content in the generated pdf wasn't up to date. By running this Tool before running "pdflatex.exe", all generated files are deleted and "pdflatex.exe" has to regenerate all files.

Furthermore, this tool can be used to delete specified file extensions in a directory recursively. 

This tool was tested sucessfully under Python 2.7.14!

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

## Building
If you want to run this tool on machines without a python installation. You can build stand-alone executables. 
1. Install `pyinstaller`:
```console
pip install pyinstaller
```
2. Build stand-alone executables:
```console
pyinstaller CleanUp.py
```


