# API reference

## Creating activities.json file

??? note "example"
    ### Short example
    ```python
    from locdataMAC.timer import start
    start()
    ```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| Nothing    | nothing | No argument is requied for start method |

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| File    |  activities.json   | After pressing ctrl+c, it should return activities.json file       |


## Generating data.json file

??? note "example"
    ### Short example
    ```python
    from locdataMAC.analytics import json_data
    path = "/Users/sachinmishra/Desktop/check/activities.json"
    json_data(path)
    ```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| path    | str |input path of activiries.json file |

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| File    |  data.json   | return data.json file |


## Creating data folder and geting final file.

??? note "example"
    ### Short example
    ```python
    from assesment_creator import create_assesment
    create_assesment(url_link,filename)
    ```

| Args   | Type | Description | 
|:--------:|:------:|:-------|
| path    | str |valid url link |
| filename    | str | any word file name |

| Returns   |Type | Description | 
|:--------:|:--------:|:-----|
| str    |  str  | returns data folder and with data folder final scraped file |