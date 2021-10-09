
class vector:
    # vectors
    # add
    def add(vector1, vector2):
        return (vector1[0]+vector2[0],vector1[1]+vector2[1])
    # scaling 
    def scale(vector, scalar):
        return (vector[0]*scalar, vector[1]*scalar)

    # iHat, jHat chu chu, ahhh basis vectors
    # linear combinations
    # span
    # linear transformation, transformation isa fancy word for function
    # matrix vector multiplication
    def comp(matrix1, matrix2):
        i_hat=[(matrix2[0][0]*matrix1[0][0])+(matrix1[0][1]*matrix2[1][0]),(matrix1[0][0]*matrix2[0][1])+(matrix1[0][1]*matrix2[1][1])]
        j_hat=[(matrix1[1][1]*matrix2[0][0])+(matrix1[1][1]*matrix2[1][0]),(matrix1[1][0]*matrix2[0][1])+(matrix1[1][1]*matrix2[1][1])]
        return i_hat,j_hat
    


# linear transformation
class grid:
    def __init__(self,transformed_i,transformed_j) -> None:
        self.i_hat=transformed_i
        self.j_hat=transformed_j
    
    def vectorAt(self,vector):
        a=self
        return (vector[0]*a.i_hat[0]+vector[1]*a.j_hat[0],vector[0]*a.i_hat[1]+vector[1]*a.j_hat[1])





