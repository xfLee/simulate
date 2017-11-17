import numpy as np

iter = 1e+07
i = 1
while i <= iter:
    # Set beta2, beta3, beta4 to be 0
    sample1 = np.random.normal(loc = 1.4, scale = 1.2, size = 1)
    sigma = 1.2
    # qz is reference distribution, like Gaussian(1.4, 1.2).
    # Change default parameters to your convenience
    qz1 = 1 / (np.sqrt(2 * np.pi) * sigma**2) * np.exp(-0.5 * (sample1 - 1.4)**2 / sigma**2)
    k = 3
    u1 = np.random.uniform(low = 0, high = k * qz1, size = 1)
    
    # pz is your target distribution to sample. Substitute to your setting distribution
    pz1 =  0.3 * np.exp(-(sample1 - 0.3) ** 2) + 0.7 * np.exp(-(sample1 -2) ** 2 / 0.3)
    if pz1 >= u1:
        beta1 = sample1
    else: 
        beta1 = 0
    '''
    Codes to sample beta2, beta3, beta4 go here, similar to sample beta1. 
    Substitute parameters to corresponding settings following the explanation.
    '''
    i += 1
