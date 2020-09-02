#!/usr/bin/env python3
from sys import argv, exit
from json import load
from os.path import basename
from datetime import datetime
from pandas import read_csv
import xarray as xr

__timestamp__ = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

__datasets__ = read_csv("datasets.csv")

with open("keywords.json", "r") as f:
    __keywords__ = load(f)


def apply_some_metadata_modifiers(filename: str):
    """Return revised file metadata based on an input ECCO `filename`.
    
    This should consistently parse a filename that conforms to the 
    ECCO filename conventions and match it to a row in my metadata 
    table.

    """
    # Use filename components to find metadata row from __datasets__.
    if "_snap_" in filename:
        head, tail = filename.split("_snap_")
        head = f"{head}_snap"
    elif "_mean_" in filename:
        head, tail = filename.split("_mean_")
    else:
        raise Exception("Error: filename may not conform to ECCO V4r4 convention.")
    tail = tail.split("_ECCO_V4r4_")[1]
    
    # Get the filenames column from my table as a list of strings.
    names = __datasets__['DATASET.FILENAME']
    
    # Find the index of the row with a filename with matching head, tail chars.
    index = names.apply(lambda x: all([x.startswith(head), x.endswith(tail)]))
    
    # Select that row from __datasets__ table and make a copy of it.
    metadata = __datasets__[index].iloc[0].to_dict()
    
    # Select the gcmd keywords to match this dataset ShortName.
    for prefix, keywords in __keywords__.items():
        if metadata['DATASET.SHORT_NAME'].startswith(prefix):
            gcmd_keywords = ", ".join([" > ".join(kw.values()) for kw in keywords])
            break

    __modifiers__ = {
        #'acknowledgement': 'This research was carried out by the Jet Propulsion Laboratory, managed by the California Institute of Technology under a contract with the National Aeronautics and Space Administration.',
        #'author': 'Ian Fenty and Ou Wang',
        #'cdm_data_type': 'Grid',
        #'comment': 'These fields are provided on a regular lat-lon grid. They have been mapped to the regular lat-lon grid from the original ECCO lat-lon-cap 90 (llc90) native model grid.',
        #'conventions': 'CF-1.8, ACDD-1.3',
        #'creator_email': 'ecco-group@mit.edu',
        #'creator_institution': 'NASA Jet Propulsion Laboratory (JPL)',
        #'creator_name': 'ECCO Consortium',
        #'creator_type': 'group',
        'creator_url': 'https://ecco.jpl.nasa.gov',
        'date_created': __timestamp__,
        'date_issued': __timestamp__,
        'date_metadata_modified': __timestamp__,
        'date_modified': __timestamp__,
        'GCMD_keywords': None,
        'geospatial_bound_crs': None,
        'geospatial_bounds_crs': 'EPSG:4326',
        #'geospatial_lat_max': 90.0,
        #'geospatial_lat_min': -90.0,
        #'geospatial_lat_resolution': 0.5,
        #'geospatial_lat_units': 'degrees_north',
        #'geospatial_lon_max': 180.0,
        #'geospatial_lon_min': -180.0,
        #'geospatial_lon_resolution': 0.5,
        #'geospatial_lon_units': 'degrees_east',
        'grid_mapping_name': None,
        'history': 'Inaugural release of an ECCO "Central Estimate" solution to PO.DAAC',
        'id': metadata['DATASET.PERSISTENT_ID'].replace("PODAAC-","10.5067/"),
        #'institution': 'NASA Jet Propulsion Laboratory (JPL)',
        #'instrument_vocabulary': 'GCMD instrument keywords',
        'keywords': f'{gcmd_keywords}, ECCO, State Estimate, Estimating the Circulation and Climate of the Ocean',
        #'keywords_vocabulary': 'NASA Global Change Master Directory (GCMD) Science Keywords',
        #'license': 'Public Domain',
        'metadata_link': f"https://cmr.earthdata.nasa.gov/search/collections.umm_json?ShortName={metadata['DATASET.SHORT_NAME']}",
        #'naming_authority': 'gov.nasa.jpl',
        'nx': None,
        'ny': None,
        #'platform': 'ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1, Jason-2, CryoSat-2, SARAL/AltiKa, Jason-3, AVHRR, Aquarius, SSM/I, SSMIS, GRACE, DTU17MDT, Argo, WOCE, GO-SHIP, MEOP, ITP',
        #'platform_vocabulary': 'GCMD platform keywords',
        #'processing_level': 'L4',
        'product_name': filename,
        #'product_time_coverage_end': '2017-12-31T12:00:00',
        #'product_time_coverage_start': '1992-01-01T12:00:00',
        #'product_version': 'Version 4, Release 4',
        #'program': 'NASA Physical Oceanography, Cryosphere, Modeling, Analysis, and Prediction (MAP)',
        'project': 'Estimating the Circulation and Climate of the Ocean (ECCO)',
        #'publisher_email': 'podaac@podaac.jpl.nasa.gov',
        'publisher_insitution': None,
        'publisher_institution': 'PO.DAAC',
        #'publisher_name': 'Physical Oceanography Distributed Active Archive Center (PO.DAAC)',
        #'publisher_type': 'institution',
        'publisher_url': 'https://podaac.jpl.nasa.gov',
        'reference': None,
        #'references': 'ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M. 2020. Synopsis of the ECCO Central Production Global Ocean and Sea-Ice State Estimate (Version 4 Release 4).doi:10.5281/zenodo.3765929',
        #'standard_name_vocabulary': 'NetCDF Climate and Forecast (CF) Metadata Convention',
        'summary': metadata['DATASET.DESCRIPTION'],
        #'time_coverage_duration': 'P1M',
        'time_coverage_end': lambda x: x[:19],  #'1992-02-01T00:00:00.000000000',
        #'time_coverage_resolution': 'P1M',
        'time_coverage_start': lambda x: x[:19],  #'1992-01-01T00:00:00.000000000',
        'title': metadata['DATASET.LONG_NAME'],
        'uuid': None,
    }

    def apply_modifiers(xrds):
        """Apply attributes modifiers to ECCO dataset and its variables.

        Attributes that are commented `#` are retained with no modifications.
        Attributes that are assigned `None` are dropped.
        New attributes added to dataset.
        
        """
        # REPLACE GLOBAL ATTRIBUTES WITH NEW/UPDATED DICTIONARY.
        atts = xrds.attrs
        for name, modifier in __modifiers__.items():
            if callable(modifier):
                atts.update({name: modifier(x=atts[name])})
            elif modifier is None:
                del atts[name]
            else:
                atts.update({name: modifier})
        xrds.attrs = atts
        # MODIFY VARIABLE ATTRIBUTES IN A LOOP.
        for v in xrds.variables:
            if "gmcd_keywords" in xrds.variables[v].attrs:
                del xrds.variables[v].attrs['gmcd_keywords']
        return xrds  # Return the updated xarray Dataset.
    
    return apply_modifiers  # Return the function.


#f = "../../ecco4vr4-post-processing-for-podaac/20200831/ATM_SURFACE_TEMP_HUM_WIND_PRES_day_mean_1992-01-01_ECCO_V4r4_latlon_0p50deg.nc"
if __name__ == "__main__":
    try:
        f = argv[1]
    except IndexError as e:
        raise e  # ...
    except Exception as e:
        raise e  # ...
    else:
        fx = apply_some_metadata_modifiers(basename(f))
        with xr.open_dataset(f) as ds:
            ds = fx(ds)
            exit(print(ds))
