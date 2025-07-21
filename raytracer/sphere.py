#render the sphere
#
from raytracer.hittable import Hittable
from raytracer.vec3 import Vec3



class Sphere(Hittable):
    _center: Vec3
    _radius: float

    
