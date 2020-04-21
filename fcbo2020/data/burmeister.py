import intbitset as bs
from ..core import Context


# this does not need a special (heavy) conext object from the core
# * we might get by just returning a (G, M binary matrix) tuple
# * there is no save(G, M, ctx) here
# * context transposing is not a part of loading files!

def skip_empty(f):
    # Skip an empty line if there is one
    pos = f.tell()
    if f.readline().rstrip():
        f.seek(pos)


def load(filename):
    with open(filename, "r") as f:
        # File format marker
        txt = f.readline().strip()
        if txt != "B":
            raise Exception("Bad file format")

        # The name of the context
        name = f.readline().strip()
        # Read the volume of the extent and the intent
        G = int(f.readline().strip())
        M = int(f.readline().strip())
        skip_empty(f)

        # Read the labels first the extent, last the intent
        extent = [f.readline().strip() for x in range(G)]
        intent = [f.readline().strip() for x in range(M)]
        skip_empty(f)

        # Load and process the object-attribute relationship,
        #   expect that it is stored extent-wise
        ctx0 = []
        for g in range(G):
            line = f.readline().rstrip()
            ctx0.append(bs.intbitset([m for m in range(M) if line[m] in "X"], M))
        # Transpose the context
        ctxt = [
            bs.intbitset([g for g in range(G) if m in ctx0[g]], G) for m in range(M)
        ]

        return Context(extent, intent, (ctx0, ctxt), name)
