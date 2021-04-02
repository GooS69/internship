class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(list):
    if len(list) != 2:
        raise WrongNumberOfPlayersError

    p1 = list[0][1]
    p2 = list[1][1]

    if p1 == p2 or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P") or (p1 == "R" and p2 == "S"):
        print(list[0][0] + " " + p1)
    elif (p2 == "P" and p1 == "R") or (p2 == "S" and p1 == "P") or (p2 == "R" and p1 == "S"):
        print(list[1][0] + " " + p2)
    else:
        raise NoSuchStrategyError()


rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])  # => WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']])  # => NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']])  # => 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']])  # => 'player1 P'
