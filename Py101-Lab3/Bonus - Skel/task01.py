
class Complex:

    def __init__(self, real_part: int = 0, imaginary_part: int = 0, var_name: str = 'var') -> None:
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        self.var_name = var_name

    def __str__(self) -> str:
        a = self.real_part
        b = self.imaginary_part
        if a == 0 and b != 0:
            return (f'{self.var_name} = {self.imaginary_part}i')
        elif a != 0 and b == 0:
            return (f'{self.var_name} = {self.real_part}')
        elif a == 0 and b == 0:
            return (f'{self.var_name} = 0')
        elif b < 0:
            return (f'{self.var_name} = {self.real_part} - {self.imaginary_part * -1}i')
        else:
            return (f'{self.var_name} = {self.real_part} + {self.imaginary_part}i')
    def add_complex_numbers(self, other) -> None:
        self.real_part += other.real_part
        self.imaginary_part += other.imaginary_part

    def substract_complex_numbers(self, other) -> None:
        self.real_part -= other.real_part
        self.imaginary_part -= other.imaginary_part

    def multiply_complex_numbers(self, other) -> None:
        x = self.real_part * other.real_part - (self.imaginary_part * other.imaginary_part)
        y = (self.real_part * other.imaginary_part) + (self.imaginary_part * other.real_part)
        self.real_part = x
        self.imaginary_part = y
        """
        We know you all love Math. :)
        """