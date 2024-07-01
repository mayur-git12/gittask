square={num:num**2 for num in range(1,11)}
print(square)

#square={f"square of {num} is":num**2 for num in range(1,11)}
#for k,v in square.items():
#    print(f"{k}:{v}")

#word count:-
string='abdhish'
word_count={char:string.count(char) for char in string}
print(word_count)

#DC with ifelse:-
odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)