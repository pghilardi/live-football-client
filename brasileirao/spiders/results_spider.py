import scrapy

import scrapy.selector
from brasileirao.items import BrasileiraoItem
import hashlib

class ResultsSpider(scrapy.Spider):
    name = "results"

    start_urls = [
        'https://esporte.uol.com.br/futebol/campeonatos/brasileirao/jogos/',
    ]

    def parse(self, response):
        actual_round = 0

        for rodada in response.css('.rodadas .confrontos li'):
            actual_round += 1

            for game in rodada.css(".confronto"):
                home_team = game.css(".partida .time1")
                away_team = game.css(".partida .time2")

                item = BrasileiraoItem()
                item['rodada'] = actual_round
                item['home_team'] = home_team.css("abbr::attr(title)").extract_first().encode('utf8')
                item['away_team'] = away_team.css("abbr::attr(title)").extract_first().encode('utf8')
                item['home_score'] = home_team.css(".gols::text").extract_first()
                item['away_score'] = away_team.css(".gols::text").extract_first()

                item['date'] = game.css(".info-partida time::attr(datetime)").extract_first()

                id = item['home_team'] + item['away_team']
                item['id'] = hashlib.md5(id).hexdigest()

                yield item
