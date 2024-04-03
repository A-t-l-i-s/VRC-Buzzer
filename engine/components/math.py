from engine.require import *





__all__ = ("Components_add", "Components_sub", "Components_mul", "Components_div", "Components_rdiv", "Components_exp")





def Components_add(value, constant, swap):
	if (swap):
		return constant + value

	else:
		return value + constant



def Components_sub(value, constant, swap):
	if (swap):
		return constant - value

	else:
		return value - constant



def Components_mul(value, constant, swap):
	if (swap):
		return constant * value

	else:
		return value * constant



def Components_div(value, constant, swap):
	if (swap):
		return constant / value

	else:
		return value / constant



def Components_rdiv(value, constant, swap):
	if (swap):
		return constant // value

	else:
		return value // constant



def Components_exp(value, constant, swap):
	if (swap):
		return constant ** value

	else:
		return value ** constant





