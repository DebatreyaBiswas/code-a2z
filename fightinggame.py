import random
import time

class Fighter:
    """Represents a character in the fighting game."""
    
    def __init__(self, name, health, min_attack, max_attack):
        """Initializes a fighter with name, health, and attack range."""
        self.name = name
        self.health = health
        self.min_attack = min_attack
        self.max_attack = max_attack

    def attack(self, opponent):
        """Calculates random damage and applies it to the opponent."""
        
        damage = random.randint(self.min_attack, self.max_attack)
        
        
        opponent.health -= damage
        
        
        if opponent.health < 0:
            opponent.health = 0
            
        print(f"💥 {self.name} attacks {opponent.name} for {damage} damage!")
        print(f"❤️ {opponent.name} Health: {opponent.health}")

    def is_alive(self):
        """Checks if the fighter is still alive."""
        return self.health > 0

def start_duel():
    """Sets up the fighters and runs the main game loop."""
    
   
    fighter1 = Fighter("Iron Fist", 100, 10, 20)
    fighter2 = Fighter("Shadow Kick", 90, 15, 25)
    
    print("------------------------------------------")
    print(f"🥊 Duel Start: {fighter1.name} (HP: {fighter1.health}) vs {fighter2.name} (HP: {fighter2.health})")
    print("------------------------------------------")

   
    current_attacker = fighter1
    current_defender = fighter2
    if random.choice([True, False]):
        current_attacker, current_defender = fighter2, fighter1
    
    print(f"First turn goes to: {current_attacker.name}!\n")
    
   
    while fighter1.is_alive() and fighter2.is_alive():
        
       
        current_attacker.attack(current_defender)
        
        
        time.sleep(1) 
        
       
        if not current_defender.is_alive():
            break
            
        
        current_attacker, current_defender = current_defender, current_attacker
        
        print("\n--- Next Round ---")
    
    
    print("\n------------------------------------------")
    if fighter1.is_alive():
        print(f"🏆 Winner: {fighter1.name} remains victorious with {fighter1.health} health! 🏆")
    else:
        print(f"🏆 Winner: {fighter2.
