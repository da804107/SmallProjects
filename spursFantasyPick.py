#python3 install nba_api
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.endpoints import teamplayerdashboard

team = 'San Antonio Spurs'
season_year = '2023-24'
season_type = 'Regular Season'

# Get Spurs team info
team_info = teams.find_teams_by_full_name(team)[0]
cur_team_id = team_info['id']

# Fetch current roster for the Spurs using the team ID
roster = commonteamroster.CommonTeamRoster(team_id=cur_team_id).get_data_frames()[0]
#print(roster.columns)
#print(roster[['PLAYER', 'PLAYER_ID', 'POSITION', 'HEIGHT', 'WEIGHT', 'SCHOOL']])

#key stats for good fantasy picks: PPG, Rebounds & Assists, Steals & Blocks, FG%, and Turnovers

player_stats = teamplayerdashboard.TeamPlayerDashboard(
    team_id=cur_team_id,
    season=season_year,
    season_type_all_star=season_type
).get_data_frames()[1]
#print(player_stats.columns)
#print(player_stats[['PLAYER_NAME', 'GP', 'PTS', 'REB', 'AST', 'STL', 'BLK']])

player_stats['Fantasy_Score'] = player_stats['PTS'] + player_stats['REB'] + player_stats['AST'] + player_stats['STL'] + player_stats['BLK']

# Sort and select the top 3 players
top_3_players = player_stats.sort_values(by='Fantasy_Score', ascending=False).head(3)

print(f"The following are the top three {team} picks based on {season_year} {season_type} season is:")

# Print the top 3 players
for idx, player in top_3_players.iterrows():
    print(f"Player: {player['PLAYER_NAME']}, Fantasy Score: {player['Fantasy_Score']}")
