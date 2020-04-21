import argparse

from .core import Context
from .data.burmeister import load


def main(context, output, intent=False):
    ctx = load(context)

    if intent:
        ## Intent driven CbO
        (Tree, Lattice), Duality_Flag = ctx.CbOM()
    else:
        ## Extent driven CbO
        (Tree, Lattice), Duality_Flag = ctx.CbOG()

    ## Save the lattice
    ctx.save_lattice(Lattice, output, Duality_Flag)


parser = argparse.ArgumentParser()
parser.add_argument('context', type=str)
parser.add_argument('output', type=str)
parser.add_argument('--intent', default=False, action='store_true')

main(**vars(parser.parse_args()))
