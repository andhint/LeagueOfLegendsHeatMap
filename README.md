# LeagueOfLegendsHeatMap
Using the Riot API to create a heatmap of player's movement during a League of Legends map

The purpose of this project is to aggregate data from my League of Legends matches to create a 
heatmap to show the most traveled routes on the map. I came up with this idea when playing a character 
called Teemo who can set invisible traps around the map. This traps are activated and damage an enemy when they walk over them. 
By creating a heatmap of the players position during the game I hope to find the best places to set these traps.

As of 5/18/16 I have the script made for scraping data from a recent game. The API only stores data from the last 10 games played so 
I run the script after each game I play and add the data to a master file. Once I have a enough data I plan to make a heatmap using D3.js. 
Here is an example of a scatter plot of the data overlaid on an image of the map. http://jsfiddle.net/utwvqsrg/512/
