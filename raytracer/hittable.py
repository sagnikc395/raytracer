# an abstract class for a hittable object
# for anything a ray might hit and make both a sphere and a list
# of spheres just something that can be hit
#

from abc import ABC, abstractmethod
from raytracer.ray import Ray
from raytracer.vec3 import Vec3
from raytracer.utils import dot_product 


class HitRecord:
    p: Vec3
    normal: Vec3
    t: float
    front_face: bool

    @staticmethod 
    def set_face_normal(r: Ray, outward_normal: Vec3):
        # set the hit record normal vector
        # parameter : outward_normal is assumed to have unit length
        HitRecord.front_face = dot_product(r.direction(),outward_normal) < 0.0
        HitRecord.normal =  outward_normal if HitRecord.front_face else -outward_normal  


class Hittable(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def hit(self,r: Ray,ray_tmin: float,ray_tmax: float,rec:HitRecord) -> bool:
        pass 
