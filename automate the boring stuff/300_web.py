#%% [markdown]

# https://www.codevoila.com/post/45/open-web-browser-window-or-new-tab-with-python


import webbrowser as wb
a_website = "https://www.google.com"

#%% [markdown]

wb.open('http://google.de')
wb.open_new(a_website) # should open a new window, does not work for edge

#%% [markdown]


# wb._browsers[0]
# wb._browsers[1]
# wb.register('mychrome', None, wb.MacOSXOSAScript('Google Chrome'), -1)

#%% [markdown]
wb._browsers
wb.get('firefox').open_new_tab(a_website)

# Open url in a new window of the default browser, if possible
