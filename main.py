import os

ENTRY = "Introducing NapDebt: for $12 a month, it tracks the sleep you lost last night, converts it into a loan, and wakes you hourly to collect interest in the form of more lost sleep."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
