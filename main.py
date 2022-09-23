class Interpreter:
    def __init__(self):
        self.varlist = {}

    def run(self, program):
        for sub_lst in program:
            self.eval(sub_lst)

    def Print(self, sub_lst):
        for i, x in enumerate(sub_lst[1:]):
            e = self.eval(x)
            if e != ",":
                print(e)

    def eval(self, sub_lst):
        if isinstance(sub_lst, list):
            if isinstance(sub_lst[0], int):
                return sub_lst[0]
            elif sub_lst[0] == '+':
                return self.eval(sub_lst[1]) + self.eval(sub_lst[2])
            elif sub_lst[0] == '-':
                return self.eval(sub_lst[1]) - self.eval(sub_lst[2])
            elif sub_lst[0] == '/':
                if sub_lst[2] == 0:
                    return 0
                return self.eval(sub_lst[1]) / self.eval(sub_lst[2])
            elif sub_lst[0] == '*':
                return self.eval(sub_lst[1]) * self.eval(sub_lst[2])
            elif sub_lst[0] == '<':
                return self.eval(sub_lst[1]) < self.eval(sub_lst[2])
            elif sub_lst[0] == '==':
                return self.eval(sub_lst[1]) == self.eval(sub_lst[2])
            elif sub_lst[0] == 'if':
                return self.eval(sub_lst[2]) if self.eval(sub_lst[1]) else self.eval(sub_lst[3])
            elif sub_lst[0] == 'Let':
                self.varlist[sub_lst[1]] = self.eval(sub_lst[2])
                return self.eval(sub_lst[3])
            elif sub_lst[0] == 'Identifier':
                return self.varlist[sub_lst[1]]
            elif sub_lst[0] == 'While':
                a = self.eval(sub_lst[1])
                sum= 0
                while a <= self.eval(sub_lst[2]):
                    sum = sum+a
                    a = a+1
                return sum
            return self.__getattribute__(sub_lst[0])(sub_lst)
        return sub_lst


program_Constant = [["Print", [474]],
                    ]

program_Binop = [
                 ["Print", ["/",["+", 400, 74], 3]]
                 ]

program_Comparison = [
                      ["Print", ["==", ["/",["+", 400, 74], 3], 158]]
                      ]

program_Conditional_Expression = [
    ["Print", ["if", ["==", ["/", ["+", 400, 74], 3], 158], [474], ["/", 474, 0]]],
                                  ]

program_Variables = [
        ["Print", ["Let", "bot", 3, ["+", ["Let", "bot", 2, ["Identifier", "bot"]],
             ["if", ["==", ["Identifier", "bot"], 0], ["/", 474, 0],
              ["/", ["+", 400, 74], ["Identifier", "bot"]]]]]]
                    ]
program_Loop = [
    ["Print",["While", ["Let", "bot", ["+", 1, 0], ["Identifier", "bot"]], ["Let", "bot", ["+", 100, 0], ["Identifier", "bot"]]]]
]
# print("P1-Constants")
# Interpreter().run(program_Constant)
# print("P2-Binary Operation")
# Interpreter().run(program_Binop)
# print("P3-Comparison")
# Interpreter().run(program_Comparison)
# print("P4-Conditional Expression")
# Interpreter().run(program_Conditional_Expression)
# print("P5-Variables")
# Interpreter().run(program_Variables)
Interpreter().run(program_Loop)
