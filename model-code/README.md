# Feature selection algorithm code

This directory contains all of the Python scripts used to run the various Relief and other feature selection algorithms on the benchmark datasets.

These Python scripts are written to receive the path to a benchmark dataset as input, fit the feature selection algorithm to the dataset, and print the feature rankings and scores for every feature in the dataset.

The following Python code will run every algorithm on every data file in the benchmark, if run in this directory.

```Python
import os
import sys
from glob import glob

for algorithm_file in glob('*py'):
    for dirpath, dirnames, filenames in os.walk('../benchmark-data/Simulated_Benchmark_Archive/'):
        # In some directories, there are report files. Skip these files.
        if len(filenames) < 10 and len(dirpath) > 0:
            continue

        for filename in filenames:
            if not filename.endswith('.txt.gz'):
                continue
            dataset_file = os.path.join(dirpath, filename)
            os.system('python {} {}'.format(algorithm_file, dataset_file))
```
