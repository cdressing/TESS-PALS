import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("exofop_tess_tois.csv")
exofop = pd.DataFrame(data)
#print(exofop)
exofop

Period = exofop["Period (days)"]
P_Radius = exofop["Planet Radius (R_Earth)"]
Distance = (Period / 365.25)**(2/3)

plt.plot(Period, Distance, 'r.')
plt.xlabel("Period (Days)")
plt.ylabel("Distance (AU)")

plt.plot(Period, P_Radius, 'r.')
plt.xlabel("Period (Days)")
plt.ylabel("Planetary Radius (R_Earth)")
plt.xscale("log")
plt.yscale("log")

App_Mag = exofop["TESS mag"]

plt.plot(P_Radius, App_Mag, 'b.')
plt.xlabel("Planetary Radius (R_Earth)")
plt.ylabel("Apparent Magnitude (from TESS)")

S_Radius = exofop["Stellar Radius (R_Sun)"]
plt.plot(S_Radius, App_Mag, 'b.')
plt.xlabel("Stellar Radius (R_Sun)")
plt.ylabel("Apparent Magnitude (from TESS)")

Stellar_D = exofop["Stellar Distance (pc)"]
Stellar_Mag = App_Mag - 5*np.log10(Stellar_D) + 5

plt.plot(P_Radius, Stellar_Mag, 'g.')
plt.xlabel("Planetary Radius (R_Earth)")
plt.ylabel("Stellar Magnitude (Absolute)")

plt.plot(S_Radius, Stellar_Mag, 'g.')
plt.xlabel("Stellar Radius (R_Sun)")
plt.ylabel("Stellar Magnitude (Absolute)")

P_Insol = exofop["Planet Insolation (Earth flux)"]
P_Eq_Temp = exofop["Planet Eq Temp (K)"]

plt.plot(P_Insol, P_Eq_Temp, 'r.')
plt.xlabel("Planet Insolation (Earth Flux)")
plt.ylabel ("Planet Eq Temperature (K)")