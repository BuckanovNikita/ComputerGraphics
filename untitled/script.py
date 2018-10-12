from sympy import *
import numpy as np

def f(a):
    return x1**2+a*x2**2

def rec_step(al, ah, f, F, sym, alpha, x, fx, fx_diff, df, c1, c2):
    j = 1
    while True:
        aj = al + (ah - al) * np.random.rand()
        print(al, aj, ah)
        if F.subs({alpha: aj}) > fx + c1 * aj * np.dot(fx_diff, df) or F.subs({alpha: aj}) >= F.subs({alpha: al}):
            ah = al
            j = j + 1
            continue
        F_ = np.array([f.diff(sym[0]).subs(zip(sym, x + aj * df)).evalf(16),
                       f.diff(sym[1]).subs(zip(sym, x + aj * df)).evalf(16)]).astype(np.float64)
        F_ = np.dot(F_, df)
        if abs(F_) <= -c2 * np.dot(fx_diff, df):
            return F.subs({alpha: aj}), aj, 0
        if abs(F_) * (ah - al) >= 0:
            ah = al
        al = aj


def wolf_rule(f, sym, x, df):
    alpha = symbols('alpha')
    a0 = 0
    a_max = 100
    c1 = 1e-4
    c2 = 0.1
    a1 = a_max * np.random.rand()
    i = 1
    F = f.subs(zip(sym, x - alpha * df))
    fx = f.subs(zip(sym, x))
    fx_diff = np.array([f.diff(sym[0]).subs(zip(sym, x)).evalf(16), f.diff(sym[1]).subs(zip(sym, x)).evalf(16)]).astype(
        np.float64)
    while True:
        if (F.subs({alpha: a1}) > fx + c1 * a1 * np.dot(fx_diff, df) or F.subs({alpha: a1}) > F.subs(
                {alpha: a0})) and i > 1:
            return rec_step(a0, a1, f, F, sym, alpha, x, fx, fx_diff, df, c1, c2)
        F_ = np.array([f.diff(sym[0]).subs(zip(sym, x + a1 * df)).evalf(16),
                       f.diff(sym[1]).subs(zip(sym, x + a1 * df)).evalf(16)]).astype(np.float64)
        F_ = np.dot(F_, df)
        if abs(F_) <= -c2 * np.dot(fx_diff, df):
            return F.subs({alpha: a1}), a1, 0
        if F_ >= 0:
            return rec_step(a1, a0, f, F, sym, alpha, x, fx, fx_diff, df, c1, c2)
        i = i + 1

def orthogonal_descent(f, sym, x0, eps=1e-4, restart=0, beta='v2'):
    theta = symbols('theta')
    i = 0
    it = 0
    df = np.array([f.diff(sym[0]).subs(zip(sym, x0)).evalf(16), f.diff(sym[1]).subs(zip(sym, x0)).evalf(16)]).astype(
        np.float64)
    df_1 = 0
    while eps < np.linalg.norm(df):
        print(x0)
        y = df - df_1
        theta_min = wolf_rule(f, sym, x0, df)
        print(theta_min)
        # minimizer(f.subs(zip(sym, x0-theta*df)), theta)
        x0 = x0 - theta_min[1] * df
        i = i + 2 + theta_min[2]
        s = np.array([f.diff(sym[0]).subs(zip(sym, x0)).evalf(16), f.diff(sym[1]).subs(zip(sym, x0)).evalf(16)]).astype(
            np.float64)

        if beta == 'v3':
            b = (np.linalg.norm(s) / np.linalg.norm(df)) ** 2
        elif beta == 'v1':
            b = float(re(np.dot(y, s) / np.dot(y, df)))
        elif beta == 'v2':
            b = float(np.dot(y, s) / (np.linalg.norm(df) ** 2))
        else:
            raise Exception("Unknown beta type")

        df_1 = df
        df = np.array(-1 * s + df * b)
        it = it + 1
        if restart and it % restart == 0:
            df = np.array(
                [f.diff(sym[0]).subs(zip(sym, x0)).evalf(16), f.diff(sym[1]).subs(zip(sym, x0)).evalf(16)]).astype(
                np.float64)
    return f.subs(zip(sym, x0)).evalf(16), x0, i, it


def main():
    x1 = symbols('x1')
    x2 = symbols('x2')
    theta = symbols('theta')
    eps=1e-4
    ortogonal_descent(f(5), [x1, x2], [2, 4], eps=eps, restart=2)