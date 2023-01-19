
'''
Created on Dec 2, 2022

@author: aniru
'''

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches
import pandas as pd
import math





def plotOne():
    
    
    #setting up my panda dataFrame 
    data = {'key': ['000000, 0', 'basketball, 1', 'cheese, 17', 'hunter, 22','lovely1234, 268' , 'monkeyprincess, 1557', 'passportpass, 1897',
                     'testpurplemonkey, 39947', 'tweetywelcomesebastian, 144575','starwarssoccermonkey, 203685'], 
                       'color': ['#00EAFF', '#FF7F00', '#FFD400', '#6AFF00', '#BFFF00', '#FFFF00',
                                  '#AA00FF', '#0095FF', '#0040FF', '#FF0000'],
                        'Password Difficulty': [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                         'Number of guesses': [0, 1, 17, 22, 1557, 268, 1897, 39947, 144575, 203685]}
    df = pd.DataFrame(data)
    #setting up the scatter plot
    final = df.plot.scatter(x='Password Difficulty', y='Number of guesses', color=df['color'])
    #making a plot with different colors
    colorlist = zip(df['key'], df['color'])
    heading = [mpatches.Patch(color=c, label=titl) for titl, c in colorlist]
    title = df['key'] #title
    #dimensions and customizations for this key
    final.legend(heading, title, ncol=2, bbox_to_anchor=(0.7, 1))
    plt.title("difficulty vs guesses (Dictionary Size: 100)")
    plt.show()
    

def graphTwo():   
    #setting up my panda dataFrame  
    data = {'key': ['000000, 0.0', 'basketball, 0.0', 'cheese, 0.0022389', 'hunter, 0.001498','lovely1234, 0.090005' , 'monkeyprincess, 0.0146315', 'passportpass, 0.093424',
                     'testpurplemonkey, 2.632551', 'tweetywelcomesebastian, 7.90350','starwarssoccermonkey, 10.948393'], 
                       'color': ['#00EAFF', '#FF7F00', '#FFD400', '#6AFF00', '#BFFF00', '#FFFF00',
                                  '#AA00FF', '#0095FF', '#0040FF', '#FF0000'],
                        'Password Difficulty': [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                         'seconds taken to crack SHA256': [0.0, 0.0,  0.002238, 0.001498,
                                                            0.090005,
                                                            0.014631, 0.093424,
                                                             2.632551, 7.9035055, 10.948393]}
    df = pd.DataFrame(data)
    #setting up the scatter plot
    final = df.plot.scatter(x='Password Difficulty', y='seconds taken to crack SHA256', color=df['color'])
    #making a plot with different colors
    colorlist = zip(df['key'], df['color'])
    heading = [mpatches.Patch(color=c, label=titl) for titl, c in colorlist]
    title = df['key']
    #making the y axis to meet reqs
    plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])
    #dimensions and customizations for this key
    final.legend(heading, title, ncol=2, bbox_to_anchor=(0.7, 1))
    plt.title("difficulty vs time taken to crack SHA256 (Dictionary Size: 100)")
  
    
    plt.show()
    
    
    
    
def graphThree():
    #setting up my panda dataFrame 
    data = {'key': ['000000, 0.00099', 'basketball, 0.000999', 'cheese, 0.002078', 'hunter, 0.002985','lovely1234, 0.218450' , 'monkeyprincess, 0.04203', 'passportpass, 0.24436',
                     'testpurplemonkey, 6.07490', 'tweetywelcomesebastian, 20.12302','starwarssoccermonkey, 28.90400'], 
                       'color': ['#00EAFF', '#FF7F00', '#FFD400', '#6AFF00', '#BFFF00', '#FFFF00',
                                  '#AA00FF', '#0095FF', '#0040FF', '#FF0000'],
                        'Password Difficulty': [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                         'seconds taken to crack SHA512': [0.00099, 0.000999, 0.002078,
                                                            0.002985, 0.218450, 0.04203,
                                                             0.24436, 6.07490, 20.12302, 28.90400]}
    df = pd.DataFrame(data)
    #setting the color of the plots
    final = df.plot.scatter(x='Password Difficulty', y='seconds taken to crack SHA512', color=df['color'])
    
    colorlist = zip(df['key'], df['color'])
    heading = [mpatches.Patch(color=c, label=titl) for titl, c in colorlist]
    title = df['key']
    
    #customizing the key
    final.legend(heading, title, ncol=2, bbox_to_anchor=(0.7, 1))
    plt.title("difficulty vs time taken to crack SHA512 (Dictionary Size: 100)")
    
    
    
    plt.show()
#calling all the functions
plotOne()
graphTwo()
graphThree()

