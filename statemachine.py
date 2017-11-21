def event_prob(prob_matrix, step, state):
    if step == 0:
        return prob_matrix[step][state]
    else:
        return sum(map(
            lambda x: prob_matrix[x][state] * event_prob(prob_matrix, step - 1, x),
            range(0, len(prob_matrix) - 1)
        ))


def print_event_prob(states, prob_matrix, step, state):
    state_prob = event_prob(prob_matrix, step=step, state=state)
    print('Probability of system state', states[state], ' at step:', step, '=', round(state_prob, 4))