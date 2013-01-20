from brew import Brew

BuGn9=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B'], 'BuGn', colorblind_safe=True)
BuGn8=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#005824'], 'BuGn', colorblind_safe=True)
BuGn7=Brew('sequential', ['#EDF8FB', '#CCECE6', '#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#005824'], 'BuGn', colorblind_safe=True)
BuGn6=Brew('sequential', ['#EDF8FB'. '#CCECE6', '#99D8C9', '#66C2A4', '#2CA25F', '#006D2C'], 'BuGn', colorblind_safe=True)
BuGn5=Brew('sequential', ['#EDF8FB', '#B2E2E2', '#66C2A4', '#2CA25F', '#006D2C'], 'BuGn', colorblind_safe=True)
BuGn4=Brew('sequential', ['#EDF8FB', '#B2E2E2', '#66C2A4', '#238B45'], 'BuGn', colorblind_safe=True)
BuGn3=Brew('sequential', ['#E5F5F9', '#99D8C9', '#2CA25F'], 'BuGn', colorblind_safe=True)


class BrewSelector:
    def __init__(self):
        self.brews={'sequential': {
                        3:{'BuGn': BuGn3},
                        4:{'BuGn': BuGn4},
                        5:{'BuGn': BuGn5},
                        6:{'BuGn': BuGn6},
                        7:{'BuGn': BuGn7},
                        8:{'BuGn': BuGn8},
                        9:{'BuGn': BuGn9}
                    }, 
           
                    'diverging': {
                        9:{'RdGn': BuGn,}
                    }, 
           
                    'qualitative': {
                        9:{'Colors':BuGn},
                    },
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
