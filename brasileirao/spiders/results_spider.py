import scrapy

LAST_ROUND = 7

class ResultsSpider(scrapy.Spider):
    name = "results"

    start_urls = [
        'https://esporte.uol.com.br/futebol/campeonatos/brasileirao/jogos/',
    ]

    def parse(self, response):
        for rodada in response.css('.rodadas .confrontos li'):
            for game in rodada.css(".confronto"):
                home_team = game.css(".partida .time1")
                away_team = game.css(".partida .time2")

                yield {
                    'home_team': home_team.css("abbr::attr(title)").extract_first().encode('utf8'),
                    'away_team': away_team.css("abbr::attr(title)").extract_first().encode('utf8'),
                    'home_score': home_team.css(".gols::text").extract_first(),
                    'away_score': away_team.css(".gols::text").extract_first(),
                    'date': game.css(".info-partida time::attr(datetime)").extract_first(),
                }
