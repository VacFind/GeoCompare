# GeoCompare

[![codecov](https://codecov.io/gh/VacFind/GeoCompare/branch/main/graph/badge.svg?token=7RGJPCEA3H)](https://codecov.io/gh/VacFind/GeoCompare)

A tool to help automate the merging of geographical data (i.e. data that has coordinate values) across datasets.

This is useful for things like combining state-level vaccination site data into a national data set, and associating existing lists of vaccination sites with entries in a national database

## Running for Development

Here are the commands you will need to run the GeoCompare Command-Line interface :

```
pipenv install
pipenv shell
python3 ./main.py
```



## Documentation

End user Documentation is hosted on [Github Pages](https://vacfind.github.io/GeoCompare) and built using [MkDocs](https://www.mkdocs.org/).

Developer documentation can be found on the [wiki](https://github.com/VacFind/GeoCompare/wiki).


## Tests

to run unit tests, use the command `python3 -m unittest`

### Coverage

to run tests with coverage, run `coverage run --source=. -m unittest`

to view the coverage report, run `coverage report`, or `coverage html` for an in-browser version


## TODO:

Data cleaning/canonicalization
location matching/concordances

compare by multiple factors (like address, or google placeID's)
human comparison webpage?
