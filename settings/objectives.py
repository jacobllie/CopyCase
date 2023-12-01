# encoding: utf8

# Import system libraries:
from __future__ import division
import math
from connect import *
import clr, sys
from tkinter import messagebox

# Import local files:
import gui_functions as GUIF
import margins as MARGINS
import patient_model_functions as PMF
import rois as ROIS
import roi as ROI
import roi_functions as ROIF
import objective_functions as OF
import region_codes as RC
import structure_set_functions as SSF
import tolerance_doses as TOL

# OAR objectives:
# Brain
brain_oar_objectives = []
brain_whole_oar_objectives = [ROIS.lens_l, ROIS.lens_r, ROIS.nasal_cavity]
brain_stereotactic_oar_objectives = []
# Breast
breast_tang_oar_objectives = []
breast_reg_l_oar_objectives = []
breast_reg_r_oar_objectives = []
breast_reg_oar_objectives = []
# Head Neck
head_neck_objectives = []
# Esophagus
esophagus_objectives = []
# Lung
def lung_objectives(ss, target):
  if target in [ROIS.ctv.name, ROIS.gtv.name]:
    lung_objectives = [ROIS.spinal_canal, ROIS.heart, ROIS.lungs_gtv]
  elif target in [ROIS.ictv.name, ROIS.ictv_p.name, ROIS.ictv_n.name]:
    lung_objectives = [ROIS.spinal_canal, ROIS.heart, ROIS.lungs_igtv]
  if SSF.has_roi_with_shape(ss, ROIS.esophagus.name):
    lung_objectives.extend([ROIS.esophagus])
  return lung_objectives
    
lung_4dct_objectives = [ROIS.spinal_canal, ROIS.heart, ROIS.lungs_igtv]
# Liver
liver_objectives = []
# Palliative
palliative_head_oar_objectives = [ROIS.spinal_canal_head, ROIS.eye_l, ROIS.eye_r]
palliative_neck_oar_objectives = [ROIS.spinal_canal_head, ROIS.parotids, ROIS.trachea]
palliative_head_and_neck_objectives = [ROIS.spinal_cord, ROIS.brainstem, ROIS.parotid_l, ROIS.parotid_r, ROIS.submand_l, ROIS.submand_r, ROIS.oral_cavity, ROIS.x_skulder_h, ROIS.x_skulder_v, ROIS.x_sparevolum]
palliative_thorax_oar_objectives =  [ROIS.spinal_canal, ROIS.heart, ROIS.lungs, ROIS.esophagus, ROIS.liver, ROIS.trachea]
palliative_thorax_and_abdomen_oar_objectives =  [ROIS.spinal_canal, ROIS.heart, ROIS.lungs, ROIS.kidney_l, ROIS.kidney_r,  ROIS.liver, ROIS.stomach, ROIS.bowel_space]
palliative_abdomen_oar_objectives =  [ROIS.spinal_canal, ROIS.kidney_l, ROIS.kidney_r,  ROIS.bowel_space, ROIS.stomach]
palliative_abdomen_and_pelvis_objectives = [ROIS.spinal_canal, ROIS.kidney_l, ROIS.kidney_r, ROIS.bowel_space, ROIS.bladder, ROIS.rectum]
palliative_pelvis_oar_objectives =  [ROIS.bowel_space, ROIS.bladder, ROIS.rectum, ROIS.spinal_canal]
palliative_other_oar_objectives =  []
palliative_prostate_oar_objectives = [ROIS.bowel_space, ROIS.bladder, ROIS.rectum, ROIS.anal_canal]
# Bladder
bladder_objectives = [ROIS.bowel_bag, ROIS.rectum, ROIS.genitals]
# Prostate
prostate_objectives = []
prostate_bed_objectives = []
#Gyn
gyn_objectives = []
palliative_gyn_objectives =[ROIS.bowel_space, ROIS.bladder, ROIS.rectum]
# Rectum
rectum_objectives = []
anus_objectives = []

# Functions that creates objectives in the RayStation Plan Optimization module for various cases:

# Create common objectives.
def create_common_objectives(ss, plan, total_dose):
  OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 30)
  OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
  OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 80)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30)


# Create palliative objectives.
def create_palliative_objectives(ss, plan, total_dose, region_code, target):
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
  if nr_targets > 1:
    if len(target) > 0: # Multiple targets
      for i in range(len(target)):
        OF.uniform_dose(ss, plan, target[i], total_dose*100, 30)
      for i in range(len(target)):  
        OF.min_dose(ss, plan, target[i].replace("C", "P"), total_dose*100*0.95, 150)
        OF.max_dose(ss, plan, target[i].replace("C", "P"), total_dose*100*1.05, 80)
      OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 1.5, 30)
      OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 30)
  else:
    OF.uniform_dose(ss, plan, target, total_dose*100, 30)
    OF.min_dose(ss, plan, target.replace("C", "P"), total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, target.replace("C", "P"), total_dose*100*1.05, 80)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 1.5, 30)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 30)
    #if SSF.has_roi_with_shape(ss, ROIS.spinal_canal.name) and region_code not in RC.palliative_columna_codes:
    #  OF.max_dose(ss, plan, ROIS.spinal_canal.name, total_dose*100*0.9, 2)
      


# BRAIN Whole
def create_whole_brain_objectives(ss, plan, total_dose):
  OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 30)
  OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.97, 150)
  OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.03, 80)
  OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, total_dose*100/2, 1.5, 30)
  OF.max_dose(ss, plan, ROIS.external.name, total_dose*100*1.05, 30)



# BRAIN Partial 
def create_brain_objectives(pm, examination, ss, plan, total_dose, target, nr_fractions):
  if nr_fractions in [1, 3]: # Stereotactic brain
    if nr_fractions == 1: # One fraction
      if target == ROIS.ptv.name: # one target
        OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 500)
        OF.max_dose(ss, plan, ROIS.ptv.name, 1.5*total_dose*100, 100)
        OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 2, 10)
        OF.fall_off(ss, plan, ROIS.x_ptv_ring_1.name, total_dose*100, total_dose*100/2, 0.5, 1)
      elif len(target) > 0: # Multiple targets
        for i in range(len(target)):
          OF.min_dose(ss, plan, target[i], total_dose*100, 500)
          OF.max_dose(ss, plan, target[i], 1.5*total_dose*100, 100)
        OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 2, 10)
        for i in range(len(target)):
          OF.fall_off(ss, plan, "x"+target[i]+"_Ring0-1cm", total_dose*100, total_dose*100/2, 0.5, 1)
    if nr_fractions == 3:# Three fractions
      if target == ROIS.ptv.name: # one target
        OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 1500)
        OF.max_dose(ss, plan, ROIS.ptv.name, 1.463*total_dose*100, 100)
        OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 2, 10)
        OF.fall_off(ss, plan, ROIS.x_ptv_ring_1.name, total_dose*100, 12*100, 0.5, 1)
      elif len(target) > 0: # Multiple targets
        for i in range(len(target)):
          OF.min_dose(ss, plan, target[i], total_dose*100, 1500)
          OF.max_dose(ss, plan, target[i], 1.463*total_dose*100, 100)
        OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 2, 10)
        for i in range(len(target)):
          OF.fall_off(ss, plan, "x"+target[i]+"_Ring0-1cm", total_dose*100, 12*100, 0.5, 1)
  else: # Partial brain
    # Objectives for prioritized OARs:
    prioritized_oars = [ROIS.brainstem_core, ROIS.brainstem_surface, ROIS.optic_chiasm, ROIS.optic_nrv_l, ROIS.optic_nrv_r, ROIS.spinal_cord]
    if nr_fractions <20:
      tolerances = [
        TOL.brainstem_core_v003_adx, TOL.brainstem_surface_v003_adx, TOL.optic_chiasm_v003_adx,
        TOL.optic_nrv_v003_adx, TOL.optic_nrv_v003_adx, TOL.spinalcord_v2_adx
      ]
    elif nr_fractions == 30:
      tolerances = [
        TOL.brainstem_core_30_v003_adx, TOL.brainstem_surface_v003_adx, TOL.optic_chiasm_30_v003_adx,
        TOL.optic_nrv_30_v003_adx, TOL.optic_nrv_30_v003_adx, TOL.spinalcord30_v0_03_adx
      ]
    elif nr_fractions == 33:
      tolerances = [
        TOL.brainstem_core_33_v003_adx, TOL.brainstem_surface_33_v003_adx, TOL.optic_chiasm_33_v003_adx,
        TOL.optic_nrv_33_v003_adx, TOL.optic_nrv_33_v003_adx, TOL.spinalcord33_v0_03_adx
      ]
    conflict_oars = []
    ptv_overlap = False
    for i in range(len(prioritized_oars)):
      if tolerances[i].equivalent(nr_fractions) < total_dose*0.95:
        conflict_oars.append(prioritized_oars[i])
        
      if SSF.roi_overlap(pm, examination, ss, ROIS.ptv, prioritized_oars[i], 1.5):
        ptv_overlap = True
        #messagebox.showinfo("", str(SSF.roi_overlap(pm, examination, ss, ROIS.ptv, prioritized_oars[i], 1.5)))
    # Setup of min and uniform doses depends on presence of critical overlaps or not:
    if len(conflict_oars) > 0 and ptv_overlap:
      # Create subtraction and intersect ROIs for planning of conflicting sites:
      ctv_oars = ROI.ROIAlgebra(ROIS.ctv_oars.name, ROIS.ctv_oars.type, ROIS.ctv.color, sourcesA = [ROIS.ctv], sourcesB = conflict_oars, operator = 'Subtraction',
                                marginsA = MARGINS.zero, marginsB = MARGINS.uniform_2mm_expansion)
      ptv_oars = ROI.ROIAlgebra(ROIS.ptv_oars.name, ROIS.ptv_oars.type, ROIS.ptv.color, sourcesA = [ROIS.ptv], sourcesB = conflict_oars, operator = 'Subtraction',
                                marginsA = MARGINS.zero, marginsB = MARGINS.uniform_2mm_expansion)
      ptv_and_oars = ROI.ROIAlgebra(ROIS.ptv_and_oars.name, ROIS.ptv_and_oars.type, ROIS.other_ptv.color, sourcesA = [ROIS.ptv],
                                    sourcesB = conflict_oars, operator='Intersection')
      rois = [ctv_oars, ptv_oars, ptv_and_oars]
      PMF.delete_matching_rois(pm, rois)
      for i in range(len(rois)):
        PMF.create_algebra_roi(pm, examination, ss, rois[i])
        PMF.exclude_roi_from_export(pm, rois[i].name)
      # Create objectives for the subtraction/intersect ROIs:
      OF.uniform_dose(ss, plan, ROIS.ptv_and_oars.name, (tolerances[0].equivalent(nr_fractions)*100-50), 5) # (Note that this assumes our OARs have the same tolerance dose...)
      OF.uniform_dose(ss, plan, ROIS.ctv_oars.name, total_dose*100, 30)
      OF.min_dose(ss, plan, ROIS.ptv_oars.name, total_dose*100*0.95, 150)
    else:
      OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 30)
      OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 80)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/3, 1.5, 10)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/12, 4, 30)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 30)
    if nr_fractions <20:
      OF.max_dose(ss, plan, ROIS.brainstem_surface.name, total_dose*105 , 60)
      OF.max_dose(ss, plan, ROIS.brainstem_core.name,  total_dose*105, 80)
      OF.max_dose(ss, plan, ROIS.optic_chiasm.name,  total_dose*105, 40)
      OF.max_dose(ss, plan, ROIS.optic_nrv_l.name,  total_dose*105, 20)
      OF.max_dose(ss, plan, ROIS.optic_nrv_r.name,  total_dose*105, 20)
      OF.max_dose(ss, plan, ROIS.spinal_cord.name, (TOL.spinalcord_v2_adx.equivalent(nr_fractions)*100)-50, 20)
    elif nr_fractions == 30:
      OF.max_dose(ss, plan, ROIS.brainstem_surface.name, (TOL.brainstem_surface_v003_adx.equivalent(nr_fractions)*100)-50, 60)
      OF.max_dose(ss, plan, ROIS.brainstem_core.name, (TOL.brainstem_core_30_v003_adx.equivalent(nr_fractions)*100)-50, 80)
      OF.max_dose(ss, plan, ROIS.optic_chiasm.name, (TOL.optic_chiasm_30_v003_adx.equivalent(nr_fractions)*100)-50, 40)
      OF.max_dose(ss, plan, ROIS.optic_nrv_l.name, (TOL.optic_nrv_30_v003_adx.equivalent(nr_fractions)*100)-50, 20)
      OF.max_dose(ss, plan, ROIS.optic_nrv_r.name, (TOL.optic_nrv_30_v003_adx.equivalent(nr_fractions)*100)-50, 20)
      OF.max_dose(ss, plan, ROIS.spinal_cord.name, (TOL.spinalcord30_v0_03_adx.equivalent(nr_fractions)*100)-50, 20)
    elif nr_fractions == 33:
      OF.max_dose(ss, plan, ROIS.brainstem_surface.name, (TOL.brainstem_surface_33_v003_adx.equivalent(nr_fractions)*100)-50, 60)
      OF.max_dose(ss, plan, ROIS.brainstem_core.name, (TOL.brainstem_core_33_v003_adx.equivalent(nr_fractions)*100)-50, 80)
      OF.max_dose(ss, plan, ROIS.optic_chiasm.name, (TOL.optic_chiasm_33_v003_adx.equivalent(nr_fractions)*100)-50, 40)
      OF.max_dose(ss, plan, ROIS.optic_nrv_l.name, (TOL.optic_nrv_33_v003_adx.equivalent(nr_fractions)*100)-50, 20)
      OF.max_dose(ss, plan, ROIS.optic_nrv_r.name, (TOL.optic_nrv_33_v003_adx.equivalent(nr_fractions)*100)-50, 20)
      OF.max_dose(ss, plan, ROIS.spinal_cord.name, (TOL.spinalcord33_v0_03_adx.equivalent(nr_fractions)*100)-50, 20)   
    # Setup of objectives for less prioritized OARs:
    other_oars = [
      ROIS.retina_l, ROIS.retina_r, ROIS.cornea_r, ROIS.cornea_l,
      ROIS.cochlea_l, ROIS.cochlea_r, ROIS.hippocampus_l, ROIS.hippocampus_r,ROIS.brain_ptv,
       ROIS.pituitary,  ROIS.lacrimal_l, ROIS.lacrimal_r,ROIS.lens_l, ROIS.lens_r
    ]
    if nr_fractions < 20:
      tolerances = [
        TOL.retina_v003_adx, TOL.retina_v003_adx, TOL.cornea_v003_adx, TOL.cornea_v003_adx, 
        TOL.cochlea_mean_tinnitus, TOL.cochlea_mean_tinnitus, TOL.hippocampus_v40, TOL.hippocampus_v40,TOL.brain_ptv_33_mean,
        TOL.pituitary_mean,  TOL.lacrimal_mean, TOL.lacrimal_mean,TOL.lens_v003_adx, TOL.lens_v003_adx
      ]
    elif nr_fractions == 30:
      tolerances = [
        TOL.retina_v003_30_adx, TOL.retina_v003_30_adx, TOL.cornea_v003_30_adx, TOL.cornea_v003_30_adx, 
        TOL.cochlea_mean_tinnitus, TOL.cochlea_mean_tinnitus, TOL.hippocampus_30_v40, TOL.hippocampus_30_v40,TOL.brain_ptv_30_mean,
        TOL.pituitary_mean_30,  TOL.lacrimal_mean_30, TOL.lacrimal_mean_30,TOL.lens_v003_30_adx, TOL.lens_v003_30_adx
      ]
    elif nr_fractions == 33:
      tolerances = [
        TOL.retina_v003_33_adx, TOL.retina_v003_33_adx, TOL.cornea_v003_33_adx, TOL.cornea_v003_33_adx, 
        TOL.cochlea_mean_tinnitus, TOL.cochlea_mean_tinnitus, TOL.hippocampus_33_v40, TOL.hippocampus_33_v40,TOL.brain_ptv_33_mean,
        TOL.pituitary_mean_33,  TOL.lacrimal_mean_33, TOL.lacrimal_mean_33,TOL.lens_v003_33_adx, TOL.lens_v003_33_adx
      ]
    for i in range(len(other_oars)):
      if SSF.has_named_roi_with_contours(ss, other_oars[i].name):
        
        weight = None
        # Conflict with dose?
        if tolerances[i].equivalent(nr_fractions) < total_dose*0.95:
          # Conflict with dose:
          if not SSF.roi_overlap(pm, examination, ss, ROIS.ptv, other_oars[i], 1):
            #messagebox.showinfo("Error.",other_oars[i].name)
            if ROIF.roi_vicinity_approximate(SSF.rg(ss, ROIS.ptv.name), SSF.rg(ss, other_oars[i].name), 2):
              # OAR is close, but not overlapping:
              weight = 2
            else:
              weight = 20
          elif other_oars[i].name == ROIS.brain_gtv.name:
            weight = 2
        else:
          # No conflict with dose:
          weight = 20
        # Create objective if indicated:
        if weight:
          if other_oars[i].name in  [ROIS.cochlea_r.name, ROIS.cochlea_l.name,ROIS.brain_ptv.name]:
            OF.max_eud(ss, plan, other_oars[i].name, tolerances[i].equivalent(nr_fractions)*100-50, 1, weight)
          elif other_oars[i].name in  [ROIS.lacrimal_l.name, ROIS.lacrimal_r.name, ROIS.hippocampus_l.name, ROIS.hippocampus_r.name]:
            OF.max_eud(ss, plan, other_oars[i].name, tolerances[i].dose*100-50, 1, weight)
          elif other_oars[i].name in  [ROIS.lens_l.name, ROIS.lens_r.name]:
            OF.max_dose(ss, plan, other_oars[i].name, tolerances[i].dose*100-50, weight)
          else:
            OF.max_dose(ss, plan, other_oars[i].name, (tolerances[i].equivalent(nr_fractions)*100)-50, weight)
      else:
        GUIF.handle_missing_roi_for_objective(other_oars[i].name)

# HEAD AND NECK
def create_head_neck_objectives(ss, plan, total_dose, opt):
  if total_dose in [60, 64, 66, 68, 70]:
    high = int(total_dose)
    dose_high = str(high)
    mid = 60
    dose_mid = str(mid)
    low = 54
    if SSF.has_roi_with_shape(ss, ROIS.x_ctv_54.name):
      low = 54
    elif SSF.has_roi_with_shape(ss, ROIS.x_ctv_50.name):
      low = 50
    dose_low = str(low)

    if total_dose in [60, 64]:
      if SSF.has_roi_with_shape(ss, ROIS.ctv_sb_64.name):
        OF.uniform_dose(ss, plan, ROIS.ctv_sb_64.name, total_dose * 100, 10)
      if total_dose == 60:
        OF.uniform_dose(ss, plan, ROIS.ctv_sb_60.name, mid * 100, 10)
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_.name + '_' + dose_low):
        OF.uniform_dose(ss, plan, ROIS.x_ctv_.name + '_' + dose_low, low * 100, 10)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_sb_64.name):
        OF.min_dose(ss, plan, ROIS.ptv_sb_64.name, total_dose * 0.95 * 100, 300)
        OF.max_dose(ss, plan, ROIS.ptv_sb_64.name, total_dose * 1.05 * 100, 10000)
        if SSF.has_roi_with_shape(ss, ROIS.x_ctv_60.name):  
          OF.uniform_dose(ss, plan, ROIS.x_ctv_60.name, 60 * 100, 10)
      OF.min_dose(ss, plan, ROIS.ptv_sb_60.name, mid * 0.95 * 100, 300)
      if total_dose == 60:
        OF.min_dose(ss, plan, ROIS.ptv_sb_60.name, total_dose * 0.95 * 100, 300)
        OF.max_dose(ss, plan, ROIS.ptv_sb_60.name, mid * 1.05 * 100, 10000)
      if total_dose == 64:
        OF.fall_off(ss, plan, ROIS.ptv_sb_60.name, total_dose * 100, mid * 105, 0.4, 10)
    elif total_dose > 65:
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name + '_' + dose_high, total_dose * 100, 10)
      ctv_n_high = [ROIS.ctv_n.name + '_' + dose_high, ROIS.ctv_n1.name + '_' + dose_high,
                    ROIS.ctv_n2.name + '_' + dose_high, ROIS.ctv_n3.name + '_' + dose_high,
                    ROIS.ctv_n4.name + '_' + dose_high]
      for c in ctv_n_high:
        if SSF.has_roi_with_shape(ss, c):
          OF.uniform_dose(ss, plan, c, total_dose * 100, 10)
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_60.name): 
        OF.uniform_dose(ss, plan, ROIS.x_ctv_60.name, 60 * 100, 10)
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_.name + '_' + dose_low):
        OF.uniform_dose(ss, plan, ROIS.x_ctv_.name + '_' + dose_low, low * 100, 10)
      OF.min_dose(ss, plan, ROIS.ptv_p.name + '_' + dose_high, high * 0.95 * 100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_p.name + '_' + dose_high, high * 1.05 * 100, 10000)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name + '_' + dose_high):
        OF.min_dose(ss, plan, ROIS.ptv_n.name + '_' + dose_high, high * 0.95 * 100, 300)
        OF.max_dose(ss, plan, ROIS.ptv_n.name + '_' + dose_high, high * 1.05 * 100, 10000)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_p.name + '_' + dose_mid):
        OF.min_dose(ss, plan, ROIS.ptv_p.name + '_' + dose_mid, mid * 0.95 * 100, 300)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name + '_' + dose_high):
        OF.min_dose(ss, plan, ROIS.ptv_n.name + '_' + dose_mid, mid * 0.95 * 100, 300)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_p.name + '_' + dose_mid):
        OF.fall_off(ss, plan, ROIS.ptv_p.name + '_' + dose_mid, total_dose * 100, mid * 100, 0.5, 100)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name + '_' + dose_high):
        OF.fall_off(ss, plan, ROIS.ptv_n.name + '_' + dose_mid, total_dose * 100, mid * 100, 0.5, 100)
      # Common for all head and neck except glottis
      # PTVe_50/54
    if not SSF.has_roi_with_shape(ss, ROIS.a_carotid_r.name) and total_dose > 40:
      OF.min_dose(ss, plan, ROIS.ptv_e.name + '_' + dose_low, low * 0.95 * 100, 500)
      OF.max_dose(ss, plan, ROIS.x_ptv_.name + '_' + dose_low, low * 1.04 * 100, 5000)  

    # OARs
    OF.max_dose(ss, plan, ROIS.body.name, total_dose * 1.05 * 100, 100)
    if not SSF.has_roi_with_shape(ss, ROIS.ctv_e_l.name + '_' + dose_low) or not SSF.has_roi_with_shape(ss,ROIS.ctv_e_l.name + '_' + dose_low):
      OF.fall_off(ss, plan, ROIS.body.name, total_dose * 100, 25 * 100, 3, 10)  # for å heller spare meir på motsatt side (xSparevolum ved enkeltsidig bestråling)
    else:
      OF.fall_off(ss, plan, ROIS.body.name, total_dose * 100, 25 * 100, 3, 50)

    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 44.5 * 100, 10000)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 38 * 100, 500)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 49.5 * 100, 10000)
    OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 45 * 100, 500)
    OF.max_eud(ss, plan, ROIS.body.name, 15 * 100, 1, 5)
    if SSF.has_roi_with_shape(ss, ROIS.brain.name):
      OF.max_eud(ss, plan, ROIS.brain.name, 3 * 100, 1, 5)
      OF.fall_off(ss, plan, ROIS.brain.name, total_dose * 100, 10 * 100, 1, 300)
    if SSF.has_roi_with_shape(ss, ROIS.brainstem.name):
      OF.max_dose(ss, plan, ROIS.brainstem.name, 53.5 * 100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.eye_l.name):
      OF.max_eud(ss, plan, ROIS.eye_l.name, 10 * 100, 1, 1)
    if SSF.has_roi_with_shape(ss, ROIS.eye_r.name):
      OF.max_eud(ss, plan, ROIS.eye_r.name, 10 * 100, 1, 1)
    if SSF.has_roi_with_shape(ss, ROIS.optic_nrv_r.name):
      OF.max_dose(ss, plan, ROIS.optic_nrv_r.name, 52 * 100, 1000)
    if SSF.has_roi_with_shape(ss, ROIS.optic_nrv_l.name):
      OF.max_dose(ss, plan, ROIS.optic_nrv_l.name, 52 * 100, 1000)
    if SSF.has_roi_with_shape(ss, ROIS.optic_chiasm.name):
      OF.max_dose(ss, plan, ROIS.optic_chiasm.name, 52 * 100, 1000)
    if SSF.has_roi_with_shape(ss, ROIS.lens_r.name):
      OF.max_dose(ss, plan, ROIS.lens_r.name, 10 * 100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.lens_l.name):
      OF.max_dose(ss, plan, ROIS.lens_l.name, 10 * 100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.lacrimal_l.name):
      OF.max_eud(ss, plan, ROIS.lacrimal_l.name, 20 * 100, 1, 100)
    if SSF.has_roi_with_shape(ss, ROIS.lacrimal_r.name):
      OF.max_eud(ss, plan, ROIS.lacrimal_r.name, 20 * 100, 1, 100)
    if not SSF.has_roi_with_shape(ss, ROIS.a_carotid_r.name):  # all head and neck except glottis
      OF.max_eud(ss, plan, ROIS.x_oral_cavity.name, 25 * 100, 1, 8)
      OF.fall_off(ss, plan, ROIS.oral_cavity.name, total_dose * 100, 30 * 100, 1, 100)
      OF.max_eud(ss, plan, ROIS.x_parotid_l.name, 15 * 100, 1, 7) 
      OF.fall_off(ss, plan, ROIS.parotid_l.name, total_dose * 100, 30 * 100, 1, 30)  
      OF.max_eud(ss, plan, ROIS.x_parotid_r.name, 15 * 100, 1, 7)  
      OF.fall_off(ss, plan, ROIS.parotid_r.name, total_dose * 100, 30 * 100, 1, 30) 
      OF.max_eud(ss, plan, ROIS.x_skulder_h.name, 5 * 100, 1, 1)
      OF.max_eud(ss, plan, ROIS.x_skulder_v.name, 5 * 100, 1, 1)
      if not SSF.has_roi_with_shape(ss, ROIS.ctv_e_l.name + '_' + dose_low) or not SSF.has_roi_with_shape(ss, ROIS.ctv_e_r.name + '_' + dose_low):
        if SSF.has_roi_with_shape(ss, ROIS.x_sparevolum.name):  
          OF.max_eud(ss, plan, ROIS.x_sparevolum.name, 15 * 100, 1, 10)
          OF.fall_off(ss, plan, ROIS.x_sparevolum.name, total_dose * 100, 20 * 100, 2, 50)
      if SSF.has_roi_with_shape(ss, ROIS.mandible.name):
        OF.fall_off(ss, plan, ROIS.mandible.name, total_dose * 100, 40 * 100, 1, 30)
      if SSF.has_roi_with_shape(ss, ROIS.x_submand_r.name):
        OF.max_eud(ss, plan, ROIS.x_submand_r.name, 30 * 100, 1, 4)
      if SSF.has_roi_with_shape(ss, ROIS.x_submand_l.name): 
        OF.max_eud(ss, plan, ROIS.x_submand_l.name, 30 * 100, 1, 4)
      if SSF.has_roi_with_shape(ss, ROIS.pharynx_constr_s.name):
        OF.max_eud(ss, plan, ROIS.pharynx_constr_s.name, 50 * 100, 1, 2)
      if SSF.has_roi_with_shape(ss, ROIS.pharynx_constr_m.name):
        OF.max_eud(ss, plan, ROIS.pharynx_constr_m.name, 50 * 100, 1, 2)
      if SSF.has_roi_with_shape(ss, ROIS.pharynx_constr_i.name):
        OF.max_eud(ss, plan, ROIS.pharynx_constr_i.name, 50 * 100, 1, 2)
      if SSF.has_roi_with_shape(ss, ROIS.lung_r.name):
        OF.max_eud(ss, plan, ROIS.lung_r.name, 2 * 100, 1, 1)
      if SSF.has_roi_with_shape(ss, ROIS.lung_l.name):
        OF.max_eud(ss, plan, ROIS.lung_l.name, 2 * 100, 1, 1)
      if SSF.has_roi_with_shape(ss, ROIS.lips.name):  
        OF.max_eud(ss, plan, ROIS.lips.name, 15 * 100, 1, 2)
      if SSF.has_roi_with_shape(ss, ROIS.x_spare_caud.name):  
        OF.max_eud(ss, plan, ROIS.x_spare_caud.name, 12 * 100, 1, 3)
      if SSF.has_roi_with_shape(ss, ROIS.x_spare_mid.name):  
        OF.max_eud(ss, plan, ROIS.x_spare_mid.name, 35 * 100, 1, 3)
      if SSF.has_roi_with_shape(ss, ROIS.x_spare_cran.name):  
        OF.max_eud(ss, plan, ROIS.x_spare_cran.name, 35 * 100, 1, 3)
    if SSF.has_roi_with_shape(ss, ROIS.a_carotid_r.name):  # Glottis
      OF.max_dose(ss, plan, ROIS.a_carotid_l.name, 38 * 100, 1000)
      OF.max_dose(ss, plan, ROIS.a_carotid_r.name, 38 * 100, 1000)

  else: # Palliative Head and Neck
    OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose * 100, 30)
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose * 0.95 * 100, 150)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose * 1.05 * 100, 80)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose * 100, total_dose * 100 / 2, 1.5, 30)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose * 1.05 * 100, 100)


# ESOPHAGUS
def create_esophagus_objectives(ss, plan, total_dose):
  
  if SSF.has_roi_with_shape(ss, ROIS.ctv_p_66.name) or SSF.has_roi_with_shape(ss, ROIS.ictv_p_66.name):
    OF.uniform_dose(ss, plan, ROIS.ctv_p_66.name, total_dose*100, 30)
    ctv_n_66 = [ROIS.ctv_n_66.name, ROIS.ctv_n1_66.name,ROIS.ctv_n2_66.name,ROIS.ctv_n3_66.name,ROIS.ictv_n_66.name, ROIS.ictv_n1_66.name,ROIS.ictv_n2_66.name,ROIS.ictv_n3_66.name]
    for c in ctv_n_66: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, total_dose*100, 30)
  if SSF.has_roi_with_shape(ss, ROIS.ctv_p_60.name) or SSF.has_roi_with_shape(ss, ROIS.ictv_p_60.name):
    OF.uniform_dose(ss, plan, ROIS.ctv_p_60.name, total_dose*100, 30)
    ctv_n_60 = [ROIS.ctv_n_60.name, ROIS.ctv_n1_60.name,ROIS.ctv_n2_60.name,ROIS.ctv_n3_60.name,ROIS.ictv_n_60.name, ROIS.ictv_n1_60.name,ROIS.ictv_n2_60.name,ROIS.ictv_n3_60.name]
    for c in ctv_n_60: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, total_dose*100, 30)
  if total_dose == 46:
    OF.uniform_dose(ss, plan, ROIS.ctv_e_46.name, total_dose*100, 30)
  elif total_dose == 50:
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p_50.name):
      OF.uniform_dose(ss, plan, ROIS.ctv_p_50.name, total_dose*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p_50.name):
      OF.uniform_dose(ss, plan, ROIS.ictv_p_50.name, total_dose*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p.name):
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p.name):
      OF.uniform_dose(ss, plan, ROIS.ictv_p.name, total_dose*100, 30)
    ctv_n_50 = [ROIS.ctv_n_50.name, ROIS.ctv_n1_50.name,ROIS.ctv_n2_50.name,ROIS.ctv_n3_50.name,ROIS.ictv_n_50.name, ROIS.ictv_n1_50.name,ROIS.ictv_n2_50.name,ROIS.ictv_n3_50.name,
                ROIS.ctv_n.name, ROIS.ctv_n1.name,ROIS.ctv_n2.name,ROIS.ctv_n3.name,ROIS.ictv_n.name, ROIS.ictv_n1.name,ROIS.ictv_n2.name,ROIS.ictv_n3.name]
    for c in ctv_n_50: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, total_dose*100, 30)
  elif total_dose > 40:
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p.name):
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p.name):
      OF.uniform_dose(ss, plan, ROIS.ictv_p.name, total_dose*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ictv_n.name):
      OF.uniform_dose(ss, plan, ROIS.ictv_n.name, total_dose*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ctv_n.name):
      OF.uniform_dose(ss, plan, ROIS.ctv_n.name, total_dose*100, 30)
  if SSF.has_roi_with_shape(ss, ROIS.ctv.name) and total_dose < 40:
    OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 30)
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e_46_5.name):
    OF.uniform_dose(ss, plan, ROIS.x_ctv_46_5.name, 46.5*100, 30)
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e.name):
    OF.uniform_dose(ss, plan, ROIS.ctv_e.name, total_dose*100, 30)
  #if total_dose == 66:
  #  OF.min_dose(ss, plan, ROIS.ptv_66.name, total_dose*100*0.95, 150)
  #  OF.max_dose(ss, plan, ROIS.ptv_66.name, total_dose*100*1.05, 80)
  #elif total_dose == 60:
  #  OF.min_dose(ss, plan, ROIS.ptv_60.name, total_dose*100*0.95, 150)
  #  OF.max_dose(ss, plan, ROIS.ptv_60.name, total_dose*100*1.05, 80)
  #elif total_dose == 50:
  #  OF.min_dose(ss, plan, ROIS.ptv_p_50.name, total_dose*100*0.95, 150)
  #  OF.max_dose(ss, plan, ROIS.ptv_p_50.name, total_dose*100*1.05, 80)
  #  OF.min_dose(ss, plan, ROIS.ptv_n_50.name, total_dose*100*0.95, 150)
  #  OF.max_dose(ss, plan, ROIS.ptv_n_50.name, total_dose*100*1.05, 80)

  if SSF.has_roi_with_shape(ss, ROIS.ptv_66.name):
    ptv_target = ROIS.ptv_66.name
  elif SSF.has_roi_with_shape(ss, ROIS.ptv_60.name):
    ptv_target = ROIS.ptv_60.name
  elif SSF.has_roi_with_shape(ss, ROIS.ptv_50.name):
    ptv_target = ROIS.ptv_50.name
  else:
    ptv_target = ROIS.ptv.name
  
  OF.min_dose(ss, plan, ptv_target, total_dose*100*0.95, 300)
  OF.max_dose(ss, plan, ptv_target, total_dose*100*1.05, 100)

  if total_dose < 21:
    OF.fall_off(ss, plan, ROIS.x_ptv_46.name, total_dose*100, total_dose*100/2, 3, 20)
  if SSF.has_roi_with_shape(ss, ROIS.ptv_e_46_5.name):
    OF.min_dose(ss, plan, ROIS.ptv_e_46_5.name, 46.5*100*0.95, 300)
    OF.max_dose(ss, plan, ROIS.x_ptv_46_5.name, 46.5*100*1.05, 100)
  if SSF.has_roi_with_shape(ss, ROIS.ptv_e_46.name) and total_dose == 46:
    OF.min_dose(ss, plan, ROIS.ptv_e_46.name, 46*100*0.95, 300)
    OF.max_dose(ss, plan, ROIS.ptv_e_46.name, 46*100*1.05, 100)
  OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 3, 30)
  OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 30)
  if total_dose > 40:
    OF.max_eud(ss, plan, ROIS.heart.name, 15*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.kidneys.name, 5*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.lungs.name, 10*100, 1, 10)
    OF.max_dose(ss, plan, ROIS.spinal_canal.name, 44*100, 80)
    if SSF.has_roi_with_shape(ss, ROIS.bowel_bag.name):
      OF.max_eud(ss, plan, ROIS.bowel_bag.name, 10*100, 1, 10)
    if SSF.has_roi_with_shape(ss, ROIS.liver.name):
      OF.max_eud(ss, plan, ROIS.liver.name, 10*100, 1, 10)
  else:
    OF.max_eud(ss, plan, ROIS.heart.name, 5*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.kidneys.name, 1*100, 1, 10)
    OF.max_eud(ss, plan, ROIS.lungs.name, 5*100, 1, 10)
    OF.max_dose(ss, plan, ROIS.spinal_canal.name, 5*100, 80)
    if SSF.has_roi_with_shape(ss, ROIS.bowel_bag.name):
      OF.max_eud(ss, plan, ROIS.bowel_bag.name, 5*100, 1, 10)
    if SSF.has_roi_with_shape(ss, ROIS.liver.name):
      OF.max_eud(ss, plan, ROIS.liver.name, 5*100, 1, 10)
    
# LUNG
def create_lung_objectives(ss, plan, region_code, target, total_dose, nr_fractions):
  if total_dose > 40: # Curative fractionation
    ictv_n = [ROIS.ictv_n1.name, ROIS.ictv_n2.name,ROIS.ictv_n3.name,ROIS.ictv_n4.name,ROIS.ictv_n5.name,ROIS.ictv_n6.name, ROIS.ictv_p]
    if SSF.has_roi_with_shape(ss, ROIS.ictv_n1.name):
      for c in ictv_n:
        if SSF.has_roi_with_shape(ss, c):
          OF.uniform_dose(ss, plan, c, total_dose*100, 20)
    else:
      if SSF.has_roi_with_shape(ss, ROIS.ictv_n.name):
        OF.uniform_dose(ss, plan, ROIS.ictv_n.name, total_dose*100, 20)
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p.name):
      OF.uniform_dose(ss, plan, ROIS.ictv_p.name, total_dose*100, 20)
    elif SSF.has_roi_with_shape(ss, ROIS.ictv.name):
      OF.uniform_dose(ss, plan, ROIS.ictv.name, total_dose*100, 20)
    elif SSF.has_roi_with_shape(ss, ROIS.ctv.name):
      OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 20) 
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.02, 100)
    OF.min_dose(ss, plan, ROIS.x_ptv_vev.name, total_dose*0.95*100, 100)
    OF.min_dose(ss, plan, ROIS.x_ptv_lunge.name, total_dose*0.95*100, 100)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 2, 10)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.02, 1000)
    match = False
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
      l = ROIS.lungs_gtv.name
    elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
      l = ROIS.lungs_igtv.name
    OF.max_eud(ss, plan, l, 18*100, 1, 1) 
    OF.max_dvh(ss, plan, l, 5*100, 50, 1) 
    OF.max_dvh(ss, plan, l, 20*100, 30, 1)
    if region_code in RC.lung_r_codes:
      OF.max_dvh(ss, plan, ROIS.lung_l.name, 5*100, 10, 1)
    elif region_code in RC.lung_l_codes:
      OF.max_dvh(ss, plan, ROIS.lung_r.name, 5*100, 10, 1)
    OF.max_eud(ss, plan, ROIS.heart.name, 20*100, 1, 1)
    OF.fall_off(ss, plan, ROIS.heart.name, total_dose*100, total_dose*100/2, 1, 1)
    OF.max_dose(ss, plan, ROIS.esophagus.name, total_dose*100, 1)
    OF.fall_off(ss, plan, ROIS.esophagus.name, total_dose*100, total_dose*100/2, 1, 1)
    OF.max_dose(ss, plan, ROIS.x_trachea_bronchus.name, total_dose*100, 1)
    if SSF.has_roi_with_shape(ss, ROIS.x_a_aorta.name):
      OF.max_dose(ss, plan, ROIS.x_a_aorta.name, total_dose*100, 1)
    elif SSF.has_roi_with_shape(ss, ROIS.a_aorta.name):
      OF.max_dose(ss, plan, ROIS.a_aorta.name, total_dose*100, 1)
    if nr_fractions == 40:
      dose = (TOL.spinalcanal_40_v0_03_adx_chemo.equivalent(nr_fractions)*100)-50
    elif nr_fractions == 35:
      dose = (TOL.spinalcanal_35_v0_03_adx_chemo.equivalent(nr_fractions)*100)-50
    elif nr_fractions == 33:
      dose = (TOL.spinalcanal_33_v0_03_adx_chemo.equivalent(nr_fractions)*100)-50
    elif nr_fractions == 30:
      dose = (TOL.spinalcanal_30_v0_03_adx_chemo.equivalent(nr_fractions)*100)-50
    elif nr_fractions == 17:
      dose = (TOL.spinalcanal_17_v0_03_adx_chemo.equivalent(nr_fractions)*100)-50
    elif nr_fractions == 15:
      dose = (TOL.spinalcanal_15_v0_03_adx_chemo.equivalent(nr_fractions)*100)-50
    else:
      dose = (TOL.spinalcanal_v0_03_adx_chemo.equivalent(nr_fractions)*100)-50
    OF.max_dose(ss, plan, ROIS.x_spinal_canal.name, dose, 20)   

  elif total_dose < 40: # Palliative fractionation
    OF.uniform_dose(ss, plan, target, total_dose*100, 30)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 80)
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 30)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 2, 30)
    #OF.max_eud(ss, plan, ROIS.heart.name, 0.29*total_dose*100, 1, 10)
    #OF.max_eud(ss, plan, ROIS.spinal_canal.name, 0.9*total_dose*100, 1, 5)
    #if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
    #  l = ROIS.lungs_gtv.name
    #elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
    #  l = ROIS.lungs_igtv.name
    #OF.max_eud(ss, plan, l, 0.23*total_dose*100, 1, 15)

  
# LUNG Stereotactic 
def create_lung_stereotactic_objectives(ss, plan, region_code, total_dose,target):
  if target == ROIS.ptv.name:
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 250)
    OF.fall_off(ss, plan, ROIS.x_ptv_ring_1.name, total_dose*100, total_dose/2.7*100, 1, 5)
  elif len(target)>0:
    for i in range(len(target)):
      OF.min_dose(ss, plan,  target[i], total_dose*100, 250)
      OF.max_dose(ss, plan, target[i], total_dose*138, 100)
      OF.fall_off(ss, plan, "x"+target[i]+"_Ring0-1cm", total_dose*100, total_dose/2.7*100, 1, 5)
  OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 3*100, 2.5, 5)
  
  if region_code in RC.lung_r_codes:
    OF.max_eud(ss, plan, ROIS.lung_l.name, 3*100, 1, 3)
  else:
    OF.max_eud(ss, plan, ROIS.lung_r.name, 3*100, 1, 3)

# LIVER Stereotactic 
def create_liver_stereotactic_objectives(ss, plan, total_dose, target):
  if target == ROIS.ptv.name:
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 250)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*138, 100)
    OF.fall_off(ss, plan, ROIS.x_ptv_ring_1.name, total_dose*100, total_dose/2.7*100, 0.5, 5)
  elif len(target)>0:
    for i in range(len(target)):
      OF.min_dose(ss, plan, target[i], total_dose*100, 250)
      OF.max_dose(ss, plan, target[i], total_dose*138, 100)
      OF.fall_off(ss, plan, "x"+target[i]+"_Ring0-1cm", total_dose*100, total_dose/2.7*100, 0.5, 5)
  OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 3*100, 3, 5)


# BREAST
def create_breast_objectives(ss, plan, region_code, total_dose, technique_name, opt):
  if region_code in RC.breast_l_codes: # Left
    contralateral_lung = ROIS.lung_r.name
    ipsilateral_lung = ROIS.lung_l.name
    contralateral_breast = ROIS.breast_r.name
    ipsilateral_humeral = ROIS.humeral_l.name
  else: # Right
    contralateral_lung = ROIS.lung_l.name
    ipsilateral_lung = ROIS.lung_r.name
    contralateral_breast = ROIS.breast_l.name
    ipsilateral_humeral = ROIS.humeral_r.name
  index = 0
  if technique_name == '3D-CRT': # For hybrid boost (because of two beam sets)
    index = 1
  if region_code in RC.breast_partial_codes: # Breast boost 2 Gy x 8
    ctv = [ROIS.ctv_boost.name, ROIS.ctv_boost_r.name, ROIS.ctv_boost_l.name]
    ptv = [ROIS.ptv_boost.name, ROIS.ptv_boost_r.name, ROIS.ptv_boost_l.name]
    for i in range(len(ctv)):
      if SSF.has_roi_with_shape(ss, ctv[i]):
        OF.uniform_dose(ss, plan, ctv[i], total_dose*100, 10, beam_set_index = index)
    for i in range(len(ptv)):
      if SSF.has_roi_with_shape(ss, ptv[i]):
        OF.min_dose(ss, plan, ptv[i], 0.95*total_dose*100, 1000, beam_set_index = index)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose/2*100, 1, 1, beam_set_index = index)
    OF.max_dose(ss, plan, ROIS.body.name, 1.035*total_dose*100, 30000, beam_set_index = index)
    if SSF.has_roi_with_shape(ss, contralateral_breast):
      OF.max_eud(ss, plan, contralateral_breast, 0.1*100, 1, 1, beam_set_index = index)
    OF.max_dvh(ss, plan, ipsilateral_lung, 0.5*100, 35, 1, beam_set_index = index)
    OF.max_eud(ss, plan, ipsilateral_lung, 1*100, 1, 1, beam_set_index = index)
    OF.max_eud(ss, plan, contralateral_lung, 0.1*100, 1, 1, beam_set_index = index)
    OF.max_eud(ss, plan, ROIS.heart.name, 0.1*100, 1, 1, beam_set_index = index)
    for i in range(len(ptv)):
      if SSF.has_roi_with_shape(ss, ptv[i]):
        OF.min_dose_robust(ss, plan, ptv[i], 0.95*total_dose*100, 1000)
        OF.max_dose_robust(ss, plan, ptv[i], 1.05*total_dose*100, 3000)
  if technique_name == '3D-CRT': # Hybrid VMAT
    if region_code in RC.breast_tang_codes: # Hybrid VMAT Breast tangential
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 100, beam_set_index = 1)
      OF.min_dose(ss, plan, ROIS.ptv_pc.name, 38.5*100, 3000, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 20*100, 1, 1, beam_set_index = 1)
      OF.max_dose(ss, plan, ROIS.body.name,41.5*100, 30000, beam_set_index = 1)
      OF.max_eud(ss, plan, contralateral_breast, 0.5*100, 1, 1, beam_set_index = 1)
      OF.max_eud(ss, plan, ipsilateral_lung, 4*100, 1, 1, beam_set_index = 1)
      OF.max_eud(ss, plan, contralateral_lung, 0.5*100, 1, 1, beam_set_index = 1)
      if region_code in RC.breast_tang_l_codes: # Hybrid VMAT Breast tangential left
        OF.max_eud(ss, plan, ROIS.heart.name, 1.6*100, 1, 1, beam_set_index = 1)
      elif region_code in RC.breast_tang_r_codes: # Hybrid VMAT Breast tangential right
        OF.max_eud(ss, plan, ROIS.heart.name, 1*100, 1, 1, beam_set_index = 1)
    elif region_code in RC.breast_reg_codes: # Hybrid VMAT Breast regional
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 30, beam_set_index = 1)
      OF.uniform_dose(ss, plan, ROIS.ctv_n.name, total_dose*100, 30, beam_set_index = 1)
      OF.min_dose(ss, plan, ROIS.x_ptv_cran.name, 38.4*100, 1000, beam_set_index = 1)
      OF.min_dose(ss, plan, ROIS.ptv_pc.name, 38.4*100, 1000, beam_set_index = 1)
      OF.min_dose(ss, plan, ROIS.ptv_nc.name, 38.4*100, 1000, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.x_ptv_cran.name, total_dose*100, 38.05*100, 1, 10, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.external.name, total_dose*100, 30*100, 2, 1, beam_set_index = 1)
      OF.max_dose(ss, plan, ROIS.external.name, 42*100, 50000, beam_set_index = 1)
      OF.max_eud(ss, plan, ROIS.heart.name, 1.8*100, 1, 5, beam_set_index = 1)
      OF.max_dvh(ss, plan, ipsilateral_lung, 18*100, 20, 5, beam_set_index = 1)
      OF.max_dvh(ss, plan, ipsilateral_lung, 5*100, 45, 5, beam_set_index = 1)
      OF.max_eud(ss, plan, ipsilateral_lung, 10*100, 1, 1, beam_set_index = 1)
      OF.max_eud(ss, plan, contralateral_lung, 0.5*100, 1, 1, beam_set_index = 1)
      OF.max_dvh(ss, plan, contralateral_lung, 5*100, 1, 5, beam_set_index = 1)
      OF.max_eud(ss, plan, contralateral_breast, 0.8*100, 1, 1, beam_set_index = 1)
      OF.max_eud(ss, plan, ipsilateral_humeral , 15*100, 1, 10, beam_set_index = 1)
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_n_ring.name):
        OF.fall_off(ss, plan, ROIS.x_ctv_n_ring.name, total_dose*100, 30*100, 2, 20, beam_set_index = 1)
      elif SSF.has_roi_with_shape(ss, "xCTVn_L2-L4_Ring"):
        OF.fall_off(ss, plan, "xCTVn_L2-L4_Ring", total_dose*100, 30*100, 2, 20, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.esophagus.name, 40*100, 10*100, 1, 10, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.thyroid.name, 40*100, 10*100, 1, 10, beam_set_index = 1)
      OF.fall_off(ss, plan, ROIS.trachea.name, 40*100, 10*100, 1, 10, beam_set_index = 1)
  elif technique_name == 'VMAT' and region_code not in RC.breast_partial_codes: # VMAT except boost
    # VMAT automatic optimization
    # Common for all VMAT breast automatic (except boost)
    ctv = [ROIS.ctv_p.name, ROIS.ctv_n.name, ROIS.ctv_p_l.name, ROIS.ctv_p_r.name, ROIS.ctv_n_l.name, ROIS.ctv_n_r.name, ROIS.ctv_n_imn.name,  ROIS.ctv_n_imn_r.name,  ROIS.ctv_n_imn_l.name ]
    ptv = [ROIS.ptv_pc.name, ROIS.ptv_nc.name, ROIS.ptv_pc_l.name, ROIS.ptv_pc_r.name, ROIS.ptv_nc_l.name, ROIS.ptv_nc_r.name,ROIS.ptv_n_imn.name,ROIS.ptv_n_imn_r.name,ROIS.ptv_n_imn_l.name]
    for i in range(len(ctv)):
      if SSF.has_roi_with_shape(ss, ctv[i]):
        OF.uniform_dose(ss, plan, ctv[i], total_dose*100, 10)
    for i in range(len(ctv)):
      if SSF.has_roi_with_shape(ss, ctv[i]):
        OF.min_dose(ss, plan, ctv[i], 38.5*100, 300)
    for i in range(len(ptv)):
      if SSF.has_roi_with_shape(ss, ptv[i]):
        OF.min_dose(ss, plan, ptv[i], 38.2*100, 300)
    OF.max_dose(ss, plan, ROIS.body.name, 42.5*100, 50000)
    OF.fall_off(ss, plan, ROIS.body.name, 40*100, 20*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.heart.name, 1*100, 1, 10)
    if region_code in RC.breast_l_codes:
      OF.max_eud(ss, plan, ROIS.a_lad.name, 7*100, 1, 10)
      if SSF.has_roi_with_shape(ss, ROIS.ctv_p_r.name):
        OF.max_eud(ss, plan, ROIS.liver.name, 5*100, 1, 2)
    elif region_code in RC.breast_r_codes:
      OF.max_eud(ss, plan, ROIS.liver.name, 5*100, 1, 2)
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p_r.name) and SSF.has_roi_with_shape(ss, ROIS.ctv_p_l.name): # VMAT Breast bilateral automatic
      OF.max_eud(ss, plan, ROIS.lung_l.name, 5*100, 1, 20)
      OF.max_eud(ss, plan, ROIS.lung_r.name, 5*100, 1, 20)
      OF.max_dvh(ss, plan, ROIS.lung_l.name, 2*100, 45, 10)
      OF.max_dvh(ss, plan, ROIS.lung_r.name, 2*100, 45, 10)
      if region_code in RC.breast_tang_codes: # VMAT tangential breast bilateral automatic
        OF.fall_off(ss, plan, ROIS.sternum_box.name, 38*100, 30*100, 1, 100)
      if region_code in RC.breast_reg_codes: # VMAT regional breast bilateral automatic
        if SSF.has_roi_with_shape(ss, ROIS.ctv_n_l.name):
          OF.max_dose(ss, plan, ROIS.humeral_l.name, 30*100, 2)
          OF.max_eud(ss, plan, ROIS.humeral_l.name, 4*100, 1, 2)
        if SSF.has_roi_with_shape(ss, ROIS.ctv_n_r.name):
          OF.max_dose(ss, plan, ROIS.humeral_r.name, 30*100, 2)
          OF.max_eud(ss, plan, ROIS.humeral_r.name, 4*100, 1, 2)  
    else: # VMAT Breast one sided automatic
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n_imn.name): # VMAT breast with IMN automatic
        OF.max_eud(ss, plan, ipsilateral_lung, 6*100, 1, 20)
      else: #VMAT breast reginal without IMN automatic
        OF.max_eud(ss, plan, ipsilateral_lung, 5*100, 1, 20)
      OF.max_dvh(ss, plan, ipsilateral_lung, 2*100, 35, 10)
      OF.max_eud(ss, plan, contralateral_lung, 1*100, 1, 10)
      OF.max_eud(ss, plan, contralateral_breast, 1*100, 1, 10)
      if region_code in RC.breast_reg_codes: # VMAT Breast regional not bilateral automatic
        OF.max_eud(ss, plan, ipsilateral_humeral, 4*100, 1, 2)
        OF.max_dose(ss, plan, ipsilateral_humeral, 30*100, 2)
    if region_code in RC.breast_reg_codes: # VMAT Breast regional automatic
      OF.max_eud(ss, plan, ROIS.esophagus.name, 2*100, 1, 2)
      OF.max_eud(ss, plan, ROIS.trachea.name, 3*100, 1, 2)
      OF.max_eud(ss, plan, ROIS.thyroid.name, 4*100, 1, 2)
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_n_ring.name):
        OF.fall_off(ss, plan, ROIS.x_ctv_n_ring.name, 42*100, 20*100, 1.5, 100)
      elif SSF.has_roi_with_shape(ss, "xCTVn_L2-L4_Ring"):
        OF.fall_off(ss, plan, "xCTVn_L2-L4_Ring", 42*100, 20*100, 1.5, 100)
      OF.fall_off(ss, plan, ROIS.sternum_box.name, 38*100, 25*100, 1, 100)
    ptv = [ROIS.ptv_pc.name, ROIS.ptv_nc.name, ROIS.ptv_pc_l.name, ROIS.ptv_pc_r.name, ROIS.ptv_nc_l.name, ROIS.ptv_nc_r.name]
    for i in range(len(ptv)):
      if SSF.has_roi_with_shape(ss, ptv[i]):
        OF.min_dose_robust(ss, plan, ptv[i], 37.5*100, 1000)
        OF.max_dose_robust(ss, plan, ptv[i], 42*100, 5000)

      
def create_prostate_objectives(ss, plan, total_dose, opt):
  if total_dose == 60:
    if opt == 'auto':
      OF.uniform_dose(ss, plan, ROIS.ctv_p1_60.name, total_dose*100, 10)
      OF.min_dose(ss, plan, ROIS.ptv_p1_60.name, 57*100, 1000)
      OF.max_dose(ss, plan, ROIS.ptv_p1_60.name, 62.5*100, 3000)
      OF.min_dose(ss, plan, ROIS.ctv_p1_60.name, 60 * 0.97 *100, 300)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_p2_57.name):
        OF.min_dose(ss, plan, ROIS.ptv_p2_57.name, 57*0.95*100, 1000)
        OF.max_dose(ss, plan, ROIS.x_ptv_57.name, 57*1.05*100, 1000)
        OF.uniform_dose(ss, plan, ROIS.x_ptv_57.name, 57 * 100, 10)
      if SSF.has_roi_with_shape(ss, ROIS.ctv_p2_57.name):
        OF.min_dose(ss, plan, ROIS.ctv_p2_57.name, 57 * 0.97 *100, 300)
      OF.max_eud(ss, plan, ROIS.body.name, 6*100, 1, 2)
      OF.max_dose(ss, plan, ROIS.body.name, 63*100, 10000)
      OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 45*100, 0.5, 500)
      OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 20*100, 3, 1000)
      OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 35*100, 0.5, 500)
      OF.max_eud(ss, plan, ROIS.x_rectum.name, 25 * 100, 1, 20)
      OF.max_dose(ss, plan, ROIS.rectum.name, 60*100*0.965, 5000)
      OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 35*100, 0.5, 500)
      OF.max_dose(ss, plan, ROIS.anal_canal.name, 60*100*0.965, 10000)
      OF.max_eud(ss, plan, ROIS.x_anal_canal.name,5 * 100, 1, 7)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 40*100, 0.5, 500)
      OF.max_dose(ss, plan, ROIS.bladder.name, 60*100*0.98, 1000)
      OF.max_eud(ss, plan, ROIS.x_bladder.name, 20 * 100, 1, 12)
      OF.max_eud(ss, plan, ROIS.penile_bulb.name, 15*100, 1, 2)
      #OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 10*100, 1,3)
      OF.max_dose(ss, plan, ROIS.femoral_l.name, 35*100, 100)
      OF.max_dose(ss, plan, ROIS.femoral_r.name, 35*100, 100)
    else:
      OF.uniform_dose(ss, plan, ROIS.ctv_p1_60.name, total_dose*100, 10)
      OF.uniform_dose(ss, plan, ROIS.ctv_p2_60.name, total_dose*100, 10)
      OF.min_dose(ss, plan, ROIS.ptv_p1_60.name, 57*100, 100)
      OF.max_dose(ss, plan, ROIS.ptv_p1_60.name, 63*100, 100)
      OF.min_dose(ss, plan, ROIS.ptv_p2_60.name, 57*100, 100)
      OF.max_dose(ss, plan, ROIS.ptv_p2_60.name, 63*100, 100)
      OF.max_dose(ss, plan, ROIS.body.name, 63*100, 100)
      OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 25*100, 3.5, 3)
      OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 20*100, 2, 3)
      OF.max_eud(ss, plan, ROIS.rectum.name, 30*100, 1, 1)
      OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 20*100, 2, 3)
      OF.max_eud(ss, plan, ROIS.anal_canal.name, 30*100, 1, 1)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 20*100, 2, 1)
      OF.max_eud(ss, plan, ROIS.bladder.name, 30*100, 1, 1)
      OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 30*100, 1, 1)
      OF.max_dose(ss, plan, ROIS.femoral_l.name, 44*100, 1)
      OF.max_dose(ss, plan, ROIS.femoral_r.name, 44*100, 1)
  elif total_dose == 67.5:
    OF.uniform_dose(ss, plan, ROIS.ctv_p1_67_5.name, 67.5*100, 10)
    OF.uniform_dose(ss, plan, ROIS.x_ptv_62_5.name, 62.5*100, 10)
    ctv_n_62_5 = [ROIS.ctv_n_62_5.name, ROIS.ctv_n1_62_5.name,ROIS.ctv_n2_62_5.name,ROIS.ctv_n3_62_5.name]
    for c in ctv_n_62_5: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, 62.5*100, 10)
    if SSF.has_roi_with_shape(ss, ROIS.x_ctv_50.name):
      OF.uniform_dose(ss, plan, ROIS.x_ctv_50.name, 50*100, 10)
      OF.min_dose(ss, plan, ROIS.ctv_p1_67_5.name, total_dose*100*0.97, 300)
      OF.min_dose(ss, plan, ROIS.ctv_p2_62_5.name, 62.5*0.97*100, 300)
      OF.min_dose(ss, plan, ROIS.ptv_p1_67_5.name, total_dose*100*0.955, 500)
      OF.max_dose(ss, plan, ROIS.ptv_p1_67_5.name, total_dose*100*1.03, 10000)
      OF.min_dose(ss, plan, ROIS.ptv_p2_62_5.name, 62.5*0.954*100, 500)
      OF.max_dose(ss, plan, ROIS.x_ptv_62_5.name, 62.5 * 100 * 1.04, 300)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n_62_5.name): # With boost to lymph node
        OF.min_dose(ss, plan, ROIS.ptv_n_62_5.name, 62.5*0.955*100, 500)
        OF.max_dose(ss, plan, ROIS.ptv_n_62_5.name, 62.5*1.04*100, 300)
        for c in ctv_n_62_5: #with boost to lymph node
          if SSF.has_roi_with_shape(ss, c):
            OF.min_dose(ss, plan, c, 62.5 * 0.97 * 100, 300)
      if SSF.has_roi_with_shape(ss, ROIS.x_ptv_50.name):
        OF.min_dose(ss, plan, ROIS.ptv_e_50.name, 50*0.954*100, 1000)
        OF.max_dose(ss, plan, ROIS.x_ptv_50.name, 52.3*100, 10000)
        OF.min_dose(ss, plan, ROIS.x_ctv_50.name, 50 * 0.97 * 100, 300)
        OF.fall_off(ss, plan, ROIS.ptv_e_50.name, 67.5*0.98*100, 50*100, 0.5, 3)
      OF.fall_off(ss, plan, ROIS.body.name, 67*100, 17*100, 4, 30)
      OF.fall_off(ss, plan, ROIS.body.name, 67*100, 42*100, 1.0, 50)
      OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 300)
      OF.max_eud(ss, plan, ROIS.body.name, 11*100, 1, 3)
      OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*0.98*100, 44*100, 0.5, 100)
      OF.max_eud(ss, plan, ROIS.x_rectum.name, 34 * 100, 1, 20)
      OF.max_dose(ss, plan, ROIS.rectum.name, 67.5*100*0.965, 10000)
      OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*0.98*100, 44*100, 0.5, 100)
      OF.max_dose(ss, plan, ROIS.anal_canal.name, 67.5*100*0.965, 10000)
      OF.max_eud(ss, plan, ROIS.x_anal_canal.name, 20 * 100, 1, 7)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose * 0.98 * 100, 20 * 100, 2.5, 100)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*0.98*100, 44*100, 0.5, 100)
      OF.max_dose(ss, plan, ROIS.bladder.name, 67.5*100*0.98, 1000)
      OF.max_eud(ss, plan, ROIS.x_bladder.name, 39 * 100, 1, 10)
      OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 18*100, 1, 17)
      OF.fall_off(ss, plan, ROIS.bowel_bag.name, 49*100, 40*100, 1, 1000)
      OF.max_eud(ss, plan, ROIS.penile_bulb.name, 17*100, 1, 2)
      OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*0.98*100, 25*100, 1, 100)
      OF.max_dose(ss, plan, ROIS.femoral_l.name, 40*100, 30)
      OF.max_dose(ss, plan, ROIS.femoral_r.name, 40*100, 30)
  elif total_dose == 77: # Normo-fractionation
    OF.uniform_dose(ss, plan, ROIS.ctv_p1_77.name, 77*100, 10)
    OF.uniform_dose(ss, plan, ROIS.x_ptv_70.name, 70*100, 10)
    ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
    for c in ctv_n_70: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, 70*100, 10)
    if SSF.has_roi_with_shape(ss, ROIS.x_ctv_56.name):
      OF.uniform_dose(ss, plan, ROIS.x_ctv_56.name, 56*100, 10)
    if opt == 'auto':
      OF.min_dose(ss, plan, ROIS.ctv_p1_77.name, total_dose*100*0.97, 300)
      OF.min_dose(ss, plan, ROIS.ctv_p2_70.name, 67.9*100, 300)
      OF.min_dose(ss, plan, ROIS.ptv_p1_77.name, total_dose*100*0.955, 300)
      OF.max_dose(ss, plan, ROIS.ptv_p1_77.name, total_dose*100*1.03, 10000)
      OF.min_dose(ss, plan, ROIS.ptv_p2_70.name, 67*100, 500)
      OF.max_dose(ss, plan, ROIS.x_ptv_70.name, 70 * 100 * 1.04, 300)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name):
        OF.min_dose(ss, plan, ROIS.ptv_n_70.name, 66.8*100, 300)
        OF.max_dose(ss, plan, ROIS.ptv_n_70.name, 73*100, 300)
        for c in ctv_n_70: # With boost to lymph node
          if SSF.has_roi_with_shape(ss, c):
            OF.min_dose(ss, plan, c, 70 * 0.97 *100, 300) # legge inn for-løkke her?
      if SSF.has_roi_with_shape(ss, ROIS.x_ptv_56.name):
        OF.min_dose(ss, plan, ROIS.ptv_e_56.name, 53.5*100, 500)
        OF.max_dose(ss, plan, ROIS.x_ptv_56.name, 58.5*100, 10000)
        OF.min_dose(ss, plan, ROIS.x_ctv_56.name, 56 * 0.97 * 100, 300)
        OF.fall_off(ss, plan, ROIS.ptv_e_56.name, 77*100, 56*100, 0.5, 3)
      OF.fall_off(ss, plan, ROIS.body.name, 77*100, 20*100, 4, 30)
      OF.fall_off(ss, plan, ROIS.body.name, 77*100, 45*100, 1.0, 50)
      OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 300)
      OF.max_eud(ss, plan, ROIS.body.name, 13*100, 1, 3)
      OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*0.98*100, 50*100, 0.5, 100)
      OF.max_eud(ss, plan, ROIS.x_rectum.name, 39 * 100, 1, 20)
      OF.max_dose(ss, plan, ROIS.rectum.name, 77*100*0.965, 10000)
      OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*0.98*100, 50*100, 0.5, 100)
      OF.max_dose(ss, plan, ROIS.anal_canal.name, 77*100*0.965, 10000)
      OF.max_eud(ss, plan, ROIS.x_anal_canal.name, 23 * 100, 1, 7)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose * 0.98 * 100, 25 * 100, 2.5, 100)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*0.98*100, 50*100, 0.5, 100)
      OF.max_dose(ss, plan, ROIS.bladder.name, 77*100*0.98, 1000)
      OF.max_eud(ss, plan, ROIS.x_bladder.name, 45 * 100, 1, 10)
      OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 21*100, 1, 17)
      OF.fall_off(ss, plan, ROIS.bowel_bag.name, 55*100, 45*100, 1, 1000)
      OF.max_eud(ss, plan, ROIS.penile_bulb.name, 20*100, 1, 2)
      OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*0.98*100, 30*100, 1, 100)
      OF.max_dose(ss, plan, ROIS.femoral_l.name, 50*100, 10)
      OF.max_dose(ss, plan, ROIS.femoral_r.name, 50*100, 10)
    else:
      OF.min_dose(ss, plan, ROIS.ptv_p1_77.name, total_dose*100*0.95, 100)
      OF.max_dose(ss, plan, ROIS.ptv_p1_77.name, total_dose*100*1.05, 100)
      OF.min_dose(ss, plan, ROIS.ptv_p2_70.name, 66.5*100, 100)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name):
        OF.min_dose(ss, plan, ROIS.ptv_n_70.name, 66.5*100, 100)
        OF.max_dose(ss, plan, ROIS.ptv_n_70.name, 73.5*100, 100)
      if SSF.has_roi_with_shape(ss, ROIS.x_ptv_56.name):
        OF.min_dose(ss, plan, ROIS.ptv_e_56.name, 53.2*100, 100)
        OF.max_dose(ss, plan, ROIS.x_ptv_56.name, 58.8*100, 100)
      OF.fall_off(ss, plan, ROIS.ptv_p2_70.name, 77*100, 70*100, 0.4, 10)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name):
        OF.fall_off(ss, plan, ROIS.ptv_e_56.name, 77*100, 56*100, 0.5, 3)
      OF.fall_off(ss, plan, ROIS.body.name, 77*100, 30*100, 3.5, 3)
      OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 100)
      OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 25*100, 2, 3)
      OF.max_eud(ss, plan, ROIS.rectum.name, 30*100, 1, 1)
      OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, 25*100, 3, 3)
      OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 30*100, 1, 1)
      OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 25*100, 2, 3)
      OF.max_eud(ss, plan, ROIS.anal_canal.name, 30*100, 1, 1)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 40*100, 1.5, 1)
      OF.max_eud(ss, plan, ROIS.bladder.name, 30*100, 1, 1)
      OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 35*100, 1, 1)
      OF.max_dose(ss, plan, ROIS.femoral_l.name, 51*100, 1)
      OF.max_dose(ss, plan, ROIS.femoral_r.name, 51*100, 1)
  else:
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p.name+'_'+str(total_dose)):
      OF.uniform_dose(ss, plan, ROIS.ctv_p.name+'_'+str(total_dose), total_dose*100, 10)
      OF.min_dose(ss, plan, ROIS.ptv_p.name+'_'+str(total_dose), 0.95*total_dose*100, 100)
      OF.max_dose(ss, plan, ROIS.ptv_p.name+'_'+str(total_dose), 1.05*total_dose*100, 100)
    else:
      OF.uniform_dose(ss, plan, ROIS.ctv.name+'_'+str(total_dose), total_dose*100, 10)
      OF.min_dose(ss, plan, ROIS.ptv.name, 0.95*total_dose*100, 100)
      OF.max_dose(ss, plan, ROIS.ptv.name, 1.05*total_dose*100, 100)
    OF.max_dose(ss, plan, ROIS.body.name, 1.05*total_dose*100, 100)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose/2*100, 3.5, 3)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 20*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 20*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 20*100, 2, 1)
    OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 30*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 44*100, 1)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 44*100, 1)



# Prostate bed
def create_prostate_bed_objectives(ss, plan, total_dose, opt):
  if total_dose > 69:
    OF.uniform_dose(ss, plan, ROIS.ctv_sb_70.name, total_dose*100, 10)
    ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
    for c in ctv_n_70: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, total_dose*100, 10)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name): # With lymph node volume
      OF.uniform_dose(ss, plan, ROIS.x_ctv_56.name, 56*100, 10)
    OF.min_dose(ss, plan, ROIS.ptv_sb_70.name, 66.5*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_sb_70.name, 73.5*100, 300)
    OF.fall_off(ss, plan, ROIS.ptv_sb_70.name, 70*100, 67*100, 1, 3)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name): # With boost to lymph node
      OF.min_dose(ss, plan, ROIS.ptv_n_70.name, 66.5*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_n_70.name, 73.5*100, 300)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name): # With lymph node volume
      OF.min_dose(ss, plan, ROIS.ptv_e_56.name, 53.2*100, 300)
      OF.max_dose(ss, plan, ROIS.x_ptv_56.name, 58.8*100, 300)
      OF.fall_off(ss, plan, ROIS.ptv_e_56.name, 70*100, 56*100, 0.5, 3)
    OF.max_dose(ss, plan, ROIS.body.name, 73.5*100, 300)
    OF.fall_off(ss, plan, ROIS.body.name, 70*100, 20*100, 3.5, 30)
    OF.fall_off(ss, plan, ROIS.body.name, 70 * 100, 40 * 100, 1, 50)
    if opt == 'auto':
      if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name):  # With lymph node volume
        OF.min_dose(ss, plan, ROIS.x_ctv_56.name, 56*0.97 * 100, 300)
      for c in ctv_n_70:  # With boost to lymph node
        if SSF.has_roi_with_shape(ss, c):
          OF.min_dose(ss, plan, c, total_dose * 0.97 * 100, 300)
      OF.min_dose(ss, plan, ROIS.ctv_sb_70.name, 70*0.97 * 100, 300)
      OF.max_eud(ss, plan, ROIS.body.name, 13*100, 1, 5)
      OF.max_eud(ss, plan, ROIS.x_rectum.name, 39*100, 1, 20)
      OF.max_dose(ss, plan, ROIS.rectum.name, 70*100*0.965, 1000)
      OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*0.98*100, 30*100, 0.8, 100)
      OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*0.98*100, 30*100, 1, 100)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*0.98*100, 50*100, 0.5, 100)
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*0.98*100, 25*100, 2.5, 100)
      OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*0.98*100, 40*100, 1.5, 1000)
      OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*0.98*100, 50*100, 0.5, 100)
      OF.max_eud(ss, plan, ROIS.x_anal_canal.name, 23*100, 1, 7)
      OF.max_eud(ss, plan, ROIS.x_bladder.name, 45*100, 1, 12)
      OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 20*100, 1, 18)
      OF.max_eud(ss, plan, ROIS.penile_bulb.name, 20*100, 1, 2)
      OF.max_dose(ss, plan, ROIS.bladder.name, 70*100*0.98, 1000) 
      OF.max_dose(ss, plan, ROIS.anal_canal.name, 70*100*0.965, 10000)
      OF.max_dose(ss, plan, ROIS.femoral_l.name, 50*100, 10)
      OF.max_dose(ss, plan, ROIS.femoral_r.name, 50*100, 10)
    else: 
      OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 25*100, 2, 3)
      OF.max_eud(ss, plan, ROIS.rectum.name, 30*100, 1, 1) #ses på
      OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, 25*100, 2.5, 3)
      #OF.max_eud(ss, plan, ROIS.bowel_bag.name, 30*100, 1, 1) #ses på
      OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 25*100, 2, 3)
      OF.max_eud(ss, plan, ROIS.anal_canal.name, 30*100, 1, 1) #ses på
      OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 40*100, 1.5, 1)
      OF.max_eud(ss, plan, ROIS.bladder.name, 30*100, 1, 1) #ses på
      OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 35*100, 1, 1)
      OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 30*100, 1, 1)
      OF.max_dose(ss, plan, ROIS.femoral_l.name, 51*100, 1)
      OF.max_dose(ss, plan, ROIS.femoral_r.name, 51*100, 1)
  else:
    OF.uniform_dose(ss, plan, ROIS.ctv_sb.name, total_dose*100, 3)
    OF.min_dose(ss, plan, ROIS.ptv_sb.name, total_dose*0.95*100, 100)
    OF.max_dose(ss, plan, ROIS.ptv_sb.name, total_dose*1.05*100, 100)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*1.05*100, 100)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose/2*100, 3.5, 3)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 25*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, 25*100, 2.5, 3)
    OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 25*100, 2, 3)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 40*100, 1.5, 1)
    OF.fall_off(ss, plan, ROIS.penile_bulb.name, total_dose*100, 35*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 30*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 51*100, 1)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 51*100, 1)


# Gyn
def create_gyn_objectives(pm, examination, ss, plan, total_dose, opt):
  if total_dose == 45:# Total dose 45 Gy, no lymph nodes included
    OF.uniform_dose(ss, plan, ROIS.ctv_45.name, 45*100, 20)
    OF.min_dose(ss, plan, ROIS.ctv_45.name, 42.9*100, 400)
    OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.9*100, 800)
    OF.max_dose(ss, plan, ROIS.ptv_45.name, 47*100, 2000)
    OF.max_dose(ss, plan, ROIS.x_ctv_p.name, 46*100, 10)
    OF.max_dose(ss, plan, ROIS.body.name, 47*100, 300)
    OF.fall_off(ss, plan, ROIS.body.name, 45*100, 20*100, 2, 1)
    OF.max_dose(ss, plan, ROIS.spinal_cord.name, 30*100, 50)
    OF.max_eud(ss, plan, ROIS.body.name, 15*100, 2, 3)
    if SSF.has_roi_with_shape(ss, ROIS.rectum.name):
      #OF.fall_off(ss, plan, ROIS.rectum.name, 45*100, 15*100, 2, 5)
      OF.max_dvh(ss, plan, ROIS.rectum.name, 35*100, 50, 50)
      if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.rectum, ROIS.ptv_45, 10):
        OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 2, 7)
    if SSF.has_roi_with_shape(ss, ROIS.sigmoid.name):
      #OF.fall_off(ss, plan, ROIS.sigmoid.name, 45*100, 22*100, 2, 3)
      if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.sigmoid, ROIS.ptv_45, 10):
        OF.max_eud(ss, plan, ROIS.sigmoid.name, 40*100,2, 7)
    if SSF.has_roi_with_shape(ss, ROIS.bladder.name):
      #OF.fall_off(ss, plan, ROIS.bladder.name, 45*100, 26*100, 2, 30)
      OF.max_dvh(ss, plan, ROIS.bladder.name, 35*100, 50, 50)
      OF.max_dvh(ss, plan, ROIS.bladder.name, 25*100, 50, 30)
      if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.bladder, ROIS.ptv_45, 10):
        OF.max_eud(ss, plan, ROIS.bladder.name, 36*100, 2, 7)
    if SSF.has_roi_with_shape(ss, ROIS.bowel_bag.name):
      #OF.fall_off(ss, plan, ROIS.bowel_bag.name, 45*100, 15*100, 3, 3)
      OF.max_dvh(ss, plan, ROIS.x_bowelbag.name, 35*100, 50, 600)
      OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 20*100, 2, 7)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 10)
    if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
      OF.max_eud(ss, plan, ROIS.kidney_l.name, 3*100, 1, 50)
    if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
      OF.max_eud(ss, plan, ROIS.kidney_r.name, 3*100, 1, 50)
  elif total_dose > 54: # Total dose 55 or 57.5
    if opt == 'auto':
      if total_dose == 57.5:
        ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name,ROIS.ctv_n5_57.name]
        if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
          for c in ctv_n_57: # With boost to lymph node
            if SSF.has_roi_with_shape(ss, c):
              OF.uniform_dose(ss, plan, c, 58.7*100, 30)
        elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_57.name):
          OF.uniform_dose(ss, plan, ROIS.ctv_n_57.name, 58.7*100, 30)
      ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name,ROIS.ctv_n5_55.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
        for c in ctv_n_55: # With boost to lymph node
          if SSF.has_roi_with_shape(ss, c):
            OF.uniform_dose(ss, plan, c, 56.2*100, 30)
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_55.name):
        OF.uniform_dose(ss, plan, ROIS.ctv_n_55.name, 56.2*100, 30)

      OF.uniform_dose(ss, plan, ROIS.x_ctv_45.name, 45*100, 30)
      if total_dose == 57.5:
        ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name,ROIS.ctv_n5_57.name]
        if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
          for c in ctv_n_57: # With boost to lymph node
            if SSF.has_roi_with_shape(ss, c):
              OF.min_dose(ss, plan, c, total_dose*100+10, 400)
        elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_57.name):
          OF.min_dose(ss, plan, ROIS.ctv_n_57.name, total_dose*100+10, 250)
      ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name,ROIS.ctv_n5_55.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
        for c in ctv_n_55: # With boost to lymph node
          if SSF.has_roi_with_shape(ss, c):
            OF.min_dose(ss, plan, c, 55*100+10, 500) 
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_55.name):
        OF.min_dose(ss, plan, ROIS.ctv_n_55.name, 55*100+10, 250) 
      if total_dose == 57.5:
        OF.min_dose(ss, plan, ROIS.ptv_n_57.name, 0.90*57.5*100, 300) 
        OF.max_dose(ss, plan, ROIS.ptv_n_57.name, 61.5*100, 600)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n_55.name):
        OF.min_dose(ss, plan, ROIS.ptv_n_55.name, 0.90*55*100, 300)
        OF.max_dose(ss, plan, ROIS.ptv_n_55.name, 58*100, 600)
      OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.9*100, 800)

      OF.max_dose(ss, plan, ROIS.x_ptv_45.name, 47.2*100, 2000)
      if SSF.has_roi_with_shape(ss, ROIS.x_gtv_p.name):
        OF.max_dose(ss, plan, ROIS.x_gtv_p.name, 46.5*100, 50)
      if SSF.has_roi_with_shape(ss, ROIS.x_ctv_p.name):
        OF.max_dose(ss, plan, ROIS.x_ctv_p.name, 46.5*100, 50)
      if total_dose == 57.5:
        OF.fall_off(ss, plan, ROIS.body.name, 57.5*100, 58/2*100, 2, 3)
        OF.max_dose(ss, plan, ROIS.body.name, 61*100, 400)
      elif total_dose == 55:
        OF.fall_off(ss, plan, ROIS.body.name, 55*100, 35*100, 1, 1)
        OF.max_dose(ss, plan, ROIS.body.name, 57.75*100, 100)

      OF.max_eud(ss, plan, ROIS.body.name, 15*100, 2, 3)
      OF.max_dose(ss, plan, ROIS.spinal_cord_prv.name, 45*100, 1000)
      if SSF.has_roi_with_shape(ss, ROIS.cauda_equina.name):
        OF.max_dose(ss, plan, ROIS.cauda_equina.name, 48*100, 1000)
      if SSF.has_roi_with_shape(ss, ROIS.rectum.name):
        OF.max_dvh(ss, plan, ROIS.x_rectum_ptv_n.name, 35*100, 50, 50)
        OF.max_dvh(ss, plan, ROIS.x_rectum_ptv_n.name, 42*100, 50, 300)
        if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.rectum, ROIS.ptv_45, 10):
          OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 2, 10)
        else:
          OF.max_eud(ss, plan, ROIS.rectum.name, 40*100, 2, 10) 
      if SSF.has_roi_with_shape(ss, ROIS.sigmoid.name):
        if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.sigmoid, ROIS.ptv_45, 10):
          OF.max_eud(ss, plan, ROIS.sigmoid.name, 40*100,2, 10)
        else:
          OF.max_eud(ss, plan, ROIS.sigmoid.name, 43*100,2, 10)
      if SSF.has_roi_with_shape(ss, ROIS.bladder.name):
        OF.max_dvh(ss, plan, ROIS.x_bladder_ptv_n.name, 35*100, 50, 50)
        OF.max_dvh(ss, plan, ROIS.x_bladder_ptv_n.name, 25*100, 50, 50)
        if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.bladder, ROIS.ptv_45, 10):
          OF.max_eud(ss, plan, ROIS.bladder.name, 32*100, 2, 10)
        else:
          OF.max_eud(ss, plan, ROIS.bladder.name, 36*100, 2, 10)
      if SSF.has_roi_with_shape(ss, ROIS.bowel_bag.name):
        OF.max_dvh(ss, plan, ROIS.x_bowelbag_ptv_n.name, 35*100, 10, 600)
        OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 20*100, 2, 10)
      if total_dose == 57.5:
        OF.max_dose(ss, plan, ROIS.bowel_bag.name, 57.4*100, 1500)
      elif total_dose == 55:
        OF.max_dose(ss, plan, ROIS.bowel_bag.name, 54.9*100, 1500) 
      OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 10)
      OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 10)
      if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
        OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 10)
      if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
        OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 10)
    else: # NOT AUTOMATIC
      if total_dose > 57:
        ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name,ROIS.ctv_n5_57.name]
        if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
          for c in ctv_n_57: # With boost to lymph node
            if SSF.has_roi_with_shape(ss, c):
              OF.uniform_dose(ss, plan, c, 58.7*100, 30)
        elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_57.name):
          OF.uniform_dose(ss, plan, ROIS.ctv_n_57.name, 58.7*100, 30)
      ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name,ROIS.ctv_n5_55.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
        for c in ctv_n_55: # With boost to lymph node
          if SSF.has_roi_with_shape(ss, c):
            OF.uniform_dose(ss, plan, c, 56.2*100, 30)
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_55.name):
        OF.uniform_dose(ss, plan, ROIS.ctv_n_55.name, 56.2*100, 30)
      OF.uniform_dose(ss, plan, ROIS.x_ctv_45.name, 45*100, 30)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing_45.name):
        OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_r_45.name, 45*100, 30)
        OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_l_45.name, 45*100, 30)
      if total_dose > 57:  
        ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name,ROIS.ctv_n5_57.name]
        if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
          for c in ctv_n_57: # With boost to lymph node
            if SSF.has_roi_with_shape(ss, c):
              OF.min_dose(ss, plan, c, total_dose*100, 600)
        elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_57.name):
          OF.min_dose(ss, plan, ROIS.ctv_n_57.name, total_dose*100, 600)
      ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name,ROIS.ctv_n5_55.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
        for c in ctv_n_55: # With boost to lymph node
          if SSF.has_roi_with_shape(ss, c):
            OF.min_dose(ss, plan, c, 55*100, 600)
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_55.name):
        OF.min_dose(ss, plan, ROIS.ctv_n_55.name, 55*100, 600)
      if total_dose > 57:
        OF.min_dose(ss, plan, ROIS.ptv_n_57.name, 0.90*57.5*100, 1500)
        OF.max_dose(ss, plan, ROIS.ptv_n_57.name, 61.5*100, 600)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n_55.name):  
        OF.min_dose(ss, plan, ROIS.ptv_n_55.name, 0.90*55*100, 1500)
        OF.max_dose(ss, plan, ROIS.ptv_n_55.name, 58*100, 600)
      OF.min_dose(ss, plan, ROIS.ptv_45.name, 42.8*100, 2000)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing_45.name):
        OF.min_dose(ss, plan, ROIS.ptv_e_ing_45.name, 42.8*100, 2000)
      if SSF.has_roi_with_shape(ss, ROIS.x_ptv_45_1.name):
        OF.max_dose(ss, plan, ROIS.x_ptv_45_1.name, 47.5*100, 400)
      else:
        OF.max_dose(ss, plan, ROIS.x_ptv_45.name, 47.5*100, 400)
      OF.max_dose(ss, plan, ROIS.x_ctv_p.name, 46.5*100, 50)
      if total_dose > 57:
        OF.fall_off(ss, plan, ROIS.body.name, 58*100, 58/2*100, 2, 3)
        OF.max_dose(ss, plan, ROIS.body.name, 61*100, 400)
      else:
        OF.fall_off(ss, plan, ROIS.body.name, 55*100, 23*100, 2, 3)
        OF.max_dose(ss, plan, ROIS.body.name, 57.5*100, 100)
      OF.max_dose(ss, plan, ROIS.spinal_cord.name, 45*100, 100)
      OF.max_dose(ss, plan, ROIS.cauda_equina.name, 48*100, 100)
      if SSF.has_roi_with_shape(ss, ROIS.rectum.name):
        OF.fall_off(ss, plan, ROIS.rectum.name, 45*100, 20*100, 2, 5)
        if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.rectum, ROIS.ptv_45, 10):
          OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 1, 10)
      if SSF.has_roi_with_shape(ss, ROIS.sigmoid.name):
        OF.fall_off(ss, plan, ROIS.sigmoid.name, 45*100, 22*100, 2, 3)
        if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.sigmoid, ROIS.ptv_45, 10):
          OF.max_eud(ss, plan, ROIS.sigmoid.name, 40*100,1, 10)
      if SSF.has_roi_with_shape(ss, ROIS.bladder.name):
        OF.fall_off(ss, plan, ROIS.bladder.name, 45*100, 22*100, 2, 30)
        if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.bladder, ROIS.ptv_45, 10):
          OF.max_eud(ss, plan, ROIS.bladder.name, 36*100, 1, 15)
      if SSF.has_roi_with_shape(ss, ROIS.bowel_bag.name):
        OF.fall_off(ss, plan, ROIS.bowel_bag.name, 45*100, 15*100, 3, 3)
        OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 20*100, 1, 15)
      if total_dose > 57:
        OF.max_dose(ss, plan, ROIS.femoral_l.name, 50*100, 10)
        OF.max_dose(ss, plan, ROIS.femoral_r.name, 50*100, 10)
        if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
          OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 30)
        if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
          OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 30)
      else:   
        OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 20)
        OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 20)
        if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
          OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 50)
        if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
          OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 50)
  else:
    OF.uniform_dose(ss, plan, ROIS.ctv.name, total_dose*100, 20)
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*0.95*100, 800)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*1.05*100, 400)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*1.04*100, 300)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 2, 1)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 15*100, 2, 3) 
    OF.max_eud(ss, plan, ROIS.rectum.name, 25*100, 1, 1)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, 20*100, 2, 3)
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 20*100, 1, 3)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 26*100, 2, 3)
    OF.max_eud(ss, plan, ROIS.bladder.name, 25*100, 1, 1)
    OF.fall_off(ss, plan, ROIS.sigmoid.name, total_dose*100, 23*100, 2, 3)
    OF.max_eud(ss, plan, ROIS.sigmoid.name, 25*100,1, 10)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 50*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 50*100, 10)
    if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
      OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 30)
    if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
      OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 30)

def create_gyn_vulva_objectives(pm, examination, ss, plan, total_dose):

  if total_dose > 66: # primary radiotherapy
    OF.uniform_dose(ss, plan, ROIS.ctv_p_67.name, 67.2*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_64.name): # With boost to lymph node
      ctv_n_64 = [ROIS.ctv_n1_64.name,ROIS.ctv_n2_64.name,ROIS.ctv_n3_64.name,ROIS.ctv_n4_64.name,ROIS.ctv_n5_64.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_64.name):
        for c in ctv_n_64: 
          if SSF.has_roi_with_shape(ss, c):
            OF.uniform_dose(ss, plan, c, 64.4*102, 30)
      else:
        OF.uniform_dose(ss, plan, ROIS.ctv_n_64.name, 64.4*102, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_59.name): # With boost to lymph node
      ctv_n_59 = [ROIS.ctv_n1_59.name,ROIS.ctv_n2_59.name,ROIS.ctv_n3_59.name,ROIS.ctv_n4_59.name,ROIS.ctv_n5_59.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_59.name):
        for c in ctv_n_59: 
          if SSF.has_roi_with_shape(ss, c):
            OF.uniform_dose(ss, plan, c, 58.8*102, 30)
      else:
        OF.uniform_dose(ss, plan, ROIS.ctv_n_59.name, 58.8*102, 30)
    OF.uniform_dose(ss, plan, ROIS.x_ctv_48.name, 47.6*100, 30)
    if not SSF.has_roi_with_shape(ss, ROIS.ptv_n_64.name):
      OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_r_48.name, 47.6*100, 30)
      OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_l_48.name, 47.6*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_64.name): # With boost to lymph node
      ctv_n_64 = [ROIS.ctv_n1_64.name,ROIS.ctv_n2_64.name,ROIS.ctv_n3_64.name,ROIS.ctv_n4_64.name,ROIS.ctv_n5_64.name]

      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_64.name):
        for c in ctv_n_64: # With boost to lymph node
          if SSF.has_roi_with_shape(ss, c):
            OF.min_dose(ss, plan, c, 64.4*100, 300)
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_64.name):
        OF.min_dose(ss, plan, ROIS.ctv_n_64.name, 64.4*100, 300)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_59.name): # With boost to lymph node
      ctv_n_59 = [ROIS.ctv_n1_59.name,ROIS.ctv_n2_59.name,ROIS.ctv_n3_59.name,ROIS.ctv_n4_59.name,ROIS.ctv_n5_59.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_59.name):
        for c in ctv_n_59: 
          if SSF.has_roi_with_shape(ss, c):
            OF.min_dose(ss, plan, c, 58.8*100, 30)
      else:
        OF.min_dose(ss, plan, ROIS.ctv_n_59.name, 58.8*100, 30)
    OF.min_dose(ss, plan, ROIS.ptv_p_67.name, 0.95*67.2*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_p_67.name, 67.2*106, 150)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_64.name):
      OF.min_dose(ss, plan, ROIS.ptv_n_64.name, 0.90*64.4*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_n_64.name, 64.4*106, 150)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_59.name): 
      OF.min_dose(ss, plan, ROIS.ptv_n_59.name, 0.90*58.8*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_n_59.name, 58.8*106, 150)
    OF.min_dose(ss, plan, ROIS.ptv_e_pelvic_48.name, 47.6*0.95*100, 300)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing_48.name):
      OF.min_dose(ss, plan, ROIS.ptv_e_ing_48.name, 47.6*0.95*100, 300)
    OF.max_dose(ss, plan, ROIS.x_ptv_48.name, 47.6*105, 150)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose/2*100, 2, 3)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*106, 400)
    OF.max_eud(ss, plan, ROIS.body.name, 15*100, 1, 50)
    if SSF.has_roi_with_shape(ss, ROIS.cauda_equina.name):
      OF.max_dose(ss, plan, ROIS.cauda_equina.name, 45*100, 150)
    if SSF.has_roi_with_shape(ss, ROIS.rectum.name):
      OF.fall_off(ss, plan, ROIS.rectum.name, 67*100, 15*100, 2, 30) 
      if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.rectum, ROIS.ptv_e_pelvic_48, 10):
        OF.max_eud(ss, plan, ROIS.rectum.name, 35*100, 1, 5)
      OF.max_dose(ss, plan, ROIS.rectum.name, 67*100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.anal_canal.name):
      OF.fall_off(ss, plan, ROIS.anal_canal.name, 67*100, 15*100, 2, 30) 
      if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.anal_canal, ROIS.ptv_e_pelvic_48, 10):
        OF.max_eud(ss, plan, ROIS.anal_canal.name, 35*100, 1, 5)
      OF.max_dose(ss, plan, ROIS.anal_canal.name, 67*100, 100)
    if SSF.has_roi_with_shape(ss, ROIS.bladder.name):
      OF.fall_off(ss, plan, ROIS.bladder.name, 67*100, 15*100, 2, 30)
      if not SSF.roi_outside_overlap_by_percent(pm, examination, ss, ROIS.bladder, ROIS.ptv_e_pelvic_48, 10):
        OF.max_eud(ss, plan, ROIS.bladder.name, 32*100, 1, 5)
      OF.max_dose(ss, plan, ROIS.bladder.name, 47.6*104, 100)
    if SSF.has_roi_with_shape(ss, ROIS.bowel_bag.name):
      OF.fall_off(ss, plan, ROIS.bowel_bag.name, 47.6*100, 15*100, 3, 50)
      OF.fall_off(ss, plan, ROIS.x_bowelbag.name, 47.6*100, 15*100, 2, 50)
      OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 23*100, 1, 5)
      OF.max_dose(ss, plan, ROIS.bowel_bag.name, 47.6*104, 100)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 20)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 20)
    if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
      OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 10)
    if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
      OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 10)
  else:
    OF.uniform_dose(ss, plan, ROIS.ctv_sb_57.name, 57.5*100, 30)
    OF.uniform_dose(ss, plan, ROIS.x_ctv_45.name, 45*100, 30)
    #if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ing_r_45.name):
    #  OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_r_45.name, 45*100, 30)
    #  OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_l_45.name, 45*100, 30)
    OF.min_dose(ss, plan, ROIS.ptv_sb_57.name, total_dose*0.95*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_sb_57.name, total_dose*1.05*100, 150)
    OF.min_dose(ss, plan, ROIS.ptv_e_pelvic_45.name, 45*0.95*100, 300)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing_45.name):
      OF.min_dose(ss, plan, ROIS.ptv_e_ing_45.name, 45*0.95*100, 300)
    OF.max_dose(ss, plan, ROIS.x_ptv_45.name, 45*105, 150)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*1.04*100, 300)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 2, 1)
    OF.fall_off(ss, plan, ROIS.rectum.name, total_dose*100, 15*100, 2, 3) 
    OF.max_eud(ss, plan, ROIS.rectum.name, 25*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.rectum.name, 57*100, 100)
    OF.fall_off(ss, plan, ROIS.anal_canal.name, total_dose*100, 15*100, 2, 3) 
    OF.max_eud(ss, plan, ROIS.anal_canal.name, 25*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.anal_canal.name, 57*100, 100)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, 20*100, 2, 3)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, 45*104, 100)
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 20*100, 1, 3)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, 26*100, 2, 3)
    OF.max_eud(ss, plan, ROIS.bladder.name, 25*100, 1, 1)
    OF.max_dose(ss, plan, ROIS.bladder.name, 45*104, 100)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 10)
    if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
      OF.max_eud(ss, plan, ROIS.kidney_l.name, 5*100, 1, 10)
    if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
      OF.max_eud(ss, plan, ROIS.kidney_r.name, 5*100, 1, 10)
    if SSF.has_roi_with_shape(ss, ROIS.cauda_equina.name):
      OF.max_dose(ss, plan, ROIS.cauda_equina.name, 45*100, 150)



# Bladder
def create_bladder_objectives(plan, ss, total_dose):
  OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 30)
  OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 150)
  OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 80)
  OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 1.5, 30)
  OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 30)
  OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 10)
  OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 10)


# Rectum
def create_rectum_objectives(ss, plan, total_dose):
  if total_dose == 50:
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p_50.name):
      OF.uniform_dose(ss, plan, ROIS.ctv_p_50.name, total_dose*100, 30)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n_50.name): # With boost to lymph node
        ctv_n_50 = [ROIS.ctv_n1_50.name,ROIS.ctv_n2_50.name,ROIS.ctv_n3_50.name,ROIS.ctv_n4_50.name]
        if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_50.name):
          for c in ctv_n_50: 
            if SSF.has_roi_with_shape(ss, c):
              OF.uniform_dose(ss, plan, c, total_dose*100, 30)
        else:
          OF.uniform_dose(ss, plan, ROIS.ctv_n_50.name,total_dose*100 , 30)
      if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ing_r_46.name):
        OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_r_46.name, 46.5*100, 30)
        OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_l_46.name, 46.5*100, 30)
      OF.uniform_dose(ss, plan, ROIS.x_ctv_46_5.name, 46.5*100, 30)
      OF.min_dose(ss, plan, ROIS.ptv_p_50.name, total_dose*0.95*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_p_50.name, total_dose*100*1.05, 150)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n_50.name):
        OF.min_dose(ss, plan, ROIS.ptv_n_50.name, total_dose*0.95*100, 300)
        OF.max_dose(ss, plan, ROIS.ptv_n_50.name, total_dose*100*1.05, 150)
      OF.min_dose(ss, plan, ROIS.ptv_e_pelvic_46_5.name, 44.3*100, 300)
      
      if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing_46.name):
        OF.min_dose(ss, plan, ROIS.ptv_e_ing_46.name, 44.3*100, 300)
      OF.max_dose(ss, plan, ROIS.x_ptv_46_5.name,46.5*100*1.04, 150)
    else:
      OF.uniform_dose(ss, plan, ROIS.ctv_sb.name, total_dose*100, 30)
      OF.uniform_dose(ss, plan, ROIS.ctv_e_pelvic.name, total_dose*100, 30)
      OF.min_dose(ss, plan, ROIS.ptv_sb.name, total_dose*0.95*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_sb.name, total_dose*100*1.05, 150)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name):
        OF.min_dose(ss, plan, ROIS.ptv_n.name, total_dose*0.95*100, 300)
        OF.max_dose(ss, plan, ROIS.ptv_n.name, total_dose*100*1.05, 150)
      OF.min_dose(ss, plan, ROIS.ptv_e_pelvic.name, total_dose*0.95*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_e_pelvic.name, total_dose*100*1.05, 150)
      if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing.name):
        OF.min_dose(ss, plan, ROIS.ptv_e_ing.name, total_dose*0.95*100, 300)
        OF.max_dose(ss, plan, ROIS.ptv_e_ing.name, total_dose*100*1.05, 150)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 2, 10)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 1000)
    OF.max_eud(ss, plan, ROIS.body.name, 15*100, 1, 5)
    OF.max_dose(ss, plan, ROIS.bladder.name, total_dose*0.95*100, 100) 
    OF.max_eud(ss, plan, ROIS.bladder.name, 28*100, 1, 2)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, total_dose/2*100, 1, 20)
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 20*100, 1, 5)
    OF.fall_off(ss, plan, ROIS.x_bowelbag.name, total_dose*100, total_dose/2*100, 1, 10)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, total_dose/2*100, 1, 10)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, total_dose*0.95*100, 100)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 10)
    OF.max_eud(ss, plan, ROIS.genitals.name, 25*100, 1, 5)
    OF.max_dose(ss, plan, ROIS.genitals.name, 47.5*100, 10)
  elif total_dose > 40:
    OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name): # With boost to lymph node
      ctv_n = [ROIS.ctv_n1.name,ROIS.ctv_n2.name,ROIS.ctv_n3.name,ROIS.ctv_n4.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1.name):
        for c in ctv_n: 
          if SSF.has_roi_with_shape(ss, c):
            OF.uniform_dose(ss, plan, c, total_dose*100, 30)
      else:
        OF.uniform_dose(ss, plan, ROIS.ctv_n.name,total_dose*100 , 30)
    OF.min_dose(ss, plan, ROIS.ptv_p.name, total_dose*0.95*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_p.name, total_dose*100*1.05, 150)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name):
      OF.min_dose(ss, plan, ROIS.ptv_n.name, total_dose*0.95*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_n.name, total_dose*100*1.05, 150)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 2, 10)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 1000)
    OF.max_eud(ss, plan, ROIS.body.name, 15*100, 1, 5)
    OF.max_dose(ss, plan, ROIS.bladder.name, total_dose*0.95*100, 100) 
    OF.max_eud(ss, plan, ROIS.bladder.name, 28*100, 1, 2)
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, total_dose/2*100, 1, 20)
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 20*100, 1, 5)
    OF.fall_off(ss, plan, ROIS.x_bowelbag.name, total_dose*100, total_dose/2*100, 1, 10)
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, total_dose/2*100, 1, 10)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, total_dose*0.95*100, 100)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, total_dose*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, total_dose*100, 10)
    OF.max_eud(ss, plan, ROIS.genitals.name, 25*100, 1, 5)
    OF.max_dose(ss, plan, ROIS.genitals.name, total_dose*100, 10)
  elif total_dose == 25:
    OF.uniform_dose(ss, plan, ROIS.ctv_p.name, total_dose*100, 30)
    if SSF.has_roi_with_shape(ss, ROIS.ctv_n.name): # With boost to lymph node
      ctv_n = [ROIS.ctv_n1.name,ROIS.ctv_n2.name,ROIS.ctv_n3.name,ROIS.ctv_n4.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1.name):
        for c in ctv_n: 
          if SSF.has_roi_with_shape(ss, c):
            OF.uniform_dose(ss, plan, c, total_dose*100, 30)
      else:
        OF.uniform_dose(ss, plan, ROIS.ctv_n.name,total_dose*100 , 30)
    if SSF.has_roi_with_shape(ss, ROIS.ctv_e.name): # If CTVe is present
      OF.uniform_dose(ss, plan, ROIS.ctv_e.name, total_dose*100, 30) 
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 300)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 150)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 2, 8)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 1000)
    #OF.max_eud(ss, plan, ROIS.body.name, 5*100, 1, 5) #JSK slettet 2023-02-16
    OF.max_eud(ss, plan, ROIS.body_ptv.name, 5*100, 1, 3)  #JSK 2023-02-16
    OF.max_dose(ss, plan, ROIS.bladder.name, total_dose*0.95*100, 100) 
    #OF.max_eud(ss, plan, ROIS.bladder.name, 17*100, 1, 2) #JSK slettet 2023-02-16
    OF.max_eud(ss, plan, ROIS.x_bladder.name, 10*100, 1, 2) #JSK 2023-02-16
    OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, total_dose/2*100, 1, 10)
    OF.max_dose(ss, plan, ROIS.bowel_bag.name, total_dose*0.95*100, 100)
    #OF.max_eud(ss, plan, ROIS.bowel_bag.name, 10*100, 1, 2) #JSK slettet 2023-02-16
    OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 8*100, 1, 2) #JSK 2023-02-16
    OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, total_dose/2*100, 1, 8)
    OF.max_dose(ss, plan, ROIS.femoral_l.name, total_dose*100, 10)
    OF.max_dose(ss, plan, ROIS.femoral_r.name, total_dose*100, 10)
  else:
    OF.uniform_dose(ss, plan, ROIS.ctv_e.name, total_dose*100, 30)
    OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100*0.95, 300)
    OF.max_dose(ss, plan, ROIS.ptv.name, total_dose*100*1.05, 150)
    OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose*100/2, 1.8, 15)
    OF.max_dose(ss, plan, ROIS.body.name, total_dose*100*1.05, 20)
    OF.max_eud(ss, plan, ROIS.bladder.name, 16.2*100, 1, 1)
    OF.max_eud(ss, plan, ROIS.bowel_bag.name, 14*100, 1, 2)


# Anus
def create_anus_objectives(ss, plan, total_dose):
  ctv_n_present = False
  if total_dose > 57:
    OF.uniform_dose(ss, plan, ROIS.ctv_p_57.name, 57.5*100, 30)
  ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
    ctv_n_present = True
    for c in ctv_n_57: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, 57.5*100, 30)
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_57.name):
    ctv_n_present = True
    OF.uniform_dose(ss, plan, ROIS.ctv_n_57.name, 57.5*100, 30)
  if SSF.has_roi_with_shape(ss, ROIS.ctv_p_54.name):
    OF.uniform_dose(ss, plan, ROIS.ctv_p_54.name, 54*100, 30)
  ctv_n_54 = [ROIS.ctv_n1_54.name,ROIS.ctv_n2_54.name,ROIS.ctv_n3_54.name,ROIS.ctv_n4_54.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_54.name):
    ctv_n_present = True
    for c in ctv_n_54: # With boost to lymph node
      if SSF.has_roi_with_shape(ss, c):
        OF.uniform_dose(ss, plan, c, 54*100, 30)
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_54.name):
    ctv_n_present = True
    OF.uniform_dose(ss, plan, ROIS.ctv_n_54.name, 54*100, 30)
  OF.uniform_dose(ss, plan, ROIS.x_ctv_41.name, 41.6*100, 30)
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ing_r_41.name) and ctv_n_present == False:
    OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_r_41.name, 41.6*100, 30)
    OF.uniform_dose(ss, plan, ROIS.ctv_e_ing_l_41.name, 41.6*100, 30)
  if total_dose > 57:
    OF.min_dose(ss, plan, ROIS.ptv_p_57.name, 0.95*57.5*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_p_57.name, 1.05*57.5*100, 300)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_57.name):
      OF.min_dose(ss, plan, ROIS.ptv_n_57.name, 0.95*57.5*100, 300)
      OF.max_dose(ss, plan, ROIS.ptv_n_57.name, 1.05*57.5*100, 300)
  if SSF.has_roi_with_shape(ss, ROIS.ptv_p_54.name):
    OF.min_dose(ss, plan, ROIS.ptv_p_54.name, 0.95*54*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_p_54.name, 1.05*54*100, 300)  
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n_54.name):
    OF.min_dose(ss, plan, ROIS.ptv_n_54.name, 0.95*54*100, 300)
    OF.max_dose(ss, plan, ROIS.ptv_n_54.name, 1.05*54*100, 300)
  OF.min_dose(ss, plan, ROIS.ptv_e_pelvic_41.name, 0.95*41.6*100, 300)
  if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing_41.name):
    OF.min_dose(ss, plan, ROIS.ptv_e_ing_41.name, 0.95*41.6*100, 300)
  OF.max_dose(ss, plan, ROIS.x_ptv_41.name, 41.6*100*1.05, 150)
  OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, total_dose/2*100, 2, 10)
  OF.max_dose(ss, plan, ROIS.body.name, 1.04*total_dose*100, 400)
  OF.max_eud(ss, plan, ROIS.body.name, 20*100, 1, 5)
  OF.fall_off(ss, plan, ROIS.bladder.name, total_dose*100, total_dose/2*100, 1, 20) 
  OF.max_eud(ss, plan, ROIS.bladder.name, 25*100, 1, 5)
  OF.max_dose(ss, plan, ROIS.bladder.name, total_dose*0.95*100, 100)
  OF.max_eud(ss, plan, ROIS.x_bowelbag.name, 15*100, 1, 5)
  OF.fall_off(ss, plan, ROIS.x_bowelbag.name, total_dose*100, total_dose/2*100, 1, 10) 
  OF.fall_off(ss, plan, ROIS.bowel_bag.name, total_dose*100, total_dose/2*100, 1, 10)
  OF.max_dose(ss, plan, ROIS.bowel_bag.name, total_dose*0.95*100, 100) 
  OF.max_dose(ss, plan, ROIS.femoral_l.name, 45*100, 10)
  OF.max_dose(ss, plan, ROIS.femoral_r.name, 45*100, 10)
  OF.max_eud(ss, plan, ROIS.genitals.name, 25*100, 1, 5)
  OF.max_dose(ss, plan, ROIS.genitals.name, 45*100, 10)



# Bone/Spine SBRT
def create_bone_stereotactic_objectives(ss, plan, total_dose):
  OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 250)
  OF.fall_off(ss, plan, ROIS.x_ptv_ring_1.name, total_dose*100, 0.5*total_dose*100, 0.5, 5)
  OF.fall_off(ss, plan, ROIS.body.name, total_dose*100, 2*100, 2, 5)

  #OF.min_dose(ss, plan, ROIS.ptv.name, total_dose*100, 200)
  #OF.fall_off(ss, plan, ROIS.body.name, total_dose*106, 3*100, 3, 3)
  #OF.fall_off(ss, plan, ROIS.x_ptv_ring_1.name, total_dose*100, 0.65*total_dose*100, 0.5, 10)
