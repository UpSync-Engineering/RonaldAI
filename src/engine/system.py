from datetime import datetime as dt
import webbrowser
import sys
import re


def get_current_time():
    return dt.now().strftime('%Y-%m-%d %H:%M:%S')


def open_website(website):
    webbrowser.open(website)


# Kept outside simple_eval() just for performance
_re_simple_eval = re.compile(rb'd([\x00-\xFF]+)S\x00')


def simple_eval(expr):
    """
    Got from the following source: https://stackoverflow.com/a/65945969/5015219
    :param expr: Mathematical expression
    :type expr: str
    :return:
    """
    try:
        c = compile(expr, 'userinput', 'eval')
    except SyntaxError:
        raise ValueError(f"Malformed expression: {expr}")
    m = _re_simple_eval.fullmatch(c.co_code)
    if not m:
        raise ValueError(f"Not a simple algebraic expression: {expr}")
    try:
        return c.co_consts[int.from_bytes(m.group(1), sys.byteorder)]
    except IndexError:
        raise ValueError(f"Expression not evaluated as constant: {expr}")


def execute_math_calculation_from_string(math_string):
    return simple_eval(math_string.replace('^', '**'))
