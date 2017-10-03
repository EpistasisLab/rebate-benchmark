# ReBATE Benchmark

A centralized repository to benchmark ReBATE feature selection algorithm performance across a variety of parameter settings and datasets.

## Directory contents

The following directories are included in this repository, all of which can be used to replicate the experimental results of our ReBATE benchmark:

* `benchmark-data`: Contains all of the supervised classification benchmark datasets used in this benchmark study. All datasets are tab-separated, gzipped, and use the column header `Class` for the target column.

* `model-code`: Contains all of the Python scripts used to run the various Relief and other feature selection algorithms on the benchmark datasets.

* `post-analysis`: Contains the Jupyter notebooks and Python scripts used to analyze and visualize the results of the ReBATE benchmark.

## License

Please see the [repository license](https://github.com/EpistasisLab/rebate-benchmark/blob/master/LICENSE) for the licensing and usage information for the contents of this repository.

## Required software packages

This benchmark study uses several existing software packages, including:

* [NumPy](http://www.numpy.org/)

* [SciPy](https://www.scipy.org/)

* [pandas](http://pandas.pydata.org)

* [scikit-learn](http://www.scikit-learn.org/)

* [matplotlib](https://matplotlib.org/)

* [Seaborn](https://seaborn.pydata.org/)

* [scikit-rebate](https://github.com/EpistasisLab/scikit-rebate)

Most of the necessary Python packages can be installed via the [Anaconda Python distribution](https://www.anaconda.com/download/), which we strongly recommend that you use. We also strongly recommend that you use of Python 3 over Python 2 if you're given the choice.

NumPy, SciPy, pandas, scikit-learn, matplotlib, and Seaborn can be installed in Anaconda via the command:

```Shell
conda install numpy scipy pandas scikit-learn matplotlib seaborn
```

scikit-rebate can be installed with `pip` via the command:

```Shell
pip install skrebate
```

Please [file a new issue](https://github.com/EpistasisLab/rebate-benchmark/issues/new) if you run into installation problems.

## Contributing

If you would like to contribute to the ReBATE feature selection benchmark, please [check the existing issues](https://github.com/EpistasisLab/rebate-benchmark/issues) to see if there is an ongoing project you can contribute to.

If you have a suggestion or comment for the benchmark, please [file a new issue](https://github.com/EpistasisLab/rebate-benchmark/issues/new) and thoroughly describe your suggestion or comment. Be sure to first check the [existing and closed issues](https://github.com/EpistasisLab/rebate-benchmark/issues?utf8=%E2%9C%93&q=is%3Aissue) to see if the suggestion or comment hasn't already been discussed.

## Citing

If you would like to cite this benchmark study, please cite the research papers listed below.

[blank until preprints are posted]
