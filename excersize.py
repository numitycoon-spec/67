import random
import math

participant = int(input("number participant: "))
winner = int(input("winner number: "))

tickets = list(range(1, participant + 1))

tickets_per_sheet = 8

sheets_needed = math.ceil(participant / tickets_per_sheet)

jackpot = 8888

prize_per_winner = math.floor(jackpot / winner)

winning_tickets = random.sample(tickets, winner)

print(f"Total sheets needed: {sheets_needed}")
print(f"Jackpot: {jackpot} THB")
print(f"Prize per winner: {prize_per_winner} THB")
print(f"Winning tickets: {winning_tickets}")







