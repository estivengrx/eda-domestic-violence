#Bar graph

def bargraph(x, y, xtitle: str, ytitle: str, main_title: str=None, main_subtitle: str=None, graph_title: str=None, source: str=None, xlabels=None, ylabels=None, ax=None):
    """This functions takes x and y values and turn them into a nice-looking barplot from matplotlib

    Args:
        x (pandas.Series): The data that will go to x label
        
        y (pandas.Series): The data that will go to y label
        
        xtitle (str): title of x label
        
        ytitle (str): title of y label
        
        main_title (str, optional): Text of main title. Default to None. (Main title and main subtitle works better for subplots)
        
        main_subtitle (str, optional): Default to None. (Main title and main subtitle works better for subplots)
        
        graph_title (str, optional): Individual title for graphs. Default to None. 
        
        source (str, optional): Source of information where the data comes from. Default to None.
        
        xlabels (list of str, optional): What names do you want to put on every bar on the x axis. Default to None.
        
        ylabels (list of str, optional): What names do you want to put on the scale of y axis, mainly this will go None. Default to None.
        
        ax (ax, optional): It is used mainly to specify axis on subplots. Default to None.

    """
    import matplotlib.pyplot as plt
    from matplotlib import colors
    from matplotlib.ticker import MaxNLocator

    # fig, axes = plt.subplots(figsize=(13, 7), dpi=96)
    bar1 = ax.bar(x, y, width=0.6)
    ax.grid(alpha=0.5)
    
    
    # Reformat x-axis label and tick labels
    ax.set_xlabel(xtitle, fontsize=12, labelpad=10) # No need for an axis label
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.set_major_formatter(lambda s, i : f'{s:,.0f}')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_tick_params(pad=2, labelbottom=True, bottom=True, labelsize=12, labelrotation=0)
    if xlabels:
        ax.set_xticks(x, xlabels) # Map integers numbers from the series to labels list
    

    # Reformat y-axis
    ax.set_ylabel(ytitle, fontsize=12, labelpad=10)
    ax.yaxis.set_label_position("left")
    ax.yaxis.set_major_formatter(lambda s, i : f'{s:,.0f}')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_tick_params(pad=2, labeltop=False, labelbottom=True, bottom=False, labelsize=12)
    if ylabels:
        ax.set_xticks(y, ylabels) # Map integers numbers from the series to labels list

    # Add label on top of each bar
    ax.bar_label(bar1, labels=[f'{e:,.1f}' for e in y], padding=3, color='black', fontsize=8) 

    # Remove the spines
    ax.spines[['top','left','bottom','right']].set_visible(False)

    # Make the left spine thicker
    ax.spines['right'].set_linewidth(1.1)

    # Add in main title and subtitle
    ax.text(x=0.12, y=.93, s=main_title, transform=fig.transFigure, ha='left', fontsize=14, weight='bold', alpha=.8)
    ax.text(x=0.12, y=.90, s=main_subtitle, transform=fig.transFigure, ha='left', fontsize=12, alpha=.8)
    
    # Graph title
    ax.set_title(graph_title)

    # Set source text
    ax.text(x=0.1, y=0.12, s=source, transform=fig.transFigure, ha='left', fontsize=10, alpha=.7)

    # Adjust the margins around the plot area
    plt.subplots_adjust(left=None, right=None, wspace=True, hspace=0.3)

    # Set a white background
    fig.patch.set_facecolor('white')

    # Colours - Choose the extreme colours of the colour map
    colours = ["#2196f2", "#bbdefb"]

    # Colormap - Build the colour maps
    cmap = colors.LinearSegmentedColormap.from_list("colour_map", colours, N=256)
    norm = colors.Normalize(y.min(), y.max()) # linearly normalizes data into the [0.0, 1.0] interval

    # Plot bars
    ax.bar(x, y, color=cmap(norm(y)), width=0.6, zorder=2)
    

#Line graph, line plot

def linegraph(x, y, xtitle: str, ytitle: str, main_title: str=None, main_subtitle: str=None, graph_title: str=None, source: str=None, xlabels=None, ylabels=None, ax=None):
    """This functions takes x and y values and turn them into a nice-looking line plot from matplotlib

    Args:
        x (pandas.Series): The data that will go to x label
        
        y (pandas.Series): The data that will go to y label
        
        xtitle (str): title of x label
        
        ytitle (str): title of y label
        
        main_title (str, optional): Text of main title. Default to None. (Main title and main subtitle works better for subplots)
        
        main_subtitle (str, optional): Default to None. (Main title and main subtitle works better for subplots)
        
        graph_title (str, optional): Individual title for graphs. Default to None. 
        
        source (str, optional): Source of information where the data comes from. Default to None.
        
        xlabels (list of str, optional): What names do you want to put on every bar on the x axis. Default to None.
        
        ylabels (list of str, optional): What names do you want to put on the scale of y axis, mainly this will go None. Default to None.
        
        ax (ax, optional): It is used mainly to specify axis on subplots. Default to None.

    """
    import matplotlib.pyplot as plt
    from matplotlib import colors
    from matplotlib.dates import YearLocator
    from matplotlib.dates import DateFormatter
    from matplotlib.ticker import MaxNLocator

    bar1 = ax.plot(x, y, color='#53a9ed')
    ax.grid(alpha=0.5)
    
    
    # Reformat x-axis label and tick labels
    ax.set_xlabel(xtitle, fontsize=12, labelpad=10) # No need for an axis label
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.set_major_locator(YearLocator(1))      #Showing years on xlabel
    ax.xaxis.set_major_formatter(DateFormatter("%Y"))
    ax.xaxis.set_tick_params(labelbottom=True, bottom=True, labelsize=12, labelrotation=0)
    if xlabels:
        ax.set_xticks(x, xlabels) # Map integers numbers from the series to labels list


    # Reformat y-axis
    ax.set_ylabel(ytitle, fontsize=12, labelpad=10)
    ax.yaxis.set_label_position("left")
    ax.yaxis.set_major_formatter(lambda s, i : f'{s:,.0f}')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_tick_params(pad=2, labeltop=False, labelbottom=True, bottom=False, labelsize=12)
    if ylabels:
        ax.set_xticks(y, ylabels) # Map integers numbers from the series to labels list
    
    # Remove the spines
    ax.spines[['top','left','bottom','right']].set_visible(False)

    # Make the left spine thicker
    ax.spines['right'].set_linewidth(1.1)
    
    # Graph title
    ax.set_title(graph_title)

    # Add in title and subtitle
    ax.text(x=0.12, y=.93, s=main_title, transform=fig.transFigure, ha='left', fontsize=14, weight='bold', alpha=.8)
    ax.text(x=0.12, y=.90, s=main_subtitle, transform=fig.transFigure, ha='left', fontsize=12, alpha=.8)

    # Set source text
    ax.text(x=0.1, y=0.12, s=source, transform=fig.transFigure, ha='left', fontsize=10, alpha=.7)

    # Adjust the margins around the plot area
    plt.subplots_adjust(left=None, right=None, wspace=None, hspace=0.4)