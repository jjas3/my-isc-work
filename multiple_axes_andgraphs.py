import matplotlib.pyplot as plt

# multiple y axis
t = range(7)
CO2 = [250,567,432,345,222,123,678]
T = [14.5,6,7,8,9,12,3]

fig, ax1=plt.subplots()

ax1.plot(t,CO2)
ax1.set_ylabel('[CO2]')

ax2 = ax1.twinx()
ax2.plot(t,T)
ax1.set_ylabel('Temo oC')
plt.show()


# multiple plots

 #1
plt.subplot(1,3,1)
plt.plot(t)
plt.ylabel('t')

 #2
plt.subplot(1,3,2)
plt.plot(CO2)


 #3
plt.subplot(1,3,3)
plt.plot(T)

plt.show()
