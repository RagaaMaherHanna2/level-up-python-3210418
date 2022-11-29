import random
import time
def waiting_game():
    random_time = random.randint(2, 4)
    start = time.time()
    user_input = input(f'Your target time {random_time}\n')
    end = time.time()
    elapsed = end-start
    if elapsed < random_time:
      print("Elapsed Time: " + str(elapsed) +
            " seconds. Man, you're too fast.")

    elif elapsed == random_time:
      print("Elapsed Time: " + str(elapsed) +
            " seconds. Man, you've got it.")
    else:
      print("Elapsed Time: " + str(elapsed) +
            " seconds. Man, you're too slow.")


if __name__ == '__main__':
  waiting_game()