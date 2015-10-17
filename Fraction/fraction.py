__author__ = 'Dandelion'


class Fraction:
    """
    Main class for performing actions on the fraction. 
    Stores fraction as numerator and denominator and computes representation in different notations
    """
    def __init__(self, numerator, denominator):
        if numerator * denominator < 0:
            self.sign = '-'
        else:
            self.sign = ''
        self.int = abs(numerator) / abs(denominator)
        self.frac = abs(numerator) % abs(denominator)
        self.denom = abs(denominator)
        self.rem_history = []

    def represent(self, notation):
        """
        Represent fraction in given notation.
        
        :param int notation: Notation base that fraction should be represented in.
        :return: Nothing is returned. 
        
        Method separately represent integer (:py:meth:`._repr_int()`) and fractional (:py:meth:`._repr_frac()`) part.
        After that method combines all representations into the result one and prints it. Each character of
        representation looks like `#<val>`, where `<val>` is digit in given notation.
        """
        int_digits = self._repr_int(notation)
        frac_digits = self._repr_frac(notation)
        int_str = "".join(map(lambda x: '#' + str(x), int_digits))  
        # non-periodic fractional part
        if frac_digits[1]:
            # periodic fractional part
            frac_str = "(" + "".join(map(lambda x: '#' + str(x), frac_digits[1])) + ")"
        else:
            frac_str = ""
        if not (frac_digits[0] or frac_str):
            frac_str = '#0'
        else:
            frac_str = "".join(map(lambda x: '#' + str(x), frac_digits[0])) + frac_str
        print self.sign + int_str + '.' + frac_str

    def _repr_int(self, notation):
        """
        Represent integer part of the fraction in the given notation.

        :param int notation: Notation base that fraction should be represented in.
        :return: List of digits representing integer part of the fraction.

        Algorithm of consequent divisions and taking remainders is used.
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
        
        :param int notation: Notation base that fraction should be represented in.
        :return: Pair of lists of digits representing fractional part of the fraction. The first one represents non-periodical fractional part. The last one represents period of fraction.
        
        Improved algorithm of consequent multiplications is used. The difference from the classical algorithm of
        converting finite decimal fraction to the other notation is that fraction can be infinite. As soon as fraction
        is represented by it's numerator and denominator (numerator < denominator), the classical algorithm can be
        improved. During every step of algorithm we need multiply numerator and notation base and then divide it by
        denominator. Quotient is the computed digit of representation, remainder is used in further computations.
        The whole history of remainders should be stored. Process is finished when current remainder is 0 (in this case
        fractional part in given notation is finite) or it is stored in history of remainders (in this case fractional
        part is infinite with digits from rest found earlier to rest found in previous step as period).
        
        Checks of continuing process is performed by :py:meth:`._comp_over()`.
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
            nonp_digits = frac_digits[:self.rem_history.index(rest)]
            p_digits = frac_digits[self.rem_history.index(rest):]
            return (nonp_digits, p_digits)
        
    def _comp_over(self, cur_rem):
        """
        Check if process of computing representation of fractional part is over or not.
        
        :param int cur_rem: Current rest in computation process.
        :return: ``True`` if process is over and ``False`` otherwise.
        
        Method is used in :py:meth:`._repr_frac()` to control computation process.
        
        Computing is over when current remainder is 0 (in this case fractional part in given notation is finite) or is
        met earlier (in this case fractional part has period and it's finished by remainder computed during previous
        step).
        """
        if not cur_rem or cur_rem in self.rem_history:
            return True
        else:
            self.rem_history.append(cur_rem)
            return False
    

def input_int(welcome, cond, cond_str):
    """
    Input integer value from console.

    :param str welcome: String that is shown in console to specify input value.
    :param function cond: Checking function of 1 argument that returns ``True`` if extracted value is acceptable and ``False`` otherwise.
    :param str cond_str: String that is shown in console in case of checking function failure.
    :return: Integer value extracted from input string.

    In case of any error while extracting values from input string error message is shown and `input_int()` welcomes to
    try input again. Input is retried until it is successful.
    """
    while True:
        input_str = raw_input(welcome)
        try:
            value = int(input_str)
            if cond(value):
                return value
            else:
                print "Invalid input string:", cond_str
        except ValueError as er:
            print "Invalid input string:", er.message

            
def main():
    """
    The main function that get numerator, denominator and notation base from console and then print representation of
    the fraction.
    """
    while True:
        num = input_int("Input numerator: ", lambda x: True, "")
        denom = input_int("Input denominator: ", lambda x: x != 0, "denominator can't be 0")
        notation = input_int("Input notation base: ", lambda x: x > 1, "notation base must be greater than 1")
        frac = Fraction(num, denom)
        frac.represent(notation)
    

if __name__ == "__main__":
    main()
