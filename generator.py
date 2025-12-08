import random
import datetime

# ---------- WORD POOLS ---------- #

SUBJECTS = {
    "tech": [
        "Local programmer",
        "Mysterious AI bot",
        "Forgotten Github repo",
        "Outdated laptop",
        "Bug in production"
    ],
    "sports": [
        "Unknown cricket team",
        "Retired footballer",
        "Random gully cricketer",
        "Neighborhood coach",
        "Benchwarmer player"
    ],
    "bollywood": [
        "Famous actor",
        "Struggling actor",
        "Overexcited director",
        "Drama queen celebrity",
        "Legendary background dancer"
    ],
    "random": [
        "Confused student",
        "Sleepy cat",
        "Chai seller",
        "College canteen aunty",
        "Silent library guy"
    ],
}

VERBS = [
    "shocks everyone by",
    "goes viral after",
    "secretly starts",
    "publicly refuses",
    "accidentally invents",
    "unexpectedly wins",
]

OBJECTS = [
    "solving 100 LeetCode problems in one night",
    "eating 50 samosas during standup meeting",
    "deleting entire codebase before release",
    "replacing all bugs with TODO comments",
    "using ChatGPT for every assignment",
]

EVENTS = [
    "online exam crashes",
    "Wi-Fi stops working",
    "boss checks Git history",
    "friend asks for notes",
    "deadline gets preponed",
]

TEMPLATES = [
    "Breaking: {subject} {verb} {object}",
    "Shocking report: {subject} {verb} after {event}",
    "Experts confused as {subject} {verb} {object}",
    "Local news: {subject} {verb} when {event}",
]


# ---------- GENERATOR LOGIC ---------- #

def get_subject(category: str) -> str:
    """Return a random subject from the given category or random."""
    category = category.lower()
    if category not in SUBJECTS:
        category = "random"
    return random.choice(SUBJECTS[category])


def generate_headline(category: str = "random") -> str:
    template = random.choice(TEMPLATES)
    headline = template.format(
        subject=get_subject(category),
        verb=random.choice(VERBS),
        object=random.choice(OBJECTS),
        event=random.choice(EVENTS),
    )
    return headline


def save_to_file(headlines, filename="history.txt"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n--- {now} ---\n")
        for h in headlines:
            f.write(h + "\n")


def main():
    print("🎭 Fake News Headline Generator (For Fun Only)")
    print("-------------------------------------------")

    category = input(
        "Choose category (tech / sports / bollywood / random): "
    ).strip().lower()
    if category not in SUBJECTS:
        print("Unknown category, using 'random'")
        category = "random"

    try:
        count = int(input("How many headlines do you want? "))
    except ValueError:
        print("Invalid number, generating 3 headlines by default.")
        count = 3

    headlines = [generate_headline(category) for _ in range(count)]

    print("\nGenerated Headlines:\n")
    for i, h in enumerate(headlines, start=1):
        print(f"{i}. {h}")

    save_choice = input("\nSave these headlines to history.txt? (y/n): ").strip().lower()
    if save_choice == "y":
        save_to_file(headlines)
        print("Saved to history.txt")

    print("\nDone. Use responsibly and only for fun 😄")


if __name__ == "__main__":
    main()
