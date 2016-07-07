# LeagueOfLegendsHeatMap
Using the Riot API to create a heatmap of player's movement during a League of Legends map

The purpose of this project is to aggregate data from my League of Legends matches to create a 
heatmap to show the most traveled routes on the map. I came up with this idea when playing a character 
called Teemo who can set invisible traps around the map. This traps are activated and damage an enemy when they walk over them. 
By creating a heatmap of the players position during the game I hope to find the best places to set these traps.

Uses python to scrape the data from the Riot API. For a given player ID it's possible to get data for every game they have played. The player's position data is recorded once a minute for for each game. Through aggregating data from multiple games it's possible to get enough information for a heatmap. The data is processed using R and the visualization is created using d3.js.
