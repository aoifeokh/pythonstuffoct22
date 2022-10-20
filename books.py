bookdict = {
  "Claudia Carroll": "the secrets of primrose square",
  "Matt Haig": "Reasons to stay alive, notes on a nervous planet, how to stop time",
  "Liane Moriarty": "Big Little Lies, The apple never falls, nine perfect strangers",
  "Roald Dahl": "Charlie and the chocolate factory, The twits, Boy, Going Solo"
}

user = input("Choose an Author: ")

x = bookdict.get(user)
print(x)

