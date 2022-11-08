# pyTools
List of python based tools that were created/used for CTFs and to get a better understanding of things.

* #### Affine Cipher Decoder
	* `$ ./affine_decode.py "String to decode"`
		* If no string is provided on CLI, you will be prompted for a string
	* Because of how the affine cipher works, a dictionary.txt file also needs to be provided.  It will attempt to decode the data with all possible variations, but then cross reference those results with the dictionary file.  If the decoded data contains a word from the dictionary, it will output that data along with the key data that was used to find it.  This means that you will likely get false positives in the results, but _hopefully_ only one will have a full english string of text.
	* To Do List
		* Add a more robust `dictionary.txt` so that it can be more precise
		* Clean up the code/variable names to be less INTENSE

* #### Barcode Decoder
	* `$ ./barcode_decode.py /path/to/barcode/image`
		* If no path is provided on CLI, you will be prompted for one
	* This requires an additional library:  pyzbar
	  `pip install pyzbar`
	  It takes an image of a barcode and parses the image and decodes the obtained barcode data as ASCII.

* #### LSB Extractor
	* `$ ./lsb_decode.py /path/to/image`
		* If no path is provided on CLI, you will be prompted for one
	* A _very very_ basic LSB Extractor.  Given an image, it will extract the LSB of each pixel and then re-create another image containing that data and show it to you.  If the LSB was hiding ASCII data, this will not do much for you.
	* To Do List
		* Add ASCII Dump of the LSB data -- This won't always be meaningful data, but if its ASCII data that was hidden, then it would be nice to see.
			* Possible could implement the dictionary trick from Affine cipher so that this doesn't output unless its meaningful data.
		* Add binary data output so that the data extracted is written into a new file that can then be analyzed (IE: Hiding a ZIP in the LSB)

* #### Morse Code Decoder
	* `$ ./morse_decode.py "String containing morse code"`
		* If no string is provided on CLI, you will be prompted for one 
	* Decodes morse code strings that use `.` and `-` as the characters.  It also assumes that words are separated with spaces.  If this is not the case, then you could just end up with a run of characters.
	* To Do List
		* Change the CLI to parse arguments (or prompt for them if not provided) to ask for the delimiter and the characters that were used instead of the standard dots and slashes.

* #### Railfence Decoder
	* `$ ./rail_decode.py "string to decode" Rails(INT) Cols(INT)`
		* If all arguments are not provided at the CLI, then you will be prompted for all of them.
	* Uses the railfence cipher to decode strings using the specified Rails and Columns values.  If using the prompt mode, it provides the means to enter a brute-force mode where you can specify a Max Rails to try and it will spit out all those combinations.
	* To Do List
		* Allow for brute-force mode to be triggered from the CLI arguments
		* Implement the dictionary trick from affine cipher in brute-force mode so that only meaningful output is printed along with the key.

* #### ROT Decoder
	* `$ ./rot_decode.py "String to decode" RotValue(INT)`
		* If all arguments are not provided on the CLI, it will prompt for them
	* Classic Caesar Cipher decoding.  If a rot value of `0` is specified, it will brute-force all 26 possible rotations and print them.
	* To Do List
		* Implement the dictionary trick from the affine cipher in brute-force mode so that only the meaningful output is printed along with the key.

* #### T9 Decoder
	* `$ ./t9_decode.py "String of T9 Numbers to decode"`
		* If a string is not provided on CLI, it will prompt for the data
	* Decodes the old-school, awesomely fast, T9 codes that used to be used for text messaging.
	* To Do List
		* Allow for arguments to be parsed from CLI for the delimiters that were used (IE: `" "` for the word delimiter and `"-"` for the character delimiter.

* #### Vigenere Decoder
	* `$ ./vigenere_decode.py "ciphertext to decode" "key"`
		* If all arguments are not provided on CLI, it will prompt for them
	* Does the standard vigenere cipher, using the provided key, in reverse to obtain the original ASCII value of the string.  If they key is not known, it is not possible to decode without bruteforce which would take forever.

