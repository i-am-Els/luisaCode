
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import collections

# Gutenberg-Richter-Periodizität
#def Gutenberg_Richter(M):

    #return np.log(N) == a - b*M

# Einlesen der Daten
Daten = pd.read_csv('Eifel_katalog.txt', sep = '\s+')
cols = Daten.keys()
Daten.index.droplevel(level=0)

Daten = Daten.reset_index()
Daten.drop(Daten.columns[[0,-4,-1]],axis=1,inplace=True)
Daten.columns = cols[1:]


Magnituden = Daten['Ml'].values
#num = len(Magnituden)
#min_Magnitude = 0,10
#max_Magnitude = 3,50

bins = np.arange(0, 4.1, 1)  # Magnituden in Intervallen von 1 
bin_midpoints = (bins[:-1] + bins[1:]) / 2  # Mittelpunkte der Bins
hist, _ = np.histogram(Magnituden, bins=bins) # Anzahl der Erdbeben pro Bin

valid_bins = hist > 0 #leere Bins raus
hist = hist[valid_bins]
bin_midpoints = bin_midpoints[valid_bins]
log_num = np.log(hist)

#Magnituden_counts = collections.Counter(np.round(Magnituden, 2))
#Magnituden_sorted = sorted(Magnituden_counts.keys())
#Anzahl_sorted = [Magnituden_counts[m]for m in Magnituden_sorted]
#log_Anzahl = np.log(Anzahl_sorted)

# Ausgleichsgerade
from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(bin_midpoints, log_num)



# Darstellung
#x = Magnituden
#y = log_Anzahl
plt.figure(figsize=(8, 6))
plt.scatter(bin_midpoints, log_num, color='blue', label='Beobachtete Daten')
plt.plot(bin_midpoints, intercept + slope * bin_midpoints, color='red', label=f'Anpassung: ln(N) = {intercept:.2f} - {slope:.2f} * M')
plt.xlabel('Magnitude')
plt.ylabel('ln(N)')
plt.title('Gutenberg-Richter-Verteilung')
plt.legend()
plt.show()

