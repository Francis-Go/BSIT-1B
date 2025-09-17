print("🦜: Hello I'm Bob,the Parrot Interpreter")
user=input("\n🦜: What do you want me to say? " )
times=eval(input("\n🦜: How many times would I repeat it? " ))

for repeat in range(times):
  print("\n🦜:", user)
