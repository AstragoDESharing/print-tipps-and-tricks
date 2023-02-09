from rich import print


# === Main Function ===
def main():
    text = "AstragoDE"

    print(f"{text:.<20}")
    print(f"{text:_>20}")
    print(f"{text:#^20}")

    print("==================================")

    print(f"{text:<20}")
    print(f"{text:>20}")
    print(f"{text:^20}")


if __name__ == "__main__":
    main()