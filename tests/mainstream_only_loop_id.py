# testing the identification of mainstream-only loop in a pfd.
#
# Author: Kai Zhang
#
# Change Log:
# 2019-07-21: revised to use the updated classes structure/funcs
# 2019-03-17: testing pfd_check(), specifically mainstream-only loop finding
#

from unit_procs.streams import influent, effluent, WAS, splitter, pipe
from unit_procs.bio import asm_reactor
from unit_procs.physchem import final_clarifier
from utils.pfd import check_pfd, show_pfd
import pdb


if __name__ == "__main__":

    inlet = influent()

    p1 = pipe()

    ra = asm_reactor()

    p2 = pipe()

    RAS = pipe()  # p3

    p4 = pipe()  # to outlet

    outlet = effluent()

    splt = splitter()

    wwtp = [inlet, p1, p2, RAS, p4, ra, outlet, splt]

    #pdb.set_trace()
    def construct_bad_pfd():
        # this PFD has a mainstream-only loop
        inlet.set_downstream_main(p1)
        p1.set_downstream_main(ra)
        ra.set_downstream_main(p2)
        p2.set_downstream_main(splt)
        splt.set_downstream_main(RAS)
        splt.set_downstream_side(p4)
        RAS.set_downstream_main(ra)
        p4.set_downstream_main(outlet)
        print("PFD constructed.")
        return None

    construct_bad_pfd()
    check_pfd(wwtp)
    show_pfd(wwtp)
