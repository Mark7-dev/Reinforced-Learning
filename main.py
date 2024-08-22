# gym==0.26.2
# gym-notices==0.0.8

# gymnasium==0.27.0

import gymnasium as gym

import time


env = gym.make('CartPole-v1', render_mode='human')
# reset the environment,
# returns an initial state
(state, _) = env.reset()

# State contains: cart position, cart velocity, pole angle, pole angular velocity

# render the environment
env.render()
# close the environment
# env.close()

# Test a single step in the environment by pushing the cart left
env.step(0)


env.observation_space  # state space details
env.observation_space.high  # max state values
env.observation_space.low  # min state values
env.action_space  # available actions
env.spec  # environment specifications

# check the environment's constraints
env.spec.max_episode_steps

# reward threshold per episode
env.spec.reward_threshold

episodeNumber = 1000
timeSteps = 100 #steps per episode

for episodeIndex in range(episodeNumber):
    initial_state = env.reset()
    print(episodeIndex) # track episode number
    env.render()
    appendedObservations = []
    for timeIndex in range(timeSteps):
        print(timeIndex)
        random_action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(random_action)
        appendedObservations.append(observation)
        if (terminated):
            time.sleep(.5)
            break
env.close()