import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
# print(steel_rankings.head(), wood_rankings.head())

rankings = []
ranking_year = []
# write function to plot rankings over time for 1 roller coaster here:
"""Pull Rank for a Roller Coaster"""
def roller_customer_rank(roller_coaster, roller_coaster_park):
    if len(wood_rankings[(wood_rankings['Name'] == roller_coaster)&
                         (wood_rankings['Park'] == roller_coaster_park)]) > 0:
        rankings.append(wood_rankings.Rank.loc[(wood_rankings['Name'] ==
              roller_coaster)&(wood_rankings['Park'] ==
              roller_coaster_park)].reset_index())
        ranking_year.append(wood_rankings['Year of Rank'].loc[
            (wood_rankings['Name'] == roller_coaster)&
            (wood_rankings['Park'] == roller_coaster_park)].reset_index())
        print(rankings, ranking_year)
    elif len(steel_rankings[(steel_rankings['Name'] == roller_coaster)
                        &(steel_rankings['Park'] == roller_coaster_park)]) > 0:
        rankings.append(steel_rankings.Rank.loc[
            (wood_rankings['Name'] == roller_coaster)&
            (steel_rankings['Park'] == roller_coaster_park)].reset_index())
        ranking_year.append(steel_rankings['Year of Rank'].loc[
            (steel_rankings['Name'] == roller_coaster)&
            (steel_rankings['Park'] == roller_coaster_park)].reset_index())
        print(rankings, ranking_year)
    else:
        print(roller_coaster + 'is not ranked.')
    
    plt.plot(ranking_year, rankings)
    plt.show()
    plt.clf()


roller_customer_rank('El Toro', 'Six Flags Great Adventure')











# write function to plot rankings over time for 2 roller coasters here:










plt.clf()

# write function to plot top n rankings over time here:










plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
