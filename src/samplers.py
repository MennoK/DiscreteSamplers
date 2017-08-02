import numpy as np


def uniform_discrete_sampler_hemisphere(dim_u1, dim_u2):
    samples = np.zeros((dim_u1*dim_u2, 3))
    step_u1 = 1.0 / dim_u1
    step_u2 = 1.0 / dim_u2

    for i in range(dim_u1):
        for j in range(dim_u2):

            x = i + dim_u1 * j

            u1 = (i * step_u1 + ((i + 1) * step_u1 - i * step_u1) / 2)
            u2 = (j * step_u2 + ((j + 1) * step_u2 - j * step_u2) / 2)

            cos_theta = u1
            sin_theta = np.sqrt(np.maximum(0.0, 1.0 - u1 * u1))
            phi = 2 * np.pi * u2

            samples[x] = np.array([np.cos(phi) * sin_theta, np.sin(phi) * sin_theta, cos_theta], dtype=np.float64)

    return samples


def cosine_weighted_discrete_sampler_hemisphere(dim_u1, dim_u2):
    samples = np.zeros((dim_u1*dim_u2, 3))
    step_u1 = 1.0 / dim_u1
    step_u2 = 1.0 / dim_u2

    for i in range(dim_u1):
        for j in range(dim_u2):

            x = i + dim_u1 * j

            u1 = (i * step_u1 + ((i + 1) * step_u1 - i * step_u1) / 2)
            u2 = (j * step_u2 + ((j + 1) * step_u2 - j * step_u2) / 2)

            cos_theta = np.sqrt(1 - u1)
            sin_theta = np.sqrt(u1)
            phi = 2 * np.pi * u2

            samples[x] = np.array([np.cos(phi) * sin_theta, np.sin(phi) * sin_theta, cos_theta], dtype=np.float64)

    return samples

