import os, json
from pathlib import Path
from models.source import Source

class Config:
	def __init__(self, sources=[], actions=[]):
		self.sources = sources


	@classmethod
	def from_file(cls, filename):
		path = Path(filename)
		data = json.loads(path.read_text())
		return cls.from_dict(data)

	@classmethod
	def from_dict(cls, data):
		sources = []
		actions = []
		for source in data["sources"]:
			sources.append(Source.fromDict(source))

		if data.get("actions"):
			for action in data["actions"]:
				actions.append(Action.from_dict(action))
		
		return cls(sources=sources, actions=actions)


	def get_sources(self):
		return self.sources