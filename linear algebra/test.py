from linear import vector as vc
from linear import grid as gd

# print(vc.add([1,2],[3,-1]))
# print(vc.scale([1,2],2))

# i_hat tranformation, j_hat transformation
plane=gd([1,2],[3,1])
# print(plane.vectorAt([-1,2]))
plane.comp([[5,7],[3,-3]],[[-3,2],[1,5]])