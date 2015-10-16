__author__ = 'Dandelion'


class Fraction:
    """
    Main class for performing actions on the fraction. 
    Stores fraction as nominator and denominator and computes representation in different notations
    """
    def __init__(self, nominator, denominator):
        self.int = nominator / denominator
        self.frac = nominator % denominator
        self.denom = denominator
        self.rest_history = []

    def represent(self, notation):
        """
        Represent fraction in given notation.
        
        :param int notation: Power of notation that fraction should be represented in. 
        :return: Nothing is returned. 
        
        Method separately represent integer (:py:meth:`._repr_int()`) and fractional (:py:meth:`._repr_frac()`) part. After that method combines all representations into the result one and prints it. Each character of representation looks like `#<val>`, where `<val>` is digit in given notation.
        """
        int_digits = self._repr_int(notation)
        frac_digits = self._repr_frac(notation)
        int_str = "".join(map(lambda x: '#' + str(x), int_digits))  
        # non-periodic fractional part
        frac_str = "".join(map(lambda x: '#' + str(x), frac_digits[0]))
        if frac_digits[1]:
            # periodic fractional part
            frac_str += "(" + "".join(map(lambda x: '#' + str(x), frac_digits[1])) + ")"
        print int_str + '.' + frac_str

    def _repr_int(self, notation):
        """
        Represent integer part of the fraction in the given notation.

        :param int notation: Power of notation that fraction should be represented in.
        :return: List of digits representing integer part of the fraction.

        Representing is performing by algorithm of consequent divisions and taking rests.
        """
        int_digits = [self.int % notation]
        integer = self.int / notation
        while integer:
            int_digits.append(integer % notation)
            integer /= notation
        int_digits.reverse()
        return int_digits
    
    def _repr_frac(self, notation):
        """
        Represent fractional part of the fraction in the given notation.
        
        :param int notation: Power of notation that fraction should be represented in. 
        :return: Pair of lists of digits representing fractional part of the fraction. The first one represents non-periodical fractional part. The last one represents period of fraction.
        
        Representing is performing by improved algorithm of consequent multiplications. The difference from the classical algorithm of converting finite decimal fraction to the other notation is that fraction can be infinite. As soon as fraction is represented by it's nominator and denominator (nominator < denominator), the classical algorithm can be improved. During every step of algorithm we need multiply nominator and power of notation and then divide it by denominator. Quotient is the computed digit of representation, rest is used in further computations. The whole history of rests should be stored. Process is finished when current rest is 0 (in this case fractional part in given notation is finite) or it is stored in history of rests (in this case fractional part is infinite with digits from rest found earlier to rest found in previous step as period).
        
        Checks of continuing process is made by :py:meth:`._comp_over()`.
        """
        rest = self.frac
        frac_digits = []
        while not self._comp_over(rest):
            frac_digits.append(rest * notation / self.denom)
            rest = rest * notation % self.denom
        if not rest:
            # fraction is finite
            return (frac_digits, [])
        else:
            nonp_digits = frac_digits[:self.rest_history.index(rest)]
            p_digits = frac_digits[self.rest_history.index(rest):]
            return (nonp_digits, p_digits)
        
    def _comp_over(self, cur_rest):
        """
        Check if process of computing representation of fractional part is over or not.
        
        :param int cur_rest: Current rest in computation process.
        :return: ``True`` if process is over and ``False`` otherwise.
        
        Method is used in :py:meth:`._repr_frac()` to control computation process.
        
        Computing is over when current rest is 0 (in this case fractional part in given notation is finite) or is met earlier (in this case fractional part has period and it's finished by rest computed during previous step).
        """
        if not cur_rest or cur_rest in self.rest_history:
            return True
        else:
            self.rest_history.append(cur_rest)
            return False
    

def input_int(welcome):
    """
    Input integer value from console.

    :param str welcome: String that is shown in console to specify input value.
    :return: Integer value extracted from input string.

    In case of any error while extracting floats from input string error message is shown and `input_int()` welcomes to try input again.
    Input is retried until it is successful.
    """
    while True:
        input_str = raw_input(welcome)
        try:
            return int(input_str)
        except ValueError as er:
            print "Invalid input string:", er.message

            
def main():
    """
    The main function that get nominator, denominator and power of notation from console and then print representation of the fraction.
    """
    nom = input_int("Input nominator: ")
    denom = input_int("Input denominator: ")
    notation = input_int("Input power of notation: ")
    frac = Fraction(nom, denom)
    frac.represent(notation)
    

if __name__ == "__main__":
    main()
