s = "abbc"
is_unique = True

for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            is_unique = False
            break

print(is_unique)        