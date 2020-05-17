#!/usr/bin/python
# coding=utf-8
import os
import json
from unidecode import unidecode
from transliterate import translit, get_available_language_codes

o_paths = ("./orig_trans", "./transliterd")

def mkdir_translit(path):
	if not os.path.exists(path):
		os.mkdir(path, 7777)
set(map(mkdir_translit, o_paths))


if __name__ == "__main__":
	with open("words_alpha") as f: # check the wordlist
		to_trans_dsets = [nn for nn in f.read().split("\n") if bool(nn) and nn.isalpha()] # filter the blanks
	
	for to_trans in to_trans_dsets:
		done_word = False
		while not done_word:
			#data = os.popen("proxychains trans -b -t=af+sq+am+ar+be+hy+az+ba+eu+bn+bs+bg+yue+ca+ceb+ny+zh-CN+co+hr+cs+da+nl+mhr+emj+eo+et+fj+tl+fi+fr+fy+gl+ka+de+el+gu+ht+ha+haw+he+mrj+hi+hmn+id+mww+hu+is+ig+ga+it+ja+jv+kn+kk+km+tlh+th-Qaak+ko+ku+ky+lo+la+lv+lt+lb+mk+mg+ms+ml+mt+mi+mr+mn+my+ne+no+pap+ps+fa+pl+pt+pa+otq+ro+sr-Latn+ru+sm+gd+sr-Cyrl+st+sn+sd+si+sk+sl+so+es+su+sw+sv+ty+tg+ta+tt+te+th+to+tr+udm+uk+ur+uz+vi+cy+xh+yi+yo+yua+zu \"{0}\"".format(to_trans)).read()
			data = os.popen("proxychains trans -b -t=af+sq+am+ar+be \"hello\"").read()
			
			if bool(data.replace("\n","")):
				lang_dat = data.split("\n")[:-1]
				for _dat in lang_dat:
					try:
						cc = unidecode(u"{0}".format(_dat))
					except:
						cc = translit(u"{0}".format(_dat), reversed=True)
					
					alpha_filter = "".join(filter(lambda x: str(x).isalpha(), str(cc)))
					print(_dat, alpha_filter)
					
					with open(o_paths[0]+"/{0}".format(to_trans),"a") as f:
						f.write(_dat + "\n")
					
					with open(o_paths[1]+"/{0}".format(to_trans),"a") as f:
						f.write(alpha_filter + "\n")
					
					# set to done!
					done_word = True
			else:
				os.system("service tor restart")



