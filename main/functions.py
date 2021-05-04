import os
import PIL
from PIL import Image
def handle_uploaded_file(f):  
    print(os.path.exists('./test.jpg'))
    img=Image.open(f)
    img = img.convert('RGB')
    img.save('main/templates/test.jpg')
    