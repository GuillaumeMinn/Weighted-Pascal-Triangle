def build_weighted_pascal(n, w):
    triangle = [[1]]

    for i in range(1, n + 1):
        row = []
        previous = triangle[i - 1]

        for j in range(i + 1):
            left = previous[j - 1] if j - 1 >= 0 else 0
            right = previous[j] if j < len(previous) else 0
            value = w * left + right
            row.append(value)

        triangle.append(row)

    return triangle


def print_triangle(triangle):
    width = len("   ".join(map(str, triangle[-1])))
    for i, row in enumerate(triangle):
        line = "   ".join(map(str, row))
        print(f"Row {i}: {line.center(width)}")


def main():
    try:
        n = int(input("Enter number of rows (n ≥ 0): "))
        w = int(input("Enter weight factor (w ≥ 1): "))
    except ValueError:
        print("Please enter valid integers.")
        return

    if n < 0 or w < 1:
        print("Invalid input. n must be ≥ 0 and w must be ≥ 1.")
        return

    triangle = build_weighted_pascal(n, w)

    print("\nGenerated Triangle:\n")
    print_triangle(triangle)

    print("\nRow sums:")
    for i, row in enumerate(triangle):
        print(f"Row {i} sum = {sum(row)}")

    expected = (w + 1) ** n
    print(f"\nCheck for final row:")
    print(f"Sum = {sum(triangle[-1])}")
    print(f"(w + 1)^n = {expected}")

    if sum(triangle[-1]) == expected:
        print("Result confirmed.")
    else:
        print("Result does not match expectation.")


if __name__ == "__main__":
    main()
