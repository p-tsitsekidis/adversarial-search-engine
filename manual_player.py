def manual_player(game, state):
    """A manual player."""
    game.display(state)
    actions = game.actions(state)
    while True:
        action = input("Enter your move (e.g., 2,3): ")
        try:
            action = action.split(',')
            action = [int(v) for v in action]
            action = tuple(action)
            if action not in actions:
                print('invalid action!!')
            else:
                return action
        except (ValueError, IndexError):
            print('Invalid action! Please use format "x,y".')