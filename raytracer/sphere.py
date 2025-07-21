#render the sphere
#
from raytracer.hittable import Hittable , HitRecord
from raytracer.vec3 import Vec3
from raytracer.ray import Ray
from raytracer.utils import dot_product 
import math 


class Sphere(Hittable):
    
    def __init__(self,center : Vec3, radius: float):
        self.center = center
        self.radius = radius 

    def hit(self,r : Ray ,ray_tmin : float,ray_tmax: float,rec: HitRecord) -> bool:
        oc = self.center - r.origin()
        a = r.direction()._length_squared()
        h = dot_product(r.direction(),oc)
        c = oc._length_squared() - (self.radius * self.radius)

        discriminant = (h*h) - (a*c)
        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)

        # find th nearest root that lies in acceptable range
        root = (h - sqrtd) / a
        if (root <= ray_tmin or ray_tmax <= root):
            root = (h + sqrtd) / a
            if (root <= ray_tmin or ray_tmax <= root):
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        rec.normal = (rec.p - self.center) / self.radius

        return True
        
