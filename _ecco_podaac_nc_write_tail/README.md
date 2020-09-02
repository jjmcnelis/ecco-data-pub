# ecco podaac nc adjustments

There's a function in `podaac.py` that'll modify the xarray dataset just before it's output.


```python
files=!ls
files
```




    ['ATM_SURFACE_TEMP_HUM_WIND_PRES_day_mean_1992-01-01_ECCO_V4r4_latlon_0p50deg.nc',
     'datasets.csv',
     'ecco_podaac.py',
     'keywords.json',
     '__pycache__',
     'README.ipynb',
     'README.md']




```python
f = files[0]
f
```




    'ATM_SURFACE_TEMP_HUM_WIND_PRES_day_mean_1992-01-01_ECCO_V4r4_latlon_0p50deg.nc'



## example output


```python
!python ecco_podaac.py $f
```

    <xarray.Dataset>
    Dimensions:         (latitude: 360, longitude: 720, nv: 2, time: 1)
    Coordinates:
      * time            (time) datetime64[ns] 1992-01-01T12:00:00
      * latitude        (latitude) float32 -89.75 -89.25 -88.75 ... 89.25 89.75
      * longitude       (longitude) float32 -179.75 -179.25 ... 179.25 179.75
        time_step       (time) timedelta64[ns] ...
        latitude_bnds   (latitude, nv) float32 ...
        longitude_bnds  (longitude, nv) float32 ...
        time_bnds       (time, nv) datetime64[ns] ...
    Dimensions without coordinates: nv
    Data variables:
        EXFatemp        (time, latitude, longitude) float32 ...
        EXFaqh          (time, latitude, longitude) float32 ...
        EXFewind        (time, latitude, longitude) float32 ...
        EXFnwind        (time, latitude, longitude) float32 ...
        EXFwspee        (time, latitude, longitude) float32 ...
        EXFpress        (time, latitude, longitude) float32 ...
    Attributes:
        acknowledgement:              This research was carried out by the Jet Pr...
        author:                       Ian Fenty and Ou Wang
        cdm_data_type:                Grid
        comment:                      These fields are provided on a regular lat-...
        conventions:                  CF-1.8, ACDD-1.3
        creator_email:                ecco-group@mit.edu
        creator_institution:          NASA Jet Propulsion Laboratory (JPL)
        creator_name:                 ECCO Consortium
        creator_type:                 group
        creator_url:                  https://ecco.jpl.nasa.gov
        date_created:                 2020-09-02T09:13:10
        date_issued:                  2020-09-02T09:13:10
        date_metadata_modified:       2020-09-02T09:13:10
        date_modified:                2020-09-02T09:13:10
        geospatial_lat_max:           90.0
        geospatial_lat_min:           -90.0
        geospatial_lat_resolution:    0.5
        geospatial_lat_units:         degrees_north
        geospatial_lon_max:           180.0
        geospatial_lon_min:           -180.0
        geospatial_lon_resolution:    0.5
        geospatial_lon_units:         degrees_east
        history:                      Inaugural release of an ECCO "Central Estim...
        id:                           10.5067/ECG5D-ATM44
        institution:                  NASA Jet Propulsion Laboratory (JPL)
        instrument_vocabulary:        GCMD instrument keywords
        keywords:                     EARTH SCIENCE > OCEANS > OCEAN TEMPERATURE ...
        keywords_vocabulary:          NASA Global Change Master Directory (GCMD) ...
        license:                      Public Domain
        naming_authority:             gov.nasa.jpl
        platform:                     ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jaso...
        platform_vocabulary:          GCMD platform keywords
        processing_level:             L4
        product_name:                 ATM_SURFACE_TEMP_HUM_WIND_PRES_day_mean_199...
        product_time_coverage_end:    2017-12-31T12:00:00
        product_time_coverage_start:  1992-01-01T12:00:00
        product_version:              Version 4, Release 4
        program:                      NASA Physical Oceanography, Cryosphere, Mod...
        project:                      Estimating the Circulation and Climate of t...
        publisher_email:              podaac@podaac.jpl.nasa.gov
        publisher_name:               Physical Oceanography Distributed Active Ar...
        publisher_type:               institution
        publisher_url:                https://podaac.jpl.nasa.gov
        references:                   ECCO Consortium, Fukumori, I., Wang, O., Fe...
        standard_name_vocabulary:     NetCDF Climate and Forecast (CF) Metadata C...
        summary:                      This dataset provides daily average atmosph...
        time_coverage_duration:       P1D
        time_coverage_end:            1992-01-02T00:00:00
        time_coverage_resolution:     P1D
        time_coverage_start:          1992-01-01T00:00:00
        title:                        ECCO Atmosphere Surface Temperature, Humidi...
        geospatial_bounds_crs:        EPSG:4326
        metadata_link:                https://cmr.earthdata.nasa.gov/search/colle...
        publisher_institution:        PO.DAAC


## more like ecco procedure


```python
from ecco_podaac import apply_some_metadata_modifiers
import xarray as xr

# Get a function to apply to the xr Dataset just before write to netCDF.
func = apply_some_metadata_modifiers(f)

# Here I open a test file for the example and apply the func.
with xr.open_dataset(f) as ds:
    print(func(ds))
    
    # Then you write out the file.
```

    <xarray.Dataset>
    Dimensions:         (latitude: 360, longitude: 720, nv: 2, time: 1)
    Coordinates:
      * time            (time) datetime64[ns] 1992-01-01T12:00:00
      * latitude        (latitude) float32 -89.75 -89.25 -88.75 ... 89.25 89.75
      * longitude       (longitude) float32 -179.75 -179.25 ... 179.25 179.75
        time_step       (time) timedelta64[ns] ...
        latitude_bnds   (latitude, nv) float32 ...
        longitude_bnds  (longitude, nv) float32 ...
        time_bnds       (time, nv) datetime64[ns] ...
    Dimensions without coordinates: nv
    Data variables:
        EXFatemp        (time, latitude, longitude) float32 ...
        EXFaqh          (time, latitude, longitude) float32 ...
        EXFewind        (time, latitude, longitude) float32 ...
        EXFnwind        (time, latitude, longitude) float32 ...
        EXFwspee        (time, latitude, longitude) float32 ...
        EXFpress        (time, latitude, longitude) float32 ...
    Attributes:
        acknowledgement:              This research was carried out by the Jet Pr...
        author:                       Ian Fenty and Ou Wang
        cdm_data_type:                Grid
        comment:                      These fields are provided on a regular lat-...
        conventions:                  CF-1.8, ACDD-1.3
        creator_email:                ecco-group@mit.edu
        creator_institution:          NASA Jet Propulsion Laboratory (JPL)
        creator_name:                 ECCO Consortium
        creator_type:                 group
        creator_url:                  https://ecco.jpl.nasa.gov
        date_created:                 2020-09-02T09:13:11
        date_issued:                  2020-09-02T09:13:11
        date_metadata_modified:       2020-09-02T09:13:11
        date_modified:                2020-09-02T09:13:11
        geospatial_lat_max:           90.0
        geospatial_lat_min:           -90.0
        geospatial_lat_resolution:    0.5
        geospatial_lat_units:         degrees_north
        geospatial_lon_max:           180.0
        geospatial_lon_min:           -180.0
        geospatial_lon_resolution:    0.5
        geospatial_lon_units:         degrees_east
        history:                      Inaugural release of an ECCO "Central Estim...
        id:                           10.5067/ECG5D-ATM44
        institution:                  NASA Jet Propulsion Laboratory (JPL)
        instrument_vocabulary:        GCMD instrument keywords
        keywords:                     EARTH SCIENCE > OCEANS > OCEAN TEMPERATURE ...
        keywords_vocabulary:          NASA Global Change Master Directory (GCMD) ...
        license:                      Public Domain
        naming_authority:             gov.nasa.jpl
        platform:                     ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jaso...
        platform_vocabulary:          GCMD platform keywords
        processing_level:             L4
        product_name:                 ATM_SURFACE_TEMP_HUM_WIND_PRES_day_mean_199...
        product_time_coverage_end:    2017-12-31T12:00:00
        product_time_coverage_start:  1992-01-01T12:00:00
        product_version:              Version 4, Release 4
        program:                      NASA Physical Oceanography, Cryosphere, Mod...
        project:                      Estimating the Circulation and Climate of t...
        publisher_email:              podaac@podaac.jpl.nasa.gov
        publisher_name:               Physical Oceanography Distributed Active Ar...
        publisher_type:               institution
        publisher_url:                https://podaac.jpl.nasa.gov
        references:                   ECCO Consortium, Fukumori, I., Wang, O., Fe...
        standard_name_vocabulary:     NetCDF Climate and Forecast (CF) Metadata C...
        summary:                      This dataset provides daily average atmosph...
        time_coverage_duration:       P1D
        time_coverage_end:            1992-01-02T00:00:00
        time_coverage_resolution:     P1D
        time_coverage_start:          1992-01-01T00:00:00
        title:                        ECCO Atmosphere Surface Temperature, Humidi...
        geospatial_bounds_crs:        EPSG:4326
        metadata_link:                https://cmr.earthdata.nasa.gov/search/colle...
        publisher_institution:        PO.DAAC



```python

```
