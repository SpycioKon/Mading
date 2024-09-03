def TSP(cap, mang1, mang2):
    if cap <= 0:
        return 0
    return (mang2[cap] - mang2[cap - 1]) / (mang1[cap] - mang1[cap - 1])


X = [0, 2, 3, 5, 6]  
Y = [1, 3, 2, 5, 6]  
x = 1.25

Pn = Y[0]  
product_term = 1

print(f"Bước 0: Pn = {Pn}")

for i in range(1, len(Y)):
    tsp_value = TSP(i, X, Y)  
    product_term *= (x - X[i - 1])
    term_value = product_term * tsp_value  
    Pn += term_value 
    print(f"Bước {i}: TSP cấp {i} = {tsp_value}")

print(f"Tổng = {Pn}")
