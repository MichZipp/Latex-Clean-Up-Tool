import glob, os, json, fnmatch

print('CleanUp Started!')

with open('CleanUpConfig.json') as json_file:    
    print(json_file)
    data = json.load(json_file)
    path = data['path']

print('CleanUp Path: ' + path)

for element in data['extensions']:
    filename = '*.' + element
    # for file in glob.glob(os.path.join(path + '**/', filename)):
      #  os.remove(file)
       # print('Deleted: ' + file)
    for root, dirnames, filenames in os.walk(path):
        for file in fnmatch.filter(filenames, filename):
            filepath = os.path.join(root, file)
            os.remove(filepath)
            print('Deleted: ' + filepath)
            
print('CleanUp Finished!')