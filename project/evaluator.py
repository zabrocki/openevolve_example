from functools import lru_cache
from itertools import combinations
import numpy as np
import math
import concurrent.futures
import importlib.util
import traceback
import sys
sys.path.append('../')
from collections import defaultdict

# Expose the loaded mutant at module scope so helpers can use it.
mutant = None

# MZ: I believe that this is the general function we keep
def call_with_timeout(func, timeout=120, *args, **kwargs):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args, **kwargs)
        try:
            return future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            return None

#def compute_score_with_logs():
#    """
#    """
#    sco = my_score(20)
#    log_entry = {
#        "combined_score": sco,
#        "failure": False
#    }
#
#    return log_entry

def my_score(sequ):
    final_count = 0
    def sequence(x: int):
        L = [3,4,7,12,19,28,39,52,67,84,103,124,147,172,199,228,259,292,327,364]
        return L[x]
    for m in range(20):
        if sequ(m) == sequence(m):
            final_count += 10
        else:
            final_count = final_count - abs(np.log(max(abs(sequ(m)/(sequence(m)+.001)),0.001)))
    return {"combined_score": final_count}


def evaluate(program_path):
    global mutant
    try:
        # Load the evolved program as "mutant"
        spec = importlib.util.spec_from_file_location("mutant_program", program_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        mutant = module

        # Call decompose() with timeout (no args)
        S = call_with_timeout(mutant.guess_sequence, 120)
        sco = my_score(S)
        if sco is None:
            return {
              "combined_score": -1000,
              "failure": "timeout"
            }
        # Compute score with per-height logs
        return sco

    except Exception as e:
        print("Error during evaluation:", e)
        traceback.print_exc()
        return {
              "combined_score": -1000,
              "failure": str(e)
            }

if __name__ == "__main__":
    # Local test run; OpenEvolve will supply the path when evaluating mutants.
    result = evaluate("initial_program.py")
    print("Evaluation result:", result)
