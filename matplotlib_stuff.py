import matplotlib.pyplot as plt

Time = range(7)
CO2_ppm = [250, 265, 272, 260, 300, 320, 389]

plt.plot(Time, CO2_ppm, 'b--', label='co2')
plt.plot(Time, CO2_ppm, 'g', label='co2(v2)')
plt.title("CO2 as a function of time (decade)")
plt.ylabel("CO2 ppm")
plt.xlabel("Time (decade)")
plt.legend(loc='upper right')
plt.show()
