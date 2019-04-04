# import os
# os.system("cd..")
#
# for i in range(1):
# 	os.system("./paste-feats ark:../mfcc/raw_mfcc_test." + str(i + 1) + ".ark" + " ark:../plp/raw_plp_test." + str(i + 1) + ".ark" + " ark:raw_mfcc+plp_test." + str(i + 1) + ".ark")
# 	os.system("./paste-feats ark:../mfcc/raw_mfcc_train." + str(i + 1) + ".ark" + " ark:../plp/raw_plp_train." + str(i + 1) + ".ark" + " ark:raw_mfcc+plp_train." + str(i + 1) + ".ark")

import os

for i in range(1):
	os.system("./paste-feats --length-tolerance=2 ark:../mfcc/raw_mfcc_test." + str(i + 1) + ".ark" + " ark:../plp/raw_plp_test." + str(i + 1) + ".ark" + " ark:raw_mfcc+plp_test." + str(i + 1) + ".ark")
	os.system("./paste-feats --length-tolerance=2 ark:../mfcc/raw_mfcc_train." + str(i + 1) + ".ark" + " ark:../plp/raw_plp_train." + str(i + 1) + ".ark" + " ark:raw_mfcc+plp_train." + str(i + 1) + ".ark")

