alice_inventory = {
    "sword": {"type": "weapon", "rarity": "rare", "count": 1, "cost": 500},
    "potion": {"type": "consumable", "rarity": "common", "count": 5, "cost": 50},
    "shield": {"type": "armor", "rarity": "uncommon", "count": 1, "cost": 200},

}
bob_inventory = {
    "magic_ring": {"type": "accessory", "rarity": "rare", "count": 1, "cost": 400}

}

print("=== Alice's Inventory ===")

inventory_value = 0
item_count = 0

for key in alice_inventory:

    print(f"{key} ({alice_inventory[key]["type"]}, {alice_inventory[key]["rarity"]}): "
          f"{alice_inventory[key]["count"]}x @ {alice_inventory[key]["cost"]} gold each "
          f"= {alice_inventory[key]["count"] * alice_inventory[key]["cost"]} gold")

    inventory_value += alice_inventory[key]["count"] * alice_inventory[key]["cost"]
    item_count += alice_inventory[key]["count"]

print(f"\nInventory value: {inventory_value} gold")
print(f"Item count: {item_count} items")
print("Categories: ", end="")

dict_len = len(alice_inventory)
for key in alice_inventory:
    print(f"{alice_inventory[key]["type"]}({alice_inventory[key]["count"]})", end="")
    if dict_len > 1:
        print(",", end=" ")
    dict_len -= 1

print("=== Transaction: Alice gives Bob 2 potions ===")

def update_bob_inventory():
    alice_inventory["potion"]["count"] -= 2

    bob_inventory.update({
                "potion": {"type": "consumable","rarity": "common",
                "count": 0,"cost": 0}
                })
    bob_inventory["potion"]["count"] += 2
    bob_inventory["potion"]["cost"] = alice_inventory["potion"]["cost"]

    print("Transaction successful!")

update_bob_inventory()

print("=== Updated Inventories ===")

print(f"Alice potions: {alice_inventory["potion"]["count"]}")
print(f"Bob potions: {bob_inventory["potion"]["count"]}")

alice_value = 0
alice_items = 0
for key in alice_inventory:
    alice_value += alice_inventory[key]["count"] * alice_inventory[key]["count"]
    alice_items += alice_inventory[key]["count"]

bob_value = 0
bob_items = 0
for key in bob_inventory:
    bob_value += bob_inventory[key]["count"] * bob_inventory[key]["count"]
    bob_items += bob_inventory[key]["count"]

if alice_value > bob_value:
    print(f"Most valuable player: Alice ({alice_value} gold)")
else:
    print(f"Most valuable player: Bob ({bob_value} gold)")

if alice_items > bob_items:
    print(f"Most items: Alice ({alice_value} items)")
else:
    print(f"Most items: Bob ({bob_value} items)")

rarest_items = []

for key in alice_inventory:
    if alice_inventory[key]["rarity"] == "rare":
        rarest_items.append(key)

for key in bob_inventory:
    if bob_inventory[key]["rarity"] == "rare":
        rarest_items.append(key)

items_len = len(rarest_items)

print("Rarest items:", end=" ")
for item in rarest_items:
    print(item, end="")
    if items_len > 1:
        print(", ", end="")
    items_len -= 1