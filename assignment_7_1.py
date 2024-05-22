...


if __name__ == "__main__":
    hp_characters = load_hp_data("datasets\\Characters.csv")
    hp_dialogues = load_hp_data("datasets\\Dialogue.csv")

    houses, most_talks = main(hp_characters, hp_dialogues)

    print(f"Percentage of characters in each house:\n"
          f"\tGryffindor: {round(houses[0], 2)}%\n"
          f"\tHufflepuff: {round(houses[1], 2)}%\n"
          f"\tRavenclaw: {round(houses[2], 2)}%\n"
          f"\tSlytherin: {round(houses[3], 2)}%\n")
    print(f"The characters with the most dialogue lines:")
    for name, number in most_talks:
        print(f"\t{name} had {number} lines.")
