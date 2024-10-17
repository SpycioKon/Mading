# Hàm và đạo hàm bậc nhất, bậc hai của phương trình f(x) = x^2 - 2
import numpy as np

f = lambda x: 2**x - 4*x
df = lambda x: np.log(2) * 2**x - 4
d2f = lambda x: (np.log(2)) **2 * 2**x   # Đạo hàm bậc hai 

# Hàm tìm khoảng phân ly nghiệm [a, b]
def Khoang_phan_ly(f, a, b, step=0.1):
    """
    Tìm khoảng phân ly nghiệm trên đoạn [a, b].
    Nếu f(a) * f(b) < 0, trả về khoảng phân ly.
    """
    while f(a) * f(b) >= 0 and a < b:
        a += step  # Dịch chuyển a và b đdể tìm khoảng phân ly
        b -= step
    if f(a) * f(b) < 0:
        print(f"Khoảng phân ly nghiệm tìm được là [{a}, {b}]")
        return a, b
    else:
        print(f"Không tìm thấy khoảng phân ly nghiệm.")
        return None, None

# Hàm tìm giá trị ban đầu x0 sao cho f(x) * f''(x) > 0
def Tim_x0(f, d2f, a, b, step=0.1):
    x = a
    while x <= b:
        if f(x) * d2f(x) > 0:
            print(f"Tìm thấy x0 : {x} ")
            return x
        x += step
    print(f"Không tìm thấy x0 thỏa mãn điều kiện.")
    return None

# Phương pháp Newton-Raphson
def newton_raphson(f, df, x0, eps=1e-5, max_vong=100):
    xn = x0
    M = max([abs(d2f(x)) for x in np.linspace(a, b, 100)])
    m = min([abs(df(x)) for x in np.linspace(a, b, 100) if df(x) != 0])
    for n in range(max_vong):
        fxn = f(xn)
        dfxn = df(xn)
        
         # Đánh giá sai số bằng công thức đã cung cấp
        dif = (M / (2 * m)) * abs(fxn)**2
        print(f"Lần lặp {n }: x = {xn}, f(x) = {fxn}, Sai số đánh giá = {dif}")
        
        if  dif < eps:
            xn = xn - fxn / dfxn
            n += 1
            print(f"Nghiệm gần đúng tìm được là: {xn} sau {n } lần lặp")
            print(f"Sai số nhỏ hơn epsilon ({eps}): {dif}")
            return xn, n
        
        if dfxn == 0:
            print(f"Đạo hàm bằng 0, không thể tiếp tục.")
            return None, n  # Đạo hàm bằng 0, không thể tiếp tục
        
        xn = xn - fxn / dfxn
    
    print(f"Không tìm thấy nghiệm sau số lần lặp tối đa.")
    return None, max_vong

# Bước 1: Tìm khoảng phân ly nghiệm [a, b]
a, b = Khoang_phan_ly(f, 0, 1)  # Tìm khoảng phân ly trong khoảng [0, 2]

# Bước 2: Tìm giá trị ban đầu thỏa mãn f(x) * f''(x) > 0
if a is not None and b is not None:
    x0 =Tim_x0(f, d2f, a, b)

    # Bước 3: Áp dụng phương pháp Newton-Raphson
    if x_initial is not None:
        kq, lap = newton_raphson(f, df, x0)

        print(f"Nghiệm dương của phương trình là: {kq}")
        print(f"Số lần lặp: {lap} ")
