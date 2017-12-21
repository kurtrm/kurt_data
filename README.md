[![Build Status](https://travis-ci.org/kurtrm/kurt_data.svg?branch=master)](https://travis-ci.org/kurtrm/kurt_data) [![Coverage Status](https://coveralls.io/repos/github/kurtrm/kurt_data/badge.svg?branch=master)](https://coveralls.io/github/kurtrm/kurt_data?branch=master)

# Sources of Data on Kurt
Repository to house scripts for personal data analysis.

## Fitbit Data

The function to pull and refresh tokens has been implemented, no data has been accumulated yet.
I have to determine which data I care about, pull it, and look at it. More to come.

## Communication Graph

Graph databases are growing in popularity. While searching for possible sources of personal information, I discovered my cell phone bill provides a fairly comprehensive and detailed source of calls, text, and data usage.
I also realized that this is a perfect candidate source to both visualize and store in a graph data structure.

My goals are to:

- [x] Parse each bill to retrieve the data. (Still requires testing.)
- [x] Plug the data into a DataFrame.
- [x] Analyze which columns need to be discarded and which are useful.
- [x] Research existing graph implementations and databases.
- [ ] Determine perspectives on the data and how to present each layer.
- [ ] Refactor the graph to incorporate more advanced Pythonic tools.

To do:

- ~~Stick to one type for each node. Right now you change between a string and a list, which clutters the code.~~
- ~~Define __repr__ for relationship and node classes.~~
- Determine useful attributes that can be placed on these nodes besides their properties.
- Implement a CLI.
- Refactor tables as described in notebook.
- Put it into an existing graph database.
- ~~Make various visualizations using Matplotlib, networkx (See notebook for more information.)~~ D3.js

## Google Maps Location History

Plans to explore this are still in development.
