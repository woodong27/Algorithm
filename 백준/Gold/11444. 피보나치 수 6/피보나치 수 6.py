# BOJ 11444 G2 피보나치 수 6


def multi(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """
    행렬 곱
    :param matrix1:
    :param matrix2:
    :return:
    """
    n = len(matrix1)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += matrix1[i][k] * matrix2[k][j]
            result[i][j] = temp % DIVISION

    return result


def power(matrix: list[list[int]], n: int) -> list[list[int]]:
    """
    행렬 제곱
    :param matrix:
    :param n:
    :return:
    """
    if n == 1:
        return matrix

    temp = power(matrix, n // 2)
    if n % 2:
        return multi(multi(temp, temp), matrix)
    else:
        return multi(temp, temp)


if __name__ == '__main__':
    N = int(input())
    DIVISION = 1_000_000_007

    matrix_ = [[1, 1], [1, 0]]
    answer = power(matrix_, N)
    print(answer[1][0] % DIVISION)
