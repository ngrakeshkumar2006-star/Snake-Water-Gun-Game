import random
choices = {
    's': '🐍 Snake',
    'w': '💧 Water',
    'g': '🔫 Gun'
}
print("================================")
print("     🐍 SNAKE 💧WATER GUN 🔫")
print("================================")
user = input("Enter s 🐍, w 💧, or g 🔫 : ").lower()
computer = random.choice(['s', 'w', 'g'])
print("\n🙋 You      :", choices[user])
print("🤖 Computer :", choices[computer])
if user == computer:
    print("\n🤝 Match Draw!")
elif user == 's' and computer == 'w':
    print("\n🎉 Snake drinks Water! You Win!")
elif user == 'w' and computer == 'g':
    print("\n🎉 Water drown Gun! You Win!")
elif user == 'g' and computer == 's':
    print("\n🎉 Gun kills Snake! You Win!")
elif user == 'w' and computer == 's':
    print("\n😢 Snake drinks Water! Computer Wins!")
elif user == 'g' and computer == 'w':
    print("\n😢 Water drown Gun! Computer Wins!")
elif user == 's' and computer == 'g':
    print("\n😢 Gun kills Snake! Computer Wins!")
else:
    print("\n❌ Invalid Input!")
print("\n❤️ Thanks for Playing!")