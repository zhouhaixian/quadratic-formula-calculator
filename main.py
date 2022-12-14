# GPL-3.0 Licensed | Made by Zhou Haixian
from license import get_license


def parse(equation):
    """
    解析一般形式的一元二次方程

    :param equation: 一般形式的一元二次方程 ( ax²+bx+c )
    :return: [a, b, c]: 一个由方程的一次项系数、二次项系数、常数项组成的数组
    """
    result = equation.replace("²", "").replace(" ", "").split("x")
    for i in range(0, len(result)):
        if (result[i] == "") | (result[i] == "+"):
            result[i] = "1"
        elif result[i] == "-":
            result[i] = "-1"
        result[i] = int(result[i])
    return result


def calculate_discriminant(abc):
    """
    计算方程的 △

    :param abc: 一个由方程的一次项系数、二次项系数、常数项组成的数组
    :return: discriminant: △
    """
    a = abc[0]
    b = abc[1]
    c = abc[2]

    # △ = b² - 4ac
    return (b ** 2) - (4 * a * c)


def solve(abc, discriminant):
    """
    求出方程的实数根

    :param abc: 一个由方程的一次项系数、二次项系数、常数项组成的数组
    :param discriminant: △
    :return: 方程的实数解
    """
    a = abc[0]
    b = abc[1]
    if discriminant > 0:
        # x1 = (-b + √△) / (2a)
        x1 = (-b + (discriminant ** 0.5)) / (2 * a)
        # x2 = (-b - √△) / (2a)
        x2 = (-b - (discriminant ** 0.5)) / (2 * a)
        return f"x1 = {x1}, x2 = {x2}"
    elif discriminant == 0:
        x = (-b) / (2 * a)
        return f"x1=x2={x}"
    elif discriminant < 0:
        return "方程无实数根"


def calculate(equation):
    """
    计算一般形式的一元二次方程

    :param equation: 一般形式的一元二次方程 ( ax²+bx+c )
    :return: 方程的实数解
    """
    abc = parse(equation)
    discriminant = calculate_discriminant(abc)
    return solve(abc, discriminant)


def print_license():
    """
    打印许可证信息
    """
    print(get_license())


def print_help():
    """
    打印帮助信息
    """
    print(
        """
    ====================================================================================
            Quadratic Formula Calculator
                - Version: 1.0.7
                - Author:  周海衔
                - License: GPL-3.0
                - Repository: https://github.com/zhouhaixian/quadratic-formula-calculator
    ====================================================================================
        Quadratic Formula Calculator Copyright (C) 2022 Zhou Haixian
        This program comes with ABSOLUTELY NO WARRANTY; for details type `license'.
        This is free software, and you are welcome to redistribute it
        under certain conditions; type `license' for details.
        
        软件名称：一元二次方程计算器
        作者：周海衔
        许可证：GPL-3.0
        源代码存储库：https://github.com/zhouhaixian/quadratic-formula-calculator
        键入 "license" 显示许可证信息，键入 "help" 显示帮助信息，键入 "quit" 或 "exit" 退出。
        键入一元二次方程（例如：x²+6x-7）以开始计算
        请输入: """
        , end="")


if __name__ == '__main__':
    while True:
        try:
            print_help()
            content = input()
            match content:
                case "help":
                    continue
                case "license":
                    print_license()
                    input("\n\n\n请按任意键继续")
                case "quit" | "exit":
                    break
                case _:
                    input(f"        解得: {calculate(content)}，请按任意键继续")
        except (ValueError, IndexError):
            input("        命令或方程不合法，请按任意键继续")
