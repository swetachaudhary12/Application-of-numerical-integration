# Application-of-numerical-integration


**Introduction:**
 Designed for calculating the toughness of a material using numerical integration methods in Python. It reads strain and stress data from an Excel file, processes the data, and applies numerical integration rules (Trapezoidal, Simpson's 1/3, and Simpson's 3/8) to determine material toughness.

**Overview:**

1. Data Processing: The strain and stress data are then extracted from the DataFrame . 
2. Numerical Integration Functions: Three numerical integration functions, 'Trap', 'Simp13', and 'Simp38', are defined to calculate area under the curve using the Trapezoidal, Simpson's 1/3, and Simpson's 3/8 rules, respectively.

3. Material Toughness Calculation: The main function 'Uneven' iterates through the data points, applying appropriate integration rules based on the data pattern to calculate the material toughness.

4. Result Display: The calculated material toughness value is displayed as output.




