import sys
import ujson as json
from BackRecon import BackRecon
from ancillary import list_recursive


def remote_spatially_constrained_ica(args):

    recon = BackRecon()
    recon.inputs.files = args["input"]["file_names"]
    recon.inputs.mask = args["input"]["mask"]
    recon.inputs.ica_sig = args["input"]["ica_sig"]
    recon.inputs.ica_varname = args["input"]["ica_varname"]
    recon.inputs.preproc_type = args["input"]["preproc_type"]
    recon.inputs.algorithm = args["input"]["algorithm"]
    out = recon.run()
    output_dict = {'output_files': [], 'computation_phase': 'spatially_constrained_ica'}
    cache_dict = {}
    computation_output = {"output": output_dict, "cache": cache_dict, "success": True}

    return json.dumps(computation_output)


if __name__ == '__main__':
    parsed_args = json.loads(sys.stdin.read())
    phase_key = list(list_recursive(parsed_args, 'computation_phase'))

    if not phase_key:
        computation_output = remote_spatially_constrained_ica(parsed_args)
        sys.stdout.write(computation_output)
    else:
        raise ValueError("Error occurred at Local")
