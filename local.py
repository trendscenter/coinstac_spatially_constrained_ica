import sys
import ujson as json
from .BackRecon import gift_gica
from utils import listRecursive
import utils as ut
import os


def scica_local_1(args):
    state = args["state"]
    in_files = ut.read_file_list_csv(
        os.path.join(state["baseDirectory"], args["input"]["datafile"][0]),
        state["baseDirectory"],
        state["clientId"]
    )
    maskfile = os.path.join(state["baseDirectory"], args["input"]["mask"][0])
    template = os.path.join(
        state["baseDirectory"], args["input"]["scica_template"][0])
    ut.log("Existence of files %s, mask %s, template %s, output %s" % (
        [str((f, os.path.exists(f))) for f in in_files],
        str((maskfile, os.path.exists(maskfile))),
        str((template, os.path.exists(template))),
        str((state["outputDirectory"], os.path.exists(state["outputDirectory"])))
    ), state)
    output = gift_gica(
        in_files=in_files,
        refFiles=[template],
        mask=maskfile,
        out_dir=state["outputDirectory"],
    )
    output_dict = {
        'computation_phase': 'scica_local_1'}
    cache_dict = {}
    computation_output = {
        "output": output_dict,
        "cache": cache_dict,
        "state": state
    }

    return computation_output


if __name__ == '__main__':
    parsed_args = json.loads(sys.stdin.read())
    phase_key = list(listRecursive(parsed_args, 'computation_phase'))

    if not phase_key:
        computation_output = local_noop(parsed_args)
        sys.stdout.write(computation_output)
    else:
        raise ValueError("Error occurred at Local")
