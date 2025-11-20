import gym
from stable_baselines3 import DQN
from stable_baselines3 import PPO
from stable_baselines3 import A2C
from stable_baselines3.common.env_checker import check_env

class Learner():

	def __init__(self, failed_state, goal_state, random_seed=3, env="BirthdayPresent-v0", display=False) -> None:

		#self.env_to_reset = copy.deepcopy(env) # copy the complete environment instance
		self.env = env
		self.goal_state = goal_state
		self.failed_state = failed_state
		self.random_seed = random_seed
		self.display = display

	def learn(self):
		env = gym.make(self.env, initial_state=self.failed_state, goal_state=self.goal_state, display=self.display)
		check_env(env)

		success_rate = 0
		model = None
		trials = 0

		learned_policy = True

		while success_rate<0.99:

			success_list = list()
			reward_list = list()
			reward = 0

			if model == None:
				model = PPO("MlpPolicy", env, verbose=0, seed=0)#, tensorboard_log="./DQN_tensorboard/")
			else:
				model = model

			model.learn(total_timesteps=1_000, log_interval=1)
			model.save("ppo_"+self.env)

			for i in range(100):
				success = False
				done = False
				obs = env.reset()
				while not done:
					action = model.predict(obs)[0]
					obs, rew, done, info = env.step(action)
					reward += rew
					success = info["is_success"]
				reward_list.append(reward)
				success_list.append(success)
			success_rate = sum(success_list)/100
			print("\nLearning:::\nSuccess rate on Test %d: " %(trials+1), success_rate)
			trials += 1
			if trials > 50:
				learned_policy = False
				break
		
		return learned_policy, model


