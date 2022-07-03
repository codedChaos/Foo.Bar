# coding=utf-8
#!/usr/bin/python

import random
import time

def timerfunc(func):
	"""
	A Timer Decorator
	"""
	def function_timer(*args, **kwargs):
		"""
		A nested function for timing other functions
		"""
		start = time.time()
		value = func(*args, **kwargs)
		end = time.time()
		runtime = end - start
		msg = "The runtime for {func} took {time} seconds to complete"
		print(msg.format(func=func.__name__, time=runtime))
		return value
	return function_timer

@timerfunc
def solution0(x):
	"""
	>>> solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
	"did you see last night's episode?"
	>>> solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
	"Yeah! I can't believe Lance lost his job at the colony!!"
	"""
	import string
	# string variable holding encrypted character set in order
	encryptedKeyMap = str(sorted(string.ascii_lowercase, reverse = True))
	# string variable holding decrypted character set in order
	decryptedKeyMap = str(sorted(string.ascii_lowercase))
	# translation table that maps the two
	superSecretDecoderRing = string.maketrans(encryptedKeyMap,
	                                          decryptedKeyMap)
	return x.translate(superSecretDecoderRing)

@timerfunc
def solution1(x):
	"""
	>>> solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
	"did you see last night's episode?"
	>>> solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
	"Yeah! I can't believe Lance lost his job at the colony!!"
	"""
	import string
	encodedTxt = x
	decodedTxt = str()
	aDict = dict(zip(string.ascii_lowercase,
	                 sorted(string.ascii_lowercase, reverse=True)))
	for char in encodedTxt:
		newChar = char
	 	if char.isalpha():
	 		if char.islower():
	 			newChar = aDict[char]

	 	decodedTxt = decodedTxt + newChar
	return decodedTxt

if __name__ == '__main__':
	solution0("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
	solution0("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
	solution1("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
	solution1("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
