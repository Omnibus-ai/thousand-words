# Thousand Words

Use as a Python module to turn Text into image pixels.


## Usage

Create image pixels from text:
```
from twords import Twords
tw = Twords()
# encode text to pixels
img=tw.token_words(input_text) #input text string
# returns PIL image
```

Retrieve text from encoded image:
```
from twords import Twords
tw = Twords()
# decode text from pixels
txt=tw.decode_im(img) #input image path
# returns formatted text string
