from src.plot_utils import vis_samples_3D, vis_samples_2D
import src.samplers as sp


def test():
    vis_samples_2D(sp.uniform_discrete_sampler_hemisphere(8, 8))
    vis_samples_2D(sp.cosine_weighted_discrete_sampler_hemisphere(8, 8))
    
    vis_samples_3D(sp.uniform_discrete_sampler_hemisphere(8, 8))
    vis_samples_3D(sp.cosine_weighted_discrete_sampler_hemisphere(8, 8))

test()
