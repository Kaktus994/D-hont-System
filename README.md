# D-hont-System

Made with PyQt5. This GUI app is used to calculate the number of mandates each party won based on the number of votes (<a href="https://en.wikipedia.org/wiki/D%27Hondt_method"> "D'Hondt method" </a>) as well as other factors such as:

1. is party a minority party,
2. does the party have enough votes to pass the census,
3. party rank.

Rules for minority party follow ones which was applied during the 2020. Parliament elections in Serbia. If minority party does not have enough votes to pass the census it's "score" is multiplied with "1.35". This, modified, number of votes is then taken into calculation.
If you want to select a party to be a minority you need to tick the checkbox by its name field.

If two(or more) parties have the same number of votes the one with highest rank number (first applied for the elections) will get the mandate.

Before calculating and plotting the results make sure to hit the LOCK button.
