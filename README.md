[![DOI](https://zenodo.org/badge/342729167.svg)](https://zenodo.org/badge/latestdoi/342729167)
# electivity
Ecological electivity and forage indices

## Description

A compact scientific package for calculating electivity and forage preference indices including Ivlev E, Jacobs D, and Vanderploeg and Scavia E\*.

Designed to work seamlessly with Pandas dataframes.

## Installation

### Using pip

```
pip install electivity
```

### Using pipenv

```
pipenv install electivity
pipenv shell
```

## Usage

Every `electivity` [function](https://github.com/aazuspan/electivity#Functions-and-indices) take two parameters—a list of available resources and a list of consumed resources—and return an equal-length list of electivity values calculated element-wise. The easiest way to work with `electivity` is using Pandas dataframes, but any list-like data input will work.

### Example

```python
import pandas as pd
import electivity

# Build a dataframe of resource data
data = pd.DataFrame({"available": [10, 10, 10], "consumed": [10, 3, 0]})

# Calculate Ivlev electivity and assign it to a new column
data = data.assign(E=electivity.ivlev_electivity(data.available, data.consumed))
```

### Functions and indices

| Function               | Algorithm                                                     |
| ---------------------- | ------------------------------------------------------------- |
| ivlev_forage_ratio     | Ivlev Forage Ratio E' (Ivlev 1961)                            |
| ivlev_electivity       | Ivlev Electivity E (Ivlev 1961)                               |
| jacobs_electivity      | Jacobs' Electivity D (Jacobs 1974)                            |
| jacobs_forage_ratio    | Jacobs' Forage Ratio Q (Jacobs 1974)                          |
| strauss_linear         | Strauss' Linear Index L (Strauss 1979)                        |
| chessons_alpha         | Chesson's Alpha α (Chesson 1978)                              |
| relativized_electivity | Relativized Electivity Index E\* (Vanderploeg & Scavia, 1979) |

## Citation
Zuspan, A. 2021. electivity: Ecological electivity and forage indices, v1.0.0, Zenodo, doi:10.5281/zenodo.4567591

## References

- Chesson, J. 1978. Measuring preference in selective predation. Ecology 59:211-215.
- Ivlev, V. S. 1961. Experimental ecology of the feeding of fishes. Yale Univ. Press, New Haven.
- Jacobs, J. 1974. Quantitative measurement of food selection. Oecologia (Berl) 14:413-417.
- Strauss, R. E. 1979. Reliability estimates for Ivlev's electivity index, the forage ratio, and a proposed linear index of food selection. Trans Am Fish Soc 108: 344-352.
- Vanderploeg H. A. and Scavia D. 1979. Calculation and use of selectivity coefficients of feeding: zooplankton grazing. Ecol Modelling 7:135-149.
