# sas-log-search

Parse SAS logs looking for

* ERROR
    * any `ERROR` in the SAS logs
* WARNING
    * any `WARNING` in the SAS logs [ignoring a `WARNING` that starts with `Unable to copy SASUSER…`]
* NOTE
    * `NOTE` that informs one that a variable is uninitialized
    * `NOTE` that informs one of missing value operations
 
## Usage

```
python sas-log-search.py
```

Folder and file locations are hard-coded within the script.


## Future

Turn into an actual script using [click](http://click.pocoo.org) allowing the user to pass in the log file to search.
