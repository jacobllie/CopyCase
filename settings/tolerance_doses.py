# encoding: utf8

# Import local files:
import tolerance as EQD


# Alpha/beta values:
ab_kidney = 2
ab_kidneys = 2
ab_lung = 3
ab_heart = 3
ab_bowelspace = 3
ab_spinalcord = 2
ab_eye = 3
ab_lens = 1
ab_parotid = 3
ab_brain = 2
ab_esophagus = 3
ab_lung = 3
ab_bladder = 5
ab_rectum = 3
ab_femoral = 3
ab_brainstem = 2
ab_optic_nerve = 2
ab_optic_chiasm = 2
ab_lacrimal = 3
ab_cochlea = 3
ab_hippocampus = 2
ab_pituitary = 2
ab_retina = 3
ab_scalp = 2
ab_larynx_sg = 3
ab_humeral = 3
ab_trachea = 3
ab_chestwall = 3
ab_ribs = 3
ab_greatves = 3
ab_bronchus = 3
ab_liver = 2
ab_brachial = 2
ab_stomach = 3
ab_skin = 2
ab_kidney_hilum = 2
ab_cauda = 3
ab_colon = 3
ab_bowel = 3
ab_breast = 3
ab_lad = 2
ab_cornea = 3
ab_ovary = 3
ab_sigmoid = 3
ab_aorta = 3
ab_connective_tissue = 3
ab_penile_bulb = 3
ab_anal_canal = 3
ab_pharynx_constr = 3
ab_submand = 3
ab_carotid = 3
ab_oral_cavity = 3
ab_bile_duct = 3

# Reference number of fractions:
fractions_kidney = 25
fractions_lung = 33
fractions_heart = 33
#fractions_bowelspace = 25
fractions_bowelspace = 35
fractions_bowelspace_27 = 27
fractions_spinalcord_eqd2 = 22.5
fractions_spinalcord = 25
fractions_spinalcord_35 = 35
fractions_spinalcord_34 = 34
fractions_spinalcord_33 = 33
fractions_spinalcord_30 = 30
fractions_parotid = 34
fractions_parotid_30 = 30
fractions_parotid_35 = 35
fractions_parotid_33 = 33
fractions_esophagus = 33
#fractions_bladder = 41
fractions_bladder = 35
fractions_bladder_hypo = 20
fractions_bladder_gyn = 25
fractions_bladder_25 = 25
fractions_bladder_27 = 27
#fractions_rectum = 39
fractions_rectum = 35
fractions_rectum_hypo = 20
fractions_rectum_25 = 25
fractions_rectum_gyn = 25
#fractions_femoral = 21
fractions_femoral = 35
fractions_femoral_gyn = 25
fractions_femoral_27 = 27
fractions_femoral_25 = 25
fractions_ovary = 25
fractions_bladder_at_rectum = 25
fractions_breast = 25
fractions_breast_15 = 15
fractions_eye = 33
fractions_sbrt_3 = 3
fractions_sbrt_5 = 5
fractions_sbrt_8 = 8
fractions_sbrt_1 = 1
fractions_sbrt_12 = 12
# Til ny prosedyre, del av hjerne og total hjerne
fractions_brainstem_surface = 30
fractions_brainstem_core = 27
fractions_brainstem_30 = 30
fractions_brainstem_35 = 35
fractions_brainstem_33 = 33
fractions_brainstem_34 = 34
fractions_optic_nerve = 27.5
fractions_optic_chiasm = 27.5
fractions_cochlea = 22.5
fractions_cochlea_tinnitus = 16
fractions_hippocampus = 3.65
fractions_lens = 5
fractions_humeral = 25
fractions_pituitary = 22.5
fractions_pituitary_2 = 10
fractions_brain = 30
fractions_cornea = 25
fractions_lacrimal = 12.5
fractions_retina = 22.5
fractions_skin = 12.5
fractions_sigmoid = 25
fractions_penile_bulb = 35
fractions_penile_bulb_25 = 25
fractions_pharynx_constr = 34
fractions_submand = 34
fractions_carotid = 34
fractions_oral_cavity = 34
fractions_larynx_sg = 34
fractions_stomach = 25

# Example:
# EQD.Tolerance(organ, endpoint, alphabeta, nr_fractions, dose, criteria, comment)

# Conventional RT:

# Head


# Partial brain

lens_v003_adx = EQD.Tolerance('Lens_L','Some failure', ab_lens, fractions_lens, 10, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
lens_v003_adx_eqd2 = EQD.Tolerance('Lens_L','Some failure', ab_lens, fractions_lens, 10, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')

brain_v003 = EQD.Tolerance('Brain','Some failure', ab_brain, fractions_brain, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brain_v003_eqd2 = EQD.Tolerance('Brain','Some failure', ab_brain, fractions_brain, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')

brainstem_surface_v003_adx = EQD.Tolerance('BrainstemSurface', 'Some failure', ab_brainstem, fractions_brainstem_surface, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_core_v003_adx = EQD.Tolerance('BrainstemCore', 'Some failure', ab_brainstem, fractions_brainstem_core, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_nrv_v003_adx = EQD.Tolerance('OpticNrv','Some failure', ab_optic_nerve, fractions_optic_nerve, 55,  'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_chiasm_v003_adx = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_optic_chiasm, 55, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
lacrimal_mean = EQD.Tolerance('Glnd_Lacrimal', 'Some failure', ab_lacrimal, fractions_lacrimal, 25,  'Mean', 'Conventional RT')
cochlea_mean = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, fractions_cochlea, 45, 'Mean', 'Conventional RT')
cochlea_mean_tinnitus = EQD.Tolerance('Cochlea_R', 'Some failure', ab_cochlea, fractions_cochlea_tinnitus, 32, 'Mean', 'Conventional RT')
pituitary_mean = EQD.Tolerance('Pituitary', 'Some failure', ab_pituitary, fractions_pituitary, 45, 'Mean', 'Conventional RT')
pituitary_2_mean = EQD.Tolerance('Pituitary', 'Some failure', ab_pituitary, fractions_pituitary_2, 20, 'Mean', 'Conventional RT')
retina_v003_adx = EQD.Tolerance('Retina_R', 'Some failure', ab_retina, fractions_retina, 45, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
#cornea_v003_adx = EQD.Tolerance('Cornea', 'Some failure', ab_cornea, fractions_cornea, 50, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')

cornea_v003_adx = EQD.Tolerance('Cornea', 'Some failure', ab_cornea, fractions_cornea, 30, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
skin_v003_adx = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_skin, 25,'Maximum dose at less than 0.03cc volume', 'Conventional RT')
hippocampus_v40 = EQD.Tolerance('Hippocampus_L', 'Some failure', ab_hippocampus, fractions_hippocampus, 7.3, 'Volume receiving tolerance dose being less than 40%', 'Conventional RT')


optic_nrv_30_v003_adx = EQD.Tolerance('OpticNrv','Some failure', ab_optic_nerve, 30, 54,  'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_core_30_v003_adx = EQD.Tolerance('BrainstemCore', 'Some failure', ab_brainstem, 30, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_chiasm_30_v003_adx = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, 30, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
cochlea_mean_30 = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, 30, 45, 'Mean', 'Conventional RT')
lacrimal_mean_30 = EQD.Tolerance('Glnd_Lacrimal', 'Some failure', ab_lacrimal, 30, 25,  'Mean', 'Conventional RT')
lens_v003_30_adx = EQD.Tolerance('Lens_L','Some failure', ab_lens, 30, 10, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
pituitary_mean_30 = EQD.Tolerance('Pituitary', 'Some failure', ab_pituitary, 30, 45, 'Mean', 'Conventional RT')
retina_v003_30_adx = EQD.Tolerance('Retina_R', 'Some failure', ab_retina, 30, 45, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
cornea_v003_30_adx = EQD.Tolerance('Cornea', 'Some failure', ab_cornea, 30, 30, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
skin_v003_30_adx = EQD.Tolerance('Skin', 'Some failure', ab_skin, 30, 25,'Maximum dose at less than 0.03cc volume', 'Conventional RT')
hippocampus_30_v40 = EQD.Tolerance('Hippocampus_L', 'Some failure', ab_hippocampus, 30, 7.3, 'Volume receiving tolerance dose being less than 40%', 'Conventional RT')
brain_ptv_30_mean = EQD.Tolerance('Brain','Some failure', ab_brain, 30, 30, 'Mean', 'Conventional RT')
spinalcord30_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 30, 50, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
retina_prv_v003_30_adx = EQD.Tolerance('Retina_R_PRV', 'Some failure', ab_retina, 30, 50, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_chiasm_prv_30_v003_adx = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, 30, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_nrv_prv_30_v003_adx = EQD.Tolerance('OpticNrv','Some failure', ab_optic_nerve, 30, 60,  'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_surface_prv_30_v003_adx = EQD.Tolerance('BrainstemSurface', 'Some failure', ab_brainstem, 30, 63, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')

brainstem_surface_33_v003_adx = EQD.Tolerance('BrainstemSurface', 'Some failure', ab_brainstem, 33, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_core_33_v003_adx = EQD.Tolerance('BrainstemCore', 'Some failure', ab_brainstem, 33, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_chiasm_33_v003_adx = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, 33, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_nrv_33_v003_adx = EQD.Tolerance('OpticNrv','Some failure', ab_optic_nerve, 33, 54,  'Maximum dose at less than 0.03cc volume', 'Conventional RT')
cochlea_mean_33 = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, 33, 45, 'Mean', 'Conventional RT')
lacrimal_mean_33 = EQD.Tolerance('Glnd_Lacrimal', 'Some failure', ab_lacrimal, 33, 25,  'Mean', 'Conventional RT')
lens_v003_33_adx = EQD.Tolerance('Lens_L','Some failure', ab_lens, 33, 10, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
pituitary_mean_33 = EQD.Tolerance('Pituitary', 'Some failure', ab_pituitary, 33, 45, 'Mean', 'Conventional RT')
retina_v003_33_adx = EQD.Tolerance('Retina_R', 'Some failure', ab_retina, 33, 45, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
cornea_v003_33_adx = EQD.Tolerance('Cornea', 'Some failure', ab_cornea, 33, 30, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
skin_v003_33_adx = EQD.Tolerance('Skin', 'Some failure', ab_skin, 33, 25,'Maximum dose at less than 0.03cc volume', 'Conventional RT')
hippocampus_33_v40 = EQD.Tolerance('Hippocampus_L', 'Some failure', ab_hippocampus, 33, 7.3, 'Volume receiving tolerance dose being less than 40%', 'Conventional RT')
brain_ptv_33_mean = EQD.Tolerance('Brain','Some failure', ab_brain, 33, 30, 'Mean', 'Conventional RT')
spinalcord33_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 33, 50, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
retina_prv_v003_33_adx = EQD.Tolerance('Retina_R_PRV', 'Some failure', ab_retina, 33, 50, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_chiasm_prv_33_v003_adx = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, 33, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
optic_nrv_prv_33_v003_adx = EQD.Tolerance('OpticNrv','Some failure', ab_optic_nerve, 33, 60,  'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_surface_prv_33_v003_adx = EQD.Tolerance('BrainstemSurface', 'Some failure', ab_brainstem, 33, 63, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')

cochlea_mean_15 = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, 15, 45, 'Mean', 'Conventional RT')
lacrimal_mean_15 = EQD.Tolerance('Glnd_Lacrimal', 'Some failure', ab_lacrimal, 15, 25,  'Mean', 'Conventional RT')
lens_v003_15_adx = EQD.Tolerance('Lens_L','Some failure', ab_lens, 15, 10, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
pituitary_mean_15 = EQD.Tolerance('Pituitary', 'Some failure', ab_pituitary, 15, 45, 'Mean', 'Conventional RT')
skin_v003_15_adx = EQD.Tolerance('Skin', 'Some failure', ab_skin, 15, 25,'Maximum dose at less than 0.03cc volume', 'Conventional RT')
hippocampus_15_v40 = EQD.Tolerance('Hippocampus_L', 'Some failure', ab_hippocampus, 15, 7.3, 'Volume receiving tolerance dose being less than 40%', 'Conventional RT')
brain_ptv_15_mean = EQD.Tolerance('Brain','Some failure', ab_brain, 15, 30, 'Mean', 'Conventional RT')
cornea_v003_15_adx = EQD.Tolerance('Cornea', 'Some failure', ab_cornea, 15, 30, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')


cochlea_mean_13 = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, 13, 45, 'Mean', 'Conventional RT')
lacrimal_mean_13 = EQD.Tolerance('Glnd_Lacrimal', 'Some failure', ab_lacrimal, 13, 25,  'Mean', 'Conventional RT')
lens_v003_13_adx = EQD.Tolerance('Lens_L','Some failure', ab_lens, 13, 10, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
pituitary_mean_13 = EQD.Tolerance('Pituitary', 'Some failure', ab_pituitary, 13, 45, 'Mean', 'Conventional RT')
skin_v003_13_adx = EQD.Tolerance('Skin', 'Some failure', ab_skin, 13, 25,'Maximum dose at less than 0.03cc volume', 'Conventional RT')
hippocampus_13_v40 = EQD.Tolerance('Hippocampus_L', 'Some failure', ab_hippocampus, 13, 7.3, 'Volume receiving tolerance dose being less than 40%', 'Conventional RT')
#cornea_v003_33_adx = EQD.Tolerance('Cornea', 'Some failure', ab_cornea, 33, 30, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brain_ptv_13_mean = EQD.Tolerance('Brain','Some failure', ab_brain, 13, 30, 'Mean', 'Conventional RT')
cornea_v003_13_adx = EQD.Tolerance('Cornea', 'Some failure', ab_cornea, 13, 30, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')



# Neck
parotids_mean_eqd2 = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid, 25, 'Mean', 'Conventional RT')

parotids_mean = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid, 25, 'Mean', 'Conventional RT',compute_eqd2 = False)
parotid_mean = EQD.Tolerance('Parotid', 'Some failure', ab_parotid, fractions_parotid, 26, 'Mean', 'Conventional RT',compute_eqd2 = False)
submand_mean = EQD.Tolerance('SubmandGland', 'Some failure', ab_submand, fractions_submand, 35, 'Mean', 'Conventional RT',compute_eqd2 = False)
carotid_v003_adx = EQD.Tolerance('A_Carotid', 'Some failure', ab_carotid, fractions_carotid, 40, 'Maximum dose at less than 0.03cc volume', 'Conventional RT',compute_eqd2 = False)
submand_mean_eqd2 = EQD.Tolerance('SubmandGland', 'Some failure', ab_submand, fractions_submand, 35, 'Mean', 'Conventional RT')
carotid_v003_adx_eqd2 = EQD.Tolerance('A_Carotid', 'Some failure', ab_carotid, fractions_carotid, 40, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
oral_cavity_mean_eqd2 = EQD.Tolerance('OralCavity', 'Some failure', ab_oral_cavity, fractions_oral_cavity, 30, 'Mean', 'Conventional RT')
oral_cavity_mean = EQD.Tolerance('OralCavity', 'Some failure', ab_oral_cavity, fractions_oral_cavity, 30, 'Mean', 'Conventional RT',compute_eqd2 = False)

brainstem_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_34, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT',compute_eqd2 = False)
brainstem_prv_v003_adx = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_34, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT',compute_eqd2 = False)
brainstem_v003_adx_eqd2 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_34, 54, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')
brainstem_prv_v003_adx_eqd2 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_brainstem_34, 60, 'Maximum dose at less than 0.03cc volume', 'Conventional RT')

spinalcord_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_34, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT',compute_eqd2 = False)
spinalcord_prv_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_34, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT',compute_eqd2 = False)
spinalcord_v003_adx_eqd2 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_34, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_prv_v003_adx_eqd2 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord_34, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')

pharynx_constr_mean = EQD.Tolerance('PharynxConstr', 'Some failure', ab_pharynx_constr, fractions_pharynx_constr, 55, 'Mean', 'Conventional RT',compute_eqd2 = False)
larynx_sg_mean = EQD.Tolerance('Larynx_SG', 'Some failure', ab_larynx_sg, fractions_larynx_sg, 40, 'Mean', 'Conventional RT',compute_eqd2 = False)
esophagus_mean_head = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 30, 'Mean', 'Conventional RT', compute_eqd2 = False)

# Thorax
kidney_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 15, 'Mean', 'Conventional RT',compute_eqd2 = False)
kidney_mean_eqd2 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 15, 'Mean', 'Conventional RT')

kidney_mean_18 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 18, 'Mean', 'Conventional RT',compute_eqd2 = False)
kidney_v20_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 28, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
#kidney_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT',compute_eqd2 = False)
kidney_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 18, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT',compute_eqd2 = False)
kidney_v32_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 20, 'Volume receiving tolerance dose being less than 32%', 'Conventional RT')
kidney_v55_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 12, 'Volume receiving tolerance dose being less than 12%', 'Conventional RT')
kidney_v20_adx_eqd2 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 28, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
kidney_v30_adx_eqd2 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_v32_adx_eqd2 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 20, 'Volume receiving tolerance dose being less than 32%', 'Conventional RT')
kidney_v55_adx_eqd2 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 12, 'Volume receiving tolerance dose being less than 12%', 'Conventional RT')

lung_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Mean', 'Conventional RT',compute_eqd2 = False)
lung_mean_eqd2 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Mean', 'Conventional RT')
lung_10_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 12, 'Mean', 'Conventional RT',compute_eqd2 = False)
lung_v30_adx_eqd2 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_v35_adx_eqd2 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
lung_v55_adx_eqd2 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung,5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')

lung_v30_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT',compute_eqd2 = False)
lung_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT',compute_eqd2 = False)
lung_v65_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung, 5, 'Volume receiving tolerance dose being less than 65%', 'Conventional RT')
lung_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_lung,5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT',compute_eqd2 = False)
lung_30_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 30, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_30_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 30, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
lung_30_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 30, 20, 'Mean', 'Conventional RT')
lung_35_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 35, 20, 'Mean', 'Conventional RT')
lung_35_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 35, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_35_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 35, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
lung_15_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 15, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_15_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 15, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
lung_17_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 17, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_17_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 17, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
lung_17_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 17, 20, 'Mean', 'Conventional RT')
lung_15_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 15, 20, 'Mean', 'Conventional RT')

stomach_v003_adx = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_stomach, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT',compute_eqd2 = False)


heart_mean = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 35, 'Mean', 'Conventional RT',compute_eqd2 = False)
heart_mean_eqd2 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 35, 'Mean', 'Conventional RT')

heart_40_mean = EQD.Tolerance('Heart', 'Some failure', ab_heart, 40, 35, 'Mean', 'Conventional RT')
heart_35_mean = EQD.Tolerance('Heart', 'Some failure', ab_heart, 35, 35, 'Mean', 'Conventional RT')
heart_33_mean = EQD.Tolerance('Heart', 'Some failure', ab_heart, 33, 35, 'Mean', 'Conventional RT')
heart_30_mean = EQD.Tolerance('Heart', 'Some failure', ab_heart, 30, 35, 'Mean', 'Conventional RT')
heart_17_mean = EQD.Tolerance('Heart', 'Some failure', ab_heart, 17, 35, 'Mean', 'Conventional RT')
heart_15_mean = EQD.Tolerance('Heart', 'Some failure', ab_heart, 15, 35, 'Mean', 'Conventional RT')
heart_v25_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 50, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_v30_adx_eqd2 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 60, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_v60_adx_eqd2 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 45, 'Volume receiving tolerance dose being less than 60%', 'Conventional RT')
heart_v80_adx_eqd2 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 40, 'Volume receiving tolerance dose being less than 80%', 'Conventional RT')

heart_v30_eso_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT',compute_eqd2 = False)
heart_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 60, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_v60_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 45, 'Volume receiving tolerance dose being less than 60%', 'Conventional RT')
heart_v80_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 40, 'Volume receiving tolerance dose being less than 80%', 'Conventional RT')
heart_v10_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 10, 10, 'Volume receiving tolerance dose being less than 10%', 'Conventional RT',compute_eqd2 = False)
heart_narlal_30_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 30, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT',compute_eqd2 = False)
heart_narlal_30_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 30, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT',compute_eqd2 = False)
heart_narlal_30_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 30, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT',compute_eqd2 = False)
heart_narlal_35_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 35, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_35_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 35, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_35_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 35, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
heart_narlal_15_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 15, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_15_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 15, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_15_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 15, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
heart_narlal_17_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 17, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_17_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 17, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_17_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 17, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
heart_narlal_40_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 40, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_40_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 40, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_40_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 40, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
heart_narlal_v20_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT',compute_eqd2 = False)
heart_narlal_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT',compute_eqd2 = False)
heart_narlal_v50_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT',compute_eqd2 = False)
heart_narlal_v20_adx_eqd2 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 50, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
heart_narlal_v30_adx_eqd2 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_narlal_v50_adx_eqd2 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_heart, 25, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')


esophagus_mean = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 34, 'Mean', 'Conventional RT')
esophagus_v15_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 60, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
esophagus_v17_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 60, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
esophagus_10_v0_03_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 10, 30, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT',compute_eqd2 = False)
esophagus_v1_30_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 30, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT',compute_eqd2 = False)
esophagus_v1_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_esophagus, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT',compute_eqd2 = False)
esophagus_v1_17_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 17, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
esophagus_v1_35_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 35, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
esophagus_v1_15_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 15, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
esophagus_v1_40_adx = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, 40, 70, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')

spinalcanal_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_v0_03_adx_chemo = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 25, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_v0_03_adx_chemo_eqd2 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 25, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_v2_adx_eqd2 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcord_v2_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_v2_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')

spinalcanal_10_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 30, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT',compute_eqd2 = False)
spinalcord_33_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 33, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_33_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 33, 55, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_33_v0_03_adx_chemo = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 33, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_33_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 33, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_30_2_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 30, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_30_2_v0_03_adx_chemo = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 30, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_30_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 30, 53, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_30_v0_03_adx_chemo = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 30, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_30_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 30, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_35_v0_03_adx_chemo = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 35, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_35_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 35, 56, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_35_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 35, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_17_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 17, 43, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_17_v0_03_adx_chemo = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 17, 40, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_17_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 17, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_15_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 15, 41, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_15_v0_03_adx_chemo = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 15, 38, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_15_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 15, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_prv_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_40_v0_03_adx = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 40, 52, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinalcanal_40_v0_03_adx_chemo = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, 40, 48, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')




heart_v1_33_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
trachea_v1_33_adx = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
trachea_prv_v1_33_adx = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, 33, 78, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
bronchus_v1_33_adx = EQD.Tolerance('Bronchus', 'Some failure', ab_bronchus, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
bronchus_prv_v1_33_adx = EQD.Tolerance('Bronchus', 'Some failure', ab_bronchus, 33, 78, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
aorta_v1_33_adx = EQD.Tolerance('A Aorta', 'Some failure', ab_aorta, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
connective_tissue_v1_33_adx = EQD.Tolerance('Connective tissue', 'Some failure', ab_connective_tissue, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
chestwall_v1_33_adx = EQD.Tolerance('Chest wall', 'Some failure', ab_chestwall, 33, 74, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')

lung_40_v55_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 40, 5, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_40_v35_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 40, 20, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
lung_40_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, 40, 20, 'Mean', 'Conventional RT')

# Esophagus
heart_25_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 25, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
heart_23_v30_adx = EQD.Tolerance('Heart', 'Some failure', ab_heart, 23, 40, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_23_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 23, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_23_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 23, 18, 'Mean', 'Conventional RT')
kidney_25_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 25, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_25_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 25, 18, 'Mean', 'Conventional RT')
kidney_33_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 33, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
kidney_33_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 33, 18, 'Mean', 'Conventional RT')
kidney_30_mean = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 30, 18, 'Mean', 'Conventional RT')
kidney_30_v30_adx = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, 30, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_25_v30_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 25, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_23_v30_adx = EQD.Tolerance('Lung', 'Some failure', ab_lung, 23, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
liver_23_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung, 23, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
liver_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung, 23, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT', compute_eqd2 = False)
liver_25_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung, 25, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
liver_30_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung,30, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
liver_33_v60_adx = EQD.Tolerance('Liver', 'Some failure', ab_lung,33, 30, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
spinal_cord_prv_23_v0_03_adx = EQD.Tolerance('SpinalCord_PRV', 'Some failure', ab_spinalcord, 23, 45,'Maximum dose at less than 0.03cc volume', 'Conventional RT')

# Breast
lung_v15_adx = EQD.Tolerance('Lung_L', 'Some failure', ab_lung, fractions_breast_15, 18, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT', compute_eqd2 = False)
heart_mean_breast = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_breast, 2, 'Mean', 'Conventional RT')
heart_mean_breast_15 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_breast_15, 2, 'Mean', 'Conventional RT', compute_eqd2 = False)
humeral_v33_adx = EQD.Tolerance('Humeral', 'Some failure', ab_humeral, fractions_breast, 25, 'Volume receiving tolerance dose being less than 5 cm3', 'Conventional RT')
contralat_breast_mean = EQD.Tolerance('Breast', 'Some failure', ab_breast, fractions_breast_15, 2, 'Mean', 'Conventional RT', compute_eqd2 = False)
lung_v30_adx_25 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast, 20, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_v30_adx_15 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast_15, 18, 'Volume receiving tolerance dose being less than 30%', 'Conventional RT')
lung_v65_adx_15 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast_15, 5, 'Volume receiving tolerance dose being less than 65%', 'Conventional RT')
lad_v100_adx = EQD.Tolerance('LAD', 'Some failure', ab_lad, fractions_breast, 20, 'Volume receiving tolerance dose being less than 100%', 'Conventional RT')
lad_v100_adx_15 = EQD.Tolerance('LAD', 'Some failure', ab_lad, fractions_breast_15, 20, 'Volume receiving tolerance dose being less than 100%', 'Conventional RT')
ipsilateral_breast_v50_adx = EQD.Tolerance('Breast_L/R','Some failure', ab_heart, fractions_breast_15, 40,'Volume receiving tolerance dose being less than 50%', 'Conventional RT' )
heart_mean_breast_tang = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_breast_15, 1.5, 'Mean', 'Conventional RT')
lung_contralateral_mean = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast_15, 0.5, 'Mean', 'Conventional RT')
lung_contralateral_mean_reg = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_breast_15, 1, 'Mean', 'Conventional RT')

# Gyn
bladder_v85_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_gyn, 30, 'Volume receiving tolerance dose being less than 85%', 'Conventional RT',compute_eqd2 = False)
bladder_v75_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_gyn, 40, 'Volume receiving tolerance dose being less than 75%', 'Conventional RT',compute_eqd2 = False)
bladder_v85_adx_eqd2 = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_gyn, 30, 'Volume receiving tolerance dose being less than 85%', 'Conventional RT')
bladder_v75_adx_eqd2 = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_gyn, 40, 'Volume receiving tolerance dose being less than 75%', 'Conventional RT')

bladder_v003_adx = EQD.Tolerance('Bladder', 'Some failure', ab_bladder, fractions_bladder_gyn, 47.3, 'Maximum dose at less than 0.1cc volume', 'Conventional RT')
bladder_v003_55_adx = EQD.Tolerance('Bladder', 'Some failure', ab_bladder, fractions_bladder_gyn, 55, 'Maximum dose at less than 0.1cc volume', 'Conventional RT')
bladder_v003_57_adx = EQD.Tolerance('Bladder', 'Some failure', ab_bladder, fractions_bladder_gyn, 57.5, 'Maximum dose at less than 0.1cc volume', 'Conventional RT')
bowelbag_v350_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace, 25, 30, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT',compute_eqd2 = False)
bowelbag_v100_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace,  25, 40, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT',compute_eqd2 = False)
bowelbag_v350_adx_eqd2 = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace, 25, 30, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelbag_v100_adx_eqd2 = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace,  25, 40, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')

bowelbag_v003_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace, 25, 47.3, 'Maximum dose at less than 0.1cc volume', 'Conventional RT')
bowelbag_v003_57_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace, 25, 57.5, 'Maximum dose at less than 0.1cc volume', 'Conventional RT')
bowelbag_v003_55_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace, 25, 55, 'Maximum dose at less than 0.1cc volume', 'Conventional RT')
femoral_v003_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral_gyn, 50, 'Mean dose being less than tolerance dose', 'Conventional RT',compute_eqd2 = False)
femoral_v003_adx_eqd2 = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral_gyn, 50, 'Mean dose being less than tolerance dose', 'Conventional RT')
kidney_mean_5 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 5, 'Mean', 'Conventional RT')
kidney_mean_10 = EQD.Tolerance('Kidney', 'Some failure', ab_kidney, fractions_kidney, 10, 'Mean', 'Conventional RT')
ovary_mean_5= EQD.Tolerance('Ovary', 'Some failure', ab_ovary, fractions_ovary,5, 'Mean', 'Conventional RT')
ovary_mean_8= EQD.Tolerance('Ovary', 'Some failure', ab_ovary, fractions_ovary,8, 'Mean', 'Conventional RT')
rectum_v003_55_adx = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 55, 'Mean dose being less than tolerance dose', 'Conventional RT')
rectum_v003_adx = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 47.3, 'Mean dose being less than tolerance dose', 'Conventional RT')
rectum_v003_57_adx = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 57.5, 'Mean dose being less than tolerance dose', 'Conventional RT')
rectum_v95_adx = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 30, 'Mean dose being less than tolerance dose', 'Conventional RT',compute_eqd2 = False)
rectum_v85_adx = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 40, 'Mean dose being less than tolerance dose', 'Conventional RT',compute_eqd2 = False)
rectum_v95_adx_eqd2 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 30, 'Mean dose being less than tolerance dose', 'Conventional RT')
rectum_v85_adx_eqd2 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_rectum_gyn, 40, 'Mean dose being less than tolerance dose', 'Conventional RT')

sigmoid_v003_adx = EQD.Tolerance('Sigmoid', 'Some failure', ab_sigmoid, fractions_sigmoid, 47.3, 'Mean dose being less than tolerance dose', 'Conventional RT')
sigmoid_v003_57_adx = EQD.Tolerance('Sigmoid', 'Some failure', ab_sigmoid, fractions_sigmoid, 57.5, 'Mean dose being less than tolerance dose', 'Conventional RT')
sigmoid_v003_55_adx = EQD.Tolerance('Sigmoid', 'Some failure', ab_sigmoid, fractions_sigmoid, 55, 'Mean dose being less than tolerance dose', 'Conventional RT')
spinal_cord_38_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinal_cord_45_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 45, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinal_cord_48_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 48, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
spinal_cord_prv_v003_adx = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_spinalcord, 50, 'Volume receiving tolerance dose being less than 2 cm3', 'Conventional RT')
duodenum_v15_adx = EQD.Tolerance('BowelBag', 'Some failure', ab_bowelspace,  25, 55, 'Volume receiving tolerance dose being less than 15 cm3', 'Conventional RT')
# Prostate
#35 fx:
bladder_v50_adx_eqd2 = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 66, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
bladder_v50_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 66, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
bladder_v35_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 70, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
bladder_v25_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 74, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
bladder_v15_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder, 78, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
rectum_v50_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 50, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
rectum_v50_adx_eqd2 = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 50, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
rectum_v50_adx_bladder = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 60, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT',compute_eqd2 = False)
rectum_v35_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 60, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
rectum_v25_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 66, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
rectum_v20_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 70, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
rectum_v15_adx = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum, 73, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
femoral_v2_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral, 52, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
#fractions_bladder_at_rectum og fractions_penile_bulb = 25?
bladder_v2_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_at_rectum, 50, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
bowelspace_v195_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, fractions_bowelspace, 50, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelspace_v195_adx_eqd2 = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, fractions_bowelspace, 50, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelbag_v195_45_gy_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, fractions_bowelspace, 45, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT',compute_eqd2 = False)
penile_bulb_v90_adx = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, fractions_penile_bulb, 55, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
femoral_mean_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral, 42, 'Mean dose being less than tolerance dose', 'Conventional RT')
femoral_v49_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral, 50, 'Mean dose being less than tolerance dose', 'Conventional RT')
#25 fx:
femoral_v2_adx_hypo2_7 = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral_25, 42.5, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT') #satt ned fra 44 Gy
rectum_v50_adx_hypo2_7 = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_25, 50, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
rectum_v35_adx_hypo2_7 = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_25, 57, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
rectum_v25_adx_hypo2_7 = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_25, 60, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
rectum_v20_adx_hypo2_7 = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_25, 63, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
rectum_v15_adx_hypo2_7 = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_25, 66, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
bladder_v50_adx_hypo2_7 = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_25, 62, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
bladder_v35_adx_hypo2_7 = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_25, 65, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
bladder_v25_adx_hypo2_7 = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_25, 69, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
bowelspace_v195_adx_hypo2_7 = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, 25, 46, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
penile_bulb_v90_adx_hypo2_7 = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, fractions_penile_bulb_25, 50, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
anal_canal_mean_adx_hypo2_7 = EQD.Tolerance('AnalCanal', 'Some failure', ab_anal_canal, 25, 43, 'Mean dose being less than tolerance dose', 'Conventional RT')
#20 fx:
femoral_v2_adx_hypo = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, 20, 40, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT') #satt ned fra 44 Gy
femoral_v49_adx_hypo = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, 20, 42, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT') #brukes ikkje?
penile_bulb_v90_adx_hypo = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, 20, 48, 'Volume receiving tolerance dose being less than 90%', 'Conventional RT') #justert opp fra 46
rectum_v50_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 47, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
rectum_v35_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 53, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
rectum_v25_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 56, 'Volume receiving tolerance dose being less than 25%', 'Conventional RT')
rectum_v20_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 59, 'Volume receiving tolerance dose being less than 20%', 'Conventional RT')
rectum_v15_adx_hypo = EQD.Tolerance('Rectum','Grade >= 2 late rectal toxicity', ab_rectum, fractions_rectum_hypo, 62, 'Volume receiving tolerance dose being less than 15%', 'Conventional RT')
bladder_v50_adx_hypo = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_hypo, 58, 'Volume receiving tolerance dose being less than 50%', 'Conventional RT')
bladder_v35_adx_hypo = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_hypo, 62, 'Volume receiving tolerance dose being less than 35%', 'Conventional RT')
anal_canal_mean_adx_hypo = EQD.Tolerance('AnalCanal', 'Some failure', ab_anal_canal, 20, 40, 'Mean dose being less than tolerance dose', 'Conventional RT')

#Anus/rectum
femoral_5_v2_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, 5, 26.25, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT', compute_eqd2 = False)
bladder_mean_5_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, 5, 20, 'Mean dose being less than tolerance dose', 'Conventional RT', compute_eqd2 = False)
femoral_25_v2_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, 25, 52, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
bowelspace_25_v310_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, 25, 30, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelspace_25_v70_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, 25, 40, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bladder_mean_25_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, 25, 45, 'Mean dose being less than tolerance dose', 'Conventional RT')
femoral_27_v2_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, fractions_femoral_27, 52, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT')
bowelspace_27_v310_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, fractions_bowelspace_27, 30, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bowelspace_27_v70_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, fractions_bowelspace_27, 40, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT')
bladder_mean_27_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, fractions_bladder_27, 45, 'Mean dose being less than tolerance dose', 'Conventional RT')
femoral_30_v2_adx = EQD.Tolerance('Femoral_Heads', 'Some failure', ab_femoral, 30, 52, 'Volume receiving tolerance dose being less than 2%', 'Conventional RT', compute_eqd2 = False)
bowelspace_30_v310_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, 30, 30, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT', compute_eqd2 = False)
bowelspace_30_v70_adx = EQD.Tolerance('BowelSpace', 'Some failure', ab_bowelspace, 30, 40, 'Volume receiving tolerance dose being less than 195 cm3', 'Conventional RT', compute_eqd2 = False)
bladder_mean_30_adx = EQD.Tolerance('Bladder','Some failure', ab_bladder, 30, 45, 'Mean dose being less than tolerance dose', 'Conventional RT', compute_eqd2 = False)

# SBRT:

# SBRT 3 fractions
anal_canal_sbrt_3fx_v0 = EQD.Tolerance('AnalCanal', 'Some failure', ab_anal_canal, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
bile_duct_sbrt_3fx_v0 = EQD.Tolerance('BileDuct_Common', 'Some failure', ab_bile_duct, fractions_sbrt_3, 50, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bladder_sbrt_3fx_v0 = EQD.Tolerance('Bladder', 'Some failure', ab_bladder, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
bladder_sbrt_3fx_v15 = EQD.Tolerance('Bladder', 'Some failure', ab_bladder, fractions_sbrt_3, 17, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bowel_small_sbrt_3fx_v10 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_3, 16, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bowel_small_sbrt_3fx_v0 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_3, 25, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bowel_large_sbrt_3fx_v20 = EQD.Tolerance('Stomach', 'Some failure', ab_bowel, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bowel_large_sbrt_3fx_v0 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
brachial_sbrt_3fx_v0 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
brachial_sbrt_3fx_v3 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
bronchus_sbrt_3fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
bronchus_sbrt_3fx_v5 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_3, 25, 'Volume receiving tolerance dose being less than 4 cm3', 'SBRT')
cauda_equina_sbrt_3fx_v0 = EQD.Tolerance('CaudaEquina', 'Some failure', ab_cauda, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
cauda_equina_sbrt_3fx_v3 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_cauda, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
chestwall_sbrt_3fx_v30 = EQD.Tolerance('Chestwall', 'Some failure', ab_chestwall, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 30cm3', 'SBRT')
esophagus_sbrt_3fx_v0 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_3, 27, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT') #25.2?
esophagus_sbrt_3fx_v5 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 5 cm3', 'SBRT')
femoral_sbrt_3fx_v10 = EQD.Tolerance('FemoralHead', 'Some failure', ab_femoral, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
greatves_sbrt_3fx_v0 = EQD.Tolerance('GreatVes', 'Some failure', ab_greatves, fractions_sbrt_3, 45, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
greatves_sbrt_3fx_v10 = EQD.Tolerance('GreatVes', 'Some failure', ab_greatves, fractions_sbrt_3, 39, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
heart_sbrt_3fx_v0 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
heart_sbrt_3fx_v15 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 15 cm3', 'SBRT')
humeral_sbrt_3fx_v10 = EQD.Tolerance('FemoralHead', 'Some failure', ab_femoral, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
kidneys_3fx_v25 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_3, 10, 'Volume receiving tolerance dose being less than 200cm3', 'SBRT')
kidneys_3fx_v10 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_3, 8.5, 'Volume receiving tolerance dose being less than 33%', 'SBRT')
liver_sbrt_3fx_mean = EQD.Tolerance('Liver', 'Some failure', ab_liver, fractions_sbrt_3, 15, 'Mean', 'SBRT', compute_eqd2 = False)
#liver_sbrt_3fx_v700 = EQD.Tolerance('Liver', 'Some failure', ab_liver, fractions_sbrt_3, 17, 'Volume receiving tolerance dose being less than 700 cm3', 'SBRT')
lung_sbrt_3fx_v10 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_3, 20, 'Volume receiving tolerance dose being less than 10%', 'SBRT')
lung_sbrt_3fx_v37 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_3, 11, 'Volume receiving tolerance dose being less than 10%', 'SBRT')
nerve_root_sbrt_3fx_v0 = EQD.Tolerance('NerveRoot', 'Some failure', ab_cauda, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
nerve_root_sbrt_3fx_v3 = EQD.Tolerance('NerveRoot', 'Some failure', ab_cauda, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
nerve_peripheral_sbrt_3fx_v0 = EQD.Tolerance('NerveRoot', 'Some failure', ab_cauda, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
penile_bulb_sbrt_3fx_v0 = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, fractions_sbrt_3, 42, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
penile_bulb_sbrt_3fx_v3 = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
rectum_sbrt_3fx_v0 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
rectum_sbrt_3fx_v20 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_sbrt_3, 28, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
ribs_sbrt_3fx_v0 = EQD.Tolerance('Ribs', 'Some failure', ab_ribs, fractions_sbrt_3, 54, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
skin_sbrt_3fx_v0 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_3, 33, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT') 
skin_sbrt_3fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT') 
trachea_sbrt_3fx_v5 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_3, 25, 'Volume receiving tolerance dose being less than 4cm3', 'SBRT')
trachea_sbrt_3fx_v0 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_3, 30, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
sacral_plexus_sbrt_3fx_v0 = EQD.Tolerance('SacralPlexus', 'Some failure', ab_cauda, fractions_sbrt_3, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
sacral_plexus_sbrt_3fx_v3 = EQD.Tolerance('SacralPlexus', 'Some failure', ab_cauda, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
spinal_canal_sbrt_3fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT', compute_eqd2 = False) 
spinal_canal_sbrt_3fx_v0_35 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT', compute_eqd2 = False) 
stomach_sbrt_3fx_v0 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
stomach_sbrt_3fx_v10 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_3, 16, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
ureter_sbrt_3fx_v0 = EQD.Tolerance('Ureter', 'Some failure', ab_bladder, fractions_sbrt_3, 40, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')

# SBRT 5 fractions
bladder_sbrt_5fx_v0 = EQD.Tolerance('Bladder', 'Some failure', ab_bladder, fractions_sbrt_5, 38, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
bladder_sbrt_5fx_v15 = EQD.Tolerance('Bladder', 'Some failure', ab_bladder, fractions_sbrt_5, 20, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bowel_small_sbrt_5fx_v10 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_5, 25, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bowel_small_sbrt_5fx_v0 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bowel_large_sbrt_5fx_v20 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_5, 28, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bowel_large_sbrt_5fx_v0 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_5, 38, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
bile_duct_sbrt_5fx_v0 = EQD.Tolerance('BileDuct_Common', 'Some failure', ab_bile_duct, fractions_sbrt_5, 50, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
brachial_sbrt_sbrt_5fx_v0 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
brachial_sbrt_sbrt_5fx_v3 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_brachial, fractions_sbrt_5, 27, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
bronchus_sbrt_5fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_5, 35, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT') 
bronchus_sbrt_5fx_v5 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 4 cm3', 'SBRT') 
cauda_equina_sbrt_5fx_v0 = EQD.Tolerance('CaudaEquina', 'Some failure', ab_cauda, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
cauda_equina_sbrt_5fx_v3 = EQD.Tolerance('BrachialPlexus', 'Some failure', ab_cauda, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
chestwall_sbrt_5fx_v30 = EQD.Tolerance('Chestwall', 'Some failure', ab_chestwall, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 30cm3', 'SBRT')
esophagus_sbrt_5fx_v5 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_5, 20, 'Volume receiving tolerance dose being less than 5 cm3', 'SBRT') 
esophagus_sbrt_5fx_v0 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT') 
femoral_sbrt_5fx_v10 = EQD.Tolerance('FemoralHead', 'Some failure', ab_femoral, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
greatves_sbrt_5fx_v10 = EQD.Tolerance('GreatVes', 'Some failure', ab_greatves, fractions_sbrt_5, 47, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
greatves_sbrt_5fx_v0 = EQD.Tolerance('GreatVes', 'Some failure', ab_greatves, fractions_sbrt_5, 53, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
heart_sbrt_5fx_v15 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 15 cm3', 'SBRT')
heart_sbrt_5fx_v0 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_5, 38, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT') 
humeral_sbrt_5fx_v10 = EQD.Tolerance('FemoralHead', 'Some failure', ab_femoral, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
kidneys_5fx_v10 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_5, 10, 'Volume receiving tolerance dose being less than 33%', 'SBRT')
kidneys_5fx_v25 = EQD.Tolerance('Kidneys', 'Some failure', ab_kidneys, fractions_sbrt_5, 10, 'Volume receiving tolerance dose being less than 200cm3', 'SBRT')
liver_sbrt_5fx_v700 = EQD.Tolerance('Liver', 'Some failure', ab_liver, fractions_sbrt_5, 21, 'Volume receiving tolerance dose being less than 700 cm3', 'SBRT')
lung_sbrt_5fx_v37 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_5, 13, 'Volume receiving tolerance dose being less than 37%', 'SBRT')
lung_sbrt_5fx_v10 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_5, 20, 'Volume receiving tolerance dose being less than 10%', 'SBRT') 
nerve_root_sbrt_5fx_v0 = EQD.Tolerance('NerveRoot', 'Some failure', ab_cauda, fractions_sbrt_5, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
nerve_root_sbrt_5fx_v3 = EQD.Tolerance('NerveRoot', 'Some failure', ab_cauda, fractions_sbrt_5, 22, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
nerve_peripheral_sbrt_5fx_v0 = EQD.Tolerance('NerveRoot', 'Some failure', ab_cauda, fractions_sbrt_5, 24, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
penile_bulb_sbrt_5fx_v0 = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, fractions_sbrt_5, 50, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
penile_bulb_sbrt_5fx_v3 = EQD.Tolerance('PenileBulb', 'Some failure', ab_penile_bulb, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
rectum_sbrt_5fx_v0 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
rectum_sbrt_5fx_v20 = EQD.Tolerance('Rectum', 'Some failure', ab_rectum, fractions_sbrt_5, 24, 'Volume receiving tolerance dose being less than 5cm3', 'SBRT')
ribs_sbrt_5fx_v0 = EQD.Tolerance('Ribs', 'Some failure', ab_ribs, fractions_sbrt_5, 68, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
sacral_plexus_sbrt_5fx_v0 = EQD.Tolerance('SacralPlexus', 'Some failure', ab_cauda, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
sacral_plexus_sbrt_5fx_v3 = EQD.Tolerance('SacralPlexus', 'Some failure', ab_cauda, fractions_sbrt_5, 30, 'Volume receiving tolerance dose being less than 3cm3', 'SBRT')
skin_sbrt_5fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_5, 36, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
skin_sbrt_5fx_v0 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_5, 39, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
spinal_canal_sbrt_5fx_v0_35 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_5, 22, 'Volume receiving tolerance dose being less than 1.2 cm3', 'SBRT', compute_eqd2 = False)
spinal_canal_sbrt_5fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_5, 28, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT', compute_eqd2 = False) 
stomach_sbrt_5fx_v0 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
stomach_sbrt_5fx_v10 = EQD.Tolerance('Stomach', 'Some failure', ab_stomach, fractions_sbrt_5, 25, 'Volume receiving tolerance dose being less than 10cm3', 'SBRT')
trachea_sbrt_5fx_v5 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_5, 32, 'Volume receiving tolerance dose being less than 4cm3', 'SBRT')
trachea_sbrt_5fx_v0 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_5, 35, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')
ureter_sbrt_5fx_v0 = EQD.Tolerance('Ureter', 'Some failure', ab_bladder, fractions_sbrt_5, 45, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')

# Lung SBRT 8 fractions
esophagus_sbrt_8fx_v0 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_8, 40, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT') 
heart_sbrt_8fx_v0 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_8, 44, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT') 
lung_sbrt_8fx_v10 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_8, 20, 'Volume receiving tolerance dose being less than 10%', 'SBRT')
spinal_canal_sbrt_8fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_8, 32, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')#33.6
trachea_sbrt_8fx_v0 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_8, 44, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')#56?
bronchus_sbrt_8fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_8, 44, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')#56
bronchus_contra_sbrt_8fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_8, 48.8, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')

# Lung SBRT 12 fractions
esophagus_sbrt_12fx_v0 = EQD.Tolerance('Esophagus', 'Some failure', ab_esophagus, fractions_sbrt_12, 48, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT') #41.6
heart_sbrt_12fx_v0 = EQD.Tolerance('Heart', 'Some failure', ab_heart, fractions_sbrt_12, 54, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT') #41.6
lung_sbrt_12fx_v10 = EQD.Tolerance('Lung', 'Some failure', ab_lung, fractions_sbrt_8, 20, 'Volume receiving tolerance dose being less than 10%', 'SBRT')
spinal_canal_sbrt_12fx_v0 = EQD.Tolerance('SpinalCanal', 'Some failure', ab_spinalcord, fractions_sbrt_12, 32.4, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')#33.6
trachea_sbrt_12fx_v0 = EQD.Tolerance('Trachea', 'Some failure', ab_trachea, fractions_sbrt_12, 54, 'Volume receiving tolerance dose being less than 0cm3', 'SBRT')#56?
bronchus_sbrt_12fx_v0 = EQD.Tolerance('Main Bronchus', 'Some failure', ab_bronchus, fractions_sbrt_12, 54, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')#56

# Brain SRT 1 fraction
brainstem_srt_1fx_v0 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brainstem_srt_1fx_v1 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_1, 8, 'Volume receiving tolerance dose being less than 0.5 cm3', 'SBRT')
brainstem_prv_srt_1fx_v0 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_1, 12, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brain_srt_1fx_v10 = EQD.Tolerance('Brain', 'Some failure', ab_brain, fractions_sbrt_1, 12, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
cochlea_srt_1fx_v0 = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, fractions_sbrt_1, 9, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
eye_srt_1fx_v0 = EQD.Tolerance('Eye_R','Some failure', ab_eye, fractions_sbrt_1, 8, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
lens_srt_1fx_v0 = EQD.Tolerance('Lens_L','Some failure', ab_lens, fractions_sbrt_1, 5, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_nrv_srt_1fx_v0 = EQD.Tolerance('OpticNrv_L','Some failure', ab_optic_nerve, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_nrv_srt_1fx_v0_2 = EQD.Tolerance('OpticNrv_L','Some failure', ab_optic_nerve, fractions_sbrt_1, 8, 'Volume receiving tolerance dose being less than 0.2 cm3', 'SBRT')
optic_chiasm_srt_1fx_v0 = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_chiasm_srt_1fx_v0_2 = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_sbrt_1, 8, 'Volume receiving tolerance dose being less than 0.2 cm3', 'SBRT')
skin_srt_1fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_1, 14.4, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
spinal_cord_srt_1fx_v0 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_1, 12.5, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_cord_srt_1fx_v0_25 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_1, 10, 'Volume receiving tolerance dose being less than 0.25 cm3', 'SBRT')

# Brain SRT 3 fractions
brainstem_srt_3fx_v0 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brainstem_srt_3fx_v0_35 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brainstem_srt_3fx_v1 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_3, 13, 'Volume receiving tolerance dose being less than 0.5 cm3', 'SBRT')
brainstem_prv_srt_3fx_v0 = EQD.Tolerance('Brainstem', 'Some failure', ab_brainstem, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
brain_srt_3fx_v10 = EQD.Tolerance('Brain', 'Some failure', ab_brain, fractions_sbrt_3, 20, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
cochlea_srt_3fx_v0 = EQD.Tolerance('Cochlea_L', 'Some failure', ab_cochlea, fractions_sbrt_3, 17, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
eye_srt_3fx_v0 = EQD.Tolerance('Eye_L','Some failure', ab_eye, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
lens_srt_3fx_v0 = EQD.Tolerance('Lens_R','Some failure', ab_lens, fractions_sbrt_3, 10, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_nrv_srt_3fx_v0 = EQD.Tolerance('OpticNrv_L','Some failure', ab_optic_nerve, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_nrv_srt_3fx_v0_2 = EQD.Tolerance('OpticNrv_R','Some failure', ab_optic_nerve, fractions_sbrt_3, 13, 'Volume receiving tolerance dose being less than 0.2 cm3', 'SBRT')
optic_chiasm_srt_3fx_v0 = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
optic_chiasm_srt_3fx_v0_2 = EQD.Tolerance('OpticChiasm', 'Some failure', ab_optic_chiasm, fractions_sbrt_3, 13, 'Volume receiving tolerance dose being less than 0.2 cm3', 'SBRT')
skin_srt_3fx_v10 = EQD.Tolerance('Skin', 'Some failure', ab_skin, fractions_sbrt_3, 22.5, 'Volume receiving tolerance dose being less than 10 cm3', 'SBRT')
spinal_cord_srt_3fx_v0 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_3, 22, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')
spinal_cord_srt_3fx_v1 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_3, 13, 'Volume receiving tolerance dose being less than 0.25 cm3', 'SBRT')
spinal_cord_srt_3fx_v0_35 = EQD.Tolerance('SpinalCord', 'Some failure', ab_spinalcord, fractions_sbrt_3, 18, 'Volume receiving tolerance dose being less than 0 cm3', 'SBRT')


