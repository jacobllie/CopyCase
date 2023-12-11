# encoding: utf8

# Import local files:
import rois as ROIS


#Brain

# Whole brain
#brain_whole_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.eye_l_prv, ROIS.eye_r_prv, ROIS.lens_l_prv, ROIS.lens_r_prv, ROIS.brain, ROIS.nasal_cavity]
#brain_whole_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.brain, ROIS.lacrimal_r, ROIS.lacrimal_l, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.skin_brain, ROIS.nasal_cavity]
brain_whole_oars = [ROIS.lens_l, ROIS.lens_r, ROIS.brain, ROIS.nasal_cavity]


#brain_whole_oars = [ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.brain]
# Partial brain
#brain_partial_oars = [ROIS.nasal_cavity, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.hippocampus_l, ROIS.hippocampus_r, ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r,
#  ROIS.optic_nrv_l, ROIS.optic_nrv_r,  ROIS.lacrimal_l, ROIS.lacrimal_r, ROIS.optic_chiasm, ROIS.eye_l_prv, ROIS.eye_r_prv, ROIS.lens_l_prv, ROIS.lens_r_prv, ROIS.brainstem,
#  ROIS.brainstem_prv, ROIS.optic_nrv_l_prv, ROIS.optic_nrv_r_prv,  ROIS.lacrimal_l_prv, ROIS.lacrimal_r_prv, ROIS.optic_chiasm_prv, ROIS.brain, ROIS.skin, ROIS.spinal_canal_head
#]
brain_partial_oars = [ROIS.brain, ROIS.brainstem, ROIS.brainstem_core, ROIS.brainstem_surface, ROIS.optic_chiasm, ROIS.optic_nrv_l, ROIS.optic_nrv_r, ROIS.cochlea_l, ROIS.cochlea_r, 
	ROIS.hippocampus_l, ROIS.hippocampus_r, ROIS.lacrimal_l, ROIS.lacrimal_r, ROIS.lens_l, ROIS.lens_r, ROIS.pituitary, ROIS.skin, ROIS.eye_l, ROIS.eye_r,ROIS.retina_l,
                      ROIS.retina_r,ROIS.cornea_l,ROIS.cornea_r,ROIS.spinal_cord,ROIS.optic_nrv_l_prv, ROIS.optic_nrv_r_prv,ROIS.optic_chiasm_prv, ROIS.brainstem_surface_prv]

brain_partial_empty_oars = [ROIS.brainstem, ROIS.brainstem_core, ROIS.brainstem_surface, ROIS.optic_chiasm_empty, ROIS.optic_nrv_l_empty, ROIS.optic_nrv_r_empty, ROIS.cochlea_l, ROIS.cochlea_r, 
	ROIS.hippocampus_l, ROIS.hippocampus_r, ROIS.lacrimal_l, ROIS.lacrimal_r, ROIS.lens_l_empty, ROIS.lens_r_empty, ROIS.pituitary_empty, ROIS.skin, ROIS.eye_l_empty, ROIS.eye_r_empty, ROIS.retina_l,
                      ROIS.retina_r,ROIS.cornea_l,ROIS.cornea_r,ROIS.spinal_cord,ROIS.optic_nrv_l_prv, ROIS.optic_nrv_r_prv,ROIS.optic_chiasm_prv, ROIS.brainstem_surface_prv]
# Stereotactic
brain_stereotactic_oars = [ROIS.brain, ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.optic_nrv_l, ROIS.optic_nrv_r, ROIS.optic_chiasm,
                           ROIS.brainstem, ROIS.skin,ROIS.spinal_cord,ROIS.spinal_cord_prv_2,ROIS.brainstem_prv_2]

brain_stereotactic_empty_oars = [ROIS.eye_l_empty, ROIS.eye_r_empty, ROIS.lens_l_empty, ROIS.lens_r_empty, ROIS.cochlea_l, ROIS.cochlea_r, ROIS.optic_nrv_l_empty, ROIS.optic_nrv_r_empty, ROIS.optic_chiasm_empty,
                           ROIS.brainstem, ROIS.skin,ROIS.spinal_cord,ROIS.spinal_cord_prv_2,ROIS.brainstem_prv_2]

#Head and Neck
head_neck_oars = [ROIS.brain_head, ROIS.brainstem, ROIS.spinal_cord_head, ROIS.parotid_l, ROIS.parotid_r,  ROIS.spinal_cord_prv, ROIS.brainstem_prv, ROIS.esophagus_head, ROIS.trachea_head, ROIS.thyroid_head,
                  ROIS.lips, ROIS.x_skulder_h, ROIS.x_skulder_v, ROIS.x_sparevolum, ROIS.submand_l, ROIS.submand_r, ROIS.pharynx_constr_s, ROIS.pharynx_constr_m,
                  ROIS.pharynx_constr_i, ROIS.oral_cavity, ROIS.larynx_sg, ROIS.larynx_g, ROIS.mandible, ROIS.lung_l_head, ROIS.lung_r_head]
head_neck_glottis_oars = [ROIS.spinal_cord, ROIS.a_carotid_l_empty, ROIS.a_carotid_r, ROIS.spinal_cord_prv, ROIS.oral_cavity]

head_neck_palliative_oars = [ROIS.brainstem, ROIS.spinal_cord, ROIS.parotid_l, ROIS.parotid_r,  ROIS.spinal_cord_prv, ROIS.brainstem_prv, ROIS.x_skulder_h, ROIS.x_skulder_v,
                  ROIS.x_sparevolum, ROIS.submand_l, ROIS.submand_r, ROIS.oral_cavity]


# Lung
lung_oars = [ROIS.esophagus, ROIS.heart, ROIS.trachea, ROIS.x_trachea_bronchus, ROIS.x_a_aorta, ROIS.spinal_canal, ROIS.lung_r, ROIS.lung_l, ROIS.liver]
lung_empty_oars = [ROIS.esophagus_empty, ROIS.heart_empty, ROIS.x_trachea_bronchus, ROIS.x_a_aorta, ROIS.spinal_canal_empty]

# Liver
liver_stereotactic_oars = [ROIS.heart, ROIS.esophagus, ROIS.great_vessels, ROIS.skin, ROIS.liver, ROIS.spinal_canal, ROIS.kidney_r, ROIS.kidney_l, ROIS.kidneys, ROIS.stomach, ROIS.duodenum,
                           ROIS.bowel_small, ROIS.lung_r, ROIS.lung_l, ROIS.lungs]

liver_stereotactic_empty_oars = [ROIS.heart_empty, ROIS.esophagus_empty, ROIS.great_vessels, ROIS.skin, ROIS.liver_empty, ROIS.spinal_canal_empty, ROIS.kidney_r_empty, ROIS.kidney_l_empty,
                                 ROIS.kidneys, ROIS.stomach_empty, ROIS.duodenum, ROIS.bowel_small]


# Lung stereotactic 
lung_stereotactic_oars = [ROIS.esophagus, ROIS.heart, ROIS.trachea, ROIS.great_vessels, ROIS.skin, ROIS.spinal_canal, ROIS.lung_r, ROIS.lung_l, ROIS.liver]
lung_stereotactic_empty_oars = [ROIS.esophagus_empty, ROIS.heart_empty, ROIS.trachea_empty, ROIS.great_vessels, ROIS.skin, ROIS.spinal_canal_empty]
# Lung NARLAL
lung_narlal_oars =  [ROIS.spinal_canal_empty, ROIS.spinal_cord, ROIS.esophagus_empty, ROIS.heart_empty, ROIS.trachea_empty, ROIS.bronchus, ROIS.a_aorta, ROIS.liver_empty, ROIS.brachial_plexus_r,ROIS.brachial_plexus_l,
                     ROIS.x_spinal_canal, ROIS.esophagus_prv, ROIS.bronchus_prv, ROIS.connective_tissue, ROIS.chestwall, ROIS.trachea_prv,ROIS.spinal_cord_narlal_prv, ROIS.lung_r, ROIS.lung_l]

# Esophagus 
esophagus_oars = [ROIS.spinal_canal, ROIS.heart, ROIS.liver, ROIS.spinal_canal_prv, ROIS.bowel_bag, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.lung_r, ROIS.lung_l, ROIS.lungs]
esophagus_empty_oars = [ROIS.spinal_canal_empty, ROIS.heart_empty, ROIS.liver_empty, ROIS.spinal_canal_prv, ROIS.bowel_bag, ROIS.kidney_l_empty, ROIS.kidney_r_empty, ROIS.kidneys]

# Breast:
# Regional lymph nodes  
#breast_reg_oars = [ROIS.heart, ROIS.a_lad, ROIS.heart_prv, ROIS.sternum, ROIS.thyroid, ROIS.trachea, ROIS.esophagus, ROIS.z_crp]

# Tangential
breast_tang_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.heart, ROIS.a_lad, ROIS.heart_prv, ROIS.sternum, ROIS.liver]

breast_tang_empty_oars = [ROIS.heart_empty, ROIS.a_lad_empty, ROIS.heart_prv]

# Partial breast/ not in use
breast_part_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.heart, ROIS.spinal_canal, ROIS.lad, ROIS.surgical_bed]

breast_reg_oars = [ROIS.lung_r, ROIS.lung_l, ROIS.heart, ROIS.a_lad, ROIS.heart_prv, ROIS.sternum, ROIS.thyroid, ROIS.trachea, ROIS.esophagus, ROIS.spinal_canal, ROIS.z_crp, ROIS.liver, ROIS.humeral_r, ROIS.humeral_l, ROIS.z_crp]
breast_reg_empty_oars = [ROIS.heart_empty, ROIS.a_lad_empty, ROIS.heart_prv, ROIS.thyroid_empty, ROIS.esophagus_empty, ROIS.z_crp]

# Gyn
gyn_oars = [ ROIS.rectum, ROIS.bowel_bag,ROIS.spinal_cord, ROIS.spinal_cord_prv, ROIS.sigmoid,ROIS.bladder]

gyn_vulva_oars = [ ROIS.rectum, ROIS.bowel_bag, ROIS.bladder, ROIS.anal_canal, ROIS.cauda_equina]

gyn_palliative_oars = [ROIS.rectum, ROIS.bowel_bag, ROIS.bladder]

# Prostate
prostate_oars = [ROIS.penile_bulb,ROIS.rectum, ROIS.anal_canal, ROIS.bowel_bag, ROIS.bladder, ROIS.marker1, ROIS.marker2]

# Prostate bed
prostate_bed_oars = [ ROIS.penile_bulb, ROIS.rectum, ROIS.anal_canal, ROIS.bladder]

prostate_palliative_oars = [ROIS.penile_bulb, ROIS.rectum, ROIS.anal_canal, ROIS.bowel_bag, ROIS.bladder]

# Rectum
rectum_oars = [ROIS.bladder, ROIS.bowel_bag, ROIS.genitals]

# Anus
anus_oars = [ROIS.bladder, ROIS.bowel_bag, ROIS.genitals]

# Bladder
bladder_oars = [ ROIS.bladder, ROIS.bowel_bag, ROIS.rectum, ROIS.genitals]



# Palliative
# Head:
palliative_head_oars = [ROIS.brain, ROIS.eye_l, ROIS.eye_r, ROIS.lens_l, ROIS.lens_r, ROIS.brainstem, ROIS.spinal_canal]

palliative_head_empty_oars = [ROIS.eye_l_empty, ROIS.eye_r_empty, ROIS.lens_l_empty, ROIS.lens_r_empty, ROIS.brainstem, ROIS.spinal_canal_empty]

# Neck
palliative_neck_oars = [ROIS.spinal_canal, ROIS.parotid_l, ROIS.parotid_r, ROIS.oral_cavity]

palliative_neck_empty_oars = [ROIS.spinal_canal_empty, ROIS.parotid_l, ROIS.parotid_r, ROIS.oral_cavity]

# Thorax
palliative_thorax_oars = [ROIS.heart, ROIS.spinal_canal, ROIS.esophagus, ROIS.trachea, ROIS.lung_l, ROIS.lung_r, ROIS.lungs, ROIS.liver]
palliative_thorax_empty_oars = [ROIS.heart_empty, ROIS.spinal_canal_empty, ROIS.esophagus_empty]

# Thorax and abdomen
palliative_thorax_abdomen_oars = [ROIS.heart, ROIS.spinal_canal, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.bowel_bag, ROIS.esophagus, ROIS.stomach, ROIS.liver]

palliative_thorax_abdomen_empty_oars = [ROIS.heart_empty, ROIS.spinal_canal_empty, ROIS.kidney_l_empty, ROIS.kidney_r_empty, ROIS.kidneys, ROIS.bowel_bag, ROIS.esophagus_empty, ROIS.stomach_empty]

# Abdomen
palliative_abdomen_oars = [ROIS.bowel_bag, ROIS.spinal_canal, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.stomach, ROIS.liver]

palliative_abdomen_empty_oars = [ROIS.bowel_bag, ROIS.spinal_canal_empty, ROIS.kidney_l_empty, ROIS.kidney_r_empty, ROIS.kidneys, ROIS.stomach_empty]

#Abdomen and pelvis
palliative_abdomen_pelvis_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bowel_bag, ROIS.spinal_canal, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.rectum, ROIS.bladder]

palliative_abdomen_pelvis_empty_oars = [ROIS.bowel_bag, ROIS.spinal_canal_empty, ROIS.kidney_l_empty, ROIS.kidney_r_empty, ROIS.kidneys, ROIS.rectum, ROIS.bladder]

#Pelvis
palliative_pelvis_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.bowel_bag, ROIS.rectum, ROIS.spinal_canal, ROIS.bladder]

palliative_pelvis_empty_oars = [ROIS.bowel_bag, ROIS.rectum, ROIS.spinal_canal_empty, ROIS.bladder]

# Stereotactic, spine cervical
palliative_stereotactic_spine_cervical_oars = [ ROIS.spinal_cord, ROIS.spinal_canal_empty, ROIS.nerve_root1_l, ROIS.nerve_root2_l,ROIS.nerve_root1_r,ROIS.nerve_root2_r,ROIS.nerve_roots,  ROIS.parotid_r, ROIS.parotid_l, ROIS.esophagus, ROIS.trachea,  ROIS.skin,
                                               ROIS.spinal_cord_prv_2,  ROIS.nerve_roots_prv, ROIS.esophagus_prv]
palliative_stereotactic_spine_cervical_empty_oars = [ ROIS.spinal_cord, ROIS.spinal_canal_empty, ROIS.nerve_root1_l, ROIS.nerve_root2_l,ROIS.nerve_root1_r,ROIS.nerve_root2_r,ROIS.nerve_roots,  ROIS.parotid_r, ROIS.parotid_l, ROIS.esophagus_empty, ROIS.trachea_empty,  ROIS.skin,
                                               ROIS.spinal_cord_prv_2,  ROIS.nerve_roots_prv, ROIS.esophagus_prv]

# Stereotactic, spine thorax
palliative_stereotactic_spine_thorax_oars = [ ROIS.spinal_canal_empty, ROIS.spinal_cord, ROIS.nerve_root1_l,ROIS.nerve_root2_l,ROIS.nerve_root1_r,ROIS.nerve_root2_r,ROIS.nerve_roots, ROIS.esophagus, ROIS.trachea, ROIS.heart, ROIS.great_vessels,  ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.skin,
                                               ROIS.spinal_cord_prv_2, ROIS.nerve_roots_prv, ROIS.esophagus_prv, ROIS.great_vessels_prv]


palliative_stereotactic_spine_thorax_empty_oars = [ ROIS.spinal_canal_empty, ROIS.spinal_cord, ROIS.nerve_root1_l,ROIS.nerve_root2_l,ROIS.nerve_root1_r,ROIS.nerve_root2_r,ROIS.nerve_roots, ROIS.esophagus_empty, ROIS.trachea_empty, ROIS.heart_empty, ROIS.great_vessels,  ROIS.kidney_l_empty, ROIS.kidney_r_empty, ROIS.kidneys, ROIS.skin,
                                               ROIS.spinal_cord_prv_2, ROIS.nerve_roots_prv, ROIS.esophagus_prv, ROIS.great_vessels_prv]

# Stereotactic, thorax
palliative_stereotactic_thorax_oars = [ROIS.spinal_canal_empty, ROIS.spinal_cord, ROIS.nerve_root1_l,ROIS.nerve_root2_l,ROIS.nerve_root1_r,ROIS.nerve_root2_r,ROIS.nerve_roots,  ROIS.nerve_peripheral, ROIS.trachea, ROIS.esophagus, ROIS.heart, ROIS.great_vessels, ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.liver, ROIS.humeral_r, ROIS.humeral_l,
                                       ROIS.skin, ROIS.spinal_cord_prv_2,ROIS.nerve_peripheral_prv, ROIS.nerve_roots_prv, ROIS.esophagus_prv, ROIS.great_vessels_prv]

palliative_stereotactic_thorax_empty_oars = [ROIS.spinal_canal_empty, ROIS.spinal_cord, ROIS.nerve_root1_l,ROIS.nerve_root2_l,ROIS.nerve_root1_r,ROIS.nerve_root2_r,ROIS.nerve_roots,  ROIS.nerve_peripheral, ROIS.trachea_empty, ROIS.esophagus_empty, ROIS.heart_empty, ROIS.great_vessels, ROIS.kidney_l_empty, ROIS.kidney_r_empty, ROIS.kidneys, ROIS.liver_empty, ROIS.humeral_r_empty, ROIS.humeral_l_empty,
                                       ROIS.skin, ROIS.spinal_cord_prv_2,ROIS.nerve_peripheral_prv, ROIS.nerve_roots_prv, ROIS.esophagus_prv, ROIS.great_vessels_prv]

# Stereotactic, spine pelvis
palliative_stereotactic_spine_pelvis_oars = [ROIS.femoral_l, ROIS.femoral_r, ROIS.spinal_cord, ROIS.spinal_canal_empty, ROIS.nerve_root1_l,ROIS.nerve_root2_l,ROIS.nerve_root1_r,ROIS.nerve_root2_r,ROIS.nerve_roots, ROIS.cauda_equina, ROIS.sacral_plexus,
                                             ROIS.kidney_l, ROIS.kidney_r, ROIS.kidneys, ROIS.stomach,
                                             ROIS.duodenum, ROIS.bowel_small, ROIS.bowel_large,
                                             ROIS.anal_canal, ROIS.rectum, ROIS.bladder, ROIS.skin, ROIS.spinal_cord_prv_2,  ROIS.sacral_plexus_prv, ROIS.nerve_roots_prv,  ROIS.cauda_equina_prv,
                                             ROIS.anal_canal_prv, ROIS.rectum_prv,ROIS.bladder_prv,ROIS.stomach_prv, ROIS.duodenum_prv, ROIS.bowel_small_prv, ROIS.bowel_large_prv ]

# Stereotactic, spine pelvis
palliative_stereotactic_spine_pelvis_empty_oars = [ROIS.spinal_cord, ROIS.spinal_canal_empty, ROIS.nerve_root1_l,ROIS.nerve_root2_l,ROIS.nerve_root1_r,ROIS.nerve_root2_r,ROIS.nerve_roots, ROIS.cauda_equina, ROIS.sacral_plexus,
                                                   ROIS.kidney_l_empty, ROIS.kidney_r_empty, ROIS.kidneys, ROIS.stomach_empty, ROIS.duodenum, ROIS.bowel_small, ROIS.bowel_large,
                                                   ROIS.anal_canal, ROIS.rectum, ROIS.bladder, ROIS.skin, ROIS.spinal_cord_prv_2,  ROIS.sacral_plexus_prv, ROIS.nerve_roots_prv,  ROIS.cauda_equina_prv,
                                                   ROIS.anal_canal_prv, ROIS.rectum_prv,ROIS.bladder_prv,ROIS.stomach_prv, ROIS.duodenum_prv, ROIS.bowel_small_prv, ROIS.bowel_large_prv ]

# Stereotactic, pelvis
palliative_stereotactic_pelvis_oars = [ ROIS.femoral_l, ROIS.femoral_r, ROIS.nerve_peripheral, ROIS.sacral_plexus, ROIS.bowel_small, ROIS.bowel_large, ROIS.anal_canal, ROIS.rectum,
                                       ROIS.bladder, ROIS.penile_bulb, ROIS.skin, ROIS.nerve_peripheral_prv, ROIS.sacral_plexus_prv,ROIS.anal_canal_prv, ROIS.rectum_prv, ROIS.bladder_prv, ROIS.bowel_small_prv, ROIS.bowel_large_prv ]

palliative_stereotactic_pelvis_empty_oars = [ ROIS.nerve_peripheral, ROIS.sacral_plexus, ROIS.bowel_small, ROIS.bowel_large, ROIS.anal_canal, ROIS.rectum,
                                       ROIS.bladder, ROIS.penile_bulb,  ROIS.skin, ROIS.nerve_peripheral_prv, ROIS.sacral_plexus_prv,ROIS.anal_canal_prv, ROIS.rectum_prv, ROIS.bladder_prv, ROIS.bowel_small_prv, ROIS.bowel_large_prv ]

# Stereotactic, extremities
palliative_stereotactic_extremities_oars = [ROIS.nerve_peripheral, ROIS.skin, ROIS.nerve_peripheral_prv, ROIS.great_vessels, ROIS.great_vessels_prv]
