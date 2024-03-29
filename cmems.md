# How to retrieve data from CMEMS platforms

An example for daily MLD from GLORYS12 :
  - you need a micromamba environment :
    - you create it with [this environment file](cmems/copernicus-marine-client-env.yml) : ```micromamba env create --file copernicus-marine-client-env.yml```
    - you activate it with : ```micromamba activate cmems```
  - you need python scripts :
    - the [main script](cmems/get_glorys_mld.py) in which you have to put your CMEMS credentials
    - [ServiceDefs.py](cmems/ServiceDefs.py) and [parse_args.py](cmems/parse_args.py)
  - you get one year of data by running : ```python get_glorys_mld.py -s '2015-01-01' -e '2015-12-31'```

To get your own CMEMS dataset download, check the [catalog](https://data.marine.copernicus.eu/products) to get the path and variables suitable to your needs (look for Python Application Programming Interface in Automate download to get all dataset informations).
