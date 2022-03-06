"""
Created on Sat Feb 24 16:20:17 2022

@author: mike_
"""
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
# print(steel_rankings.head(), wood_rankings.head())

rankings = []
ranking_year = []
# write function to plot rankings over time for 1 roller coaster here:
def one_roller_customer_rank(roller_coaster, roller_coaster_park, material):
    """
    Parameters
    ----------
    roller_coaster : TYPE
        DESCRIPTION.
    roller_coaster_park : TYPE
        DESCRIPTION.
    material : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    """
    if material == 'wood':
        roller_coaster_rank = wood_rankings[(wood_rankings['Name'] ==
            roller_coaster)& (wood_rankings['Park'] == roller_coaster_park)]
    elif material =='steel':
        roller_coaster_rank = steel_rankings[(wood_rankings['Name']
             == roller_coaster)& (wood_rankings['Park'] == roller_coaster_park)]
    else:
        print(roller_coaster + 'is not ranked.')
    x_values = roller_coaster_rank['Year of Rank']
    y_values = roller_coaster_rank['Rank']
    ax_1 = plt.subplot()
    plt.plot(range(len(x_values)), y_values)
    ax_1.invert_yaxis()
    ax_1.set_xticks(range(len(x_values)))
    ax_1.set_xticklabels(x_values)
    plt.xlabel('Years')
    plt.ylabel('Rank')
    plt.title(roller_coaster + ' Rank by Year')
    plt.show()



one_roller_customer_rank('El Toro', 'Six Flags Great Adventure','wood')
plt.clf()

# 4
# Create a function that compares Roller Coasters in the same graph
def two_coaster(coaster_1, park_1, coaster_2, park_2, material):
    """
    Parameters
    ----------
    coaster_1 : TYPE
        DESCRIPTION.
    park_1 : TYPE
        DESCRIPTION.
    coaster_2 : TYPE
        DESCRIPTION.
    park_2 : TYPE
        DESCRIPTION.
    material : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if material == 'wood':
        roller_coaster_1_rank = wood_rankings[(wood_rankings['Name'] ==
            coaster_1) & (wood_rankings['Park'] == park_1)]
        roller_coaster_2_rank = wood_rankings[(wood_rankings['Name'] ==
            coaster_2) & (wood_rankings['Park'] == park_2)]
    else:
        roller_coaster_1_rank = steel_rankings[(wood_rankings['Name']
             == coaster_1) & (wood_rankings['Park'] == park_1)]
        roller_coaster_2_rank = steel_rankings[(wood_rankings['Name']
             == coaster_2) & (wood_rankings['Park'] == park_2)]
    #print(roller_coaster_1_rank, roller_coaster_2_rank)
    
    # Find values for x and y
    coaster_1_x_values = roller_coaster_1_rank['Year of Rank']
    coaster_1_y_values = roller_coaster_1_rank['Rank']
    coaster_2_x_values = roller_coaster_2_rank['Year of Rank']
    coaster_2_y_values = roller_coaster_2_rank['Rank']
    
    # plot coasters
    plt.plot(range(len(coaster_1_x_values)),coaster_1_y_values, '-', color='red', label=coaster_1)
    ax_1 = plt.subplot()
    ax_1.invert_yaxis()
    ax_1.set_xticks(range(len(coaster_1_x_values)))
    ax_1.set_xticklabels(coaster_1_x_values)
    plt.xlabel('Years')
    plt.ylabel('Rank')
    plt.title(coaster_1 + " and " + coaster_2 + ' Ranked by Year')
    plt.plot(range(len(coaster_2_x_values)),coaster_2_y_values, '--', color='blue',label=coaster_2)
    plt.legend()
    plt.show()
    

two_coaster('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 
            'Lake Compounce', 'wood')

plt.clf()

# write function to plot top n rankings over time here:
def ranking_coasters(n, material):
    """
    Parameters
    ----------
    rank : TYPE
        DESCRIPTION.
    material : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    """
    if material == 'wood':
        top_nth_ranks = wood_rankings[wood_rankings['Rank'] <= n]
    else:
        top_nth_ranks = steel_rankings[steel_rankings['Rank'] <= n]
    #print(top_nth_ranks)
    ax= plt.subplot()
    for coaster in set(top_nth_ranks['Name']):
        coaster_rankings = top_nth_ranks[top_nth_ranks['Name'] == coaster]
        ax.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'], label=coaster)
    plt.show()
    #x_values = top_nth_rank['Years in Rank']

ranking_coasters(5, 'wood')







plt.clf()

# 6
# load roller coaster data
roller_coasters_data = pd.read_csv('roller_coasters.csv')


# write function to plot histogram of column values here:
def roller_coaster_hist(df,column):
    """
    

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.
    column : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    plt.hist(df[column].dropna())
    plt.title('Roller Coaster Data')
    plt.xlabel(column)
    plt.ylabel('Quanity')
    plt.show()
    plt.clf()

# Create histogram of roller coaster speed
roller_coaster_hist(roller_coasters_data,'speed')
# Create histogram of roller coaster length
roller_coaster_hist(roller_coasters_data,'length')
# Create histogram of roller coaster number of inversions
roller_coaster_hist(roller_coasters_data,'num_inversions')
# Create a function to plot histogram of height values
heights = roller_coasters_data[roller_coasters_data['height'] <= 140] 
roller_coaster_hist(heights,'height')

# write function to plot inversions by coaster at a park here:

def park_num_inversions(df,park):
    number_inversions = df[df['park'] == park]
    y_values = number_inversions['num_inversions']
    x_values = number_inversions['name']
    ax_1 = plt.subplot()
    plt.plot(range(len(x_values)), y_values)
    plt.title('Number of Inversions for ' + park)
    plt.xlabel('Roller Coaster')
    plt.ylabel('Number of Inversions')
    ax_1.set_xticks(range(len(x_values)))
    ax_1.set_xticklabels(x_values,rotation=45,ha='right')
    plt.show()

plt.clf()

park_num_inversions(roller_coasters_data, 'Port Aventura')

# write function to plot pie chart of operating status here:
def operating_status(df):
   pie_values = [len(df[df['status']=='status.operating']),len(df[df['status']=='status.closed.definitely'])]
   pie_labels = ['Operating','Closed Definitely']
   ax_1 = plt.subplot()
   plt.pie(pie_values, labels=pie_labels, autopct='%0.1f%%')
   plt.title('Operation Status')
   ax_1.set_aspect('equal')
   plt.show()
# Create pie chart of roller coasters
operating_status(roller_coasters_data)

plt.clf()

# write function to create scatter plot of any two numeric columns here:
def coaster_scatter_plot(df, column_1, column_2):
    plt.scatter(df[column_1],df[column_2], color='blue')
    plt.title('{} vs. {}'.format(column_1, column_2))
    plt.xlabel(column_1)
    plt.ylabel(column_2)
    plt.show()
    
coaster_scatter_plot(roller_coasters_data,'speed','num_inversions')

plt.clf()
