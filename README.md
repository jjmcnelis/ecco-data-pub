# ecco-data-pub

*( this saves from [docs/README.ipynb](README.ipynb). )*


```python
from json import load
from os import chdir, listdir
from pandas import read_csv
from datetime import datetime
print("LAST RUN:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
```

    LAST RUN: 2020-08-06 06:54:42



```python
list(sorted([f"metadata/{f}" for f in listdir("../metadata") if not f.startswith(".")]))
```




    ['metadata/README.md',
     'metadata/datasets.csv',
     'metadata/platforms-instruments.json',
     'metadata/ummc',
     'metadata/ummvar',
     'metadata/variables.csv']



comma delimited table matching concept-ids to DMAS fields:


```python
read_csv('../metadata/datasets.csv')[['concept-id', 'DATASET.SHORT_NAME']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>concept-id</th>
      <th>DATASET.SHORT_NAME</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C1236799831-POCLOUD</td>
      <td>ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C1236807469-POCLOUD</td>
      <td>ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C1236807470-POCLOUD</td>
      <td>ECCO_L4_FRESH_FLUX_LLC0090GRID_SNAPSHOT_V4R4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C1236807471-POCLOUD</td>
      <td>ECCO_L4_FRESH_FLUX_LLC0090GRID_DAILY_V4R4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>C1236807472-POCLOUD</td>
      <td>ECCO_L4_FRESH_FLUX_LLC0090GRID_MONTHLY_V4R4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>60</th>
      <td>C1236807528-POCLOUD</td>
      <td>ECCO_L4_GMSL_05DEG_DAILY_V4R4</td>
    </tr>
    <tr>
      <th>61</th>
      <td>C1236807529-POCLOUD</td>
      <td>ECCO_L4_GMSL_05DEG_MONTHLY_V4R4</td>
    </tr>
    <tr>
      <th>62</th>
      <td>C1236807530-POCLOUD</td>
      <td>ECCO_L4_GMSL_LLC0090GRID_SNAPSHOT_V4R4</td>
    </tr>
    <tr>
      <th>63</th>
      <td>C1236807531-POCLOUD</td>
      <td>ECCO_L4_GMSL_LLC0090GRID_DAILY_V4R4</td>
    </tr>
    <tr>
      <th>64</th>
      <td>C1236807532-POCLOUD</td>
      <td>ECCO_L4_GMSL_LLC0090GRID_MONTHLY_V4R4</td>
    </tr>
  </tbody>
</table>
<p>65 rows × 2 columns</p>
</div>



GCMD platforms/instruments short codes reference:


```python
with open("../metadata/platforms-instruments.json", "r") as f:
    platforms_instruments = load(f)
display([p['ShortName'] for p in platforms_instruments])
```


    ['ERS-1',
     'ERS-2',
     'TOPEX/POSEIDON',
     'JASON-1',
     'OSTM/JASON-2',
     'JASON-3',
     'CRYOSAT-2',
     'SARAL',
     'ENVISAT',
     'GRACE',
     'GRACE-FO',
     'Aquarius_SAC-D',
     'METOP-A',
     'METOP-B',
     'NOAA-19',
     'NOAA-20',
     'NOAA POES',
     'DMSP 5D-2/F10',
     'DMSP 5D-2/F11',
     'DMSP 5D-2/F13',
     'DMSP 5D-2/F14',
     'DMSP 5D-2/F15',
     'DMSP 5D-2/F16',
     'DMSP 5D-3/F17',
     'DMSP 5D-3/F18',
     'MOORINGS',
     'BUOYS',
     'SEAGLIDER',
     'MODELS']



```python
#print(dumps(platforms_instruments[0], indent=2))
```

## collections


```python
list(sorted([f"../metadata/ummc/{f}"[3:] for f in listdir("../metadata/ummc") if not f.startswith(".")]))
```




    ['metadata/ummc/ECCO_L4_ATM_PROPERTIES_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_ATM_PROPERTIES_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_ATM_PROPERTIES_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_ATM_PROPERTIES_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_ATM_PROPERTIES_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_BOLUS_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_BOLUS_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_BOLUS_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_BOLUS_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_BOLUS_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_DENSE_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_DENSE_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_DENSE_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_DENSE_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_DENSE_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_FRESH_FLUX_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_FRESH_FLUX_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_FRESH_FLUX_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_GMSL_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_GMSL_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_GMSL_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_GMSL_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_GMSL_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_HEAT_FLUX_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_MIXED_LAYER_DEPTH_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_MIXED_LAYER_DEPTH_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_OBP_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_OBP_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_OBP_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_TEMP_SALINITY_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_TEMP_SALINITY_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_TEMP_SALINITY_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_VEL_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_VEL_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_VEL_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_OCEAN_VEL_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_SEA_ICE_CONCENTRATION_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_SEA_ICE_CONCENTRATION_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_SEA_ICE_CONCENTRATION_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_SSH_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_SSH_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_SSH_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4.json',
     'metadata/ummc/ECCO_L4_SURFACE_STRESS_05DEG_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_SURFACE_STRESS_05DEG_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_SURFACE_STRESS_LLC0090GRID_DAILY_V4R4.json',
     'metadata/ummc/ECCO_L4_SURFACE_STRESS_LLC0090GRID_MONTHLY_V4R4.json',
     'metadata/ummc/ECCO_L4_SURFACE_STRESS_LLC0090GRID_SNAPSHOT_V4R4.json']



## variables


```python
list(sorted([f"../metadata/ummvar/{f}"[3:] for f in listdir("../metadata/ummvar") if not f.startswith(".")]))
```




    ['metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_DAILY_V4R4-EXFaqh.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_DAILY_V4R4-EXFatemp.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_DAILY_V4R4-EXFewind.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_DAILY_V4R4-EXFnwind.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_DAILY_V4R4-EXFpress.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_DAILY_V4R4-EXFwspee.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_MONTHLY_V4R4-EXFaqh.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_MONTHLY_V4R4-EXFatemp.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_MONTHLY_V4R4-EXFewind.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_MONTHLY_V4R4-EXFnwind.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_MONTHLY_V4R4-EXFpress.json',
     'metadata/ummvar/ECCO_L4_ATM_PROPERTIES_05DEG_MONTHLY_V4R4-EXFwspee.json',
     'metadata/ummvar/ECCO_L4_BOLUS_05DEG_DAILY_V4R4-EVELSTAR.json',
     'metadata/ummvar/ECCO_L4_BOLUS_05DEG_DAILY_V4R4-NVELSTAR.json',
     'metadata/ummvar/ECCO_L4_BOLUS_05DEG_DAILY_V4R4-WVELSTAR.json',
     'metadata/ummvar/ECCO_L4_BOLUS_05DEG_MONTHLY_V4R4-EVELSTAR.json',
     'metadata/ummvar/ECCO_L4_BOLUS_05DEG_MONTHLY_V4R4-NVELSTAR.json',
     'metadata/ummvar/ECCO_L4_BOLUS_05DEG_MONTHLY_V4R4-WVELSTAR.json',
     'metadata/ummvar/ECCO_L4_DENSE_05DEG_DAILY_V4R4-DRHODR.json',
     'metadata/ummvar/ECCO_L4_DENSE_05DEG_DAILY_V4R4-PHIHYD.json',
     'metadata/ummvar/ECCO_L4_DENSE_05DEG_DAILY_V4R4-RHOAnoma.json',
     'metadata/ummvar/ECCO_L4_DENSE_05DEG_MONTHLY_V4R4-DRHODR.json',
     'metadata/ummvar/ECCO_L4_DENSE_05DEG_MONTHLY_V4R4-PHIHYD.json',
     'metadata/ummvar/ECCO_L4_DENSE_05DEG_MONTHLY_V4R4-RHOAnoma.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-EXFempmr.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-EXFevap.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-EXFpreci.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-EXFroff.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-SFLUX.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-SIacSubl.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-SIatmFW.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-SIfwThru.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-SIrsSubl.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-SIsnPrcp.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4-oceFWflx.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-EXFempmr.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-EXFevap.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-EXFpreci.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-EXFroff.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-SFLUX.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-SIacSubl.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-SIatmFW.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-SIfwThru.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-SIrsSubl.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-SIsnPrcp.json',
     'metadata/ummvar/ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4-oceFWflx.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-EXFhl.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-EXFhs.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-EXFlwdn.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-EXFlwnet.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-EXFqnet.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-EXFswdn.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-EXFswnet.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-SIaaflux.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-SIatmQnt.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-TFLUX.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-oceQnet.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4-oceQsw.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-EXFhl.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-EXFhs.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-EXFlwdn.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-EXFlwnet.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-EXFqnet.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-EXFswdn.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-EXFswnet.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-SIaaflux.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-SIatmQnt.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-TFLUX.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-oceQnet.json',
     'metadata/ummvar/ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4-oceQsw.json',
     'metadata/ummvar/ECCO_L4_MIXED_LAYER_DEPTH_05DEG_DAILY_V4R4-MXLDEPTH.json',
     'metadata/ummvar/ECCO_L4_MIXED_LAYER_DEPTH_05DEG_MONTHLY_V4R4-MXLDEPTH.json',
     'metadata/ummvar/ECCO_L4_OCEAN_TEMP_SALINITY_05DEG_DAILY_V4R4-SALT.json',
     'metadata/ummvar/ECCO_L4_OCEAN_TEMP_SALINITY_05DEG_DAILY_V4R4-THETA.json',
     'metadata/ummvar/ECCO_L4_OCEAN_TEMP_SALINITY_05DEG_MONTHLY_V4R4-SALT.json',
     'metadata/ummvar/ECCO_L4_OCEAN_TEMP_SALINITY_05DEG_MONTHLY_V4R4-THETA.json',
     'metadata/ummvar/ECCO_L4_OCEAN_VEL_05DEG_DAILY_V4R4-EVEL.json',
     'metadata/ummvar/ECCO_L4_OCEAN_VEL_05DEG_DAILY_V4R4-NVEL.json',
     'metadata/ummvar/ECCO_L4_OCEAN_VEL_05DEG_DAILY_V4R4-WVELMASS.json',
     'metadata/ummvar/ECCO_L4_OCEAN_VEL_05DEG_MONTHLY_V4R4-EVEL.json',
     'metadata/ummvar/ECCO_L4_OCEAN_VEL_05DEG_MONTHLY_V4R4-NVEL.json',
     'metadata/ummvar/ECCO_L4_OCEAN_VEL_05DEG_MONTHLY_V4R4-WVELMASS.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_DAILY_V4R4-SIarea.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_DAILY_V4R4-SIeice.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_DAILY_V4R4-SIheff.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_DAILY_V4R4-SIhsnow.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_DAILY_V4R4-SInice.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_DAILY_V4R4-sIceLoad.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_MONTHLY_V4R4-SIarea.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_MONTHLY_V4R4-SIeice.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_MONTHLY_V4R4-SIheff.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_MONTHLY_V4R4-SIhsnow.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_MONTHLY_V4R4-SInice.json',
     'metadata/ummvar/ECCO_L4_SEA_ICE_CONCENTRATION_05DEG_MONTHLY_V4R4-sIceLoad.json',
     'metadata/ummvar/ECCO_L4_SURFACE_STRESS_05DEG_DAILY_V4R4-EXFtaue.json',
     'metadata/ummvar/ECCO_L4_SURFACE_STRESS_05DEG_DAILY_V4R4-EXFtaun.json',
     'metadata/ummvar/ECCO_L4_SURFACE_STRESS_05DEG_DAILY_V4R4-oceTAUE.json',
     'metadata/ummvar/ECCO_L4_SURFACE_STRESS_05DEG_DAILY_V4R4-oceTAUN.json',
     'metadata/ummvar/ECCO_L4_SURFACE_STRESS_05DEG_MONTHLY_V4R4-EXFtaue.json',
     'metadata/ummvar/ECCO_L4_SURFACE_STRESS_05DEG_MONTHLY_V4R4-EXFtaun.json',
     'metadata/ummvar/ECCO_L4_SURFACE_STRESS_05DEG_MONTHLY_V4R4-oceTAUE.json',
     'metadata/ummvar/ECCO_L4_SURFACE_STRESS_05DEG_MONTHLY_V4R4-oceTAUN.json']




```python

```
