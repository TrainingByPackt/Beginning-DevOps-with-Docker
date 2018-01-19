print('Welcome to Codechef')
print('Please enter your name')
name = input()
print('Please enter your age')
age = input()
if age >= str(18):
    print('Welcome', name, 'please enter')
    print('Please select your coding level:')   
    print('1. Beginner')
    print('2. Intermediate')
    print('3. Advanced')
    choice = str(input())
    if choice == '1':
        print('You will be taught basic programming skills.')
        print ('Please select your module:')
        mod  = input()
        
    elif choice == '2':
        print('You will be taught intermediate programming skills')
    elif choice == '3':
        print('You are pro. You will be taught advanced concepts.')
    else:
        print('You have not entered the correct choice')
    
   
else:
    print('Sorry not allowed')



