def hex_to_rgb(value):
    """
    converts a hex value to an rbg tuple.
    >>>hex_to_rgb('#FFFFFF')
    (255, 255, 255)
    """
    value = value.lstrip('#')
    return tuple(int(value[i:i+2], 16) for i in range(0, 6, 2))

def rgb_to_hex(rgb):
    """
    converts an rgb tuple to a hex string.
    >>>rgb_to_hex((255,255,255))
    '#FFFFFF'
    """
    return '#%X%X%X' % rgb

def sequential_from_scheme(scheme, num_bins):
    """
    Each sequential scheme in Colorbrewer has 13 values, and a subset of these is returned depending on the number of bins selected by the user. 
    This is a utility function which returns the colors in a specific brew given the entire scheme. 
    For details see: http://www.albany.edu/faculty/fboscoe/papers/harrower2003.pdf, table 1
    """
    sequencedict={
        3: (3, 6, 9),
        4: (2, 5, 7, 10),
        5: (2, 5, 7, 9, 11),
        6: (2, 4, 6, 7, 9, 11),
        7: (2, 4, 6, 7, 8, 10, 12),
        8: (1, 3, 4, 6, 7, 8, 10, 12),
        9: (1, 3, 4, 6, 7, 8, 10, 11, 13)  
    }
    return tuple([scheme[x-1] for x in sequencedict[num_bins]])

def qualitative_from_scheme(scheme, num_bins):
    """
    Similar to sequential_from_scheme above, generates brew colors from full scheme. See http://www.albany.edu/faculty/fboscoe/papers/harrower2003.pdf, table 2.
    """
    return tuple(scheme[:num_bins])

def diverging_from_scheme(scheme, num_bins):
    """
    Returns brew colors from full scheme. Pattern of colors to return from http://www.albany.edu/faculty/fboscoe/papers/harrower2003.pdf, table 3.
    """
    divergedict={
        3: (5, 8, 11),
        4: (3, 6, 10, 13),
        5: (3, 6, 8, 10, 13),
        6: (2, 5, 7, 9, 11, 14),
        7: (2, 5, 7, 8, 9, 11, 14),
        8: (2, 4, 6, 7, 9, 10, 12, 14),
        9: (2, 4, 6, 7, 8, 9, 10, 12, 14),
        10: (1, 2, 4, 6, 7, 9, 10, 12, 14, 15),
        11: (1, 2, 4, 6, 7, 8, 9, 10, 12, 14, 15)
    }
    return tuple(scheme[x-1] for x in divergedict[num_bins])

class Brew:
    """
    A Brew represents a color pallete from ColorBrewer2.org. Each Brew has an associated datatype as well as the attributes colorblind_safe, print_safe, and photocopy_safe, which I hope are self explanatory. 
    """
    def __init__(self, datatype, colors, scheme, colorblind_safe=False, photocopy_safe=False, print_safe=False):
        """
        Create new Brew object. 
        TODO: specify keyword argument for color format.
        """
        self.datatype=datatype
        self.colors=tuple(colors)
        self.scheme=scheme
        self.num_bins=len(self.colors)
        self.colorblind_safe=colorblind_safe
        self.photocopy_safe=photocopy_safe
        self.print_safe=print_safe

    def __eq__(self, other):
        return self.datatype==other.datatype and self.colors==other.colors and self.scheme==other.scheme and self.colorblind_safe==other.colorblind_safe and self.photocopy_safe==other.photocopy_safe and self.print_safe==other.print_safe
        
    def __len__(self):
        return len(self.colors)

    def __getattr__(self, key):
        return self.colors[key]

    def __iter__(self):
        return iter(self.colors)

    def hexColors(self):
        return self.colors
    
    def rgbColors(self):
        return tuple([hex_to_rgb(color) for color in self.colors])
    
    def __str__(self):
        return '<Brew object: datatype=%s scheme=%s>' % (self.datatype, self.scheme)
    
    def genHexColors(self):
        for index in range(0, len(self.colors)):
            yield self.colors[index]

