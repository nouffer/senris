from pathlib import Path
from django.contrib.gis.utils import layermapping
from .models import Incident

incident_mapping = {
    'name':'org_name',
    'geom':'LINESTRING'
}

incident_shp = Path(__file__).resolve().parent / "sri-lanka" / "roads.shp"

def run(verbose=True):
    lm=layermapping(Incident, str(incident_shp), incident_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)