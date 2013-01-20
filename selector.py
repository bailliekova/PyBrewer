from brew import Brew
from collections import defaultdict

BuGn9=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B'], 'BuGn', colorblind_safe=True)
BuGn8=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#005824'], 'BuGn', colorblind_safe=True)
BuGn7=Brew('sequential', ['#EDF8FB', '#CCECE6', '#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#005824'], 'BuGn', colorblind_safe=True)
BuGn6=Brew('sequential', ['#EDF8FB', '#CCECE6', '#99D8C9', '#66C2A4', '#2CA25F', '#006D2C'], 'BuGn', colorblind_safe=True)
BuGn5=Brew('sequential', ['#EDF8FB', '#B2E2E2', '#66C2A4', '#2CA25F', '#006D2C'], 'BuGn', colorblind_safe=True)
BuGn4=Brew('sequential', ['#EDF8FB', '#B2E2E2', '#66C2A4', '#238B45'], 'BuGn', colorblind_safe=True, print_friendly=True)
BuGn3=Brew('sequential', ['#E5F5F9', '#99D8C9', '#2CA25F'], 'BuGn', colorblind_safe=True, photocopy_safe=True, print_friendly=True)

BuPu9=Brew('sequential', ['#F7FCFD', '#E0ECF4', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#810F7C', '#4D004B',], 'BuPu', colorblind_safe=True)
BuPu8=Brew('sequential', ['#F7FCFD', '#E0ECF4', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#6E016B'], 'BuPu', colorblind_safe=True)
BuPu7=Brew('sequential', ['#EDF8FB', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#6E016B'], 'BuPu', colorblind_safe=True)
BuPu6=Brew('sequential', ['#EDF8FB', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8856A7', '#810F7C'], 'BuPu', colorblind_safe=True)
BuPu5=Brew('sequential', ['#EDF8FB', '#B3CDE3', '#8C96C6', '#8856A7', '#810F7C'],'BuPu', colorblind_safe=True)
BuPu4=Brew('sequential', ['#EDF8FB', '#B3CDE3', '#8C96C6', '#88419D'],'BuPu', colorblind_safe=True ,print_friendly=True)
BuPu3=Brew('sequential', ['#E0ECF4', '#9EBCDA', '#8856A7'],'BuPu', colorblind_safe=True, photocopy_safe=True, print_friendly=True)

GnBu9=Brew('sequential', ['#F7FCF0', '#E0F3DB', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#0868AC', '#084081'], 'GnBu', colorblind_safe=True)
GnBu8=Brew('sequential', ['#F7FCF0', '#E0F3DB', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#08589E'], 'GnBu', colorblind_safe=True)
GnBu7=Brew('sequential', ['#F0F9E8', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#08589E'], 'GnBu', colorblind_safe=True)
GnBu6=Brew('sequential', ['#F0F9E8', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#43A2CA', '#0868AC'], 'GnBu', colorblind_safe=True)
GnBu5=Brew('sequential', ['#F0F9E8', '#BAE4BC', '#7BCCC4', '#43A2CA', '#0868AC'], 'GnBu', colorblind_safe=True)
GnBu4=Brew('sequential', ['#F0F9E8', '#BAE4BC', '#7BCCC4', '#2B8CBE'], 'GnBu', colorblind_safe=True, print_friendly=True)
GnBu3=Brew('sequential', ['#E0F3DB', '#A8DDB5', '#43A2CA'], 'GnBu', colorblind_safe=True, photocopy_safe=True, print_friendly=True)

#OrRd9=Brew('sequential', [])
#TODO: 3 million more brews. Great. 

class BrewSelector:
    def __init__(self):
        self.brews={'sequential': defaultdict(dict), 'diverging': defaultdict(dict), 'qualitative': defaultdict(dict)}

        # {'sequential': {
        #                 3:{'BuGn': BuGn3, 'BuPu': BuPu3, 'GnBu': GnBu3},
        #                 4:{'BuGn': BuGn4, 'BuPu': BuPu4, 'GnBu': GnBu4},
        #                 5:{'BuGn': BuGn5, 'BuPu': BuPu5, 'GnBu': GnBu5},
        #                 6:{'BuGn': BuGn6, 'BuPu': BuPu6, 'GnBu': GnBu6},
        #                 7:{'BuGn': BuGn7, 'BuPu': BuPu7, 'GnBu': GnBu7},
        #                 8:{'BuGn': BuGn8, 'BuPu': BuPu8, 'GnBu': GnBu8},
        #                 9:{'BuGn': BuGn9, 'BuPu': BuPu9, 'GnBu': GnBu9}
        #             }, 
           
        #             'diverging': {
        #                 9:{'RdGn': BuGn9,}
        #             }, 
           
        #             'qualitative': {
        #                 9:{'Colors':BuGn9},
        #             },
        #         }

    def get_brew(self, datatype, num_bins, scheme):
        try:
            return self.brews[datatype][num_bins][scheme]
        except KeyError:
            raise Exception("There is no such Brew, sorry.")
    
    def list_brew_schemes(self, datatype, num_bins, colorblind_safe=False, photocopy_safe=False, print_friendly=False):
        try:
            return tuple(brew.scheme for brew in self.brews[datatype][num_bins].values() if (not colorblind_safe or brew.colorblind_safe) and (not photocopy_safe or brew.photocopy_safe) and (not print_friendly or brew.print_friendly))
        except KeyError:
            raise Exception("There are no Brews for that many bins for that datatype")
    
    def add_brew(self, brew):
        self.brews[brew.datatype][brew.num_bins][brew.scheme]=brew
    
    def populate_brews(self,brew_iterable):
        for brew in brew_iterable:
            self.add_brew(brew)
