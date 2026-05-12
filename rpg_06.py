from pymonad.tools import curry
from pymonad.state import State

player_init = {
    "actions": [],
    "stamina": 100
}
ACTION_COST = {
    "run": 15,
    "jump": 10,
    "attack": 25,
    "sleep": -40
}
player_state = State.insert(player_init["actions"])

@curry(2)
def do_action(action_name, actions_history):
    def stamina_computation(current_stamina):

        new_stamina = current_stamina - ACTION_COST[action_name]
        if new_stamina > 100:
            new_stamina = 100
        if new_stamina < 0:
            new_stamina = 0

        new_history = actions_history + [action_name]
        return new_history, new_stamina

    return State(stamina_computation)

game = (
    player_state
    .then(do_action("run"))
    .then(do_action("jump"))
    .then(do_action("attack"))
    .then(do_action("sleep"))
    .then(do_action("run"))
)
result = game.run(player_init["stamina"])






print(result)
