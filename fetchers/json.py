from models.fetcher import Fetcher
from models.storage import CacheEntry
from helpers import fetch_unless_cache
import requests
import json
import logging 


class JSONFetcher(Fetcher):
	def __init__(self):
		super().__init__("json")
		self.logger = logging.getLogger(__name__)

		# designate a folder inside the cache for this fetchers files
		self.cachepath = self.cachepath.joinpath(self.name)

	def build_headers(self):
		return super().build_headers().update({})

	def auth(self):
		pass

	def fetch(self, source, force_fetch=False):
		urls = source.get_url_objects()
		
		for url in urls:
			url = url["url"]
			state = url["parameters"]["state"]
			if url["filename"]:
				filename = url["filename"]
			else:
				filename = self.add_extension(self.generate_filename(source.get_id(), state))
			self.fetch_json(url, filename, force_fetch=force_fetch)


	def fetch_json(self, url, filename, force_fetch=False):	
		fetch_unless_cache(self.cachepath, url, filename, self.build_headers(), force_fetch=force_fetch)

	def add_extension(self, name):
		return name + ".json"

	def generate_filename(self, source_id, state):
		return source_id + "_" + state
 