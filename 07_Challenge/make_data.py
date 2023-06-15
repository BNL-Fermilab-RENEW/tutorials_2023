
# The challenge itself is a binary classification problem with stars and galaxies 


import numpy as np 
from deepbench.astro_object import StarObject, GalaxyObject

n_stars = ''
n_galaxies = ''

noise_level = ''
image_size = ()

data = np.zeros((2, n_stars+n_galaxies, image_size[0], image_size[1]))

for n in range(n_stars): 

    radius = ""
    center_x = ""
    center_y = ""

    star = StarObject(
                image_dimensions=image_size,
                noise=noise_level,
                radius=radius
    ).create_object(center_x=center_x, center_y=center_y)

for n in range(n_galaxies): 
    galaxy = GalaxyObject(
            radius=25,
        noise_level=noise_level,
        ellipse=random.uniform(0.1, 0.9),
        theta=random.uniform(-1.5, 1.5),
    ).create_object(center_x=center_x, center_y=center_y)




