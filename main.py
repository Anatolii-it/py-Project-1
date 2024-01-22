try:
   S = input("введіть рядок")
   l = S.split()
   print("слів в рядкові", len(l))

except Exception as e:
   print(e)