def main():
    total_amount = 0

    while total_amount < 50:
        try:
            coin = int(input("Insert a coin (accepted denominations: 1, 5, 10, 25): "))
            if coin in [1, 5, 10, 25]:
                total_amount += coin
                print(f"Amount due: {50 - total_amount} cents remaining")
            else:
                print("Invalid coin denomination. Please insert a valid coin.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    change = total_amount - 50
    print(f"Change owed: {change} cents")


if __name__ == "__main__":
    main()
