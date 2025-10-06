#!/usr/bin/env python3

import re
import sys

#inStr = sys.stdin.read()

#for line in sys.stdin:
#	print(f'Input : {line}')

# inStr = "942*t3*t22*x^19*y^22 + 942*t3*t22*x^19*y^22 + 942*t3*t22*x^19*y^22"
# inStr = "(-3209472000/78961*t0^2*t72^9 + 9910947200/104939169*t72^12)/t0^26"
# NinStr = "(175*t11^3 + 756*t11*t15 + 1944*t39)"
# 
# NinStr = """(21163161600*t0*t8 - 54419558400*t0*l1 - 
#                                 4232632320*t8*l1 + 36515843*t11^6*l1 + 
#                                 287862120*t11^4*t15*l1 + 410417280*t11^3*t39*l1 
#                                 + 615625920*t11^2*t15^2*l1 + 1363848192*t11*t15\
#                                 *t39*l1 + 227308032*t15^3*l1 + 846526464*t39^2*\
#                                 l1 + 10883911680*l1^2)
# 								"""
# 
inStr = r"""
  19 │  -38/66   =   -19/33 ┬ 
                                (3*t0 - 1) or 
                                (2178*t0*t4 - 726*t4 + 35*t7^4)
     │                      │
                                (3*t0 - 1) or 
                                (2582935938*t0^3*t5 - 1721957292*t0^2*t1*t4 + 
                                249043410*t0^2*t4^2*t7^2 - 260902620*t0^2*t4*t7\
                                ^2 - 2582935938*t0^2*t5 + 166028940*t0^2*t7^3*t\
                                8 + 1147971528*t0*t1*t4 - 69178725*t0*t1*t7^4 - 
                                166028940*t0*t4^2*t7^2 + 8741040*t0*t4*t7^6 + 
                                173935080*t0*t4*t7^2 + 860978646*t0*t5 - 
                                6708240*t0*t7^6 - 110685960*t0*t7^3*t8 - 
                                191328588*t1*t4 + 23059575*t1*t7^4 + 
                                27671490*t4^2*t7^2 - 2913680*t4*t7^6 - 
                                28989180*t4*t7^2 - 95664294*t5 + 44720*t7^10 + 
                                2236080*t7^6 + 18447660*t7^3*t8)
     │                      │
                                (t7) or 
                                (3*t0 - 1)

"""
# 
# inStr = "t3+y^12345"




outStr = inStr

#outStr= outStr.replace("\\\n","")

# Remove newlines inside polynomials
outStr= re.sub(r"\\\n[ \t]*", "", outStr)
outStr = re.sub(r"\+[ \t]*\n[ \t]*", "+ ", outStr)
outStr = re.sub(r"\-[ \t]*\n[ \t]*", "- ", outStr)
# Remove product signs
outStr = outStr.replace("*", " ")
# t1 -> t_1
outStr = re.sub(r"([a-zA-Z])(\d)(?!\d)", r"\1_\2", outStr)
# t12 -> t_{12}
outStr = re.sub(r"([a-zA-Z])(\d\d+)", r"\1_{\2}", outStr)
# No space before exponentiation"
outStr = re.sub(r"[ ]*\^", r"^", outStr)
# ^12 -> ^{12}
outStr = re.sub(r"\^(\d\d+)", r"^{\1}", outStr)

print(outStr)

