# ReBATE Benchmark

A centralized repository to benchmark ReBATE feature selection algorithm performance across a variety of parameter settings and datasets.

The following directories are included in this repository, all of which can be used to replicate the experimental results of our ReBATE benchmark:

* `benchmark-data`: Contains all of the supervised classification benchmark datasets used in this benchmark study. All datasets are tab-separated, gzipped, and use the column header `Class` for the target column.

* `model-code`: Contains all of the Python scripts used to run the various Relief and other feature selection algorithms on the benchmark datasets.

* `post-analysis`: Contains the Jupyter notebooks and Python scripts used to analyze and visualize the results of the ReBATE benchmark.
