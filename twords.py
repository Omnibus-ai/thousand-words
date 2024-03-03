from PIL import Image
import math
class Twords:
    def __init__(self):
        self.char_dict={}
        self.rev_dict={}
        for i in range(256):
            print (chr(i))
            self.char_dict[chr(i)]=i
            self.rev_dict[i]=chr(i)
        self.char_keys=list(self.char_dict.keys())
        self.rev_keys=list(self.rev_dict.keys())
    
    def create_image(self,inp):
        in_len=len(inp)
        print(in_len)
        dim=(math.sqrt(in_len))
        print(dim)
        int_dim=math.ceil(dim)
        print(int_dim)
        img = Image.new(mode = "RGB", size = (int_dim, int_dim),
                                   color = (144, 144, 144))    
        pixels = img.load()
        im_width=img.size[0]
        im_height=img.size[1]
        print(f'{im_width} :: {im_height}')
        pixel_box=[]
        pixel_list={}
        cnt =0
        go=True
        if go:
            for i in range(im_width):
                if go:
                    for j in range(im_height):
                        if go:
                            r,g,b = inp[cnt]
                            pixels[i,j] = ((r,g,b))
                            cnt+=1
                            if cnt>=in_len:
                                go=False
        print(img)
        return img
    
    
    def token_words(self,inp):
        num_list=[]
        char_list=list(inp)
        #print(char_list)
        #print(len(char_list))
        for char in char_list:
            try:
                num_list.append(self.char_dict[char])
            except Exception as e:
                print("Error")
                print(e)
                print(f"Can't find::{char}::")
        sort_list=[]
        out_list=[]
        cnt=1
        for i, ea in enumerate(num_list):
            #print(f'::{ea}')
            if cnt <=3:
                #print(f'::{ea}')
                sort_list.append(ea)
                cnt+=1
            else:
                out_list.append(sort_list)
                sort_list=[ea]
                cnt=2
        if sort_list:
            if len(sort_list)==1:
                sort_list.append(144)
                sort_list.append(144)
            if len(sort_list)==2:
                sort_list.append(144)
            if len(sort_list)==3:
                print(f"Max Len:: {sort_list}")
            out_list.append(sort_list)
        #print(out_list)
        img=self.create_image(out_list)
        word_box=out_list
        rev_box=out_list
        return img, img
        
    def decode_im(self,img):
        pixels = img.load() # create the pixel map
        im_width=img.size[0]
        im_height=img.size[1]
        print(f'{im_width} :: {im_height}')
        cnt =0
        go=True
        out_string=""
        if go:
            for i in range(im_width):    # for every col:
                if go:
                    for j in range(im_height):
                        if go:    
                            out=pixels[i,j] # set the colour accordingly    
                            r,g,b=out
                            if r in self.rev_keys and r!=144:
                                out_string+=self.rev_dict[r]
                            if g in self.rev_keys and g!=144:
                                out_string+=self.rev_dict[g]
                            if b in self.rev_keys and b!=144:
                                out_string+=self.rev_dict[b]                            
                            else:
                                pass
        return out_string
