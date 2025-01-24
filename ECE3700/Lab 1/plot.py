import matplotlib.pyplot as plt
times = [3.483790, 
3.562960 ,
7.127473,
7.214124,
8.023245,
8.105161,
8.806709,
8.892715,
9.400610,
9.487262,
9.944696,
10.0327,
10.5037,
10.5903,
11.1456,
11.2319,
11.7442,
11.8333,
12.4048,
12.4923,
13.0841,
13.1700,
13.8448,
13.9263,
14.5882,
14.6744,
15.3121,
15.3958,
15.9785,
16.0639,
16.6056,
16.6923,
17.3023,
17.3879,
18.0105,
18.0967,
18.7263,
18.8040,
19.5212,
19.6071]

diffs = []
for i in range(0, len(times), 2):
    diffs.append(times[i+1] - times[i])
    print(times[i+1], times[i])

plt.plot(diffs)
plt.title('Time Delay between GET and OK request')
plt.xlabel('Request Number')
plt.ylabel('Time Delay (s)')
plt.savefig('images/p1_3.png')
plt.show()


print(sum(diffs)/len(diffs))