from brew import Brew


class BrewSelector:
    def __init__(self):
        self.brews={'sequential':[{}], 
           
                    'diverging':[{}], 
           
                    'categorical':[{}]
                    }

    def get_Brew(datatype, num_bins, scheme):
        try:
            return self.brews[datatype][num_bins-3][scheme]
        except KeyError:
            raise Exception("There is no such Brew, sorry.")
    
    def list_brew_schemes(datatype, num_bins):
        try:
            return tuple(brew.scheme for brew in self.brews[datatype][num_bins-3].values())
        except IndexError:
            raise Exception("There are no Brews for that many bins for that datatype")
        
