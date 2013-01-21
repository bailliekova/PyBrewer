from brew import *
from collections import defaultdict

BuGn=['#F7FCFD', '#EDF8FB', '#E5F5F9', '#CCECE6', '#B2E2E2', '#99D8C9', '#66C2A4', '#41AE76','#2CA25F', '#238B45', '#006D2C', '#005824', '#00441B']
BuGn9=Brew('sequential', sequential_from_scheme(BuGn, 9), 'BuGn', colorblind_safe=True)
BuGn8=Brew('sequential', sequential_from_scheme(BuGn, 8), 'BuGn', colorblind_safe=True)
BuGn7=Brew('sequential', sequential_from_scheme(BuGn, 7), 'BuGn', colorblind_safe=True)
BuGn6=Brew('sequential', sequential_from_scheme(BuGn, 6), 'BuGn', colorblind_safe=True)
BuGn5=Brew('sequential', sequential_from_scheme(BuGn, 5), 'BuGn', colorblind_safe=True)
BuGn4=Brew('sequential', sequential_from_scheme(BuGn, 4), 'BuGn', colorblind_safe=True, print_safe=True)
BuGn3=Brew('sequential', sequential_from_scheme(BuGn, 3), 'BuGn', colorblind_safe=True, photocopy_safe=True, print_safe=True)

BuPu=['#F7FCFD', '#EDF8FB', '#E0ECF4', '#BFD3E6', '#B3CDE3', '#9EBCDA', '#8C96C6', '#8C6BB1', '#8856A7', '#88419D', '#810F7C', '#6E016B', '#4D004B']
BuPu9=Brew('sequential', sequential_from_scheme(BuPu, 9), 'BuPu', colorblind_safe=True)
BuPu8=Brew('sequential', sequential_from_scheme(BuPu, 8), 'BuPu', colorblind_safe=True)
BuPu7=Brew('sequential', sequential_from_scheme(BuPu, 7), 'BuPu', colorblind_safe=True)
BuPu6=Brew('sequential', sequential_from_scheme(BuPu, 6), 'BuPu', colorblind_safe=True)
BuPu5=Brew('sequential', sequential_from_scheme(BuPu, 5),'BuPu', colorblind_safe=True)
BuPu4=Brew('sequential', sequential_from_scheme(BuPu, 4),'BuPu', colorblind_safe=True, print_safe=True)
BuPu3=Brew('sequential', sequential_from_scheme(BuPu, 3),'BuPu', colorblind_safe=True, photocopy_safe=True, print_safe=True)

GnBu=['#F7FCF0', '#F0F9E8', '#E0F3DB', '#CCEBC5', '#BAE4BC', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#43A2CA', '#2B8CBE', '#0868AC', '#08589E', '#084081']
GnBu9=Brew('sequential', sequential_from_scheme(GnBu, 9), 'GnBu', colorblind_safe=True)
GnBu8=Brew('sequential', sequential_from_scheme(GnBu, 8), 'GnBu', colorblind_safe=True)
GnBu7=Brew('sequential', sequential_from_scheme(GnBu, 7), 'GnBu', colorblind_safe=True)
GnBu6=Brew('sequential', sequential_from_scheme(GnBu, 6), 'GnBu', colorblind_safe=True)
GnBu5=Brew('sequential', sequential_from_scheme(GnBu, 5), 'GnBu', colorblind_safe=True, print_safe=True)
GnBu4=Brew('sequential', sequential_from_scheme(GnBu, 4), 'GnBu', colorblind_safe=True, print_safe=True)
GnBu3=Brew('sequential', sequential_from_scheme(GnBu, 3), 'GnBu', colorblind_safe=True, photocopy_safe=True, print_safe=True)

OrRd=['#FFF7EC', '#FEF0D9', '#FEE8C8', '#FDD49E', '#FDCCBA', '#FDBB84', '#FC8D59', '#EF6548', '#E34A33', '#D7301F', '#B30000', '#7F0000']
OrRd9=Brew('sequential', sequential_from_scheme(OrRd, 9), 'OrRd', colorblind_safe=True)
OrRd8=Brew('sequential', sequential_from_scheme(OrRd, 8), 'OrRd', colorblind_safe=True)
OrRd7=Brew('sequential', sequential_from_scheme(OrRd, 7), 'OrRd', colorblind_safe=True)
OrRd6=Brew('sequential', sequential_from_scheme(OrRd, 6), 'OrRd', colorblind_safe=True)
OrRd5=Brew('sequential', sequential_from_scheme(OrRd, 5), 'OrRd', colorblind_safe=True)
OrRd4=Brew('sequential', sequential_from_scheme(OrRd, 4), 'OrRd', colorblind_safe=True, photocopy_safe=True, print_safe=True)
OrRd3=Brew('sequential', sequential_from_scheme(OrRd, 3), 'OrRd', colorblind_safe=True, photocopy_safe=True, print_safe=True)

PuBu=['#FFF7FB', '#F1EEF6', '#ECE7F2', '#D0D1E6', '#BDC9E1', '#A6BDDB', '#74A9CF', '#3690C0', '#2B8CBE', '#0570B0', '#045A8D', '#023858']
PuBu9=Brew('sequential', sequential_from_scheme(PuBu, 9), 'PuBu', colorblind_safe=True)
PuBu8=Brew('sequential', sequential_from_scheme(PuBu, 8), 'PuBu' ,colorblind_safe=True)
PuBu7=Brew('sequential', sequential_from_scheme(PuBu, 7), 'PuBu', colorblind_safe=True)
PuBu6=Brew('sequential', sequential_from_scheme(PuBu, 6), 'PuBu', colorblind_safe=True)
PuBu5=Brew('sequential', sequential_from_scheme(PuBu, 5), 'PuBu', colorblind_safe=True)
PuBu4=Brew('sequential', sequential_from_scheme(PuBu, 4), 'PuBu', colorblind_safe=True)
PuBu3=Brew('sequential', sequential_from_scheme(PuBu, 3), 'PuBu', colorblind_safe=True, print_safe=True, photocopy_safe=True)


#TODO: 3 million more brews. Great. 

brews=[BuGn3, BuGn4, BuGn5, BuGn6, BuGn7, BuGn8, BuGn9, BuPu3, BuPu4, BuPu5, BuPu6, BuPu7, BuPu8, BuPu9, GnBu3, GnBu4, GnBu5, GnBu6, GnBu7, GnBu8, GnBu9, 
    OrRd3, OrRd4, OrRd5, OrRd6, OrRd7, OrRd8, OrRd9, PuBu3, PuBu4, PuBu5, PuBu6, PuBu7, PuBu8, PuBu9] 

class BrewSelector:
    
    def add_brew(self, brew):
        self.brews[brew.datatype][brew.num_bins][brew.scheme]=brew
    
    def add_brews(self,brew_iterable):
        for brew in brew_iterable:
            self.add_brew(brew)

    def __init__(self, empty=False):
        self.brews={'sequential': defaultdict(dict), 'diverging': defaultdict(dict), 'qualitative': defaultdict(dict)}
        if not empty:
            self.add_brews(brews)

    def get_brew(self, datatype, num_bins, scheme):
        try:
            return self.brews[datatype][num_bins][scheme]
        except KeyError:
            raise Exception("There is no such Brew, sorry.")
    
    def list_schemes(self, datatype, num_bins, colorblind_safe=False, photocopy_safe=False, print_safe=False):
        try:
            return tuple(brew.scheme for brew in self.brews[datatype][num_bins].values() if (not colorblind_safe or brew.colorblind_safe) and (not photocopy_safe or brew.photocopy_safe) and (not print_safe or brew.print_safe))
        except KeyError:
            raise Exception("There are no Brews for that many bins for that datatype")
    
    
