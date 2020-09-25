import os 
def convert():
    for I in os.listdir('.'):
        name=os.path.splitext(I)[0]
        ext=os.path.splitext(I)[1]
       
        if ext=='.jpg':
            file=open(I,'rb')
            image=file.read()
            file.close
            image=bytearray(image)
            key=50
            for i,j in enumerate(image) :
                    image[i]=j^key
            file=open(I,"wb")
            file.write(image)
            file.close

#last 
def extension_change():
    for i in os.listdir('.'):
        name=os.path.splitext(i)[0]
        ext=os.path.splitext(i)[1]
        print("name: ",name,)
        print("extension: ",ext)
        print()
        if ext=='.mp3':
                   os.rename(i,name + '.jpg')
                   print("task done")

extension_change()
convert()
