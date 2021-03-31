# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 00:28:00 2021

@author: awi027
"""


os.chdir()

PL2019_2020 = 'https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/7811/Stages/17590/TeamStatistics/England-Premier-League-2019-2020'    
LaLiga2019_2020 = 'https://www.whoscored.com/Regions/206/Tournaments/4/Seasons/7889/Stages/17702/TeamStatistics/Spain-LaLiga-2019-2020'
Ligue1_2019_2020 = 'https://www.whoscored.com/Regions/74/Tournaments/22/Seasons/7814/Stages/17593/TeamStatistics/France-Ligue-1-2019-2020'  
SerieA_2019_2020 = 'https://www.whoscored.com/Regions/108/Tournaments/5/Seasons/7928/Stages/17835/TeamStatistics/Italy-Serie-A-2019-2020'
Bundesliga_2019_2020 = 'https://www.whoscored.com/Regions/81/Tournaments/3/Seasons/7872/Stages/17682/TeamStatistics/Germany-Bundesliga-2019-2020'

PL2019_2020_df = get_league_stats(PL2019_2020, 'chromedriver.exe', 'PL2019_2020.csv')
LaLiga2019_2020_df = get_league_stats(LaLiga2019_2020, 'chromedriver.exe', 'LaLiga2019_2020.csv')
Ligue1_2019_2020_df = get_league_stats(Ligue1_2019_2020, 'chromedriver.exe', 'Ligue1_2019_2020.csv')
SeriaA_2019_2020_df = get_league_stats(SerieA_2019_2020, 'chromedriver.exe', 'SerieA_2019_2020.csv')
Bundesliga_2019_2020_df = get_league_stats(Bundesliga_2019_2020, 'chromedriver.exe', 'Bundesliga_2019_2020.csv')
