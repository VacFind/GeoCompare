from models.storage import CacheEntry
import requests
import logging
import datetime

logger = logging.getLogger(__name__)

# Since a geohash (in this implementation) is based on coordinates of longitude and latitude the distance between two geohashes reflects the distance in latitude/longitude coordinates between two points, which does not translate to actual distance, see Haversine formula. 
# https://en.wikipedia.org/wiki/Haversine_formula
# https://en.wikipedia.org/wiki/Geohash
def get_distance(x1, y1, x2, y2):
	return sqrt((y2-y1)^2+(x2-x1)^2)# no
	# use  geopy.distance.distance() instead: https://geopy.readthedocs.io/en/stable/#module-geopy.distance

def fetch_unless_cache(cachepath, url, filename, headers, force_fetch=False, cached_since=datetime.datetime.now()):
	cache_location = CacheEntry.latest_from_directory(cachepath, pattern="*"+filename)
	# if there is no existing cache, create one
	if not cache_location:
		cache_location = CacheEntry(cachepath, filename)

	if cached_since == None:
		cached_since = datetime.datetime.now()
	
	is_recent_cache = was_cached_since(cache_location.get_date_saved(), cached_since)

	if not cache_location.exists() or not is_recent_cache or force_fetch:
		logger.info("Fetching " + url)
		response = requests.get(url, headers=headers)

		if response.status_code == 200:
			cache_location.write(response.content, raw=True)
	else: 
		logger.info("resource already cached: " + url)


def was_cached_since(cache_date, since):
	return cache_date > since