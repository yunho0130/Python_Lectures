# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 06:11:42 2017

@author: Yunho
"""

from ggplot import *
import pandas as pd

# Adding a Title
ggplot(mpg, aes(x='cty', y='hwy')) + \
    geom_point() + \
    ggtitle("City vs. Highway Miles per Gallon")
    
# Adding Labels
ggplot(mpg, aes(x='cty')) + \
    geom_histogram() + \
    xlab("City MPG (Miles per Gallon)") + \
    ylab("# of Obs")

# Adjusting Shapes
ggplot(mpg, aes(x='cty', y='hwy', shape='trans')) + geom_point()

# Area Chart
ggplot(meat, aes(x='date', y='beef')) + \
    geom_area() + \
    scale_x_date(labels='%Y')

# Bar Chart
ggplot(mtcars, aes(x='factor(cyl)', fill='factor(gear)')) + geom_bar()

# Boxplots
ggplot(mtcars, aes(x='factor(cyl)', y='mpg')) + geom_boxplot()

# Color Palettes
ggplot(diamonds, aes(x='carat', y='price', color='clarity')) + \
    geom_point() + \
    scale_color_brewer()
    
# Faceting Basics
df = pd.melt(meat, id_vars="date")
ggplot(diamonds, aes(x='carat', y='price', color='cut')) + \
    geom_point() + \
    facet_grid("clarity", "color")

ggplot(diamonds, aes(x='carat', y='price')) + \
    stat_smooth(method='loess') + \
    facet_grid("clarity", "cut")

# Scatter Plot
ggplot(chopsticks, aes(x='individual', y='food_pinching_effeciency')) + geom_point()

# Smoothed Line Chart
ggplot(meat, aes(x='date', y='beef')) + \
    geom_point() + \
    stat_smooth(ma=12, color='coral')
