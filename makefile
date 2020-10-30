help:
	$(info Uses XOR to encode / decode user inputted string)
	$(info Input as: make run ARGS="human/numOut keyfilename textfilename")

run:
	python3 xor.py $(ARGS)