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

OrRd=['#FFF7EC', '#FEF0D9', '#FEE8C8', '#FDD49E', '#FDCCBA', '#FDBB84', '#FC8D59', '#EF6548', '#E34A33', '#D7301F', '#B30000', '#990000','#7F0000']
OrRd9=Brew('sequential', sequential_from_scheme(OrRd, 9), 'OrRd', colorblind_safe=True)
OrRd8=Brew('sequential', sequential_from_scheme(OrRd, 8), 'OrRd', colorblind_safe=True)
OrRd7=Brew('sequential', sequential_from_scheme(OrRd, 7), 'OrRd', colorblind_safe=True)
OrRd6=Brew('sequential', sequential_from_scheme(OrRd, 6), 'OrRd', colorblind_safe=True)
OrRd5=Brew('sequential', sequential_from_scheme(OrRd, 5), 'OrRd', colorblind_safe=True)
OrRd4=Brew('sequential', sequential_from_scheme(OrRd, 4), 'OrRd', colorblind_safe=True, photocopy_safe=True, print_safe=True)
OrRd3=Brew('sequential', sequential_from_scheme(OrRd, 3), 'OrRd', colorblind_safe=True, photocopy_safe=True, print_safe=True)

PuBu=['#FFF7FB', '$F6EFF7', '#F1EEF6', '#ECE7F2', '#D0D1E6', '#BDC9E1', '#A6BDDB', '#74A9CF', '#3690C0', '#2B8CBE', '#0570B0', '#045A8D', '#023858']
PuBu9=Brew('sequential', sequential_from_scheme(PuBu, 9), 'PuBu', colorblind_safe=True)
PuBu8=Brew('sequential', sequential_from_scheme(PuBu, 8), 'PuBu' ,colorblind_safe=True)
PuBu7=Brew('sequential', sequential_from_scheme(PuBu, 7), 'PuBu', colorblind_safe=True)
PuBu6=Brew('sequential', sequential_from_scheme(PuBu, 6), 'PuBu', colorblind_safe=True)
PuBu5=Brew('sequential', sequential_from_scheme(PuBu, 5), 'PuBu', colorblind_safe=True)
PuBu4=Brew('sequential', sequential_from_scheme(PuBu, 4), 'PuBu', colorblind_safe=True)
PuBu3=Brew('sequential', sequential_from_scheme(PuBu, 3), 'PuBu', colorblind_safe=True, print_safe=True, photocopy_safe=True)

PuBuGn=['#FFF7FB', '#F6EFF7', '#ECE2F0', '#D0D1E6', '#BDC9E1', '#A6BDDB', '#67A9CF', '#3690C0', '#1C9099', '#02818A', '#016C59', '#016450', '#014636']
PuBuGn9=Brew('sequential', sequential_from_scheme(PuBuGn, 9), 'PuBuGn', colorblind_safe=True)
PuBuGn8=Brew('sequential', sequential_from_scheme(PuBuGn, 8), 'PuBuGn', colorblind_safe=True)
PuBuGn7=Brew('sequential', sequential_from_scheme(PuBuGn, 7), 'PuBuGn', colorblind_safe=True)
PuBuGn6=Brew('sequential', sequential_from_scheme(PuBuGn, 6), 'PuBuGn', colorblind_safe=True)
PuBuGn5=Brew('sequential', sequential_from_scheme(PuBuGn, 5), 'PuBuGn', colorblind_safe=True)
PuBuGn4=Brew('sequential', sequential_from_scheme(PuBuGn, 4), 'PuBuGn', colorblind_safe=True)
PuBuGn3=Brew('sequential', sequential_from_scheme(PuBuGn, 3), 'PuBuGn', colorblind_safe=True, print_safe=True, photocopy_safe=True)

PuRd=['#F7F4F9', 'F1EEF6', '#E7E1EF', '#D7B5D8', '#D4B9DA', '#C994C7', '#DF65B0', '#E7298A', '#DD1C77', '#CE1256', '#980043', '#91003F', '#67001F'] 
PuRd9=Brew('sequential', sequential_from_scheme(PuRd, 9), 'PuRd', colorblind_safe=True)
PuRd8=Brew('sequential', sequential_from_scheme(PuRd, 8), 'PuRd', colorblind_safe=True)
PuRd7=Brew('sequential', sequential_from_scheme(PuRd, 7), 'PuRd', colorblind_safe=True)
PuRd6=Brew('sequential', sequential_from_scheme(PuRd, 6), 'PuRd', colorblind_safe=True)
PuRd5=Brew('sequential', sequential_from_scheme(PuRd, 5), 'PuRd', colorblind_safe=True, print_safe=True)
PuRd4=Brew('sequential', sequential_from_scheme(PuRd, 4), 'PuRd', colorblind_safe=True, print_safe=True)
PuRd3=Brew('sequential', sequential_from_scheme(PuRd, 3), 'PuRd', colorblind_safe=True, print_safe=True, photocopy_safe=True)

RdPu=['#FFF7F3', '#FEEBE2', '#FDE0DD', '#FCC5C0', '#FBB4B9', '#FA9FB5', '#F768A1', '#DD3497', '#C51B8A', '#AE017E', '#7A0177', '#7A0177','#49006A']
RdPu9=Brew('sequential', sequential_from_scheme(RdPu, 9), 'RdPu', colorblind_safe=True)
RdPu8=Brew('sequential', sequential_from_scheme(RdPu, 8), 'RdPu', colorblind_safe=True)
RdPu7=Brew('sequential', sequential_from_scheme(RdPu, 7), 'RdPu', colorblind_safe=True)
RdPu6=Brew('sequential', sequential_from_scheme(RdPu, 6), 'RdPu', colorblind_safe=True)
RdPu5=Brew('sequential', sequential_from_scheme(RdPu, 5), 'RdPu', colorblind_safe=True)
RdPu4=Brew('sequential', sequential_from_scheme(RdPu, 4), 'RdPu', colorblind_safe=True)
RdPu3=Brew('sequential', sequential_from_scheme(RdPu, 3), 'RdPu', colorblind_safe=True)

YlGn=['#FFFFE5', '#FFFFCC', '#F7FCB9', '#D9F0A3', '#C2E699', '#ADDD8E', '#78C679', '#41AB5D', '#31A354', '#238443', '#006837', '#005A32', '#004529']
YlGn9=Brew('sequential', sequential_from_scheme(YlGn, 9), 'YlGn', colorblind_safe=True)
YlGn8=Brew('sequential', sequential_from_scheme(YlGn, 8), 'YlGn', colorblind_safe=True)
YlGn7=Brew('sequential', sequential_from_scheme(YlGn, 7), 'YlGn', colorblind_safe=True)
YlGn6=Brew('sequential', sequential_from_scheme(YlGn, 6), 'YlGn', colorblind_safe=True)
YlGn5=Brew('sequential', sequential_from_scheme(YlGn, 5), 'YlGn', colorblind_safe=True)
YlGn4=Brew('sequential', sequential_from_scheme(YlGn, 4), 'YlGn', colorblind_safe=True)
YlGn3=Brew('sequential', sequential_from_scheme(YlGn, 3), 'YlGn', colorblind_safe=True, photocopy_safe=True, print_safe=True)

YlGnBu=['#FFFFD9', '#FFFFCC', '#EDF8B1', '#C7E9B4', '#A1DAB4', '#7FCDBB', '#41B6C4', '#1D91C0', '#2C7FB8', '#225EA8', '#253494', '#0C2C84', '#081D58']
YlGnBu9=Brew('sequential', sequential_from_scheme(YlGnBu, 9), 'YlGnBu', colorblind_safe=True)
YlGnBu8=Brew('sequential', sequential_from_scheme(YlGnBu, 8), 'YlGnBu', colorblind_safe=True)
YlGnBu7=Brew('sequential', sequential_from_scheme(YlGnBu, 7), 'YlGnBu', colorblind_safe=True)
YlGnBu6=Brew('sequential', sequential_from_scheme(YlGnBu, 6), 'YlGnBu', colorblind_safe=True)
YlGnBu5=Brew('sequential', sequential_from_scheme(YlGnBu, 5), 'YlGnBu', colorblind_safe=True, print_safe=True)
YlGnBu4=Brew('sequential', sequential_from_scheme(YlGnBu, 4), 'YlGnBu', colorblind_safe=True, print_safe=True)
YlGnBu3=Brew('sequential', sequential_from_scheme(YlGnBu, 3), 'YlGnBu', colorblind_safe=True, photocopy_safe=True, print_safe=True)

YlOrBr=['#FFFFE5', '#FFFFD4', '#FFF7BC', '#FEE391', '#FED98E', '#FEC44F', '#FE9929', '#EC7014', '#D95FOE', '#CC4C02', '#993404', '#82CD04', '#662506']
YlOrBr9=Brew('sequential', sequential_from_scheme(YlOrBr, 9), 'YlOrBr', colorblind_safe=True)
YlOrBr8=Brew('sequential', sequential_from_scheme(YlOrBr, 8), 'YlOrBr', colorblind_safe=True)
YlOrBr7=Brew('sequential', sequential_from_scheme(YlOrBr, 7), 'YlOrBr', colorblind_safe=True)
YlOrBr6=Brew('sequential', sequential_from_scheme(YlOrBr, 6), 'YlOrBr', colorblind_safe=True)
YlOrBr5=Brew('sequential', sequential_from_scheme(YlOrBr, 5), 'YlOrBr', colorblind_safe=True)
YlOrBr4=Brew('sequential', sequential_from_scheme(YlOrBr, 4), 'YlOrBr', colorblind_safe=True, print_safe=True)
YlOrBr3=Brew('sequential', sequential_from_scheme(YlOrBr, 3), 'YlOrBr', colorblind_safe=True, photocopy_safe=True,print_safe=True)

YlOrRd=['#FFFFCC', '#FFFFB2', '#FFEDA0', '#FED976', '#FECC5C', '#FEB24C', '#FD8D3C', '#FC4E2A', '#F03B20', '#E31A1C', '#BD0026', '#B10026', '#800026']
YlOrRd9=Brew('sequential', sequential_from_scheme(YlOrRd, 9), 'YlOrRd', colorblind_safe=True)
YlOrRd8=Brew('sequential', sequential_from_scheme(YlOrRd, 8), 'YlOrRd', colorblind_safe=True)
YlOrRd7=Brew('sequential', sequential_from_scheme(YlOrRd, 7), 'YlOrRd', colorblind_safe=True)
YlOrRd6=Brew('sequential', sequential_from_scheme(YlOrRd, 6), 'YlOrRd', colorblind_safe=True)
YlOrRd5=Brew('sequential', sequential_from_scheme(YlOrRd, 5), 'YlOrRd', colorblind_safe=True)
YlOrRd4=Brew('sequential', sequential_from_scheme(YlOrRd, 4), 'YlOrRd', colorblind_safe=True, print_safe=True)
YlOrRd3=Brew('sequential', sequential_from_scheme(YlOrRd, 3), 'YlOrRd', colorblind_safe=True, photocopy_safe=True, print_safe=True)

brews=[
    BuGn3, BuGn4, BuGn5, BuGn6, BuGn7, BuGn8, BuGn9, 
    BuPu3, BuPu4, BuPu5, BuPu6, BuPu7, BuPu8, BuPu9, 
    GnBu3, GnBu4, GnBu5, GnBu6, GnBu7, GnBu8, GnBu9, 
    OrRd3, OrRd4, OrRd5, OrRd6, OrRd7, OrRd8, OrRd9, 
    PuBu3, PuBu4, PuBu5, PuBu6, PuBu7, PuBu8, PuBu9, 
    PuBuGn3, PuBuGn4, PuBuGn5, PuBuGn6, PuBuGn7, PuBuGn8, PuBuGn9,
    PuRd3, PuRd4, PuRd5, PuRd6, PuRd7, PuRd8, PuRd9,
    RdPu3, RdPu4, RdPu5, RdPu6, RdPu7, RdPu8, RdPu9,
    YlGn3, YlGn4, YlGn5, YlGn6, YlGn7, YlGn8, YlGn9, 
    YlGnBu3, YlGnBu4, YlGnBu5, YlGnBu6, YlGnBu7, YlGnBu8, YlGnBu9,
    YlOrBr3, YlOrBr4, YlOrBr5, YlOrBr6, YlOrBr7, YlOrBr8, YlOrBr9,
    YlOrRd3, YlOrRd4, YlOrRd5, YlOrRd6, YlOrRd7, YlOrRd8, YlOrRd9,
] 

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
    
    
