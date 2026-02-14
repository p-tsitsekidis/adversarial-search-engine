import numpy as np

def minimax_limited_pruning_player(game, state, max_depth=3):
    """Given a state in a game, calculate the best move by searching
    forward limited to a specific depth."""
    
    a = -np.inf
    b = np.inf
    initial_depth = 0
    
    player = game.to_move(state)

    def max_value(state, a, b, current_depth):     
        if game.terminal_test(state):
            return game.utility(state, player)
        
        # Check against the dynamic max_depth parameter instead of a hardcoded 3
        if current_depth >= max_depth:
            # Dynamically call the heuristic on the passed-in 'game' object
            if hasattr(game, 'evaluateHeuristicFunction'):
                return game.evaluateHeuristicFunction(state)
            return 0  # Fallback baseline if no heuristic exists

        v = -np.inf
        for action in game.actions(state):
            v = max(v, min_value(game.result(state, action), a, b, current_depth + 1))
            if v >= b:
                return v
            a = max(a, v)
        return v

    def min_value(state, a, b, current_depth):
        if game.terminal_test(state):
            return game.utility(state, player)
            
        if current_depth >= max_depth:
            if hasattr(game, 'evaluateHeuristicFunction'):
                return game.evaluateHeuristicFunction(state)
            return 0

        v = np.inf
        for action in game.actions(state):
            v = min(v, max_value(game.result(state, action), a, b, current_depth + 1))
            if v <= a:
                return v
            b = min(b, v)
        return v

    best_action = None
    v = -np.inf
    for action in game.actions(state):
        action_value = min_value(game.result(state, action), a, b, initial_depth + 1) 
        if action_value > v:
            v = action_value
            best_action = action
        a = max(a, v)
        
    return best_action