from brew import Brew
BuGn=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B'], 'BuGn')


class BrewSelector:
    def __init__(self):
        self.brews={'sequential': {9:{'BuGn': BuGn}}, 
           
                    'diverging': {9:{'RdGn': BuGn}}, 
           
                    'qualitative': {9:{'Colors':BuGn}},
                    }

    def get_brew(self, datatype, num_bins, scheme):
        try:
            return self.brews[datatype][num_bins][scheme]
        except KeyError:
            raise Exception("There is no such Brew, sorry.")
    
    def list_brew_schemes(self, datatype, num_bins):
        try:
            return tuple(brew.scheme for brew in self.brews[datatype][num_bins].values())
        except KeyError:
            raise Exception("There are no Brews for that many bins for that datatype")
