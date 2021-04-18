
# Step 1: go through each (or just the requested) source and run it through the appropriate fetcher to save the data to cache
# (get services URL (i.e. https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/0) and list of each layer to grab)

# Step 2: go through each source again and run the desired action on the data


# step 3. run the desired action through the desired output to generate usable output files


# TODO: create "program files" that are just configs that load in all the settings for decisions made above

import json
from models.config import Config
from models.source import Source
from fetchers.arcgis import Arcgis
from fetchers.json import JSONFetcher
from fetchers.googledrive import Googledrive
# import argparse
import logging 
import datetime

def select_fetcher_for_source(source):
	fname = source.get_fetcher_name()
	fetcher = None
	if fname == 'arcgis':
		fetcher = Arcgis()
	elif fname == 'googledrive':
		fetcher = Googledrive()
	elif fname == 'json':
		fetcher = JSONFetcher()
	else:
		raise ValueError('Bad message type {}'.format(message_type))
	
	return fetcher

if __name__ == "__main__":
	# set up argparse
	# parser.add_argument('-v', '--verbose', action='count', default=0)



	# set up logging
	loglevel = logging.INFO # default loglevel
	# if args.verbose == 1:
	# 	loglevel = logging.INFO
	# elif args.verbose >= 2:
	# 	loglevel = logging.DEBUG
	logging.basicConfig(level=loglevel)
	logger = logging.getLogger(__name__)
	logger.info("starting up")


	configfile = Config.from_file('./config.json')
	for source in configfile.get_sources():
		logger.info("Checking source " + str(source))
		fetcher = select_fetcher_for_source(source)
		fetcher.fetch(source, if_since=(datetime.datetime.now() - datetime.timedelta(1)))

