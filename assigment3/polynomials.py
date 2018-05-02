
class Polynomial:
    def __init__(self,poly_list):
        if type([1,2]) != type(poly_list) or len(poly_list) == 0:
            raise TypeError('Input is not a list, or an empty list')
        self.poly_list = poly_list


    def __call__(self,assert_point):
        poly_sum = 0
        for i in range(len(self.poly_list)):
            poly_sum += self.poly_list[i]*assert_point**i
        return poly_sum


    def __add__(self,p):
        if type(p) == type(1):
            self.poly_list[0] += p
            return self.poly_list
        else:
            p = p.coefficients()

            if len(self.poly_list) < len(p):
                end = p[len(self.poly_list):]
            else:
                end = self.poly_list[len(p):]

            try:
                return [i+j for i,j in zip(self.poly_list,p)] + end
            except:
                raise ArithmeticError


    def __sub__(self,p):
        if type(p) == type(1):
            self.poly_list[0] -= p
            return self.poly_list

        else:
            p = p.coefficients()
            if len(self.poly_list) < len(p):
                end = p[len(self.poly_list):]
                for i in range(len(end)):
                    end[i] *= -1
            else:
                end = self.poly_list[len(p):]

            try:
                return [i-j for i,j in zip(self.poly_list,p)] + end
            except:
                raise ArithmeticError


    def __eq__(self,p):
        p = p = p.coefficients()
        while self.poly_list[-1] == 0:
            self.poly_list = self.poly_list[:-1]
        while p[-1] == 0:
            p = p[:-1]

        if len(self.poly_list) == len(p):
            return self.poly_list == p
        else:
            return False


    def coefficients(self):
        return self.poly_list

    def degree(self):
        while self.poly_list[-1] == 0:
            self.poly_list = self.poly_list[:-1]
            if len(self.poly_list) == 0:
                return -1
        return len(self.poly_list)-1

    def __repr__(self):
        length = len(self.poly_list)
        return_string = ""

        if length ==  1:
            return_string = "%i" % (self.poly_list[0])
        elif length >= 2:
            return_string += "%i + %ix" % (self.poly_list[0],self.poly_list[1])

        for i in range(2,len(self.poly_list)):
            if self.poly_list[i] == 0:
                continue
            return_string += " + %ix^%i" % (self.poly_list[i],i)
        return return_string


    def __mul__(self,number):
        if type(number) != type(1):
            raise ArithmeticError
        return [i*number for i in self.poly_list]


    def __rmul__(self,number):
        if type(number) != type(1):
            raise ArithmeticError
        return [i*number for i in self.poly_list]


if __name__ == "__main__":
            poly1 = Polynomial([0,0,0])
            poly2 = Polynomial([2,5,5,6,2,3,0,5,0])
            poly3 = Polynomial([1])
            print (poly1.degree())
