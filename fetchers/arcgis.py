# Fetches GeoJSON from a featureServer URL

# Step 2: append ?f=pjson and parse for the `serviceItemId` value. also check `supportedQueryFormats` for `geoJSON`. possibly also save the name and id of this layer and increment the /0 to get more if any
#Step 3: fetch geoJSON data and store in cache folder (or somewhere, probably not memory). repeat and increment the _0 (layer id) at the end until you get a 400 bad request
# https://opendata.arcgis.com/datasets/{serviceItemId}_{layerID}.geojson


# it might be better to turn this into a simple file-fetcher since these are just json files and need no special sauce to access

from models.fetcher import Fetcher
from models.storage import CacheEntry
from helpers import fetch_unless_cache
import requests
import json
import logging 


class Arcgis(Fetcher):
	def __init__(self):
		super().__init__("arcgis")
		self.logger = logging.getLogger(__name__)

		# designate a folder inside the cache for this fetchers files
		self.cachepath = self.cachepath.joinpath(self.name)

	def build_headers(self):
		return super().build_headers().update({})

	def auth(self):
		pass

	def fetch(self, source):
		urls = source.get_url_objects()
		
		for url_parts in urls:
			serviceItemID = url_parts["parameters"]["serviceItemId"]
			layerID = int(url_parts["parameters"]["layerId"])
			url = self.generate_geojson_url(serviceItemID, layerID=layerID)
			filename = self.add_extension(url_parts["filename"])
			self.fetch_geojson(url, filename)

	# use me if a baseurl is provided instead of a serviveitemid and layer
	def get_info(self, url):
		url = url + "?f=pjson"
		try:
			response = requests.get(url, headers=self.build_headers())	
			# print(vars(response))
			if response.status_code == 200:
				data = json.loads(response.content.decode())
		except requests.HTTPError as e:
			print("HTTP error while requesting " + url)

		return data

	def fetch_geojson(self, url, filename, force_fetch=False):	
		fetch_unless_cache(self.cachepath, url, filename, self.build_headers(), force_fetch=force_fetch)

	def add_extension(self, name):
		return name + ".geojson"

	def generate_geojson_url(self, serviceItemID, layerID=0):
		url = "https://opendata.arcgis.com/datasets/{serviceItemID}_{layerID}.geojson"
		return url.format(serviceItemID=serviceItemID, layerID=layerID)
