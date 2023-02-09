from rich import print


# === Main Function ===
def main():
    text = "My Text"

    print(f"{text:.<20}")
    print(f"{text:_>20}")
    print(f"{text:#^20}")

    print("\n==================================\n")

    print(f"{text:<20}")
    print(f"{text:>20}")
    print(f"{text:^20}")


if __name__ == "__main__":
    main()

# Expected Output:
# My Text.............
# ______________My Text
# ####My Text####
#
# ==================================
#
# My Text
#                My Text
#        My Text
