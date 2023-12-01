
# encoding: utf8
from __future__ import division
from tkinter import *
from tkinter import messagebox

# Import local files:
import roi as ROI
import rois as ROIS
import colors as COLORS
import gui_functions as GUIF
import structure_set_functions as SSF
import margin as MARGIN
import margins as MARGINS
import region_codes as RC
import roi_functions as ROIF
import patient_model_functions as PMF
import plan_functions as PF
import def_site as DS

def create_segmentation_oars(patient_db, pm, examination, ss, region_code, fraction_dose):
  site = DS.DefSite(patient_db, pm, examination, ss, [], targets = [], oars = [])
  if region_code in RC.brain_codes+RC.palliative_head_codes: # Brain 
    site.add_oars([ROIS.brain])
  elif region_code in RC.head_neck_codes: # Head and Neck
    site.add_oars([ROIS.mandible])
  elif region_code in RC.breast_codes: # Breast regional
    site.add_oars([ROIS.lung_l, ROIS.lung_r, ROIS.a_lad, ROIS.sternum])
    if region_code in RC.breast_reg_codes:
      site.add_oars([ROIS.spinal_canal, ROIS.thyroid, ROIS.trachea, ROIS.esophagus, ROIS.humeral_r, ROIS.humeral_l])
    if region_code in RC.breast_tang_reg_l_codes:
      if not SSF.has_named_roi_with_contours(ss, ROIS.breast_r.name):
        site.add_oars([ROIS.breast_r_contralat_draft, ROIS.breast_r])
    elif region_code in RC.breast_tang_reg_r_codes:
      site.add_oars([ROIS.liver])
      if not SSF.has_named_roi_with_contours(ss, ROIS.breast_l.name):
        site.add_oars([ROIS.breast_l_contralat_draft, ROIS.breast_l, ROIS.liver])
  elif region_code in RC.lung_and_mediastinum_codes or region_code in RC.palliative_thorax_codes+RC.palliative_thorax_and_abdomen_codes+RC.stereotactic_spine_thorax_codes: # Lung
    site.add_oars([ROIS.lung_l, ROIS.lung_r])
  elif region_code in RC.liver_codes: # Liver
    site.add_oars([ROIS.lung_l, ROIS.lung_r])
  elif region_code in RC.esophagus_codes:
    site.add_oars([ROIS.lung_l, ROIS.lung_r])
  elif region_code in RC.prostate_codes: # Prostate
    site.add_oars([ROIS.femoral_l, ROIS.femoral_r])
  elif region_code in RC.rectum_codes: # Rectum
    site.add_oars([ROIS.femoral_l, ROIS.femoral_r])
  elif region_code in RC.bladder_codes: # Bladder
    site.add_oars([ROIS.femoral_l, ROIS.femoral_r]) 
  elif region_code in RC.gyn_codes: # Gyneological
    site.add_oars([ROIS.femoral_l, ROIS.femoral_r])
  elif region_code in RC.palliative_pelvis_codes+RC.palliative_abdomen_and_pelvis_codes+RC.stereotactic_pelvis_codes:
    site.add_oars([ROIS.femoral_l, ROIS.femoral_r])
  site.create_rois()

# Create structures based on model based rois and contoured structures
def create_structures_for_plan(pm, examination, ss, region_code, fraction_dose, total_dose):
  if region_code in RC.brain_partial_codes: # Brain partial
    # Brain partial not stereotactic
    if fraction_dose < 6: 
      # Create "Brain-GTV" if it does not already exist
      if not PMF.has_roi(pm, ROIS.brain_gtv.name):
        brain_gtv = ROI.ROIAlgebra(ROIS.brain_gtv.name, ROIS.brain_gtv.type, ROIS.other_ptv.color, sourcesA = [ROIS.brain], sourcesB = [ROIS.gtv], operator = 'Subtraction')
        #PMF.delete_roi(pm, ROIS.brain_gtv.name)
        PMF.create_algebra_roi(pm, examination, ss, brain_gtv)
        roi_geometry = SSF.rg(ss, ROIS.brain_gtv.name)
        roi_geometry.OfRoi.UpdateDerivedGeometry(Examination = examination)
      # Create "Brain-PTV" if it does not already exist
      if not PMF.has_roi(pm, ROIS.brain_ptv.name):
        brain_ptv = ROI.ROIAlgebra(ROIS.brain_ptv.name, ROIS.brain_ptv.type, ROIS.other_ptv.color, sourcesA = [ROIS.brain], sourcesB = [ROIS.ptv], operator = 'Subtraction')
        #PMF.delete_roi(pm, ROIS.brain_ptv.name)
        PMF.create_algebra_roi(pm, examination, ss, brain_ptv)
        roi_geometry = SSF.rg(ss, ROIS.brain_ptv.name)
        roi_geometry.OfRoi.UpdateDerivedGeometry(Examination = examination)
      # Create "zMask" 
      create_z_mask(pm, examination, ss, region_code, fraction_dose, total_dose)
    else: # Brain stereotactic MULIGHET FOR FLERE PTV HER?
      brain_ptv = ROI.ROIAlgebra(ROIS.brain_ptv.name, ROIS.brain_ptv.type, ROIS.other_ptv.color, sourcesA = [ROIS.brain], sourcesB = [ROIS.ptv], operator = 'Subtraction')
      if not SSF.has_named_roi_with_contours(ss, ROIS.brain_ptv.name):
        PMF.delete_roi(pm, ROIS.brain_ptv.name)
        PMF.create_algebra_roi(pm, examination, ss, brain_ptv)
        roi_geometry = SSF.rg(ss, ROIS.brain_ptv.name)
        roi_geometry.OfRoi.UpdateDerivedGeometry(Examination = examination)
      create_z_mask(pm, examination, ss, region_code, fraction_dose, total_dose)
  elif region_code in RC.esophagus_codes: #ESOPHAGUS
    if not SSF.has_named_roi_with_contours(ss, ROIS.lungs.name):
      lungs = ROI.ROIAlgebra(ROIS.lungs.name, ROIS.lungs.type, COLORS.lungs, sourcesA = [ROIS.lung_r ], sourcesB = [ROIS.lung_l])
      PMF.create_algebra_roi(pm, examination, ss, lungs)
  elif region_code in RC.liver_codes: #LIVER
    if not SSF.has_named_roi_with_contours(ss, ROIS.lungs.name):
      lungs = ROI.ROIAlgebra(ROIS.lungs.name, ROIS.lungs.type, COLORS.lungs, sourcesA = [ROIS.lung_r ], sourcesB = [ROIS.lung_l])
      PMF.create_algebra_roi(pm, examination, ss, lungs)
    if not SSF.has_named_roi_with_contours(ss, ROIS.chestwall.name):
      create_chestwall(pm, examination, ss, 2)
    if not SSF.has_named_roi_with_contours(ss, ROIS.z_mask.name):
      z_mask = ROI.ROIAlgebra(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, sourcesA=[ROIS.liver], sourcesB=[ROIS.chestwall], operator = 'Subtraction',marginsA = MARGINS.uniform_5mm_expansion, marginsB = MARGINS.zero)
      PMF.delete_roi(pm, ROIS.z_mask.name)
      PMF.create_algebra_roi(pm, examination, ss, z_mask)

  elif region_code in RC.palliative_thorax_codes+RC.stereotactic_thorax_codes+RC.palliative_thorax_and_abdomen_codes: # Palliative thorax
    lungs = ROI.ROIAlgebra(ROIS.lungs.name, ROIS.lungs.type, COLORS.lungs, sourcesA = [ROIS.lung_r ], sourcesB = [ROIS.lung_l])
    if not SSF.has_named_roi_with_contours(ss, ROIS.lungs.name):
      PMF.create_algebra_roi(pm, examination, ss, lungs)
    if region_code in RC.stereotactic_thorax_codes and fraction_dose > 8: # bare not spine her kanskje?
      #messagebox.showinfo("", "hei")
      if not SSF.has_named_roi_with_contours(ss, ROIS.chestwall.name):
        create_chestwall(pm, examination, ss, 2)
  elif region_code in RC.lung_and_mediastinum_codes: # LUNG
    # Create "Lungs-IGTV" if it does not already exist
    if not SSF.has_named_roi_with_contours(ss, ROIS.lungs_igtv.name):
      create_lungs_igtv_for_lung(pm, examination, ss)
    # Create "xPTV_lunge" og "xPTV_vev" if it does not already exist 
    if SSF.has_roi_with_shape(ss, ROIS.ptv.name) and not PF.is_stereotactic(total_dose/fraction_dose, fraction_dose):
      if not SSF.has_roi_with_shape(ss, ROIS.x_ptv_lunge.name):
        if not SSF.has_roi_with_shape(ss, ROIS.x_ptv_vev.name):
          #messagebox.showinfo("", "hei")
          create_x_ptv_vev_and_x_ptv_lunge(pm, examination, ss)
        
    if total_dose > 40:
      # Create "xSpinalCanal" if it does not already exist
      if not SSF.has_named_roi_with_contours(ss, ROIS.x_spinal_canal.name): 
        PMF.create_expanded_roi(pm, examination, ss, ROIS.x_spinal_canal)
      if not SSF.has_named_roi_with_contours(ss, ROIS.x_trachea_bronchus.name) and SSF.has_named_roi_with_contours(ss, ROIS.trachea.name) and not PF.is_stereotactic(total_dose/fraction_dose, fraction_dose):
        if SSF.has_one_of_named_roi_with_contours(ss, [ROIS.bronchus.name, ROIS.main_bronchus_r.name, ROIS.main_bronchus_l.name, ROIS.bronchus_l.name, ROIS.bronchus_r.name]):
          x_trachea_bronchus = ROI.ROIAlgebra(ROIS.x_trachea_bronchus.name, ROIS.x_trachea_bronchus.type, ROIS.x_trachea_bronchus.color, sourcesA = [ROIS.trachea],
                                              sourcesB = [SSF.return_named_roi_with_contours(ss, [ROIS.bronchus, ROIS.main_bronchus_r, ROIS.main_bronchus_l, ROIS.bronchus_l, ROIS.bronchus_r])],marginsA = MARGINS.zero, marginsB = MARGINS.zero)
          PMF.delete_roi(pm, ROIS.x_trachea_bronchus.name)
          PMF.create_algebra_roi(pm, examination, ss, x_trachea_bronchus)
      if not PF.is_stereotactic(total_dose/fraction_dose, fraction_dose):
        create_z_kontroll_for_lung(pm, examination, ss)
      elif PF.is_stereotactic(total_dose/fraction_dose, fraction_dose):
        if not SSF.has_named_roi_with_contours(ss, ROIS.chestwall.name):
          create_chestwall(pm, examination, ss, 2)
      if not SSF.has_named_roi_with_contours(ss, ROIS.z_mask.name):
        create_z_mask(pm, examination, ss, region_code, fraction_dose, total_dose)


def create_lungs_igtv_for_lung(pm, examination, ss):
  igtv_n = [ROIS.igtv_n1, ROIS.igtv_n2,ROIS.igtv_n3,ROIS.igtv_n4,ROIS.igtv_n5,ROIS.igtv_n6, ROIS.igtv2,ROIS.igtv3]
  if SSF.has_one_of_named_roi_with_contours(ss, [ROIS.igtv_p.name,ROIS.igtv.name,ROIS.igtv1.name]) and SSF.has_named_roi_with_contours(ss, ROIS.lung_l.name) and SSF.has_named_roi_with_contours(ss, ROIS.lung_r.name):
    lungs_igtv = ROI.ROIAlgebra(ROIS.lungs_igtv.name, ROIS.lungs_igtv.type, COLORS.lungs, sourcesA = [ROIS.lung_r, ROIS.lung_l], sourcesB = [SSF.return_named_roi_with_contours(ss, [ROIS.igtv_p, ROIS.igtv, ROIS.igtv1])], operator='Subtraction')
    lung_r_igtv = ROI.ROIAlgebra(ROIS.lung_r_igtv.name, ROIS.lung_r_igtv.type, ROIS.lung_r_igtv.color, sourcesA = [ROIS.lung_r], sourcesB = [SSF.return_named_roi_with_contours(ss, [ROIS.igtv_p, ROIS.igtv, ROIS.igtv1])], operator='Subtraction')
    lung_l_igtv = ROI.ROIAlgebra(ROIS.lung_l_igtv.name, ROIS.lung_l_igtv.type, ROIS.lung_l_igtv.color, sourcesA = [ROIS.lung_l], sourcesB = [SSF.return_named_roi_with_contours(ss, [ROIS.igtv_p, ROIS.igtv, ROIS.igtv1])], operator='Subtraction')
    has_gtv = False
    for g in igtv_n:
      if SSF.has_roi_with_shape(ss, g.name):
        lungs_igtv.sourcesB.extend([g])
        lung_r_igtv.sourcesB.extend([g])
        lung_l_igtv.sourcesB.extend([g])

    if not SSF.has_named_roi_with_contours(ss, ROIS.lung_r_igtv.name):
      PMF.create_algebra_roi(pm, examination, ss, lung_r_igtv)
    if not SSF.has_named_roi_with_contours(ss, ROIS.lung_l_igtv.name):
      PMF.create_algebra_roi(pm, examination, ss, lung_l_igtv)
    PMF.delete_roi(pm, ROIS.lung_l.name)
    PMF.delete_roi(pm, ROIS.lung_r.name)
    pm.RegionsOfInterest[ROIS.lung_l_igtv.name].Name = ROIS.lung_l.name
    pm.RegionsOfInterest[ROIS.lung_r_igtv.name].Name = ROIS.lung_r.name
    PMF.delete_roi(pm,  ROIS.lungs_igtv.name)
    if not SSF.has_named_roi_with_contours(ss, ROIS.lungs_igtv.name):
      PMF.create_algebra_roi(pm, examination, ss, lungs_igtv)
  if not SSF.has_named_roi_with_contours(ss, ROIS.lungs_gtv.name):
    #messagebox.showinfo("", "hei")
    if SSF.has_named_roi_with_contours(ss, ROIS.gtv.name):
      
      lungs_gtv = ROI.ROIAlgebra(ROIS.lungs_gtv.name, ROIS.lungs_gtv.type, COLORS.lungs, sourcesA = [ROIS.lung_r, ROIS.lung_l], sourcesB = [ROIS.gtv], operator='Subtraction')
      lung_r_gtv = ROI.ROIAlgebra(ROIS.lung_r_gtv.name, ROIS.lung_r_gtv.type, ROIS.lung_r_gtv.color, sourcesA = [ROIS.lung_r], sourcesB = [ROIS.gtv], operator='Subtraction')
      lung_l_gtv = ROI.ROIAlgebra(ROIS.lung_l_gtv.name, ROIS.lung_l_gtv.type, ROIS.lung_l_gtv.color, sourcesA = [ROIS.lung_l], sourcesB = [ROIS.gtv], operator='Subtraction')
      if not SSF.has_named_roi_with_contours(ss, ROIS.lung_r_gtv.name):
        PMF.create_algebra_roi(pm, examination, ss, lung_r_gtv)
      if not SSF.has_named_roi_with_contours(ss, ROIS.lung_l_gtv.name):
        PMF.create_algebra_roi(pm, examination, ss, lung_l_gtv)
      PMF.delete_roi(pm, ROIS.lung_l.name)
      PMF.delete_roi(pm, ROIS.lung_r.name)
      pm.RegionsOfInterest[ROIS.lung_l_gtv.name].Name = ROIS.lung_l.name
      pm.RegionsOfInterest[ROIS.lung_r_gtv.name].Name = ROIS.lung_r.name
      PMF.create_algebra_roi(pm, examination, ss, lungs_gtv)

def create_x_ptv_vev_and_x_ptv_lunge(pm, examination, ss):
  # Create "xPTV_lunge" if it does not already exist
  if not SSF.has_named_roi_with_contours(ss, ROIS.x_ptv_lunge.name):
    #messagebox.showinfo("", "hei2")
    if SSF.has_roi_with_shape(ss, ROIS.ptv.name):
      if SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
        x_ptv_lunge = ROI.ROIAlgebra(ROIS.x_ptv_lunge.name, ROIS.x_ptv_lunge.type, ROIS.x_ptv_lunge.color, sourcesA = [ROIS.ptv], sourcesB = [ROIS.lungs_igtv], operator = 'Intersection',marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        PMF.create_algebra_roi(pm, examination, ss, x_ptv_lunge)
      elif SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
        x_ptv_lunge = ROI.ROIAlgebra(ROIS.x_ptv_lunge.name, ROIS.x_ptv_lunge.type, ROIS.x_ptv_lunge.color, sourcesA = [ROIS.ptv], sourcesB = [ROIS.lungs_gtv], operator = 'Intersection',marginsA = MARGINS.zero, marginsB = MARGINS.zero)
        PMF.create_algebra_roi(pm, examination, ss, x_ptv_lunge)
      else:
        GUIF.handle_missing_roi_for_derived_rois(ROIS.x_ptv_lunge.name, ROIS.lungs_igtv.name)
    else:
      GUIF.handle_missing_roi_for_derived_rois(ROIS.ptv.name, ROIS.lungs_igtv.name)
  # Create "xPTV_vev" if it does not already exist
  if not SSF.has_named_roi_with_contours(ss, ROIS.x_ptv_vev.name) and SSF.has_named_roi_with_contours(ss, ROIS.x_ptv_lunge.name):
    x_ptv_vev = ROI.ROIAlgebra(ROIS.x_ptv_vev.name, ROIS.x_ptv_vev.type, ROIS.x_ptv_vev.color, sourcesA = [ROIS.ptv], sourcesB = [x_ptv_lunge], operator = 'Subtraction',marginsA = MARGINS.zero, marginsB = MARGINS.zero)
    PMF.create_algebra_roi(pm, examination, ss, x_ptv_vev)


def create_z_kontroll_for_lung(pm, examination, ss):
  if SSF.has_named_roi_with_contours(ss, ROIS.ptv.name):
    if ss.RoiGeometries[ROIS.ptv.name].OfRoi.DerivedRoiExpression:
      if ss.RoiGeometries[ROIS.ptv.name].OfRoi.DerivedRoiExpression.RightDistance == 0:
        m = ss.RoiGeometries[ROIS.ptv.name].OfRoi.DerivedRoiExpression.Children[0].Children[0].RightDistance - 0.1
      else:
        m = ss.RoiGeometries[ROIS.ptv.name].OfRoi.DerivedRoiExpression.RightDistance - 0.1
    else:
      m = 0.5
  #messagebox.showinfo("", str(m))
  target_alternatives = []
  # If there exists a ICTV
  if SSF.has_one_of_named_roi_with_contours(ss, [ROIS.ictv_n.name,ROIS.ictv_p.name, ROIS.ictv_n1.name, ROIS.ictv_n2.name,ROIS.ictv_n3.name,ROIS.ictv_n4.name,ROIS.ictv_n5.name,ROIS.ictv_n6.name]):
    target_alternatives = [ROIS.ictv_n, ROIS.ictv_p, ROIS.ictv_n1, ROIS.ictv_n2,ROIS.ictv_n3,ROIS.ictv_n4,ROIS.ictv_n5,ROIS.ictv_n6]
  elif not SSF.has_one_of_named_roi_with_contours(ss, [ROIS.ictv_n.name,ROIS.ictv_p.name]) and SSF.has_named_roi_with_contours(ss, ROIS.ictv.name):
    target_alternatives = [ROIS.ictv]
  if len(target_alternatives)>0:
    lung_targets = []
    for i in range(len(target_alternatives)):
      if SSF.has_named_roi_with_contours(ss, target_alternatives[i].name):
        PMF.delete_roi(pm, ROIS.temp_target_lung.name)
        # Create a temporary expansion ROI with margin 0.1 cm less than the PTV margin
        expanded_roi= ROI.ROIExpanded(ROIS.temp_target_lung.name, ROIS.temp_target_lung.type, ROIS.temp_target_lung.color,
                                  source = target_alternatives[i], margins = MARGINS.MARGIN.Expansion(2, 2, 2, 2, 2, 2) )
        PMF.create_expanded_roi(pm, examination, ss, expanded_roi)
        #ss.RoiGeometries[ROIS.temp_target_lung.name].SetRepresentation(Representation = 'Contours') # Voxels
        #if ROIF.roi_vicinity_approximate(SSF.rg(ss, ROIS.temp_target_lung.name), SSF.rg(ss, ROIS.x_trachea_bronchus.name), 2):
        if SSF.roi_overlap(pm, examination, ss, ROIS.temp_target_lung, ROIS.x_trachea_bronchus, 2):
          lung_targets.extend([target_alternatives[i]])
          PMF.delete_roi(pm, ROIS.temp_target_lung.name)

    PMF.delete_roi(pm, ROIS.temp_target_lung.name)
    if len(lung_targets) >0:
      # Create a "zBox" which starts in the upper slice where there is a "ICTVn"[ROIS.ictv_n1, ROIS.ictv_n2,ROIS.ictv_n3,ROIS.ictv_n4,ROIS.ictv_n5,ROIS.ictv_n6, ROIS.ictv_n]
      PMF.create_bounding_box_z_from_rois(pm, ss, examination, ROIS.body, ROIS.box, lung_targets, m)
      # Create a grey value ROI with a upper and lower HU and intersect with "Bronchus" and "Trachea"
      PMF.create_grey_value_intersection_roi(pm, ss,examination,  ROIS.z_temp_grey_level, [ROIS.x_trachea_bronchus], ROIS.z_temp_grey_level_and_oars , -1024, -530)
      #PMF.create_grey_value_intersection_roi(pm, ss,examination,  ROIS.z_temp_grey_level, [ROIS.trachea, ROIS.bronchus], ROIS.z_temp_grey_level_and_oars , -1024, -530)
      # Create the "zKontroll"-object which is a intersection between the grey value ROI and the Box
      if SSF.has_named_roi_with_contours(ss, ROIS.z_temp_grey_level_and_oars.name) and SSF.has_named_roi_with_contours(ss, ROIS.box.name):
        intersection = ROI.ROIAlgebra(ROIS.z_kontroll.name, ROIS.z_kontroll.type, ROIS.z_kontroll.color,
                              sourcesA = [ROIS.z_temp_grey_level_and_oars], sourcesB = [ROIS.box],operator = 'Intersection',marginsA = MARGINS.MARGIN.Expansion(0, 0, m, m, m, m) , marginsB = MARGINS.zero)                                     
        # Delete "zKontroll" if it exists
        PMF.delete_roi(pm, intersection.name)
        # Create "zKontroll" in RayStation
        PMF.create_algebra_roi(pm, examination, ss, intersection)
    # Delete "zBox"
    PMF.delete_roi(pm, ROIS.box.name)
    # Delete the grey value ROI 
    PMF.delete_roi(pm, ROIS.z_temp_grey_level_and_oars.name)

def create_z_mask(pm, examination, ss, region_code, fraction_dose, total_dose):
  if not SSF.has_named_roi_with_contours(ss, ROIS.z_mask.name):
    if PF.is_stereotactic(total_dose/fraction_dose, fraction_dose) and region_code in RC.lung_and_mediastinum_codes:
      z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, ROIS.ptv, margins = MARGINS.zero)
      PMF.delete_roi(pm, ROIS.z_mask.name)
      PMF.create_expanded_roi(pm, examination, ss, z_mask)
    if SSF.has_named_roi_with_contours(ss, ROIS.brain.name):
      # Delete "zMask" if it exists
      if SSF.has_named_roi_with_contours(ss, ROIS.z_mask.name):
        if ss.RoiGeometries[ROIS.z_mask.name].OfRoi.DerivedRoiExpression:
          PMF.delete_roi(pm, ROIS.z_mask.name)
          z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, ROIS.brain, margins = MARGINS.z_mask_for_brain_expansion)
          PMF.create_expanded_roi(pm, examination, ss, z_mask)
      else:
        z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, ROIS.brain, margins = MARGINS.z_mask_for_brain_expansion)
        PMF.create_expanded_roi(pm, examination, ss, z_mask)
    # Create "zMask" which is a union of the "zKontroll" and the "ICTVp"/"ICTV SKAL VI HA ICTV KUN HVIS ICTVP IKKE EKSISTERER??????"
    elif SSF.has_one_of_named_roi_with_contours(ss, [ROIS.ictv_p.name, ROIS.ictv.name]) and SSF.has_named_roi_with_contours(ss, ROIS.z_kontroll.name):
      z_mask = ROI.ROIAlgebra(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, sourcesA = [ROIS.z_kontroll], sourcesB = [SSF.return_named_roi_with_contours(ss, [ROIS.ictv_p, ROIS.ictv])],marginsA = MARGINS.zero, marginsB = MARGINS.zero)
      # Delete "zMask" if it exists
      PMF.delete_roi(pm, ROIS.z_mask.name)
      # Create "zMask" in RayStation
      PMF.create_algebra_roi(pm, examination, ss, z_mask)
    elif SSF.has_one_of_named_roi_with_contours(ss, [ROIS.ictv_p.name, ROIS.ictv.name]): # If the zKontroll is not set up, use only ICTVp/ICTV ???????
      z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, SSF.return_named_roi_with_contours(ss, [ROIS.ictv_p, ROIS.ictv]), margins = MARGINS.zero)
      # Delete "zMask" if it exists
      PMF.delete_roi(pm, ROIS.z_mask.name)
      # Create "zMask" in RayStation
      PMF.create_expanded_roi(pm, examination, ss, z_mask)
    elif SSF.has_roi_with_shape(ss, ROIS.igtv.name):
      z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, ROIS.igtv, margins = MARGINS.zero)
      #z_mask = ROI.ROIAlgebra(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, sourcesA = [intersection], sourcesB = [ROIS.igtv],marginsA = MARGINS.zero, marginsB = MARGINS.zero)     
      # Delete "zMask" if it exists
      PMF.delete_roi(pm, ROIS.z_mask.name)
      # Create "zMask" in RayStation
      PMF.create_expanded_roi(pm, examination, ss, z_mask)
    if SSF.has_named_roi_with_contours(ss, ROIS.z_mask.name):
      roi_geometry = SSF.rg(ss, ROIS.z_mask.name)
      roi_geometry.OfRoi.UpdateDerivedGeometry(Examination = examination)
'''
def create_z_mask(pm, examination, ss):
  if not SSF.has_named_roi_with_contours(ss, ROIS.z_mask.name):
    if SSF.has_named_roi_with_contours(ss, ROIS.brain.name):
      # Delete "zMask" if it exists
      if SSF.has_named_roi_with_contours(ss, ROIS.z_mask.name):
        if ss.RoiGeometries[ROIS.z_mask.name].OfRoi.DerivedRoiExpression:
          PMF.delete_roi(pm, ROIS.z_mask.name)
          z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, ROIS.brain, margins = MARGINS.z_mask_for_brain_expansion)
          PMF.create_expanded_roi(pm, examination, ss, z_mask)
      else:
        z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, ROIS.brain, margins = MARGINS.z_mask_for_brain_expansion)
        PMF.create_expanded_roi(pm, examination, ss, z_mask)
    # Create "zMask" which is a union of the "zKontroll" and the "ICTVp"/"ICTV SKAL VI HA ICTV KUN HVIS ICTVP IKKE EKSISTERER??????"
    elif SSF.has_one_of_named_roi_with_contours(ss, [ROIS.ictv_p.name, ROIS.ictv.name]) and SSF.has_named_roi_with_contours(ss, ROIS.z_kontroll.name):
      z_mask = ROI.ROIAlgebra(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, sourcesA = [ROIS.z_kontroll], sourcesB = [SSF.return_named_roi_with_contours(ss, [ROIS.ictv_p, ROIS.ictv])],marginsA = MARGINS.zero, marginsB = MARGINS.zero)
      # Delete "zMask" if it exists
      PMF.delete_roi(pm, ROIS.z_mask.name)
      # Create "zMask" in RayStation
      PMF.create_algebra_roi(pm, examination, ss, z_mask)
    elif SSF.has_one_of_named_roi_with_contours(ss, [ROIS.ictv_p.name, ROIS.ictv.name]): # If the zKontroll is not set up, use only ICTVp/ICTV ???????
      z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, SSF.return_named_roi_with_contours(ss, [ROIS.ictv_p, ROIS.ictv]), margins = MARGINS.zero)
      # Delete "zMask" if it exists
      PMF.delete_roi(pm, ROIS.z_mask.name)
      # Create "zMask" in RayStation
      PMF.create_expanded_roi(pm, examination, ss, z_mask)
    elif SSF.has_roi_with_shape(ss, ROIS.igtv.name):
      z_mask = ROI.ROIExpanded(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, ROIS.igtv, margins = MARGINS.zero)
      #z_mask = ROI.ROIAlgebra(ROIS.z_mask.name, ROIS.z_mask.type, ROIS.z_mask.color, sourcesA = [intersection], sourcesB = [ROIS.igtv],marginsA = MARGINS.zero, marginsB = MARGINS.zero)     
      # Delete "zMask" if it exists
      PMF.delete_roi(pm, ROIS.z_mask.name)
      # Create "zMask" in RayStation
      PMF.create_expanded_roi(pm, examination, ss, z_mask)
    if SSF.has_named_roi_with_contours(ss, ROIS.z_mask.name):
      roi_geometry = SSF.rg(ss, ROIS.z_mask.name)
      roi_geometry.OfRoi.UpdateDerivedGeometry(Examination = examination)
'''
def create_chestwall(pm, examination, ss, cw_m):
  source_roi = ROIS.heart
  if not SSF.has_one_of_roi_with_contours(ss, [ROIS.lungs, ROIS.lungs_igtv, ROIS.lungs_gtv]) and SSF.has_roi_with_shape(ss, ROIS.lung_r.name) and SSF.has_roi_with_shape(ss, ROIS.lung_l.name):
    PMF.create_algebra_roi(pm, examination, ss, ROIS.lungs)

  source_roi_2 = SSF.return_named_roi_with_contours(ss, [ROIS.lungs, ROIS.lungs_igtv, ROIS.lungs_gtv])
  if not SSF.has_one_of_roi_with_contours(ss, [ROIS.spinal_canal, ROIS.spinal_cord, ROIS.trachea,  ROIS.esophagus]):
   messagebox.showinfo("", "SpinalCanal eller SpinalCord mangler!")
  source_roi_1 = SSF.return_named_roi_with_contours(ss, [ROIS.spinal_canal, ROIS.spinal_cord,ROIS.trachea,  ROIS.esophagus])
  grey_level_roi = ROIS.temp_chestwall
  temp_roi = ROIS.box_r
  temp_roi_2 = ROIS.y_chestwall
  temp_roi_3 = ROIS.box_l
  roi = ROIS.mediastinum
  PMF.delete_roi(pm, grey_level_roi.name)
  pm.CreateRoi(Name = grey_level_roi.name, Type = grey_level_roi.type, Color = grey_level_roi.color)
  ss.RoiGeometries[grey_level_roi.name].OfRoi.GrayLevelThreshold(Examination = examination, LowThreshold = -278, HighThreshold = 900)
  source_roi_box = ss.RoiGeometries[source_roi.name].GetBoundingBox()

  x_min = source_roi_box[0].x
  x_max = source_roi_box[1].x
  x = x_max - x_min
  y_min = source_roi_box[0].y 
  y_max = source_roi_box[1].y
  y = y_max - y_min
  z_min = source_roi_box[0].z
  z_max = source_roi_box[1].z
  z = z_max - z_min

  center_x = SSF.roi_center_x(ss, source_roi.name)
  center_y = SSF.roi_center_y(ss, source_roi.name)
  center_z = SSF.roi_center_z(ss, source_roi.name)

  source_roi_box_1 = ss.RoiGeometries[source_roi_1.name].GetBoundingBox()
  x_min = source_roi_box_1[0].x
  x_max = source_roi_box_1[1].x
  x_1 = x_max - x_min +2
  y_min = source_roi_box_1[0].y -30
  y_max = source_roi_box_1[1].y +4
  y_1 = y_max - y_min
  z_1 = source_roi_box_1[1].z - source_roi_box_1[0].z +30
  center_x_1 = SSF.roi_center_x(ss, source_roi_1.name)
  center_y_1 = SSF.roi_center_y(ss, source_roi_1.name)
  center_z_1 = SSF.roi_center_z(ss, source_roi_1.name)

  source_roi_box_2 = ss.RoiGeometries[source_roi_2.name].GetBoundingBox()
  x_2_min = source_roi_box_2[0].x
  x_2_max = source_roi_box_2[1].x
  x_2 = x_2_max - x_2_min 
  y_2_min = source_roi_box_2[0].y 
  y_2_max = source_roi_box_2[1].y 
  y_2 = y_2_max - y_2_min 
  z_2 = source_roi_box_2[1].z - source_roi_box[0].z
  z_2_center =source_roi_box_2[1].z - (z_2)/2
  center_x_2 = SSF.roi_center_x(ss, source_roi_2.name)
  center_y_2 = SSF.roi_center_y(ss, source_roi_2.name)
  center_z_2 = SSF.roi_center_z(ss, source_roi_2.name)

  PMF.delete_roi(pm, ROIS.box.name)
  box = pm.CreateRoi(Name = ROIS.box.name, Color = ROIS.box.color, Type = ROIS.box.type)
  pm.RegionsOfInterest[ROIS.box.name].CreateBoxGeometry(Size={ 'x': x, 'y': y, 'z': z}, Examination = examination, Center = { 'x': center_x, 'y': center_y, 'z': center_z })

  PMF.delete_roi(pm, ROIS.box1.name)
  box_1 = pm.CreateRoi(Name = ROIS.box1.name, Color = ROIS.box1.color, Type = ROIS.box1.type)
  pm.RegionsOfInterest[ROIS.box1.name].CreateBoxGeometry(Size={ 'x': x, 'y': y, 'z': z}, Examination = examination, Center = { 'x': center_x, 'y': center_y, 'z': z_max })

  PMF.delete_roi(pm, ROIS.box2.name)
  box_2 = pm.CreateRoi(Name = ROIS.box2.name, Color = ROIS.box2.color, Type = ROIS.box2.type)
  pm.RegionsOfInterest[ROIS.box2.name].CreateBoxGeometry(Size={ 'x': x, 'y': y, 'z': z+2}, Examination = examination, Center = { 'x': center_x, 'y': center_y, 'z': z_min })

  PMF.delete_roi(pm, ROIS.box3.name)
  box_3 = pm.CreateRoi(Name = ROIS.box3.name, Color = ROIS.box3.color, Type = ROIS.box3.type)
  pm.RegionsOfInterest[ROIS.box3.name].CreateBoxGeometry(Size={ 'x': x_1, 'y': y_1+10, 'z': z_1}, Examination = examination, Center = { 'x': center_x_1, 'y': center_y_1, 'z': center_z})

  if SSF.has_roi_with_shape(ss, ROIS.liver.name):
    source_roi_box_3 = ss.RoiGeometries[ROIS.liver.name].GetBoundingBox()
    z_min = source_roi_box_3[0].z
    z_2 = source_roi_box_2[1].z - source_roi_box_3[0].z
    z_2_center =source_roi_box_2[1].z - (z_2)/2
    
  PMF.delete_roi(pm, ROIS.box4.name)
  box_4 = pm.CreateRoi(Name = ROIS.box4.name, Color = ROIS.box4.color, Type = ROIS.box4.type)
  pm.RegionsOfInterest[ROIS.box4.name].CreateBoxGeometry(Size={ 'x': x_2+10, 'y': y_2+10, 'z': z_2}, Examination = examination, Center = { 'x': center_x_2, 'y': center_y_2, 'z':z_2_center })

  PMF.delete_roi(pm, ROIS.box5.name)
  box_5 = pm.CreateRoi(Name = ROIS.box5.name, Color = ROIS.box5.color, Type = ROIS.box5.type)
  pm.RegionsOfInterest[ROIS.box5.name].CreateBoxGeometry(Size={ 'x': x_2, 'y': y_2, 'z': z_2}, Examination = examination, Center = { 'x': center_x_2, 'y': center_y_2, 'z':center_z_2 })

  if SSF.has_one_of_roi_with_contours(ss, [ROIS.heart, ROIS.box3, ROIS.box2, ROIS.a_aorta, ROIS.x_a_aorta, ROIS.liver, ROIS.stomach, ROIS.bowel_small, ROIS.bowel_bag, ROIS.duodenum]):
    if SSF.has_roi_with_shape(ss, ROIS.a_aorta.name):
      a = ROIS.a_aorta
    elif SSF.has_roi_with_shape(ss, ROIS.x_a_aorta.name):
      a = ROIS.x_a_aorta
    elif SSF.has_roi_with_shape(ss, ROIS.great_vessels.name):
      a = ROIS.great_vessels
    elif SSF.has_roi_with_shape(ss, ROIS.great_vessel.name):
      a = ROIS.great_vessel
      
    if SSF.has_one_of_roi_with_contours(ss, [ROIS.a_aorta, ROIS.x_a_aorta, ROIS.great_vessels, ROIS.great_vessel]):
      aorta_margin = ROI.ROIExpanded('Aorta_PRV', 'Avoidance', COLORS.prv, source=a, margins=MARGINS.uniform_5mm_expansion)
      PMF.delete_roi(pm, aorta_margin.name)
      PMF.create_expanded_roi(pm, examination, ss, aorta_margin)
    else:
      aorta_margin = ''

    if SSF.has_roi_with_shape(ss, ROIS.liver.name):
      liver_margin = ROI.ROIExpanded('xLever', 'Avoidance', COLORS.prv, source=ROIS.liver, margins=MARGINS.liver_temp_expansion)
      PMF.delete_roi(pm, liver_margin.name)
      PMF.create_expanded_roi(pm, examination, ss, liver_margin)
    intersection = ROI.ROIAlgebra(roi.name, roi.type, roi.color, sourcesA =  SSF.return_all_named_rois_with_contours(ss,[ROIS.heart, ROIS.box3, ROIS.box2, ROIS.liver, ROIS.stomach, ROIS.bowel_small, ROIS.bowel_bag, ROIS.duodenum]), sourcesB = [source_roi_2], operator = 'Subtraction', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
    try:
      if SSF.has_roi_with_shape(ss, a.name):
        intersection.sourcesA.extend([aorta_margin])
    except:
      print("feil")
  if SSF.has_roi_with_shape(ss, ROIS.liver.name):
    intersection.sourcesA.extend([liver_margin])

  # LAGER midlertidig chest wall 
  # In the rare case that this ROI already exists, delete it (to avoid a crash):
  PMF.delete_roi(pm, intersection.name)
  PMF.create_algebra_roi(pm, examination, ss, intersection)
  ss.SimplifyContours(RoiNames = [ROIS.mediastinum.name], RemoveHoles3D = True, RemoveSmallContours = True, AreaThreshold = 2)
  #PMF.create_chestwall(pm, examination, ss, ROIS.temp_chestwall, ROIS.chestwall)
  wall = ROI.ROIAlgebra(temp_roi.name, temp_roi.type, temp_roi.color,
                                 sourcesA = [ROIS.lung_r, ROIS.lung_l], sourcesB = [ROIS.lung_r,ROIS.lung_l], operator = 'Subtraction', marginsA = MARGIN.Expansion(0, 0, 2, 2, 2, 2), marginsB = MARGINS.zero)
  if SSF.has_roi_with_shape(ss, ROIS.liver.name):
    wall.sourcesA.extend([ROIS.liver])
    wall.sourcesB.extend([ROIS.liver])
    #messagebox.showinfo("", "hei")
  PMF.delete_roi(pm, temp_roi_2.name)
  x_chestwall = ROI.ROIAlgebra(temp_roi_2.name, temp_roi_2.type, temp_roi_2.color,
                                 sourcesA = [wall], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero,marginsB = MARGINS.zero)
  PMF.delete_roi(pm, temp_roi_3.name)
  x_chestwall_1 = ROI.ROIAlgebra(temp_roi_3.name, temp_roi_3.type, temp_roi_3.color,
                                 sourcesA = [x_chestwall], sourcesB = [ROIS.box4], operator = 'Intersection', marginsA = MARGINS.zero,marginsB = MARGINS.zero)
  print("-----------------------------------"+str(SSF.return_all_named_rois_with_contours(ss, [roi, ROIS.igtv, ROIS.igtv_p, ROIS.igtv_n, ROIS.gtv, ROIS.igtv1, ROIS.igtv2, ROIS.igtv3, ROIS.gtv1, ROIS.gtv2, ROIS.gtv3])))
  chest_wall = ROI.ROIAlgebra(ROIS.chestwall.name, ROIS.chestwall.type, ROIS.chestwall.color, operator = 'Subtraction',sourcesA = [x_chestwall_1],
                              sourcesB = SSF.return_all_named_rois_with_contours(ss, [roi, ROIS.igtv, ROIS.igtv_p, ROIS.igtv_n, ROIS.gtv,ROIS.igtv1, ROIS.igtv2, ROIS.igtv3, ROIS.gtv1, ROIS.gtv2, ROIS.gtv3]))
  print("-----------------------------------")

  PMF.delete_roi(pm, grey_level_roi.name)
  pm.CreateRoi(Name = grey_level_roi.name, Type = grey_level_roi.type, Color = grey_level_roi.color)
  ss.RoiGeometries[grey_level_roi.name].OfRoi.GrayLevelThreshold(Examination = examination, LowThreshold = 100, HighThreshold = 900)
  ribs = ROI.ROIAlgebra(ROIS.ribs.name, ROIS.ribs.type, ROIS.ribs.color, sourcesA = [chest_wall], sourcesB = [grey_level_roi], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
  PMF.delete_roi(pm, ROIS.bone.name)
  rib_roi = pm.CreateRoi(Name=ROIS.bone.name, Color="Green", Type="Organ", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
  rib_roi.BoneSegmentationByRegionGrowing(ExaminationName=examination.Name, DelimitingRoiGeometryName=ROIS.body.name, BoneSeedThreshold=150, TissueSeedThreshold=50)

  PMF.delete_roi(pm, wall.name)
  PMF.create_algebra_roi(pm, examination, ss, wall)
  PMF.delete_roi(pm, x_chestwall.name)
  PMF.create_algebra_roi(pm, examination, ss, x_chestwall)
  PMF.delete_roi(pm, x_chestwall_1.name)
  PMF.create_algebra_roi(pm, examination, ss, x_chestwall_1)
  PMF.delete_roi(pm, chest_wall.name)
  PMF.create_algebra_roi(pm, examination, ss, chest_wall)
  #messagebox.showinfo("", "Vil du virkelig slette Ribs? Hvis ikke, avbryt skriptet")
  PMF.delete_roi(pm, ROIS.ribs.name) 
  PMF.create_algebra_roi(pm, examination, ss, ribs)
  PMF.delete_roi(pm, grey_level_roi.name)
  ss.SimplifyContours(RoiNames = [ROIS.ribs.name], RemoveHoles3D = True, RemoveSmallContours = True, AreaThreshold = 1)
  PMF.delete_roi(pm, ROIS.bone.name)

  # LAGER CHESTWALL
  wall = ROI.ROIAlgebra(temp_roi.name, temp_roi.type, temp_roi.color,
                                 sourcesA = [ROIS.lung_r, ROIS.lung_l], sourcesB = [ROIS.lung_r, ROIS.lung_l], operator = 'Subtraction', marginsA = MARGIN.Expansion(0, 0, cw_m, cw_m, cw_m, cw_m), marginsB = MARGINS.zero)
  if SSF.has_roi_with_shape(ss, ROIS.liver.name):
    wall.sourcesA.extend([ROIS.liver])
    wall.sourcesB.extend([ROIS.liver])
    #messagebox.showinfo("", "hei")
  PMF.delete_roi(pm, temp_roi_2.name)
  x_chestwall = ROI.ROIAlgebra(temp_roi_2.name, temp_roi_2.type, temp_roi_2.color,
                                 sourcesA = [wall], sourcesB = [ROIS.body], operator = 'Intersection', marginsA = MARGINS.zero, marginsB = MARGINS.zero)
  PMF.delete_roi(pm, temp_roi_3.name)
  x_chestwall_1 = ROI.ROIAlgebra(temp_roi_3.name, temp_roi_3.type, temp_roi_3.color,
                                 sourcesA = [x_chestwall], sourcesB = [ROIS.box4], operator = 'Intersection', marginsA = MARGINS.zero,marginsB = MARGINS.zero)

  chest_wall = ROI.ROIAlgebra(ROIS.chestwall.name, ROIS.chestwall.type, ROIS.chestwall.color, operator = 'Subtraction',sourcesA = [x_chestwall_1],
                              sourcesB = SSF.return_all_named_rois_with_contours(ss, [roi, ROIS.igtv, ROIS.igtv_p, ROIS.igtv_n, ROIS.gtv,ROIS.igtv1, ROIS.igtv2, ROIS.igtv3, ROIS.gtv1, ROIS.gtv2, ROIS.gtv3]))

  PMF.delete_roi(pm, wall.name)
  PMF.create_algebra_roi(pm, examination, ss, wall)
  PMF.delete_roi(pm, x_chestwall.name)
  PMF.create_algebra_roi(pm, examination, ss, x_chestwall)
  PMF.delete_roi(pm, x_chestwall_1.name)
  PMF.create_algebra_roi(pm, examination, ss, x_chestwall_1)
  PMF.delete_roi(pm, chest_wall.name)
  PMF.create_algebra_roi(pm, examination, ss, chest_wall)
  ss.SimplifyContours(RoiNames = [ROIS.chestwall.name], RemoveHoles3D = True, RemoveSmallContours = True, AreaThreshold = 5)

  PMF.delete_roi(pm, ROIS.box.name)
  PMF.delete_roi(pm, ROIS.box1.name)
  PMF.delete_roi(pm, ROIS.box2.name)
  PMF.delete_roi(pm, ROIS.box3.name)
  PMF.delete_roi(pm, ROIS.box4.name)
  PMF.delete_roi(pm, ROIS.box5.name)
  PMF.delete_roi(pm, intersection.name)
  PMF.delete_roi(pm, wall.name)
  PMF.delete_roi(pm, x_chestwall.name)
  PMF.delete_roi(pm, x_chestwall_1.name)
  PMF.delete_roi(pm, roi.name)
  PMF.delete_roi(pm, grey_level_roi.name)
  if SSF.has_one_of_roi_with_contours(ss, [ROIS.a_aorta, ROIS.x_a_aorta, ROIS.great_vessels, ROIS.great_vessel]):
    PMF.delete_roi(pm, aorta_margin.name)
  if SSF.has_roi_with_shape(ss, ROIS.liver.name):
    PMF.delete_roi(pm, liver_margin.name)


  
