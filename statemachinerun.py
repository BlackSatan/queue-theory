import statemachine
import helpers

_STEP = 2
_STATE = 0

states = [
    'Здоровий',
    'Таке',
    'Погано',
    'Мертвий',
]

prob_matrix = [
    [.55, .2, .2, .05],
    [.7, .2, .1, 0],
    [.2, 0, 0.4, .4],
    [.1, 0, .2, .1]
]

# prob_matrix = helpers.generate_random_matrix(4)
# print(prob_matrix)

statemachine.print_event_prob(states, prob_matrix, _STEP, _STATE)