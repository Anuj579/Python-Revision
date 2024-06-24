# Program to find the given post is talking about Anuj 

post = input("Enter post: ")

if 'Anuj'.lower() in post.lower():
    print("Yes, the post is talking about Anuj")
else:
    print("No, the post is not talking about Anuj")