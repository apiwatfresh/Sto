
# Stduent ID1 653040465-3 ดังนั้น y1 = 653
# Student ID2 653040629-9 ดังนั้น y2 = 299


# x0 = 653 + 299 
a = 653 + 299 

#x1 = x0+1 = ((112*x0)%111)+2
b = ((112*(a))%111)+2

#x2 = x1+1 = ((112*x1)%111)+2
c = ((112*(b))%111)+2

# 1. รหัสและพารามิเตอร์ที่เกี่ยวข้องด้วยโปรแกรมเซจ

# 1.1 พารามิเตอร์ที่เกี่ยวข้อง
# T h i s i s a s o u r c e c o d e i n S a g e m a t h
n = 10000 # s a m p l e s i z e
p = 0.31+(c/100)
N = 10 # n u m b e r o f t r i a l i n


# 1.2 รหัสสำหรับการจำลองลำดับของตัวแปรุส่มและฮิสโทแกรม
import numpy as np
import matplotlib.pyplot as plt

X = np.random.binomial(N, p, n)  # Random sequence of Binomial RV.
minX = X.min()
maxX = X.max()
e = np.arange(minX - 0.5, maxX + 1)
np.histogram(X, bins=e)
plt.hist(X, bins=e)
plt.title("Histogram with bins = e")
plt.show()

Mn = np.mean(X)
pn = Mn / N

# 1.3 รหัสสำหรับ candidate PMF
# PMF of Binomial Distributions
from scipy import stats
from scipy.stats import binom

k = np.arange(0, N + 1)
PMF = binom.pmf(k, N, pn)
fig, ax = plt.subplots(1, 1)
ax.plot(k, PMF, 'ro', ms=12, mec='r')
ax.vlines(k, 0, PMF, colors='r', lw=4)
plt.show()