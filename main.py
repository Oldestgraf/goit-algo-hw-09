import time

# Жадібний алгоритм
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    return result

# Алгоритм динамічного програмування
def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    min_coins = [0] + [float('inf')] * amount
    coin_count = [0] + [None] * amount

    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_count[x] = coin

    result = {}
    while amount > 0:
        coin = coin_count[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Оцінка ефективності алгоритмів
def evaluate_efficiency():
    amounts = [100, 1000, 10000, 100000, 1000000]
    greedy_times = []
    dp_times = []

    for amount in amounts:
        start_time = time.time()
        find_coins_greedy(amount)
        greedy_times.append(time.time() - start_time)

        start_time = time.time()
        find_min_coins(amount)
        dp_times.append(time.time() - start_time)

    return greedy_times, dp_times

def main():
    greedy_times, dp_times = evaluate_efficiency()

    print("Greedy Algorithm Times:")
    for i, t in enumerate(greedy_times):
        print(f"Amount: {10**(i+2)} - Time: {t:.6f} seconds")

    print("\nDynamic Programming Algorithm Times:")
    for i, t in enumerate(dp_times):
        print(f"Amount: {10**(i+2)} - Time: {t:.6f} seconds")

if __name__ == "__main__":
    main()
