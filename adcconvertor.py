#ADC convetor

Number_of_bits_in_ADC = int(input("enter the number of bits in ADC: "))	
Analog_Voltage_input_to_ADC	 = int(input("enter the voltage input to the adc: "))
Reference_voltage_to_ADC = int(input("Enter reference voltage to ADC: "))

#OUTPUT
Numeric_Digital_Output= (pow(2,Number_of_bits_in_ADC)*Analog_Voltage_input_to_ADC)//Reference_voltage_to_ADC
Binary_Digital_Output = bin(int(Numeric_Digital_Output))

print(f"numeric degital output {Numeric_Digital_Output}")
print(f"binary digital output {Binary_Digital_Output[2:]}")