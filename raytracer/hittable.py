# an abstract class for a hittable object
# for anything a ray might hit and make both a sphere and a list
# of spheres just something that can be hit
#

from abc import ABC, abstractmethod
from raytracer.ray import Ray
from raytracer.vec3 import Vec3


class HitRecord:
    p: Vec3
    normal: Vec3
    t: float 


class Hittable(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def hit(self,r: Ray,ray_tmin: float,ray_tmax: float,rec:HitRecord) -> bool:
        pass 
