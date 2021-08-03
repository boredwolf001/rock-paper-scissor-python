import random

options = ["r", "p", "s"]
player_score = 0
computer_score = 0

i = 0
while i < 10:
	player = input("rock[r] scissor[s] paper[p]: ")
	if player not in options:
		print("Invalid response")
		player = input("rock[r] scissor[s] paper[p]: ")

	computer = random.choice(options)

	if player.lower() == computer:
		print(f"player: {player}", f"computer: {computer}\n")
		print("It's a tie!")
		print(f"player's score: {player_score}")
		print(f"computer's score: {computer_score}\n\n")

	if (player.lower() == "r" and computer == "s") or (player.lower() == "s" and computer == "p") or (player.lower() == "p" and computer == "r"):
		print(f"player: {player}", f"computer: {computer}\n")
		player_score += 1
		print(f"player's score: {player_score}")
		print(f"computer's score: {computer_score}\n\n")

	if (player.lower() == "r" and computer == "p") or (player.lower() == "s" and computer == "r") or (player.lower() == "p" and computer == "s"):
		print(f"player: {player}", f"computer: {computer}\n")
		computer_score += 1
		print(f"player's score: {player_score}")
		print(f"computer's score: {computer_score}\n\n")

	i += 1

winner = ""
if player_score > computer_score:
	winner = "you"
elif player_score < computer_score:
	winner = "computer"
else:
	winner = "This is a draw round"

if winner != "This is draw round":
	print(f"THE WINNER IS {winner}")
else:
	print(winner)
