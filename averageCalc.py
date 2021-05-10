from calc import Calc


class AverageCalc(Calc):
    def calc(self, lst: list, with_credits=True) -> float:
        ret_val = 0.0

        if with_credits:
            ret_val = self.do_calc_with_credits(lst)
        else:
            ret_val = self.do_calc(lst)

        return ret_val

    def do_calc_with_credits(self, grade_credits: list) -> float:
        if not isinstance(grade_credits, list) and not all(isinstance(x, tuple) for x in grade_credits):
            raise ValueError("Wrong Type, each grade needs a credit")

        credit_sum = 0
        grade_credit_product = 0

        for credit, grade in grade_credits:
            credit_sum += credit
            grade_credit_product += grade * credit

        return grade_credit_product / credit_sum

    def do_calc(self, lst) -> float:
        pass
