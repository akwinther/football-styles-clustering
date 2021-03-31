# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:27:48 2021

@author: awi027
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import os
import re 

def get_league_stats(webpage, driver_path, save_as):
    
    driver = webdriver.Chrome(executable_path = driver_path)
    
    WEBPAGE = webpage
    
    driver.get(WEBPAGE)
    
    time.sleep(3)
    
    detailed_button = driver.find_element_by_css_selector('#stage-team-stats-options > li:nth-child(4) > a')
    detailed_button.click()
    
    detailed_select_category = Select(driver.find_element_by_css_selector('#category'))
    detailed_select_subcategory = Select(driver.find_element_by_css_selector('#subcategory'))
    
    # Get all shot data (Zones + Length)
    
    detailed_select_category.select_by_visible_text('Shots')
    detailed_select_subcategory.select_by_visible_text('Zones')
    
    time.sleep(3)
    
    def get_team_rank_column(css_selector):
        teams = driver.find_elements_by_css_selector(css_selector)
        teams = [i.text for i in teams]
        teams = [i for i in teams if i != ""]
        pattern = '\d*[.]'
        teams = [re.sub(pattern, '', i).lstrip(' ') for i in teams] 
        return(teams)

    def get_rows(css_selector):
        rows = driver.find_elements_by_css_selector(css_selector)
        rows = [i.text for i in rows]
        rows = [i for i in rows if i != ""]
        return(rows)
  
    teams = get_team_rank_column('#top-team-stats-summary-content .team-link')
   
    shotsTotal = get_rows('#top-team-stats-summary-content .shotsTotal')
    OutOfBox = get_rows('#top-team-stats-summary-content .shotOboxTotal')
    SixYardBox = get_rows('#top-team-stats-summary-content .shotSixYardBox')
    PenaltyArea = get_rows('#top-team-stats-summary-content .shotPenaltyArea')
    teamRatings = get_rows('#top-team-stats-summary-content .rating')
    
    detailed_select_subcategory.select_by_visible_text('Situations')
    
    time.sleep(2)
    
    OpenPlay = get_rows('#top-team-stats-summary-content .shotOpenPlay')
    Counter = get_rows('#top-team-stats-summary-content .shotCounter')
    SetPiece = get_rows('#top-team-stats-summary-content .shotSetPiece')
    PenaltyTaken = get_rows('#top-team-stats-summary-content .penaltyTaken')
    
    # Get all dribble stats
    
    detailed_select_category.select_by_visible_text('Dribbles')
    
    time.sleep(2)
    
    dribbleLost = get_rows('#top-team-stats-summary-content .dribbleLost')
    dribbleWon = get_rows('#top-team-stats-summary-content .dribbleWon')
    dribbleTotal = get_rows('#top-team-stats-summary-content .dribbleTotal')
    
    # Get all pass stats (Length + Type)
    
    detailed_select_category.select_by_visible_text('Passes')
    
    time.sleep(2)
    
    LongBallAccurate = get_rows('#top-team-stats-summary-content .passLongBallAccurate')
    LongBallInaccurate = get_rows('#top-team-stats-summary-content .passLongBallInaccurate')
    shortPassAccurate = get_rows('#top-team-stats-summary-content .shortPassAccurate')
    shortPassInaccurate = get_rows('#top-team-stats-summary-content .shortPassInaccurate')
    
    detailed_select_subcategory.select_by_visible_text('Type')
    
    time.sleep(2)
    
    CrossAccurate = get_rows('#top-team-stats-summary-content .passCrossAccurate')
    CrossInaccurate = get_rows('#top-team-stats-summary-content .passCrossInaccurate')
    CornerAccurate = get_rows('#top-team-stats-summary-content .passCornerAccurate')
    CornerInaccurate = get_rows('#top-team-stats-summary-content .passCornerInaccurate')
    FreeKickAccurate = get_rows('#top-team-stats-summary-content .passFreekickAccurate')
    FreeKickInaccurate = get_rows('#top-team-stats-summary-content .passFreekickInaccurate')
    
    # Get attack sides
    
    AttackSidesTeamRank = get_rows('#stage-touch-channels-content .team-link')
    
    LeftSide = get_rows('.sorted .rc-r')
    Middle = get_rows('.sorted+ td .rc-r')
    RightSide = get_rows('.sorted~ td+ td .rc-r')
    
    LeftSide = [re.sub('%', '', i) for i in LeftSide] 
    Middle = [re.sub('%', '', i) for i in Middle] 
    RightSide = [re.sub('%', '', i) for i in RightSide] 
    
    WideFocus = pd.DataFrame(list(zip(AttackSidesTeamRank, LeftSide, Middle, RightSide)),
                             columns = ['Team', 'LeftSide', 'Middle', 'RightSide'])
    
    # Get defensive stats
    
    detailed_select_category.select_by_visible_text('Tackles')
    time.sleep(2)
    tacklesAttempted = get_rows('#top-team-stats-summary-content .tackleTotalAttempted')
    
    detailed_select_category.select_by_visible_text('Interception')
    time.sleep(2)
    interceptions = get_rows('#top-team-stats-summary-content .interceptionAll')
    
    detailed_select_category.select_by_visible_text('Fouls')
    time.sleep(2)
    foulsCommitted = get_rows('#top-team-stats-summary-content .foulCommitted')
    
    detailed_select_category.select_by_visible_text('Clearances')
    time.sleep(2)
    TotalClearances = get_rows('#top-team-stats-summary-content .clearanceTotal')
    
    detailed_select_category.select_by_visible_text('Blocks')
    time.sleep(2)
    ShotsBlocked = get_rows('#top-team-stats-summary-content .outfielderBlock')
    CrossesBlocked = get_rows('#top-team-stats-summary-content .passCrossBlockedDefensive')
    PassesBlocked = get_rows('#top-team-stats-summary-content .outfielderBlockedPass')
    
    # Paste together in dataframe
    
    stats = pd.DataFrame(list(zip(teams, shotsTotal, OutOfBox, SixYardBox, PenaltyArea, OpenPlay, 
                                  Counter, SetPiece, PenaltyTaken, dribbleLost, dribbleWon, dribbleTotal,
                                  LongBallAccurate, LongBallInaccurate, shortPassAccurate, shortPassInaccurate,
                                  CrossAccurate, CrossInaccurate, CornerAccurate, CornerInaccurate, 
                                  FreeKickAccurate, FreeKickInaccurate, tacklesAttempted, interceptions,
                                  foulsCommitted, TotalClearances, ShotsBlocked, CrossesBlocked, PassesBlocked,
                                  teamRatings)),
                         columns = ['Team', 'ShotsTotal', 'OutOfBox', 'SixYardBox', 'PenaltyArea', 'OpenPlay',
                                    'Counter', 'SetPiece', 'PenaltiesTaken', 'DribblesLost', 'DribblesWon', 'DribblesTotal',
                                    'LongBallAccurate', 'LongBallInaccurate', 'ShortPassAccurate', 'ShortPassInaccurate', 
                                    'CrossAccurate', 'CrossInaccurate', 'CornerAccurate', 'CornerInaccurate', 
                                    'FreeKickAccurate', 'FreeKickInaccurate', 'TacklesAttempted', 'Interceptions', 
                                    'FoulsCommitted', 'TotalClearances', 'ShotsBlocked', 'CrossesBlocked', 'PassesBlocked',
                                    'Rating'])
    
    stats = pd.merge(stats, WideFocus, on = ['Team'], how = 'inner')
    stats.to_csv(save_as, index = False) 

    return(stats)

####