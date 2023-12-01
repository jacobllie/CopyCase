# encoding: utf8


# Region codes:

# Brain
brain_whole_codes = [401]
brain_partial_codes =  list(range(402, 415+1))
brain_codes = brain_whole_codes + brain_partial_codes

# Head Neck
head_neck_codes = [100, 101, 102, 116, 117,118,120,121,122,123,124,125,126,128,129,130,140,141, 142,144,145,146,148,150,151,152,154,155,156,158,160, 162, 164,166,170,171,172, 174, 175, 176, 178, 179, 180, 181]

larynx_codes = [164]
# Esophagus
esophagus_codes = [255]

# Breast
breast_partial_l_codes = [273]
breast_partial_r_codes = [274]
breast_partial_codes = breast_partial_l_codes +breast_partial_r_codes 
breast_tang_l_codes = [239, 275]
breast_tang_r_codes = [240, 275]
breast_tang_codes = breast_tang_l_codes + breast_tang_r_codes
breast_reg_l_codes = [241, 243, 276]
breast_reg_r_codes = [242, 244, 276]
breast_reg_codes = breast_reg_l_codes + breast_reg_r_codes
breast_l_codes = [239, 241, 243, 273, 275, 276]
breast_r_codes = [240, 242, 244, 274, 275, 276]
breast_tang_reg_l_codes = [239, 241, 243]
breast_tang_reg_r_codes = [240, 242, 244]
breast_not_thorax_codes = [273, 274, 239, 240, 243, 244]
breast_tang_and_partial_codes = breast_partial_codes + breast_tang_codes
breast_tang_and_partial_l_codes = breast_partial_l_codes + breast_tang_l_codes
breast_tang_and_partial_r_codes = breast_partial_r_codes + breast_tang_r_codes
breast_codes = breast_partial_r_codes + breast_partial_l_codes +breast_tang_l_codes + breast_tang_r_codes + breast_reg_l_codes + breast_reg_r_codes

# Lung
lung_codes = [245, 246, 247, 248, 249, 250, 278, 279]
lung_r_codes = [248, 250]
lung_l_codes = [247, 249]
lung_mediastinum_codes = [224, 225, 226, 228, 245, 246, 278, 279]
lung_and_mediastinum_codes = lung_codes + lung_mediastinum_codes

liver_codes = [307]

# Palliative
palliative_head_codes = list(range(1, 20+1))  + list(range(501, 506+1))
palliative_head_codes.extend((110, 111, 112, 114))
palliative_neck_codes = list(range(21, 29 +1)) 
palliative_neck_codes.extend(( 416, 517,518))
palliative_thorax_codes = list(range(30, 43+1)) + list(range(200, 223+1)) + list(range(231, 238+1)) + list(range(251, 254+1)) + list(range(256, 258+1)) + list(range(417, 419+1)) + list(range(518, 520+1)) + list(range(530, 538+1))
palliative_thorax_codes.extend((549, 550, 553, 554))
palliative_thorax_and_abdomen_codes = [521, 522]
palliative_abdomen_codes = list(range(62, 69+1)) + list(range(300, 311+1))
palliative_abdomen_codes.extend((315, 316, 318, 320, 321, 322, 523, 351, 352, 259, 260))
palliative_abdomen_and_pelvis_codes = [524]
palliative_pelvis_codes = list(range(70, 85+1)) + list(range(353, 354+1)) + list(range(512, 514+1)) + list(range(525, 527+1)) + list(range(541, 546+1))
palliative_pelvis_codes.extend((312, 313, 314, 324, 325, 326, 328, 330, 332, 333, 334, 335, 336, 338, 344, 349, 373, 374, 385, 386, 573, 574))
palliative_other_codes = list(range(44, 61 +1)) + list(range(86, 91 +1)) + list(range(261, 272 +1)) + list(range(585, 594 +1)) + list(range(561, 572 +1))
palliative_other_codes.extend((375, 376, 377, 378, 387, 388, 389, 390, 393, 394, 575, 576, 577, 578, 900, 400))
palliative_codes = palliative_head_codes + palliative_neck_codes + palliative_thorax_codes + palliative_thorax_and_abdomen_codes + palliative_abdomen_codes + palliative_abdomen_and_pelvis_codes + palliative_pelvis_codes + palliative_other_codes
palliative_columna_codes = list(range(517, 526+1))
palliative_columna_codes.extend((512, 416, 417, 418, 419))
palliative_cervical_codes = [517, 518]
palliative_thoracal_codes = [519, 520, 521, 522]
palliative_lumbal_codes = [523, 524, 525]
#palliative_columna_codes = palliative_cervical_codes + palliative_thoracal_codes + palliative_lumbal_codes
# Palliative: Stereotactic
stereotactic_pelvis_codes = [513, 514, 527, 573, 574, 575, 576, 577, 578]
stereotactic_thorax_not_spine_codes = list(range(530, 538+1))
stereotactic_thorax_not_spine_codes.extend((549, 550, 553, 554))
stereotactic_spine_thorax_codes = [519, 520, 521, 522]
stereotactic_spine_pelvis_codes = [523, 524, 525]
stereotactic_thorax_codes = stereotactic_thorax_not_spine_codes + stereotactic_spine_thorax_codes
bone_stereotactic_codes = stereotactic_pelvis_codes + stereotactic_spine_pelvis_codes + stereotactic_thorax_codes

# Bladder
bladder_codes = [341, 359]

# Gyn
gyn_codes = [312, 345, 346, 347, 350, 360]
cervix_codes = [347]
vulva_codes = [350]
gyn_except_vulva_codes = [312, 345, 346, 347, 360]
# Prostate
prostate_only_codes = [342]
prostate_vesicles_codes = [343, 355]
prostate_bed_codes = [348, 356]

prostate_codes = prostate_only_codes + prostate_vesicles_codes + prostate_bed_codes
#prostate_codes = [342, 343, 348]
# Rectum
rectum_codes = [340, 357, 358]

whole_pelvis_codes = [312, 512]

# Regions where conventional planning and vmat is both done:
conventional_and_vmat_site_codes = breast_reg_codes +brain_whole_codes

