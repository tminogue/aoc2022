import common

test_input = [
    ("A", "Y"),
    ("B", "X"),
    ("C", "Z"),
]

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

PLAY_MAP = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

SCORING_PAIRS = {
    (ROCK, ROCK): (1 + 3, 1 + 3),
    (ROCK, PAPER): (1 + 0, 2 + 6),
    (ROCK, SCISSORS): (1 + 6, 3 + 0),

    (PAPER, PAPER): (2 + 3, 2 + 3),
    (PAPER, ROCK): (2 + 3, 1 + 0),
    (PAPER, SCISSORS): (2 + 0, 3 + 6),

    (SCISSORS, SCISSORS): (3 + 3, 3 + 3),
    (SCISSORS, ROCK): (3 + 0, 1 + 6),
    (SCISSORS, PAPER): (3 + 6, 2 + 0),
}

PART2_CHOICE_MAP = {
    # lose
    "X": {ROCK:SCISSORS, PAPER:ROCK, SCISSORS:PAPER},
    # tie
    "Y": {ROCK:ROCK,PAPER:PAPER,SCISSORS:SCISSORS},
    # win
    "Z": {ROCK:PAPER, PAPER:SCISSORS,SCISSORS:ROCK},
}


def create_round_tuples(input_list):
    return [tuple(row.split()) for row in input_list]


def convert_round_values(round_values: tuple):
    return (PLAY_MAP[round_values[0]], PLAY_MAP[round_values[1]])


#guide_rounds = test_input
guide_rounds = common.deserialize_input_file("./02_input.txt")


def part_1(guide_rounds):
    player_1_score = 0
    player_2_score = 0
    for round in create_round_tuples(guide_rounds):
        round_scores = SCORING_PAIRS[convert_round_values(round)]
        player_1_score += round_scores[0]
        player_2_score += round_scores[1]
    return player_2_score

def part_2(guide_rounds):
    player_1_score = 0
    player_2_score = 0

    for player_1_choice, strategy in create_round_tuples(guide_rounds):

        my_choice = PART2_CHOICE_MAP[strategy][PLAY_MAP[player_1_choice]]

        round_scores = SCORING_PAIRS[(PLAY_MAP[player_1_choice], my_choice)]
        print(round_scores)
        player_1_score += round_scores[0]
        player_2_score += round_scores[1]

    return player_2_score


