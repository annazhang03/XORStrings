help:
	$(info Uses XOR to encode / decode user inputted string)
	$(info Input as: make run ARGS="mode keyfilename textfilename")
	$(info mode argument should be either "human" or "numOut")

run:
	python3 xor.py $(ARGS)