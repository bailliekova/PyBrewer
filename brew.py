def hex_to_rgb(value):
    value = value.lstrip('#')
    #if len(value)!=6: raise Exception("bad input")
    return tuple(int(value[i:i+2], 16) for i in range(0, 6, 2))

def rgb_to_hex(rgb):
    return '#%X%X%X' % rgb

class Brew:
    def __init__(self, datatype, colors, scheme):
        self.datatype=datatype
        self.num_bins=len(colors)
        self.colors=tuple(colors)
        self.scheme=scheme
        self.index=self.num_bins
    
    def hexColors(self):
        return self.colors
    
    def rgbColorTuples(self):
        return tuple([hex_to_rgb(color) for color in self.colors])
    
    def __str__(self):
        return '<Brew object: datatype=%s bins=%s scheme=%s>' % (self.datatype, self.num_bins, self.scheme)
    
    def genHexColors(self):
        for index in range(0, len(self.colors)):
            yield self.colors[index]


