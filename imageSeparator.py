import os, shutil, sys



def moveFile (finalPath,file):
    if not os.path.isfile(finalPath):    
        shutil.move(file,finalPath)

fileName=os.path.basename(sys.argv[0])
path = os.getcwd() 
source = ""
files = os.listdir(path)
files.sort()
for f in files:
        print(f)
        if os.path.isfile(f):
            tokens=f.split('.')
            if len(tokens) >1 and f.startswith('Screenshot') and f != fileName:
                source=tokens[1]
                dest=source
                if not os.path.isdir(dest):
                    os.makedirs(dest)
                finalPath=dest+'/'+f  
                moveFile(finalPath,f)
            else:
                dest='Miscellanea'
                if not os.path.isdir(dest):
                    os.makedirs(dest)
                finalPath=dest+'/'+f    
                moveFile(finalPath,f)


