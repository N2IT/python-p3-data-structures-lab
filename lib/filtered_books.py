books = [

   {"Title":"Angels and Demons", "Author":"Dan Brown", "Price":500},

   {"Title":"Gone Girl", "Author":"Gillian Flynn", "Price":730},

   {"Title":"The Silent Patient", "Author":"Alex Michaelidis", "Price":945},

   {"Title":"Before I Go To Sleep", "Author":"S.J Watson", "Price":400}


   ]

def func(book):

    if book["Price"] > 500:

        return True

    else:

        return False

filtered_object = filter(func, books)

for d in filtered_object:

    print(dict(d)["Title"])