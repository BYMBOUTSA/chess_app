import lichess.api
import pandas as pd




def get_games_from_player(player_name: str, n: int) -> pd.DataFrame:
    """ Request the n last games data for a given player name.

    Args:
        player_name (str): the name of the player using out platform.
        n (int): The number of games we want to get data from.
    Returns:
        pd.DataFrame: The dataframe containing all n games data.
    """

    # API call
    games = lichess.api.user_games(player_name, max=n)

    results = []
    for game in games:
        # Prendre les clefs (k) et valeurs (v) réutilisable directement dans notre nouveau format de dictionnaire
        keys = ["id", "createdAt", "speed", "rated", "status"]
        reformat_game = {k: game[k] for k in keys}

        # Il nous faut aussi sa couleur
        # Dans une partie face à l'IA, il n'y a pas de clef 'user'. On en déduit que le joueur est noir dans ce cas.
        reformat_game["player_color"] = "white" if "user" in game["players"]["white"] and game["players"]["white"]["user"]["name"] == player_name else "black"

        # Quel est son rang au moment de la partie
        reformat_game["player_rating"] = game["players"][reformat_game["player_color"]]["rating"]

        # A-t-il gagné ?
        # Dans une partie d'un draw ou stalemate, la clef "winner" n'existe pas.
        if "winner" not in game.keys():
            reformat_game['win'] = False
        elif (game["winner"] == reformat_game["player_color"]) or (game["winner"] == reformat_game["player_color"]):
            reformat_game["win"] = True
        else:
            reformat_game["win"] = False

        results.append(reformat_game)

    return pd.DataFrame(results)


if __name__ == '__main__':
    # Test out fonction
    df = get_games_from_player("cyanfish", 50)
    print(df)


