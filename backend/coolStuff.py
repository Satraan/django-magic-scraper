import json
from magicscraper.models import Card
data = json.loads(open("scryfall-oracle-cards.json").read())
for line in data:
    Card(cmc=line.get("cmc"), oracleId=line.get("oracle_id"), uri=line.get("uri"), scryfallId=line.get("scryfall_id"), scryfallUri=line.get(
        "scryfall_uri"), name=line.get("name"), imageLinks=line.get("image_uris"), rarity=line.get("rarity"), typeLine=line.get("type_line"), oracleText=line.get("oracle_text"), colorIdentity=line.get("color_identity")).save()
