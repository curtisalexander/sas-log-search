# sas-log-search

Parse SAS logs looking for
* ERROR – looks for ‘ERROR’ in the SAS logs
* WARNING – looks for ‘WARNING’ in the SAS logs, ignoring the situations when it throws a warning that starts with ‘Unable to copy SASUSER…’ which can be safely ignored
* NOTE – looks for notes that inform you that a variable is uninitialized and looks for notes that inform you of missing value operations
 
## Usage

```
python sas-log-search.py
```

Folder and file locations are hard-coded within the script.


## Future

Turn into an actual script using [click](http://click.pocoo.org) allowing the user to pass in the log file to search.
