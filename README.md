# ShoppingBasket


1. To Download the ShoppingBasket project folder to the local machine.
	-->click on the green button on the ShoppingBasket and download zip folder.

2. Open pycharm or similar ide.
	--> In pycharm --> file --> open --> go the folder path in local machine and click open.

3. Once opened allow interpreter to complete the setup. 

4. Total of 6 modules available for this project.
	-->main.py and unit_test.py available on project folder itself, 4 function modules available in function folder

5. Open main.py and allow indexing to happen.

6. After that we can execute the main.py module by selecting Run menu on the top left of the IDE
	-->In Run menu--> select Run option

7. Run will prompt input from console, please enter the items in correct format after PriceBasket. 

	Example :
	> PriceBasket Apples Bread
	
8. Until the correct format is entered further processing won't happen, main module will validate the format 
     and whether the item is present in stock. It will keep on prompting the input for correct format.

9. Once the initial items are entered correctly, main module again prompt for item quantity for each item.
     Please enter the quantity needed in integer.

	Example :
	> Apples_Quantity = 2
	> Bread_Quantity = 2

10. After entering the quantity main module pass controls to various functions and provide output like below.

	Example:
	>subtotal: £3.60
	>Apples 10% off: £0.20
	>discount_total: £0.20
	>total_price: £3.40

11. Again repeat from instruction 6., for various scenario's .

12. Unit test program is available in main folder with module name as unit_test.py, it has test cases for all the function modules.

13. To execute unit test program we need to install pytest package. 

14. Go to command prompt, open project directory and run the below command.
	-- > pip install pytest 

15. In commad prompt, enter
	--> pytest unit_test.py

16. This will provide test results of various cases for all the functions in unit test program.
      Change the various input parameters in unit_test.py module and repeat instruction 15., to run for various scenario's.
