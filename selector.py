from brew import Brew
from collections import defaultdict

BuGn9=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B'], 'BuGn', colorblind_safe=True)
BuGn8=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#005824'], 'BuGn', colorblind_safe=True)
BuGn7=Brew('sequential', ['#EDF8FB', '#CCECE6', '#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#005824'], 'BuGn', colorblind_safe=True)
BuGn6=Brew('sequential', ['#EDF8FB', '#CCECE6', '#99D8C9', '#66C2A4', '#2CA25F', '#006D2C'], 'BuGn', colorblind_safe=True)
BuGn5=Brew('sequential', ['#EDF8FB', '#B2E2E2', '#66C2A4', '#2CA25F', '#006D2C'], 'BuGn', colorblind_safe=True)
BuGn4=Brew('sequential', ['#EDF8FB', '#B2E2E2', '#66C2A4', '#238B45'], 'BuGn', colorblind_safe=True, print_safe=True)
BuGn3=Brew('sequential', ['#E5F5F9', '#99D8C9', '#2CA25F'], 'BuGn', colorblind_safe=True, photocopy_safe=True, print_safe=True)

BuPu9=Brew('sequential', ['#F7FCFD', '#E0ECF4', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#810F7C', '#4D004B',], 'BuPu', colorblind_safe=True)
BuPu8=Brew('sequential', ['#F7FCFD', '#E0ECF4', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#6E016B'], 'BuPu', colorblind_safe=True)
BuPu7=Brew('sequential', ['#EDF8FB', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8C6BB1', '#88419D', '#6E016B'], 'BuPu', colorblind_safe=True)
BuPu6=Brew('sequential', ['#EDF8FB', '#BFD3E6', '#9EBCDA', '#8C96C6', '#8856A7', '#810F7C'], 'BuPu', colorblind_safe=True)
BuPu5=Brew('sequential', ['#EDF8FB', '#B3CDE3', '#8C96C6', '#8856A7', '#810F7C'],'BuPu', colorblind_safe=True)
BuPu4=Brew('sequential', ['#EDF8FB', '#B3CDE3', '#8C96C6', '#88419D'],'BuPu', colorblind_safe=True ,print_safe=True)
BuPu3=Brew('sequential', ['#E0ECF4', '#9EBCDA', '#8856A7'],'BuPu', colorblind_safe=True, photocopy_safe=True, print_safe=True)

GnBu9=Brew('sequential', ['#F7FCF0', '#E0F3DB', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#0868AC', '#084081'], 'GnBu', colorblind_safe=True)
GnBu8=Brew('sequential', ['#F7FCF0', '#E0F3DB', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#08589E'], 'GnBu', colorblind_safe=True)
GnBu7=Brew('sequential', ['#F0F9E8', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#4EB3D3', '#2B8CBE', '#08589E'], 'GnBu', colorblind_safe=True)
GnBu6=Brew('sequential', ['#F0F9E8', '#CCEBC5', '#A8DDB5', '#7BCCC4', '#43A2CA', '#0868AC'], 'GnBu', colorblind_safe=True)
GnBu5=Brew('sequential', ['#F0F9E8', '#BAE4BC', '#7BCCC4', '#43A2CA', '#0868AC'], 'GnBu', colorblind_safe=True, print_safe=True)
GnBu4=Brew('sequential', ['#F0F9E8', '#BAE4BC', '#7BCCC4', '#2B8CBE'], 'GnBu', colorblind_safe=True, print_safe=True)
GnBu3=Brew('sequential', ['#E0F3DB', '#A8DDB5', '#43A2CA'], 'GnBu', colorblind_safe=True, photocopy_safe=True, print_safe=True)

OrRd9=Brew('sequential', ['#FFF7EC', '#FEE8C8', '#FDD49E', '#FDBB84', '#FC8D59', '#EF6548', '#D7301F', '#B30000', '#7F0000'], 'OrRd', colorblind_safe=True)
OrRd8=Brew('sequential', ['#FFF7EC', '#FEE8C8', '#FDD49E', '#FDBB84', '#FC8D59', '#EF6548', '#D7301F', '#990000'], 'OrRd', colorblind_safe=True)
OrRd7=Brew('sequential', ['#FEF0D9', '#FDD49E', '#FDBB84', '#FC8D59', '#EF6548', '#D7301F', '#990000'], 'OrRd', colorblind_safe=True)
OrRd6=Brew('sequential', ['#FEF0D9', '#FDD49E', '#FDBB84', '#FC8D59', '#E34A33', '#B30000'], 'OrRd', colorblind_safe=True)
OrRd5=Brew('sequential', ['#FEF0D9', '#FDCCBA', '#FC8D59', '#E34A33', '#B30000'], 'OrRd', colorblind_safe=True)
OrRd4=Brew('sequential', ['#FEF0D9', '#FDCCBA', '#FC8D59', '#D7301F'], 'OrRd', colorblind_safe=True, photocopy_safe=True, print_safe=True)
OrRd3=Brew('sequential', ['#FEE8C8', '#FDBB84', '#E34A33'], 'OrRd', colorblind_safe=True, photocopy_safe=True, print_safe=True)

PuBu9=Brew('sequential', ['#FFF7FB', '#ECE7F2', '#D0D1E6', '#A6BDDB', '#74A9CF', '#3690C0', '#0570B0', '#045A8D', '#023858'], 'BuPu', colorblind_safe=True)
PuBu8=Brew('sequential', ['#FFF7FB', '#ECE7F2', '#D0D1E6', '#A6BDDB','#74A9CF', '#3690C0', '#0570B0', '#034E7B'], 'BuPu' ,colorblind_safe=True)
PuBu7=Brew('sequential', ['#F1EEF6', '#D0D1E6', '#A6BDDB', '#74A9CF', '#3690C0', '#0570B0', '#034E7B'], 'BuPu', colorblind_safe=True)
PuBu6=Brew('sequential', ['#F1EEF6', '#D0D1E6', '#A6BDDB', '#74A9CF', '#2B8CBE', '#045A8D'], 'BuPu', colorblind_safe=True)
PuBu5=Brew('sequential', ['#F1EEF6', '#BDC9E1', '#74A9CF', '2B8CBE', '#045A8D'], 'BuPu', colorblind_safe=True)
PuBu4=Brew('sequential', ['#F1EEF6', '#BDC9E1', '#74A9CF', '#0570B0'], 'BuPu', colorblind_safe=True)
PuBu3=Brew('sequential', ['#ECE7F2', '#A6BDDB', '#2B8CBE'], 'BuPu', colorblind_safe=True, print_safe=True, photocopy_safe=True)

#TODO: 3 million more brews. Great. 

brews=[BuGn3, BuGn4, BuGn5, BuGn6, BuGn7, BuGn8, BuGn9, BuPu3, BuPu4, BuPu5, BuPu6, BuPu7, BuPu8, BuPu9, GnBu3, GnBu4, GnBu5, GnBu6, GnBu7, GnBu8, GnBu9, 
    OrRd3, OrRd4, OrRd5, OrRd6, OrRd7, OrRd8, OrRd9] 

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
    
    
