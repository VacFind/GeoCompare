
# Step 1: go through each (or just the requested) source and run it through the appropriate fetcher to save the data to cache
# (get services URL (i.e. https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/0) and list of each layer to grab)

# Step 2: go through each source again and run the desired action on the data


# step 3. run the desired action through the desired output to generate usable output files


# TODO: create "program files" that are just configs that load in all the settings for decisions made above

import json
from models.config import Config
from models.source import Source
from fetchers.arcgis import Arcgis
# import argparse

def fetch_source(source):
	fname = source.get_fetcher_name()
	fetcher = None
	if fname == 'arcgis':
		fetcher = Arcgis()
	else:
		raise ValueError('Bad message type {}'.format(message_type))
	
	fetcher.fetch(source)

if __name__ == "__main__":
	configfile = Config.from_file('./config.json')
	for source in configfile.get_sources():
		fetch_source(source)

