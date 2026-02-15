
data = {
    'alice': [
        'first_blood',
        'pixel_perfect',
        'speed_runner',
        'first_blood',
        'first_blood'
    ],
    'bob': [
        'level_master',
        'boss_hunter',
        'treasure_seeker',
        'level_master',
        'level_master'
    ],
    'charlie': [
        'treasure_seeker',
        'boss_hunter',
        'combo_king',
        'first_blood',
        'boss_hunter',
        'first_blood',
        'boss_hunter',
        'first_blood'
    ],
    'diana': [
        'first_blood',
        'combo_king',
        'level_master',
        'treasure_seeker',
        'speed_runner',
        'combo_king',
        'combo_king',
        'level_master'
    ],
    'eve': [
        'level_master',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker'
    ],
    'frank': [
        'explorer',
        'boss_hunter',
        'first_blood',
        'explorer',
        'first_blood',
        'boss_hunter'
    ]
}

Player_alice_achievements = set(data["alice"])
Player_bob_achievements = set(data["bob"])
Player_charlie_achievements = set(data["charlie"])

print("=== Achievement Tracker System ===\n")

print(f"Player alice achievements: {Player_alice_achievements}")
print(f"Player bob achievements: {Player_bob_achievements}")
print(f"Player charlie achievements: {Player_charlie_achievements}")

print("\n=== Achievement Analytics ===")

union_set = Player_alice_achievements.union(Player_bob_achievements).union(Player_charlie_achievements)
print(f"All unique achievements: {union_set}")
print(f"Total unique achievements: {len(union_set)}\n")

intersiction_set = Player_alice_achievements.intersection(Player_bob_achievements).intersection(Player_charlie_achievements)
print(f"Common to all players: {intersiction_set}")

bob_difference_set = Player_bob_achievements.difference(Player_charlie_achievements)
charlie_difference_set = Player_charlie_achievements.difference(Player_bob_achievements)

difference_set = bob_difference_set
difference_set.update(charlie_difference_set)

difference_sett = difference_set.difference(Player_alice_achievements)
print(f"Rare achievements (1 player): {difference_sett}\n")

alice_vs_bob = Player_alice_achievements.intersection(Player_bob_achievements)
print(f"Alice vs Bob common: {alice_vs_bob}")

alice_unique = Player_alice_achievements.difference(Player_bob_achievements)
print(f"Alice unique:: {alice_unique}")

bob_unique = Player_bob_achievements.difference(Player_alice_achievements)
print(f"Bob unique: {bob_unique}")