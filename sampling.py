import numpy as np

iter = 1e+07
i = 0
while i <= iter:
    beta1 = np.random.normal(loc = 1.4, scale = 1.2, size = 1)
    sigma = 1.2
    qz1 = 1 / (np.sqrt(2 * np.pi) * sigma**2) * np.exp(-0.5 * (beta1 - 1.4)**2 / sigma**2)
    k = 3
    u1 = np.random.uniform(low = 0, high = k * qz1, size = 1)

    pz1 =  0.3 * np.exp(-(beta1 - 0.3) ** 2) + 0.7 * np.exp(-(beta1 -2) ** 2 / 0.3)
    sample1 = beta1[pz1 >= u1]
    '''
    Codes to sample beta2, beta3, beta4 go here. Substitute parameters to corresponding settings.
    '''
    i += 1