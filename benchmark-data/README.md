# Benchmark data

This directory contains all of the supervised classification benchmark datasets used in this benchmark study.

All datasets are tab-separated, gzipped, and use the column header `Class` for the target column.

The following Python code will run a for loop through every data file in the benchmark, if run in this directory.

```Python
import os
import sys

for dirpath, dirnames, filenames in os.walk('Simulated_Benchmark_Archive/'):
    # In some directories, there are report files. Skip these files.
    if len(filenames) < 10 and len(dirpath) > 0:
        continue

    for filename in filenames:
        if not filename.endswith('.txt.gz'):
            continue
        dataset_file = os.path.join(dirpath, filename)

        # Do something with the dataset
```
