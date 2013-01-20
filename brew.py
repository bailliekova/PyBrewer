def hex_to_rgb(value):
    value = value.lstrip('#')
    return tuple(int(value[i:i+2], 16) for i in range(0, 6, 2))

def rgb_to_hex(rgb):
    return '#%X%X%X' % rgb

class Brew:
    def __init__(self, datatype, colors, scheme, colorblind_safe=False, photocopy_safe=False, print_friendly=False):
        self.datatype=datatype
        self.colors=tuple(colors)
        self.scheme=scheme
        self.num_bins=len(self.colors)
        self.colorblind_safe=colorblind_safe
        self.photocopy_safe=photocopy_safe
        self.print_friendly=print_friendly
        
    def hexColors(self):
        return self.colors
    
    def rgbColors(self):
        return tuple([hex_to_rgb(color) for color in self.colors])
    
    def __str__(self):
        return '<Brew object: datatype=%s scheme=%s>' % (self.datatype, self.scheme)
    
    def genHexColors(self):
        for index in range(0, len(self.colors)):
            yield self.colors[index]
