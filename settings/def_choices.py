# encoding: utf8

# Import local files:
import property as P

# Regions:
brain = P.Property('Hjerne', 'brain', next_category='omfang', default = True)
head_neck = P.Property('Øre-nese-hals', 'head_neck', next_category='indikasjon')
lung = P.Property('Lunge', 'lung', next_category = 'intensjon')
breast = P.Property('Bryst', 'breast', next_category = 'omfang')
liver = P.Property('Lever (SBRT)', 'liver', next_category = '')
bladder = P.Property('Blære', 'bladder')
gyn = P.Property('Gyn','gyn',next_category = 'omfang')
prostate = P.Property('Prostata', 'prostate', next_category = 'omfang')
anus = P.Property('Anus', 'anus', next_category = 'stadium')
rectum = P.Property('Rektum', 'rectum', next_category = 'indikasjon')
esophagus = P.Property('Øsofagus', 'esophagus', next_category = 'omfang' )
#gi = P.Property('GI', 'gi', next_category = 'diagnose')
other = P.Property('Palliativ (skjelett og øvrig bløtvev)', 'other', next_category = '')
#other = P.Property('Skjelett (SBRT)', 'other', next_category = 'region') 

# Brain: Scope:
brain_whole = P.Property('Hele hjernen', 'whole', parent=brain, default = True)
brain_partial = P.Property('Del av hjerne', 'part', parent=brain, next_category = '')
brain_stereotactic = P.Property('Stereotaksi','stereotactic', parent = brain, next_category ='antall målvolum')

# Brain: Stereotactic
brain_stereo_nr1 = P.Property('1','one', parent = brain_stereotactic, next_category = '', default = True)
brain_stereo_nr2 = P.Property('2','two', parent = brain_stereotactic, next_category = '')
brain_stereo_nr3 = P.Property('3','three', parent = brain_stereotactic, next_category = '')
brain_stereo_nr4 = P.Property('4','four', parent = brain_stereotactic, next_category = '')
for a in [brain_partial, brain_stereo_nr1, brain_stereo_nr2, brain_stereo_nr3, brain_stereo_nr4]:
  brain_with_oar =P.Property('Med AI-og MBS-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
  brain_without_ai =P.Property('Uten AI- og MBS-strukturer', 'without_ai', parent = a)

# Head & Neck
head_neck_primary = P.Property('Primær strålebehandling','primary',parent = head_neck, next_category ='indikasjon',default = True)
head_neck_postop = P.Property('Postoperativ strålebehandling','postop',parent = head_neck, next_category ='')
head_neck_palliative =P.Property('Palliativ strålebehandling','palliative', parent = head_neck)


# Head & Neck: indication
head_neck_glottis_t1 = P.Property('Glottis T1N0','glottis_T1',parent = head_neck_primary, next_category ='stadium')
head_neck_glottis = P.Property('Spyttkjertelkreft høyere stadium enn T1 (54-60-70)','glottis',parent = head_neck_primary, next_category ='antall affiserte lymfeknuter')
head_neck_other = P.Property('Alle andre indikasjoner i ØNH-regionen (50-60-68)','other',parent = head_neck_primary, next_category ='antall affiserte lymfeknuter', default = True)


head_neck_glottis_a = P.Property('Glottis T1A (66 Gy)','glottis_a',parent = head_neck_glottis_t1, next_category ='',default = True)
head_neck_glottis_b = P.Property('Glottis T1B (68 Gy)','glottis_b',parent = head_neck_glottis_t1, next_category ='')


# Head & Neck: Radical surgery? 
head_neck_low_risk = P.Property('Radikalt operert (R0), lavrisiko (50-60)','low risk',parent = head_neck_postop,next_category ='side')
head_neck_radical = P.Property('Radikalt operert (R0) (54-60)','radical',parent = head_neck_postop, next_category ='side',default = True)
head_neck_not_radical = P.Property('Ikke radikalt operert (R+) (54-60-64)', 'not_radical',parent = head_neck_postop,next_category ='side')

for side in [head_neck_low_risk,head_neck_radical,head_neck_not_radical]:
  head_neck_both = P.Property('Både høyre og venstre','both',parent = side,default = True)
  head_neck_right = P.Property('Høyre','right',parent = side)
  head_neck_left = P.Property('Venstre','left',parent = side)

# Head & Neck: Number of affected lymph nodes:
for nr in [head_neck_glottis, head_neck_other]:
  head_neck_nr0 = P.Property('0','zero', parent = nr, next_category ='side')
  head_neck_nr1 = P.Property('1','one', parent = nr, next_category ='side', default = True)
  head_neck_nr2 = P.Property('2','two', parent = nr, next_category ='side')
  head_neck_nr3 = P.Property('3','three', parent = nr, next_category ='side')
  head_neck_nr4 = P.Property('4','four', parent = nr, next_category ='side')
  # Head & Neck: Side:
  for side in [head_neck_nr0,head_neck_nr1,head_neck_nr2,head_neck_nr3, head_neck_nr4]:
    head_neck_both = P.Property('Både høyre og venstre','both',parent = side,default = True)
    head_neck_right = P.Property('Høyre','right',parent = side)
    head_neck_left = P.Property('Venstre','left',parent = side)

# Lung
lung_curative = P.Property('Kurativ', 'curative', parent = lung, next_category = 'diagnose', default = True)
lung_palliative = P.Property('Palliativ','palliative', parent = lung, next_category = '')
lung_stereotactic = P.Property('Stereotaksi', 'stereotactic', parent = lung, next_category ='side')

# Lung curative:
lung_nsclc = P.Property('Ikke-småcellet lungekreft/ Småcellet lungekreft (med 4DCT)','4dct', parent = lung_curative, next_category ='ICTV margin', default = True)
lung_narlal = P.Property('NARLAL2','narlal', parent = lung_curative, next_category ='antall lymfeknuter')
#lung_sclc = P.Property('Småcellet lungekreft (uten 4DCT)','sclc', parent = lung_curative)
#lung_pancoast =P.Property('Pancoast', 'pancoast', parent = lung_curative)
#lung_postop =P.Property('Postoperativ', 'postop', parent = lung_curative)

# Lung ICTV margin
lung_5mm = P.Property('5 mm','5', parent = lung_nsclc, next_category ='antall lymfeknuter', default = True)
lung_7mm = P.Property('7 mm','7', parent = lung_nsclc, next_category ='antall lymfeknuter')

# Lung palliative:
lung_with_4dct = P.Property('Med 4DCT', 'with', parent = lung_palliative, next_category ='antall lymfeknuter', default = True)
lung_without_4dct = P.Property('Uten 4DCT', 'without', parent = lung_palliative, next_category ='')

lung_without_4dct_with_oar =P.Property('Med AI-og MBS-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = lung_without_4dct, default = True)
lung_without_4dct_without_ai =P.Property('Uten AI- og MBS-strukturer', 'without_ai', parent = lung_without_4dct)

# Lung number of lymph nodes:
for p in [lung_5mm, lung_7mm,lung_narlal,lung_with_4dct]:
  lung_ln_0 = P.Property('0','zero', parent = p, next_category ='')
  lung_ln_1 = P.Property('1','one', parent = p, next_category ='', default = True)
  lung_ln_2 = P.Property('2','two', parent = p, next_category ='')
  lung_ln_3 = P.Property('3','three', parent = p, next_category ='')
  lung_ln_4 = P.Property('4','four', parent = p, next_category ='')
  lung_ln_5 = P.Property('5','five', parent = p, next_category ='')
  lung_ln_6 = P.Property('6','six', parent = p, next_category ='')
  for a in [lung_ln_0, lung_ln_1, lung_ln_2, lung_ln_3, lung_ln_4, lung_ln_5, lung_ln_6]:
    lung_with_oar =P.Property('Med AI-og MBS-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
    lung_without_ai =P.Property('Uten AI- og MBS-strukturer', 'without_ai', parent = a)

# Lung stereotactic:
stereo_lung_right = P.Property('Høyre','right', parent = lung_stereotactic, next_category ='antall målvolum', default = True)
stereo_lung_left = P.Property('Venstre','left', parent = lung_stereotactic, next_category ='antall målvolum')

for side in [stereo_lung_right, stereo_lung_left]:
  lung_stereo_nr1 = P.Property('1','one', parent = side, next_category ='', default = True)
  lung_stereo_nr2 = P.Property('2','two', parent = side, next_category ='')
  lung_stereo_nr3 = P.Property('3','three', parent = side, next_category ='')
  for a in [lung_stereo_nr1, lung_stereo_nr2, lung_stereo_nr3]:
    lung_with_oar =P.Property('Med AI-og MBS-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
    lung_without_ai =P.Property('Uten AI- og MBS-strukturer', 'without_ai', parent = a)


liver_without_4dct = P.Property('Med DIBH', 'without', parent = liver, next_category ='antall målvolum', default = True)
liver_with_4dct = P.Property('Med 4DCT', 'with',next_category ='antall målvolum', parent = liver)

for l in [liver_without_4dct, liver_with_4dct]:
  liver_stereo_nr1 = P.Property('1','one', parent = l, next_category = '', default = True)
  liver_stereo_nr2 = P.Property('2','two', parent = l, next_category = '')
  liver_stereo_nr3 = P.Property('3','three', parent = l, next_category = '')

  for a in [liver_stereo_nr1, liver_stereo_nr2, liver_stereo_nr3]:
    liver_with_oar =P.Property('Med AI-og MBS-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
    liver_without_ai =P.Property('Uten AI- og MBS-strukturer', 'without_ai', parent = a)

#Breast:
breast_tangential = P.Property('Bryst/brystvegg', 'tang', parent = breast, next_category = 'side', default = True)
breast_locoregional = P.Property('Bryst/brystvegg og regionale lymfeknuter', 'reg', parent = breast, next_category ='')
breast_locoregional_not_one = P.Property('Bryst/brystvegg og regionale lymfeknuter unntatt aksille', 'reg-1', parent = breast, next_category ='')
breast_both = P.Property('Bilateral','both', parent = breast, next_category = 'høyre side')

for b in [breast_locoregional, breast_locoregional_not_one]:
  breast_imn = P.Property('Med parasternale glandler', 'imn', parent = b, next_category = 'side',default = True)
  breast_not_imn = P.Property('Uten parasternale glandler', 'not_imn', parent = b, next_category = 'side')
  # Breast regional: 
  for b in [breast_imn, breast_not_imn]:
    breast_right = P.Property('Høyre','right', parent = b, next_category = '', default = True)
    breast_left = P.Property('Venstre','left', parent = b, next_category = '')
    # Breast youth boost:
    for p in [breast_right, breast_left]:
      breast_without_boost = P.Property('Uten boost 2 Gy x 8', 'without', parent = p, next_category = '', default = True)
      breast_with_boost = P.Property('Med boost 2 Gy x 8','with', parent = p, next_category = '')
      # Breast with, with some or without deep learning structures
      for a in [breast_without_boost, breast_with_boost]:
        breast_with_ai = P.Property('Med alle AI-strukturer', 'with_ai', parent = a, default = True)
        breast_with_oar =P.Property('Med risikoorganer som AI-strukturer', 'with_ai_oar', parent = a)
        breast_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)
  
# Breast tangential: 
breast_right = P.Property('Høyre','right', parent = breast_tangential, next_category = '', default = True)
breast_left = P.Property('Venstre','left', parent = breast_tangential, next_category = '')

# Breast tangential boost:
for p in [breast_right, breast_left]:
  breast_without_boost = P.Property('Uten boost 2 Gy x 8', 'without', parent = p, next_category = '', default = True)
  breast_with_boost = P.Property('Med boost 2 Gy x 8','with', parent = p, next_category = '')
  # Breast with, with OAR or without AI structures
  for a in [breast_without_boost, breast_with_boost]:
    breast_with_ai = P.Property('Med alle AI-strukturer', 'with_ai', parent = a, default = True)
    breast_with_oar =P.Property('Med risikoorganer som AI-strukturer', 'with_ai_oar', parent = a)
    breast_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)

# Breast bilateral
breast_tangential_r = P.Property('Bryst/brystvegg', 'tang', parent = breast_both, next_category = 'høyre side', default = True)
breast_locoregional_r = P.Property('Bryst/brystvegg og regionale lymfeknuter', 'reg', parent = breast_both, next_category ='høyre side')
breast_locoregional_not_one_r = P.Property('Bryst/brystvegg og regionale lymfeknuter unntatt aksille', 'reg-1', parent = breast_both, next_category ='høyre side')

# Breast bilateral boost, tangential on the right side
breast_without_boost_r_1 = P.Property('Uten boost 2 Gy x 8', 'without', parent = breast_tangential_r, next_category ='venstre side', default = True)
breast_with_boost_r_1 = P.Property('Med boost 2 Gy x 8','with', parent = breast_tangential_r, next_category ='venstre side')

# Breast bilateral, tangential on the right side, tangential on the left side
for bbl in [breast_without_boost_r_1, breast_with_boost_r_1]:
  breast_tangential_l_1 = P.Property('Bryst/brystvegg', 'tang', parent = bbl, next_category = 'venstre side', default = True)
  # Breast boost, tangential on the right side, tangential on the left side
  breast_without_boost_tang_l = P.Property('Uten boost 2 Gy x 8', 'without', parent = breast_tangential_l_1, next_category ='', default = True)
  breast_with_boost_tang_l = P.Property('Med boost 2 Gy x 8','with', parent = breast_tangential_l_1, next_category ='')
    # Breast with, with OAR or without AI structures
  for a in [breast_without_boost_tang_l, breast_with_boost_tang_l]:
    breast_with_ai = P.Property('Med alle AI-strukturer', 'with_ai', parent = a, default = True)
    breast_with_oar =P.Property('Med risikoorganer som AI-strukturer', 'with_ai_oar', parent = a)
    breast_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)

# Breast bilateral: tangential on the right side, locoregional on the left side
for bb in [breast_without_boost_r_1, breast_with_boost_r_1]:
  breast_locoregional_l_1 = P.Property('Bryst/brystvegg og regionale lymfeknuter', 'reg', parent = bb, next_category ='venstre side')
  breast_locoregional_not_one_l_1 = P.Property('Bryst/brystvegg og regionale lymfeknuter unntatt aksille', 'reg-1', parent = bb, next_category ='venstre side')
  # With/ without IMN
  for l in [breast_locoregional_l_1, breast_locoregional_not_one_l_1]:
    breast_imn_l_1 = P.Property('Med parasternale glandler', 'imn', parent = l, next_category = 'venstre side',default = True)
    breast_not_imn_l_1 = P.Property('Uten parasternale glandler', 'not_imn', parent = l, next_category = 'venstre side')
    # Breast boost:
    for imn in [breast_imn_l_1 , breast_not_imn_l_1]:
      breast_without_boost_l_1 = P.Property('Uten boost 2 Gy x 8', 'without', parent = imn, next_category ='', default = True)
      breast_with_boost_l_1 = P.Property('Med boost 2 Gy x 8','with', parent =imn, next_category ='')
      # Breast with, with OAR or without AI structures
      for a in [breast_without_boost_l_1, breast_with_boost_l_1]:
        breast_with_ai = P.Property('Med alle AI-strukturer', 'with_ai', parent = a, default = True)
        breast_with_oar =P.Property('Med risikoorganer som AI-strukturer', 'with_ai_oar', parent = a)
        breast_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)

# Breast bilateral: locoregional on the right side
for loco_r in [breast_locoregional_r, breast_locoregional_not_one_r]:
  # With/ without IMN on the right side
  breast_imn_r = P.Property('Med parasternale glandler', 'imn', parent = loco_r, next_category = 'høyre side',default = True)
  breast_not_imn_r = P.Property('Uten parasternale glandler', 'not_imn', parent = loco_r, next_category = 'høyre side')
  # Breast bilateral: with or without boost on the right side:
  for imn_r in [breast_imn_r , breast_not_imn_r]:
    breast_without_boost_r = P.Property('Uten boost 2 Gy x 8', 'without', parent = imn_r, next_category ='venstre side', default = True)
    breast_with_boost_r = P.Property('Med boost 2 Gy x 8','with', parent =imn_r, next_category ='venstre side')
    # Breast bilateral: left side region?
    for b_r in [breast_without_boost_r, breast_with_boost_r]:
      breast_tangential_l = P.Property('Bryst/brystvegg', 'tang', parent = b_r, next_category = 'venstre side', default = True)
      breast_locoregional_l = P.Property('Bryst/brystvegg og regionale lymfeknuter', 'reg', parent =b_r, next_category ='venstre side')
      breast_locoregional_not_one_l = P.Property('Bryst/brystvegg og regionale lymfeknuter unntatt aksille', 'reg-1', parent = b_r, next_category ='venstre side')
      # Breast bilateral: locoregional on the right side, locoregional on the left side
      for loco_l in [breast_locoregional_l, breast_locoregional_not_one_l]:
        # With/ without IMN on the left side
        breast_imn_l = P.Property('Med parasternale glandler', 'imn', parent = loco_l, next_category = 'venstre side',default = True)
        breast_not_imn_l = P.Property('Uten parasternale glandler', 'not_imn', parent = loco_l, next_category = 'venstre side')
        # Breast boost on the left side:
        for imn_l in [breast_imn_l , breast_not_imn_l]:
          breast_without_boost_l = P.Property('Uten boost 2 Gy x 8', 'without', parent = imn_l, next_category ='',  default = True)
          breast_with_boost_l = P.Property('Med boost 2 Gy x 8','with', parent =imn_l, next_category ='')
          # With, with OAR or without AI structures
          for a in [breast_without_boost_l, breast_with_boost_l]:
            breast_with_ai = P.Property('Med alle AI-strukturer', 'with_ai', parent = a, default = True)
            breast_with_oar =P.Property('Med risikoorganer som AI-strukturer', 'with_ai_oar', parent = a)
            breast_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)
          
      # Breast bilateral locoregional on the right side, tangential on the left side
      breast_without_boost_l_1 = P.Property('Uten boost 2 Gy x 8', 'without', parent = breast_tangential_l, next_category ='', default = True)
      breast_with_boost_l_1 = P.Property('Med boost 2 Gy x 8','with', parent = breast_tangential_l, next_category ='')
      # With, with OAR or without AI structures
      for a in [breast_without_boost_l_1, breast_with_boost_l_1]:
        breast_with_ai = P.Property('Med alle AI-strukturer', 'with_ai', parent = a, default = True)
        breast_with_oar =P.Property('Med risikoorganer som AI-strukturer', 'with_ai_oar', parent = a)
        breast_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)





#bladder_without_ln = P.Property('Uten lymfeknuter', 'without', parent = bladder, default = True)      
#bladder_with_ln = P.Property('Med lymfeknuter', 'with', parent = bladder) 

gyn_cervix = P.Property('Cervix', 'cervix', parent = gyn, next_category ='omfang',default = True)
gyn_vulva = P.Property('Vulva', 'vulva', parent = gyn, next_category ='omfang')
gyn_palliative = P.Property('Gyn palliativ/annet', 'palliative', parent = gyn, next_category ='omfang')

# Gyn Cervix: 
gyn_ln = P.Property('Med bekkenlymfeknuter', 'with', parent = gyn_cervix, next_category ='',default = True)
gyn_ln_n = P.Property('Med bekkenlymfeknuter og N+ i det lille bekkenet', 'with_node', parent = gyn_cervix, next_category ='antall lymfeknuter')
gyn_ln_n_57 = P.Property('Med bekkenlymfeknuter og N+ i det store bekkenet/paraaortalt', 'with_node_57', parent = gyn_cervix, next_category ='antall lymfeknuter i det lille bekkenet')

# Gyn: other/palliative:
gyn_without_ln = P.Property('Uten positive lymfeknuter', 'without', parent = gyn_palliative, default = True)
gyn_with_ln = P.Property('Med positive lymfeknuter', 'with', parent = gyn_palliative, next_category ='antall lymfeknuter')


# Gyn Cervix: Number of lymph nodes in the small pelvis
for l in [gyn_ln_n, gyn_with_ln]:  
  gyn_with_ln_n_1 = P.Property('1', 'with_node_1', parent = l, next_category ='', default = True)  
  gyn_with_ln_n_2 = P.Property('2', 'with_node_2', parent = l, next_category ='')  
  gyn_with_ln_n_3 = P.Property('3', 'with_node_3', parent = l, next_category ='')
  gyn_with_ln_n_4 = P.Property('4', 'with_node_4', parent = l, next_category ='')
  gyn_with_ln_n_5 = P.Property('5', 'with_node_5', parent = l, next_category ='')
  for i in [gyn_with_ln_n_1, gyn_with_ln_n_2, gyn_with_ln_n_3, gyn_with_ln_n_4, gyn_with_ln_n_5]:
    gyn_without_groin = P.Property('Uten lysker', 'without', parent = i, default = True)
    gyn_with_groin = P.Property('Med lysker', 'with', parent = i)

# Gyn Cervix: Number of lymph nodes in the small pelvis when choosing large pelvis
gyn_with_ln_n_55_0 = P.Property('0', 'with_node_55_0', parent = gyn_ln_n_57, next_category ='antall lymfeknuter i det store bekkenet/paraaortalt')
gyn_with_ln_n_55_1 = P.Property('1', 'with_node_55_1', parent = gyn_ln_n_57, next_category ='antall lymfeknuter i det store bekkenet/paraaortalt',default = True)
gyn_with_ln_n_55_2 = P.Property('2', 'with_node_55_2', parent = gyn_ln_n_57, next_category ='antall lymfeknuter i det store bekkenet/paraaortalt')
gyn_with_ln_n_55_3 = P.Property('3', 'with_node_55_3', parent = gyn_ln_n_57, next_category ='antall lymfeknuter i det store bekkenet/paraaortalt')
gyn_with_ln_n_55_4 = P.Property('4', 'with_node_55_4', parent = gyn_ln_n_57, next_category ='antall lymfeknuter i det store bekkenet/paraaortalt')
gyn_with_ln_n_55_5 = P.Property('5', 'with_node_55_5', parent = gyn_ln_n_57, next_category ='antall lymfeknuter i det store bekkenet/paraaortalt')

# Gyn Cervix: Number of lymph nodes in the large pelvis when choosing large pelvis
for p in [gyn_with_ln_n_55_0,gyn_with_ln_n_55_1,gyn_with_ln_n_55_2,gyn_with_ln_n_55_3,gyn_with_ln_n_55_4,gyn_with_ln_n_55_5]:
  gyn_with_ln_n_57_1 = P.Property('1', 'with_node_57_1', parent = p, next_category ='', default = True)
  gyn_with_ln_n_57_2 = P.Property('2', 'with_node_57_2', parent = p, next_category ='')
  gyn_with_ln_n_57_3 = P.Property('3', 'with_node_57_3', parent = p, next_category ='')
  gyn_with_ln_n_57_4 = P.Property('4', 'with_node_57_4', parent = p, next_category ='')
  gyn_with_ln_n_57_5 = P.Property('5', 'with_node_57_5', parent = p, next_category ='')

  for i in [gyn_with_ln_n_57_1, gyn_with_ln_n_57_2, gyn_with_ln_n_57_3, gyn_with_ln_n_57_4, gyn_with_ln_n_57_5]:
    gyn_without_groin = P.Property('Uten lysker', 'without', parent = i, default = True)
    gyn_with_groin = P.Property('Med lysker', 'with', parent = i)

# Gyn Vulva: Intent
gyn_vulva_primary = P.Property('Primær strålebehandling', 'primary', parent = gyn_vulva, next_category ='',default = True)
gyn_vulva_adjuvant = P.Property('Adjuvant strålebehandling', 'adjuvant', parent = gyn_vulva, next_category ='')

# Gyn Vulva: With or without positive lymph nodes 
gyn_vulva_pelvic = P.Property('Med bekkenlymfeknuter', 'vulva_with', parent = gyn_vulva_primary , next_category ='',default = True)
gyn_vulva_n = P.Property('Med bekkenlymfeknuter og N+ ', 'vulva_with_node', parent = gyn_vulva_primary , next_category ='antall lymfeknuter i bekkenet')

# Gyn (Vulva): Number of lymph nodes in the pelvic area
gyn_with_ln_n_0 = P.Property('0', 'with_node_0', parent = gyn_vulva_n, next_category ='antall lymfeknuter i lyskene')
gyn_with_ln_n_1 = P.Property('1', 'with_node_1', parent = gyn_vulva_n, next_category ='antall lymfeknuter i lyskene', default = True)
gyn_with_ln_n_2 = P.Property('2', 'with_node_2', parent = gyn_vulva_n, next_category ='antall lymfeknuter i lyskene')  
gyn_with_ln_n_3 = P.Property('3', 'with_node_3', parent = gyn_vulva_n, next_category ='antall lymfeknuter i lyskene')
gyn_with_ln_n_4 = P.Property('4', 'with_node_4', parent = gyn_vulva_n, next_category ='antall lymfeknuter i lyskene')
gyn_with_ln_n_5 = P.Property('5', 'with_node_5', parent = gyn_vulva_n, next_category ='antall lymfeknuter i lyskene')

# Gyn (Vulva): Number of lymph nodes in the groin area
for l in [gyn_with_ln_n_0, gyn_with_ln_n_1, gyn_with_ln_n_2,gyn_with_ln_n_3,gyn_with_ln_n_4,gyn_with_ln_n_5]:
  gyn_with_ing_n_0 = P.Property('0', 'with_node_ing_0', parent = l, next_category ='')  
  gyn_with_ing_n_1 = P.Property('1', 'with_node_ing_1', parent = l, next_category ='', default = True)
  gyn_with_ing_n_2 = P.Property('2', 'with_node_ing_2', parent = l, next_category ='')  
  gyn_with_ing_n_3 = P.Property('3', 'with_node_ing_3', parent = l, next_category ='')
  gyn_with_ing_n_4 = P.Property('4', 'with_node_ing_4', parent = l, next_category ='')
  gyn_with_ing_n_5 = P.Property('5', 'with_node_ing_5', parent = l, next_category ='')

  for i in [gyn_with_ing_n_0, gyn_with_ing_n_1, gyn_with_ing_n_2, gyn_with_ing_n_3, gyn_with_ing_n_4, gyn_with_ing_n_5]:
    gyn_without_groin = P.Property('Uten elektive lysker', 'without', parent = i, default = True)
    gyn_with_groin = P.Property('Med elektive lysker', 'with', parent = i)



for g in [gyn_vulva_adjuvant, gyn_vulva_pelvic]:
  gyn_without_groin = P.Property('Uten elektive lysker', 'without', parent = g, default = True)
  gyn_with_groin = P.Property('Med elektive lysker', 'with', parent = g)



# Prostate:
prostate_normal = P.Property('Prostata', 'prostate', parent = prostate, next_category ='', default = True)
prostate_bed = P.Property('Prostataseng', 'bed', parent = prostate, next_category ='')

# Prostate: Fractionation:
prostate_hypo = P.Property('Hypofraksjonert u/LK (3 Gy x 20)', 'hypo_60', parent = prostate_normal, default = True)
prostate_hypo_mLK = P.Property('Hypofraksjonert m/LK (2.7 Gy x 25)', 'hypo_67_5', parent = prostate_normal, next_category ='')
prostate_normo = P.Property('Konvensjonell fraksjonering (2.2 Gy x 35)', 'normo', parent = prostate_normal, next_category ='')
prostate_palliative = P.Property('Palliativ fraksjonering, uten gull', 'palliative', parent = prostate_normal, next_category ='')

prostate_bed_normo = P.Property('Konvensjonell fraksjonering', 'normo', parent = prostate_bed, next_category ='', default = True)
prostate_bed_palliative = P.Property('Palliativ fraksjonering', 'palliative', parent = prostate_bed, next_category ='')

# Prostate/bed: Lymph nodes:
for p in [prostate_normo, prostate_bed_normo, prostate_hypo_mLK]:
  prostate_without_ln =  P.Property('Uten bekkenlymfeknuter', 'without',  parent = p, next_category ='')
  prostate_with_ln =  P.Property('Med bekkenlymfeknuter', 'with', parent = p, next_category ='',default = True)
  prostate_with_ln_boost =  P.Property('Med bekkenlymfeknuter og boost til positiv lymfeknute(r)', 'with_node', parent = p, next_category ='antall lymfeknuter')

  prostate_with_ln_boost_1 =  P.Property('1', 'with_node_1', parent = prostate_with_ln_boost,default = True)
  prostate_with_ln_boost_2 =  P.Property('2', 'with_node_2', parent = prostate_with_ln_boost)
  prostate_with_ln_boost_3 =  P.Property('3', 'with_node_3', parent = prostate_with_ln_boost)


# GI

# Esophagus
# Esophagus: Indication
eso_pre = P.Property('Neoadjuvant preoperativ radiokjemoterapi (CROSS-regimet)', 'neo', parent = esophagus, next_category = '',default = True)
eso_radical = P.Property('Radikal (definitiv) radiokjemoterapi', 'radical', parent = esophagus,next_category = '')
eso_palliative = P.Property('Palliativ', 'palliative', parent = esophagus,next_category = '')

# Esophagus: Palliative: With AI OARs or without
eso_palliative_with_oar =P.Property('Med AI-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = eso_palliative, default = True)
eso_palliative_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = eso_palliative)

# Esophagus: With or without 4DCT (for neoadjuvant preoperative radiochemotherapy)
eso_not_4dct = P.Property('Uten 4DCT', 'without_4DCT', parent = eso_pre, next_category = '', default = True)
eso_4dct = P.Property('Med 4DCT', 'with_4DCT', parent = eso_pre, next_category = '')

# Esophagus: Participating or not participating in Needs study (for neoadjuvant preoperative radiochemotherapy)
for n in [eso_not_4dct, eso_4dct]:
  eso_pre_not_needs = P.Property('Deltar ikke i Needs-studien', 'not_needs', parent = n, next_category = '', default = True)
  eso_pre_needs = P.Property('Deltar i Needs-studien', 'needs', parent = n,next_category = '')
  # Esophagus: With positive lymph nodes or not (for neoadjuvant preoperative radiochemotherapy)
  for f in [eso_pre_not_needs, eso_pre_needs]:
    eso_ln = P.Property('Med positiv lymfeknute(r)', 'with', parent = f, next_category = '',default = True)
    eso_without_ln = P.Property('Uten positiv lymfeknute', 'without', next_category = '', parent = f)
    for a in [eso_ln, eso_without_ln]:
      eso_with_oar =P.Property('Med AI-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
      eso_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)

# Esophagus: With or without 4DCT (for radical radiochemotherapy)
eso_not_4dct_r = P.Property('Uten 4DCT', 'without_4DCT', parent = eso_radical, next_category = 'fraksjonering', default = True)
eso_4dct_r = P.Property('Med 4DCT', 'with_4DCT', parent = eso_radical, next_category = 'fraksjonering')

# Esophagus: Total dose 50 Gy
for ll in [eso_4dct_r, eso_not_4dct_r]:
  eso_50 = P.Property('Totaldose 50 Gy', '50', parent = ll, next_category = '', default = True)
  # Esophagus: Participating or not participating in Needs study (for 50 Gy)
  eso_not_needs = P.Property('Deltar ikke i Needs-studien (SIB)', 'not_needs', parent = eso_50, next_category = 'antall positive lymfeknuter', default = True)
  eso_needs = P.Property('Deltar i Needs-studien', 'needs', parent = eso_50, next_category = 'antall positive lymfeknuter')
  # Esophagus: Number of positive lymph nodes (for 50 Gy)
  for ln in [eso_not_needs, eso_needs]:
    eso_n_ln_0 = P.Property('0', '0', parent = ln, next_category = '')
    eso_n_ln_1 = P.Property('1', '1', parent = ln, next_category = '', default = True)
    eso_n_ln_2 = P.Property('2', '2', parent = ln, next_category = '')
    eso_n_ln_3 = P.Property('3', '3', parent = ln, next_category = '')
    for a in [eso_n_ln_0, eso_n_ln_1, eso_n_ln_2, eso_n_ln_3]:
      eso_with_oar =P.Property('Med AI-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
      eso_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)

# Esophagus: Total dose 60 or 66 Gy
for l in [eso_4dct_r, eso_not_4dct_r]:
  eso_60 = P.Property('Totaldose 60 Gy (Sekvensiell boost)', '60', parent = l, next_category = 'antall positive lymfeknuter')
  eso_66 = P.Property('Totaldose 66 Gy (Sekvensiell boost)', '66', parent = l, next_category = 'antall positive lymfeknuter')
  # Esophagus: Number of positive lymph nodes (for 60 or 66 Gy)
  for e_ln in [eso_60, eso_66]:
    eso_ln_0 = P.Property('0', '0', parent = e_ln, next_category = '')
    eso_ln_1 = P.Property('1', '1', parent = e_ln, next_category = '', default = True)
    eso_ln_2 = P.Property('2', '2', parent = e_ln, next_category = '')
    eso_ln_3 = P.Property('3', '3', parent = e_ln, next_category = '')
    for a in [eso_ln_0, eso_ln_1, eso_ln_2, eso_ln_3]:
      eso_with_oar =P.Property('Med AI-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
      eso_without_ai =P.Property('Uten AI-strukturer', 'without_ai', parent = a)



# Anus:
anus_t1 = P.Property('T1-2 N0', 't1', parent = anus, default = True)
anus_t3 = P.Property('T3-4 N0 eller N+', 't3', parent = anus, next_category ='antall lymfeknuter < 2 cm')

nr_ln_small_0 = P.Property('0', 'with_node_0', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm')
nr_ln_small_1 = P.Property('1', 'with_node_1', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm', default = True)
nr_ln_small_2 = P.Property('2', 'with_node_2', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm')
nr_ln_small_3 = P.Property('3', 'with_node_3', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm')
nr_ln_small_4 = P.Property('4', 'with_node_4', parent = anus_t3, next_category ='antall lymfeknuter > 2 cm')

for p in [nr_ln_small_0, nr_ln_small_1, nr_ln_small_2, nr_ln_small_3, nr_ln_small_4]:
  nr_ln_large_0 = P.Property('0', 'with_node_l_0', parent = p, next_category ='omfang')
  nr_ln_large_1 = P.Property('1', 'with_node_l_1', parent = p,next_category ='omfang', default = True)
  nr_ln_large_2 = P.Property('2', 'with_node_l_2', parent = p,next_category ='omfang')
  nr_ln_large_3 = P.Property('3', 'with_node_l_3', parent = p,next_category ='omfang')
  nr_ln_large_4 = P.Property('4', 'with_node_l_4', parent = p,next_category ='omfang')

#anus_without_nodes = P.Property('Uten lysker', 'without', parent = anus_t1, default = True)
#anus_with_nodes = P.Property('Med lysker', 'with', parent = anus_t1)


# Rectum:
rectum_preop = P.Property('Preoperativ strålebehandling', 'preop', parent = rectum, next_category ='fraksjonering',default = True)
rectum_postop = P.Property('Postoperativ strålebehandling', 'postop', parent = rectum, next_category ='')

rectum_normo = P.Property('Konvensjonell fraksjonering med SIB', 'normo', parent = rectum_preop, next_category ='antall positive lymfeknuter', default = True)
rectum_hypo = P.Property('Hypofraksjonering', 'hypo', parent = rectum_preop, next_category ='')
rectum_re = P.Property('Rebestråling', 're', parent = rectum_preop, next_category ='antall positive lymfeknuter')


rectum_nr_ln_0 = P.Property('0', 'with_node_0', parent = rectum_normo, next_category ='omfang')
rectum_nr_ln_1 = P.Property('1', 'with_node_1', parent = rectum_normo, next_category ='omfang', default = True)
rectum_nr_ln_2 = P.Property('2', 'with_node_2', parent = rectum_normo, next_category ='omfang')
rectum_nr_ln_3 = P.Property('3', 'with_node_3', parent = rectum_normo, next_category ='omfang')
rectum_nr_ln_4 = P.Property('4', 'with_node_4', parent = rectum_normo, next_category ='omfang')

for p1 in [rectum_nr_ln_0,rectum_nr_ln_1,rectum_nr_ln_2,rectum_nr_ln_3,rectum_nr_ln_4]:
  rectum_without_nodes = P.Property('Uten lysker', 'without', parent = p1, default = True)
  rectum_with_nodes = P.Property('Med lysker', 'with', parent = p1)

# rectum re-irradiation number of lymph nodes
rectum_nr_ln_0_re = P.Property('0', 'with_node_0', parent = rectum_re)
rectum_nr_ln_1_re = P.Property('1', 'with_node_1', parent = rectum_re, default = True)
rectum_nr_ln_2_re = P.Property('2', 'with_node_2', parent = rectum_re)
rectum_nr_ln_3_re = P.Property('3', 'with_node_3', parent = rectum_re)
rectum_nr_ln_4_re = P.Property('4', 'with_node_4', parent = rectum_re)

# Rectum normo: Nodes:
rectum_with_ln =  P.Property('Ingen boost til positiv lymfeknute', 'with', parent = rectum_hypo, next_category ='omfang',default = True)
rectum_with_ln_boost =  P.Property('Med boost til positiv lymfeknute(r)', 'with_node', parent = rectum_hypo, next_category ='omfang')

# Other (palliative): SBRT

other_stereotactic = P.Property('Stereotaksi', 'yes', parent =other, next_category = 'region', default = True)
other_non_stereotactic = P.Property('Ikke stereotaksi', 'no', parent = other, next_category = 'region', default = True)
#other_non_stereotactic = P.Property('Ikke stereotaksi', 'no', parent = other, next_category = 'region', default = True)

# Other non-SBRT: Region:
other_head = P.Property('Hode', 'head', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_neck = P.Property('Hals', 'neck', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_thorax = P.Property('Thorax', 'thorax', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_thorax_and_abdomen = P.Property('Thorax/Abdomen', 'thorax_abdomen', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_abdomen = P.Property('Abdomen', 'abdomen', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_abdomen_and_pelvis = P.Property('Abdomen/Bekken', 'abdomen_pelvis', parent=other_non_stereotactic, next_category = 'antall målvolum')
other_pelvis = P.Property('Bekken', 'pelvis', parent=other_non_stereotactic, next_category = 'antall målvolum', default = True)
other_other = P.Property('Ekstremiteter/Annet', 'other', parent=other_non_stereotactic, next_category = 'antall målvolum')
'''
# Other SBRT: Region:
other_stereotactic_col_cervical=  P.Property('Cervicalcolumna', 'col cerv', parent=other)
other_stereotactic_col_thorax =  P.Property('Thoracalcolumna', 'col thorax', parent=other)
other_stereotactic_thorax =  P.Property('Thorax unntatt columna', 'thorax', parent=other)
other_stereotactic_col_pelvis =  P.Property('Lumbalcolumna-Sacrum', 'col pelvis', parent=other)
other_stereotactic_pelvis  = P.Property('Bekken unntatt columna', 'pelvis', parent=other, default = True)
other_stereotactic_other =  P.Property('Ekstremiteter', 'other', parent=other)
'''
# Other SBRT: Region:
other_stereotactic_col_cervical=  P.Property('Cervicalcolumna', 'col cerv', parent=other_stereotactic, next_category = '')
other_stereotactic_col_thorax =  P.Property('Thoracalcolumna', 'col thorax', parent=other_stereotactic, next_category = '')
other_stereotactic_col_pelvis =  P.Property('Lumbalcolumna-Sacrum', 'col pelvis', parent=other_stereotactic, next_category = '')
other_stereotactic_thorax =  P.Property('Thorax unntatt columna', 'thorax', parent=other_stereotactic, next_category = '')
other_stereotactic_pelvis  = P.Property('Bekken unntatt columna', 'pelvis', parent=other_stereotactic, next_category = '', default = True)
other_stereotactic_other =  P.Property('Ekstremiteter', 'other', parent=other_stereotactic, next_category = '')
for a in [other_stereotactic_col_cervical,other_stereotactic_col_thorax,other_stereotactic_col_pelvis,other_stereotactic_thorax,other_stereotactic_pelvis]:
  other_stereotacic_with_ai_oar =P.Property('Med AI-og MBS-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
  other_stereotactic_without_ai =P.Property('Uten AI- og MBS-strukturer', 'without_ai', parent = a)

# Other non-SBRT: Number of target volumes:
for region in [other_head, other_neck, other_thorax, other_thorax_and_abdomen, other_abdomen, other_abdomen_and_pelvis, other_pelvis]:
  other_target_volume_one = P.Property('1','1', parent = region, next_category = '', default = True)
  other_target_volume_two = P.Property('2','2', parent = region, next_category = '')
  other_target_volume_three = P.Property('3','3', parent = region, next_category = '')
  # With or without soft tissue component:
  for tv in [other_target_volume_one, other_target_volume_two, other_target_volume_three]:
    other_with_gtv = P.Property('Bløtvevskomponent (med GTV)', 'with', parent = tv, next_category = '')
    other_without_gtv = P.Property('Skjelett (uten GTV)', 'without', parent = tv, next_category = '', default = True)
    for a in [other_with_gtv, other_without_gtv]:
      other_with_ai_oar =P.Property('Med AI-og MBS-strukturer som risikoorganer, der det er mulig', 'with_ai_oar', parent = a, default = True)
      other_without_ai =P.Property('Uten AI- og MBS-strukturer', 'without_ai', parent = a)


other_other_target_volume_one = P.Property('1','1', parent = other_other, next_category = '', default = True)
other_other_target_volume_two = P.Property('2','2', parent = other_other, next_category = '')
other_other_target_volume_three = P.Property('3','3', parent = other_other, next_category = '')
# With or without soft tissue component:
for tv in [other_other_target_volume_one, other_other_target_volume_two, other_other_target_volume_three]:
  other_with_gtv = P.Property('Bløtvevskomponent (med GTV)', 'with', parent = tv)
  other_without_gtv = P.Property('Skjelett (uten GTV)', 'without', parent = tv, default = True)



# Lists to be used with radiobutton objects:
regions = [brain, head_neck, lung, breast, esophagus, liver, bladder, prostate, gyn, rectum, anus, other]
#regions = [brain, head_neck, lung, breast, liver, bladder, gyn, prostate, gi, other]
#regions = [brain, head_neck, lung, breast, esophagus,liver, prostate, gyn, rectum, anus]
# Radiobutton choices for deleting/keeping pre-existing ROIs:
p_delete = P.Property('Slett eksisterende ROIs', 'yes')
p_delete_derived = P.Property('Slett alle bortsett fra inntegnede ROIs','some')
p_not_delete = P.Property('Ikke slett eksisterende ROIs','no', default = True)
delete = [p_delete, p_delete_derived, p_not_delete]
