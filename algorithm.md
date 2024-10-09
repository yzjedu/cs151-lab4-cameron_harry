# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1) Output the description of the program
2) Set variable additional_cost to 0
3) Set variable additional_data to 0 
4) Set variable total_cost to 0 
5) Set variable initial_cost to 0 
6) Prompt user to input if their package is ‘green’, ‘blue’, or ‘purple’ and store the input into a variable named package 
7) Set the input to all lowercase 
8) While user input does not equal ‘green’, ‘blue’, or ‘purple’ 
   A) Output ‘The plan you have entered is invalid’ 
   B) Prompt user to input the choices from ‘green’, ‘blue’, or ‘purple’ and store the input into a variable named package 
9) If package is equal to ‘green’  
   A) Set initial_cost to 49.99 
   B) Set additional_cost to 15
10) Otherwise if package is equal to ‘blue’ 
    A) Set initial_cost to 70 
    B) Set additional cost to 10 
11) Otherwise if package equals ‘purple’ 
    A) Set initial_cost to 99.95
12) If user input does not equal ‘purple’ 
    A) Prompt user to input how many additional data they want for that month and store it in a variable named additional_data 
    B) If user enters a decimal, round up the decimal to the next integer 
    C) While user input is less than 0 
        a) Output ‘The value you have entered is invalid. Please enter a value that is equal to or more than 0 
        b) Prompt user to input how many additional data they want and store in a variable named additional_data
        c) If user enters a decimal, round up the decimal to the next integer
13) If user input equals ‘green’ and coupon equals ‘yes’ 
    A) Calculate the equation (initial_cost) + (additional_data * additional_cost) and set it to total_cost 
    B) Calculate (total_cost – 20)
14) If user input equals 'green' 
    A) Calculate the equation (initial_cost) + (additional_data * additional_cost) and set it to total_cost
15) Otherwise if user input equal ‘blue’ 
    A) Calculate the equation (initial_cost) + (additional_data * additional_cost) and set it to total_cost
16) Otherwise
    A) Output ‘Your total cost is $99.95’
17) Output ('Your total cost is:' total_cost)
