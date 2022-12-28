class analyse_expression:
    def __init__(self, expression):
        self.operators = ["+", "-", "/", "*"]
        self.expression = ''.join(expression.split())
        self.list_of_operators = []
        self.list_of_digits = []
        
        for index in self.expression:
            if index in self.operators:
                self.list_of_operators.append(index)
            else:
                self.list_of_digits.append(index)
        
    def what_expression(self):
        if self.expression[-1] in self.operators:
            self.expression_type = "postfix"
        elif self.expression[0] in self.operators and len(self.list_of_operators) < len(self.list_of_digits):
            self.expression_type = "prefix"
        else:
            self.expression_type = "infix"
        return self.expression_type
    
    def calculate_expression(self):
        stack = []
        if self.expression_type == "infix":
            output = eval(self.expression)
        elif self.expression_type == "prefix":
            reversed_expression = self.expression[::-1]
            for index in reversed_expression:
                if index not in self.operators:
                    stack.append(index)
                else:
                    if index != reversed_expression[-1]:
                        last_element = stack[-1]
                        penultimate_element = stack[-2]
                        new_element = eval(f"{last_element}{index}{penultimate_element}")
                        stack.pop(-1)
                        stack.pop(-1)
                        stack.append(new_element)
                    else:
                        last_element = stack[-1]
                        penultimate_element = stack[-2]
                        new_element = eval(f"{last_element}{index}{penultimate_element}")
                        output = new_element
        else:
            for index in self.expression:
                if index not in self.operators:
                    stack.append(index)
                else:
                    if index != self.expression[-1]:
                        last_element = stack[-1]
                        penultimate_element = stack[-2]
                        new_element = eval(f"{penultimate_element}{index}{last_element}")
                        stack.pop(-1)
                        stack.pop(-1)
                        stack.append(new_element)
                    else:
                        last_element = stack[-1]
                        penultimate_element = stack[-2]
                        new_element = eval(f"{penultimate_element}{index}{last_element}")
                        output = new_element
        return output


if __name__ == "__main__":
    user_input = input("Please enter your expression\n")
    expression = analyse_expression(user_input)
    expression_type = expression.what_expression()
    expression_solution = expression.calculate_expression()

    print(f"The input expression is of type {expression_type}")
    print(f"The solution to this expression is {expression_solution}")
