import unittest
from models.source import Source

class TestSourceMethods(unittest.TestCase):

	def test_from_dict(self):
		reg = Source("id", "name", "fetcher", "parser", [], {}, parameters={"test": "true"})
		dictionary = Source.fromDict({
			"id": "id",
			"name": "name",
			"parser": "parser",
			"fetcher": "fetcher",
			"urls": [],
			"map": {},
			"parameters": {
				"test": "true"
			}
		})
		self.assertEqual(reg.id, dictionary.id)
		self.assertEqual(reg.name, dictionary.name)
		self.assertEqual(reg.fetcher_name, dictionary.fetcher_name)
		self.assertEqual(reg.urls, dictionary.urls)
		self.assertEqual(reg.parser_name, dictionary.parser_name)
		self.assertEqual(reg.parameters["test"], dictionary.get_parameter("test"))

if __name__ == '__main__':
	unittest.main()