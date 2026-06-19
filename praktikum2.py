import math

def f(x, expr):
    allowed = {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e
    }
    return eval(expr, {"__builtins__": {}}, allowed)

def trapezoidal(expr, a, b, n):
    h = (b - a) / n

    total = (f(a, expr) + f(b, expr)) / 2

    for i in range(1, n):
        total += f(a + i * h, expr)

    return h * total


print("=== METODE INTEGRASI TRAPEZOIDAL ===\n")

expr = input("Masukkan fungsi f(x): ")
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))
levels = int(input("Masukkan jumlah level: "))

exact = float(
    input(
        "\nMasukkan nilai integral analitis (0 jika tidak diketahui): "
    )
)

print("\nHasil Perhitungan")
print("-" * 55)

if exact != 0:
    print(f"{'n':<8}{'Aproksimasi':<20}{'Error (%)':<15}")
else:
    print(f"{'n':<8}{'Aproksimasi':<20}")

print("-" * 55)

# untuk integrasi romberg
R = [[0.0] * levels for _ in range(levels)]

for k in range(levels):
    n = 2 ** k
    result = trapezoidal(expr, a, b, n)
    
    # untuk integrasi romberg
    R[k][0] = result

    if exact != 0:
        error = abs((exact - result) / exact) * 100
        print(f"{n:<8}{result:<20.10f}{error:<15.4f}")
    else:
        print(f"{n:<8}{result:<20.10f}")

print("\n")
print("=" * 55)

for j in range(1, levels):
    for i in range(j, levels):
        R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / ((4**j) - 1)

print("\n\n=== TABEL INTEGRASI ROMBERG ===")
print("-" * 75)

for i in range(levels):
    baris = f"k={i+1} | "
    for j in range(i + 1):
        baris += f"{R[i][j]:<14.7f} "
    print(baris)
    
print("-" * 75)

nilai_akhir = R[levels-1][levels-1]
print(f"\nNILAI INTEGRASI ROMBERG TERBAIK : {nilai_akhir:.10f}")

if exact != 0:
    error_romberg = abs((exact - nilai_akhir) / exact) * 100
    print(f"ERROR ROMBERG TERBAIK           : {error_romberg:.6f}%")