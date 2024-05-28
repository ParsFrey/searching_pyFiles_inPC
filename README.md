os.walk(directory_to_search) generates file names in a directory tree, walking either top-down or bottom-up.
For each directory in the tree rooted at directory_to_search (including directory_to_search itself), it produces a 3-tuple: (root, dirs, files).
root is the current directory path.
dirs is a list of subdirectories in the current root.
files is a list of non-directory files in the current root.
The inner loop iterates over each file in the files list.
If the pattern_to_search is found in the file name, it appends the full path of the file to the matches list using os.path.join(root, file).

Execution Flow
os.walk starts at C:\Users\LENOVO\OneDrive\Desktop\Codes2\auoto\searching_pyFiles_inPC.
root is C:\Users\LENOVO\OneDrive\Desktop\Codes2\auoto\searching_pyFiles_inPC.
dirs contains ['folder1', 'folder2'].
files contains ['script1.py', 'script2.txt'].
It checks script1.py and finds 'py' in the file name, so it appends C:\Users\LENOVO\OneDrive\Desktop\Codes2\auoto\searching_pyFiles_inPC\script1.py to matches.
It moves to folder1.
root is C:\Users\LENOVO\OneDrive\Desktop\Codes2\auoto\searching_pyFiles_inPC\folder1.
files contains ['script3.py', 'notes.docx'].
It checks script3.py and finds 'py' in the file name, so it appends C:\Users\LENOVO\OneDrive\Desktop\Codes2\auoto\searching_pyFiles_inPC\folder1\script3.py to matches.
Similarly, it processes folder2 and finds script4.py, appending the corresponding path to matches.
The result is that all .py files in the specified directory and its subdirectories are listed.
