from pathlib import Path
import numpy as np
from sagittal_brain import run_averages

def test_avg_rows(tmp_path: Path) -> None:
    input_array = np.zeros((10, 10), dtype=int)
    input_array[-1, :] = 1

    expected_output = np.zeros((10, 10), dtype=float)
    expected_output[-1] = 1

    read_file = tmp_path = Path / "input.csv"
    np.savetxt("brain_sample.csv", input_array, delimiter=",", fmt='%d')
    write_to_file = Path / "output.csv"

    run_averages(read_file, write_to_file)

    function_results = np.loadtxt(write_to_file, delimiter=",", dtype=float)

    assert np.allclose(expected_output, function_results)

