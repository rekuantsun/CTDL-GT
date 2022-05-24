import numpy as np

def diChuyen(x:int, y:int, dem:int, A:np, n:int, X:list, Y:list):
    dem += 1
    A[x][y] = dem
    for i in range(8):
        if (dem == n ** 2):
            print("Cac buoc di la : \n")
            print(A)
            exit(0)
        u = x + X[i]
        v = y + Y[i]
        if (u >= 0 and u < n and v >= 0 and v < n and A[u][v] == 0):
            diChuyen(u, v, dem, A, n, X, Y)
    dem -= 1
    A[x][y] = 0

def main():
    n = int(input("Nhap n: "))
    A = np.zeros((n, n), int)

    X = [-2, -2, -1, -1, 1, 1, 2, 2]
    Y = [-1, 1, -2, 2, -2, 2, -1, 1]
    dem = 0
    print("Nhap vi tri ban dau ")
    a = int(input("x: "))
    b = int(input("y: "))

    diChuyen(a, b, dem, A, n, X, Y)
    print("Khong tim thay duong di.")

if __name__ == "__main__":
    main()
