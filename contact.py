contacts  = {}


while True:
    print('\nContact Book App')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. search contact')
    print('6. Count contact')
    print('7. Exit')

    choice = input('Enter Your Choice = ')

    if choice == '1':
        name = input('Enter Your Name = ')
        if name in contacts:
            print(f'contact name {name} already exists!')
        else:
            age = input('Enter Age = ')
            email = input('Enter Email = ')
            mobile = input('Enter Mobile Number = ')
            contacts[name] = {'age':int(age),'email':(email),'mobile':(mobile)}
            print(f'contact name {name} has been createdsuccessuflly!')
    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age:{age}, Mobile Number: {mobile}')
        else:
            print('Contact not found!')

    elif choice == '3':
        name = input('Enter Name To Update Contact = ')
        if name in contacts:
            age = input('Enter Update Age = ')
            email = input('Enter Update Number = ')
            mobile = input('Enter Update Mobile Number = ')
            contact[name] = {'age':int(age),'email':email,'mobile':mobile}
        else:
            print('Contact not Found!')

    elif choice =='4':
            name = input('Enter contact name to deleted = ')
            if name in contacts:
               del contacts [name]
               print(f'contact name {name} has been deleted successfully!')
            else:
                print('Contact not Found')
    elif choice =='5':
        search_name = input('Enter contact name to search = ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower()in name.lower():
                print(f'found - Name {name}, Age: {age}, Mobile Number:{mobile},Email:{email}')
                found = True
            if not found :
                print('Not contacts found with that name')
   
    elif choice == '6':
        print(f'Totalcontacts in your book : {len(contacts)}')

    elif choice == '7':
        print('Good Bye...Closing The Program')
        break
    else:
        print('Invalid input')