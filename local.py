import sys
import ujson as json
from BackRecon import BackRecon
from ancillary import list_recursive


def local_noop(args):

    output_dict = {}
    cache_dict = {}
    computation_output = {"output": output_dict,
                          "cache": cache_dict,
                          "success": True}

    return json.dumps(computation_output)


if __name__ == '__main__':
    parsed_args = json.loads(sys.stdin.read())
    phase_key = list(list_recursive(parsed_args, 'computation_phase'))

    if not phase_key:
        computation_output = local_noop(parsed_args)
        sys.stdout.write(computation_output)
    else:
        raise ValueError("Error occurred at Local")
