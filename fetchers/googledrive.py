# Fetches GeoJSON from a featureServer URL

# Step 2: append ?f=pjson and parse for the `serviceItemId` value. also check `supportedQueryFormats` for `geoJSON`. possibly also save the name and id of this layer and increment the /0 to get more if any
#Step 3: fetch geoJSON data and store in cache folder (or somewhere, probably not memory). repeat and increment the _0 (layer id) at the end until you get a 400 bad request
# https://opendata.arcgis.com/datasets/{serviceItemId}_{layerID}.geojson


# it might be better to turn this into a simple file-fetcher since these are just json files and need no special sauce to access

# Data for FL and CO to use for smaller-scale testing to see what benefits this might bring for either side

# CO:
# https://docs.google.com/spreadsheets/d/1124pvazfFxhHkfFldcdrhSoh8DlpPwu0QvUskupEiG0/gviz/tq?tqx=out:csv&sheet=CO
# same thing for FL, just... with FL instead of CO at the end

# from fheisler


from models.fetcher import Fetcher
from models.storage import CacheEntry
import requests

class Googledrive(Fetcher):
	def __init__(self):
		super().__init__("googledrive")
		# designate a folder inside the cache for this fetchers files
		self.cachepath = self.cachepath.joinpath(self.name)

	def build_headers(self):
		return super().build_headers().update({})

	def auth(self):
		pass

	def fetch(self, source):
		url = source.get_url()
		"" + "/gviz/tq?tqx=out:csv" + "&sheet=CO"
		pass

	def generate_drive_url(self, url, sheet=None):
		finalurl = url + "/gviz/tq?tqx=out:csv"
		if sheet:
			finalurl += "&sheet={sheet}".format(sheet=sheet)
		return finalurl
