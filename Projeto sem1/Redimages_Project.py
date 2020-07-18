import glob
from PIL import Image
import os


size = 128, 128


for image in glob.glob('<path onde estão as imagens>'):
    upimage = Image.open(image).convert('RGB')
    name = os.path.basename(image)
    upimage.rotate(270).resize((size)).save('<path de destino>' + name, 'JPEG')
 

