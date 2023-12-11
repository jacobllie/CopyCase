'''
# Import local files:
import beams as BEAMS
import beam_optimization_settings as BOS
import beam_set_functions as BSF
import clinical_goal as CG
import fractionation_frame as FORM
#import general_functions as GF
import gui_functions as GUIF
import margin as MARGIN
import region_codes as RC
import region_list as REGIONS
import roi as ROI
import roi_functions as ROIF
import rois as ROIS
import site_functions as SF
import ts_case as TS_C
import raystation_utilities as RSU
import create_rois_plan as RP
'''
from tkinter import *
from tkinter import messagebox
# Load plan
import rois as ROIS
import structure_set_functions as SSF
import beam_set_functions as BSF
import case_functions as CF
import objective_functions as OBJF
import patient_model_functions as PMF
import plan_functions as PF
import region_codes as RC

def create_volumes_and_settings_for_robust_breast_plan( clinic_db, patient_db, patient, case, pm, ss, plan, beam_set,  examination, isocenter, technique, region_code):
  # List of potential match volumes:
  match_volumes = [ROIS.z_match, ROIS.z_match_r, ROIS.z_match_l, ROIS.z_match_sternum]
  # List of potential density volumes:
  density_volumes = [ROIS.x_tetthetsvolum, ROIS.x_tetthetsvolum_r, ROIS.x_tetthetsvolum_l, ROIS.x_tetthetsvolum_sternum]
  density_volume_names = [ROIS.x_tetthetsvolum.name, ROIS.x_tetthetsvolum_r.name, ROIS.x_tetthetsvolum_l.name, ROIS.x_tetthetsvolum_sternum.name]
  # New examination name
  new_examination_name = "CT-Robust"
  # Breast "full" VMAT
  if technique == 'VMAT':
    # Create sternum box if bilateral tangential or breast regional
    if PMF.has_roi(pm, ROIS.z_match_r.name) and PMF.has_roi(pm, ROIS.z_match_l.name) or region_code in RC.breast_reg_codes:
      PMF.create_sternum_box_and_external(pm, examination, ss, region_code, ROIS.sternum, SSF.return_named_roi_with_contours(ss, [ROIS.x_ptv, ROIS.x_ptv_r, ROIS.x_ptv_l,ROIS.ptv_pc_l, ROIS.ptv_pc_r, ROIS.ctv]), ROIS.body, ROIS.box1, ROIS.sternum_box)
      # Create zMatch_Sternum if bilateral breast
      if PMF.has_roi(pm, ROIS.z_match_r.name) and PMF.has_roi(pm, ROIS.z_match_l.name): 
        PMF.create_match_volume_10mm(pm, ss, examination, ROIS.z_match_sternum, ROIS.sternum_box, ROIS.body)
    #messagebox.showinfo("", "før ct eksportteres")
    # Fix RBE cell type, this is a bugfix because some volumes got an (1),(2) behind the name when importing the "CT-Robust"-series
    CF.fix_rbe_cell_type(pm)

    PMF.change_type_before_export(pm, ss, region_code)
    # Export and import current CT examination, the new examination name is set
    CF.export_and_import_ct_study(clinic_db, patient_db, patient, case, examination, "C:/temp/tempexport/", "111111 11111", "Robust", new_examination_name, "CT130083")
    #messagebox.showinfo("", "etter ct eksportteres")
    PMF.change_type_after_export(pm, ss, region_code)
    if not PMF.is_approved_roi_structure_in_one_of_all_structure_sets(pm, ROIS.external.name):
      # Compute rigid registration between current and new examination (they are equal)
      CF.compute_rigid_image_registration(case, examination, new_examination_name)
    #messagebox.showinfo("", "etter registrering")
    # Set robustness to the new examination
    OBJF.set_robustness_non_planning_examinations(plan, [new_examination_name])

    # Set up volumes for breast robust optimization in new examination
    PMF.set_up_volumes_for_breast_robust_optimization_new_examination(case, pm, new_examination_name, region_code)
    #messagebox.showinfo("", "etter endring av volumer ct robust")                                                     
    # Set up volumes for breast robust optimization in current examination
    PMF.set_up_volumes_for_breast_robust_optimization(case, pm, examination, ss, region_code)  
    #messagebox.showinfo("", "etter endring av volumer plan")   
    # Create "zMatch" and density volume, "xTetthetsvolum" and set density 'Water' in new examination
    PMF.create_rois_and_set_material_in_new_examination(patient_db, case, pm, ss, new_examination_name, match_volumes, density_volumes ,'Water')


    # Create External that goes outside the density volume in the new examination
    #messagebox.showinfo("", str(SSF.has_one_of_named_roi_with_contours(pm.StructureSets[new_examination_name], density_volumes)))
    PMF.create_external_outside_density_volume_new_examination(case, pm, ss, new_examination_name, SSF.return_all_named_rois_with_contours(pm.StructureSets[new_examination_name], density_volumes))
    #messagebox.showinfo("", str(SSF.has_one_of_named_roi_with_contours(pm.StructureSets[new_examination_name], density_volumes)))
                                                
  else: # Hybrid VMAT breast regional
    if region_code in RC.breast_reg_codes: # Breast regional
      # Create xPTVcaud and xPTVcran 
      PMF.create_ptv_caudal_and_craniel(pm, examination, ss, isocenter, ROIS.x_ptv, ROIS.box, ROIS.x_ptv_cran,ROIS.x_ptv_caud)
                                                               
      # Create zMatch
      PMF.create_match_volume(pm, ss, examination, ROIS.z_match, ROIS.x_ptv_cran, ROIS.body)
                                                               
      # Create density volume, "xTetthetsvolum" and set density 'Water' FIKS HER
      PMF.create_rois_and_set_material_in_new_examination(patient_db,case, pm, ss, examination.Name, [ROIS.z_match], [ROIS.x_tetthetsvolum], 'Water')
                                                               
      # Create External that goes outside the density volume in the new examination
      PMF.create_external_outside_density_volume(case, pm, ss,examination, ROIS.x_external, ROIS.external, ROIS.x_tetthetsvolum)

  if region_code in RC.breast_reg_codes: # Breast regional
    # For all cases of breast regional, create xCTVn_L3-L4_Ring"
    PMF.create_ctv_L2_L4_and_external(pm, examination, ss, [ROIS.level3, ROIS.level4], ROIS.body, ROIS.box1, ROIS.x_ctv_n_ring)
                                                        
  # The dose grid i expanded 4 cm anteriorly (because of Breast_Draft)
  size = 0.3
  beam_set.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
  BSF.expand_dose_grid(beam_set, expand_y=4)

  # Exclude most 'Undefined" ROIs
  PMF.exclude_rois_from_export(pm)
  # Set ROIs of Type 'Undefined' to type 'Other'
  PMF.set_all_undefined_to_organ_type_other(pm, ss)

    
'''
#if technique == 'VMAT': # Full VMAT
      # New examination name
      #new_examination_name = "CT-Robust"
      # Export and import current CT examination, the new examination name is set
      #CF.export_and_import_ct_study(clinic_db,patient_db, patient, case, examination, "C:/temp/tempexport/", "111111 11111", "Robust", new_examination_name, "TRCTGA004")
      # Compute rigid registration between current and new examination (they are equal)
      #CF.compute_rigid_image_registration(case, examination, new_examination_name)
      # Set robustness to the new examination
      #OBJF.set_robustness_non_planning_examinations(plan, [new_examination_name])
      #if PMF.has_roi(pm, ROIS.z_match_r.name) and PMF.has_roi(pm, ROIS.z_match_l.name):
        # Create sternum box
      #  PMF.create_sternum_box_and_external(pm, examination, ss, region_code, ROIS.sternum, SSF.return_named_roi_with_contours(ss, [ROIS.ptv_pc_r, ROIS.ptv_pc_l]), ROIS.body, ROIS.box1, ROIS.sternum_box)
        # Create zMatch_Sternum if bilateral breast
      #  PMF.create_match_volume_10mm(pm, ss, examination, ROIS.z_match_sternum, ROIS.sternum_box, ROIS.body)

      # Create "zMatch" and density volume, "xTetthetsvolum" and set density 'Water' in new examination
      #PMF.create_rois_and_set_material_in_new_examination(patient_db, case, pm, ss, new_examination_name, match_volumes, density_volumes ,'Water')

      # Create External that goes outside the density volume in the new examination
      #PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, SSF.return_all_named_roi_with_contours(ss, density_volumes)

      # Set up volumes for breast robust optimization in new examination
      #PMF.set_up_volumes_for_breast_robust_optimization_new_examination(case,pm,new_examination_name, region_code)
      # Set up volumes for breast robust optimization in current examination
      #PMF.set_up_volumes_for_breast_robust_optimization(case,pm,examination,ss, region_code)
    # For all cases of tangential breast, the dose grid i expanded 4 cm anteriorly (because of Breast_Draft)
    #size = 0.3
    #plan.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
    #PF.expand_dose_grid(plan, expand_y=4)

def create_volumes_and_settings_for_robust_breast_plan( clinic_db, patient_db, patient, case, pm, ss, plan,  examination, technique, region_code):
  match_volumes = [ROIS.z_match, ROIS.z_match_r, ROIS.z_match_l,ROIS.z_match_sternum ]
  density_volumes = [ROIS.x_tetthetsvolum,ROIS.x_tetthetsvolum_r,ROIS.x_tetthetsvolum_l,x_tetthetsvolum_sternum]
  if region_code in RC.breast_reg_codes: # Breast regional
    if technique == 'VMAT': # Breast regional 'full' VMAT
      # New examination name
      new_examination_name = "CT-Robust"
      # Export and import current CT examination, the new examination name is set
      CF.export_and_import_ct_study(clinic_db, patient_db, patient, case, examination, "C:/temp/tempexport/", "111111 11111", "Robust", new_examination_name, "TRCTGA004")
      # Compute rigid registration between current and new examination (they are equal)
      CF.compute_rigid_image_registration(case, examination, new_examination_name)
      # Set robustness to the new examination
      OBJF.set_robustness_non_planning_examinations(plan, [new_examination_name])

      # Create sternum box
      PMF.create_sternum_box_and_external(pm, examination, ss, region_code, ROIS.sternum, SSF.return_named_roi_with_contours(ss, [ROIS.x_ptv, ROIS.x_ptv_r, ROIS.x_ptv_l]), ROIS.body, ROIS.box1, ROIS.sternum_box)
      # Create zMatch_Sternum if bilateral breast
      if PMF.has_roi(pm, ROIS.z_match_r.name) and PMF.has_roi(pm, ROIS.z_match_l.name): 
        PMF.create_match_volume_10mm(pm, ss, examination, ROIS.z_match_sternum, ROIS.sternum_box, ROIS.body)
        
      #if PMF.has_roi(pm, ROIS.z_match.name):
      # Create "zMatch" and density volume, "xTetthetsvolum" and set density 'Water' in new examination
      PMF.create_rois_and_set_material_in_new_examination(patient_db, case, pm, ss, new_examination_name, match_volumes, density_volumes ,'Water')

      # Create External that goes outside the density volume in the new examination
      PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, SSF.return_all_named_roi_with_contours(ss, density_volumes)

      
      #if PMF.has_roi(pm, ROIS.z_match_r.name):
        # Create "zMatch" and density volume, "xTetthetsvolum_R" and set density 'Water' in new examination
        #PMF.create_roi_and_set_material_in_new_examination(patient_db,case, pm, ss, new_examination_name, ROIS.z_match_r,ROIS.x_tetthetsvolum_r,'Water')
      #if PMF.has_roi(pm, ROIS.z_match_l.name):
        # Create "zMatch" and density volume, "xTetthetsvolum_L" and set density 'Water' in new examination
        #PMF.create_roi_and_set_material_in_new_examination(patient_db,case, pm, ss, new_examination_name, ROIS.z_match_l,ROIS.x_tetthetsvolum_l,'Water')

    
      #elif PMF.has_roi(pm, ROIS.z_match_r.name) and PMF.has_roi(pm, ROIS.z_match_l.name):
      #  PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, [ROIS.x_tetthetsvolum_l,ROIS.x_tetthetsvolum_r])
      #elif PMF.has_roi(pm, ROIS.z_match_r.name):
      #  PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, [ROIS.x_tetthetsvolum_r])
      #elif PMF.has_roi(pm, ROIS.z_match_l.name):
      #  PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, [ROIS.x_tetthetsvolum_l])
      
      # Set up volumes for breast robust optimization in new examination
      PMF.set_up_volumes_for_breast_robust_optimization_new_examination(case, pm, new_examination_name, region_code)
      # Set up volumes for breast robust optimization in current examination
      PMF.set_up_volumes_for_breast_robust_optimization(case, pm, examination, ss, region_code)

      #max_arc_mu = 650
      #max_del_time = 150
      # The dose grid i expanded 4 cm anteriorly (because of Breast_Draft)
      size = 0.3
      plan.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
      PF.expand_dose_grid(plan, expand_y=4)
    else: # Breast regional hybrid VMAT
      # Create xPTVcaud and xPTVcran 
      PMF.create_ptv_caudal_and_craniel(pm, examination, ss, isocenter, ROIS.x_ptv, ROIS.box, ROIS.x_ptv_cran,ROIS.x_ptv_caud)
      # Create zMatch
      PMF.create_match_volume(pm, ss, examination, ROIS.z_match, ROIS.x_ptv_cran, ROIS.body)
      # Create density volume, "xTetthetsvolum" and set density 'Water'
      PMF.create_roi_and_set_material_in_new_examination(patient_db,case, pm, ss, examination.Name, ROIS.z_match, ROIS.x_tetthetsvolum, 'Water')
      # Create External that goes outside the density volume in the new examination
      PMF.create_external_outside_density_volume(case, pm, ss,examination,ROIS.x_external,ROIS.external, ROIS.x_tetthetsvolum)
      # The dose grid i expanded 4 cm anteriorly (because of Breast_Draft)
      size = 0.3
      plan.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
      PF.expand_dose_grid(plan, expand_y=4)
    # For all cases of breast regional, create xCTVn_L3-L4_Ring"
    PMF.create_ctv_L2_L4_and_external(pm, examination, ss, [ROIS.level3,ROIS.level4], ROIS.body, ROIS.box1, ROIS.x_ctv_n_ring)
    # Exclude most 'Undefined" ROIs
    PMF.exclude_rois_from_export(pm)
    # Set ROIs of Type 'Undefined' to type 'Other'
    PMF.set_all_undefined_to_organ_type_other(pm)
  elif region_code in RC.breast_tang_codes: # Breast tangential/ Breast only
    if technique == 'VMAT': # Full VMAT
      # New examination name
      new_examination_name = "CT-Robust"
      # Export and import current CT examination, the new examination name is set
      CF.export_and_import_ct_study(clinic_db,patient_db, patient, case, examination, "C:/temp/tempexport/", "111111 11111", "Robust", new_examination_name, "TRCTGA004")
      # Compute rigid registration between current and new examination (they are equal)
      CF.compute_rigid_image_registration(case, examination, new_examination_name)
      # Set robustness to the new examination
      OBJF.set_robustness_non_planning_examinations(plan, [new_examination_name])
      if PMF.has_roi(pm, ROIS.z_match_r.name) and PMF.has_roi(pm, ROIS.z_match_l.name):
        #  # Create "zMatch" and density volume, "xTetthetsvolum" and set density 'Water' in new examination
        #  PMF.create_roi_and_set_material_in_new_examination(patient_db, case, pm, ss, new_examination_name, ROIS.z_match_r,ROIS.x_tetthetsvolum_r,'Water')
        PMF.create_sternum_box_and_external(pm, examination, ss, region_code, ROIS.sternum, SSF.return_named_roi_with_contours(ss, [ROIS.ptv_pc_r, ROIS.ptv_pc_l]), ROIS.body, ROIS.box1, ROIS.sternum_box)
        PMF.create_match_volume_10mm(pm, ss, examination, ROIS.z_match_sternum, ROIS.sternum_box, ROIS.body)

      # Create "zMatch" and density volume, "xTetthetsvolum" and set density 'Water' in new examination
      PMF.create_rois_and_set_material_in_new_examination(patient_db, case, pm, ss, new_examination_name, match_volumes, density_volumes ,'Water')

      # Create External that goes outside the density volume in the new examination
      PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, SSF.return_all_named_roi_with_contours(ss, density_volumes)

      #if PMF.has_roi(pm, ROIS.z_match.name):
      #  # Create "zMatch" and density volume, "xTetthetsvolum" and set density 'Water' in new examination
      #  PMF.create_roi_and_set_material_in_new_examination(patient_db, case, pm, ss, new_examination_name, ROIS.z_match,ROIS.x_tetthetsvolum,'Water')
          #if PMF.has_roi(pm, ROIS.z_match_l.name):
      #  # Create "zMatch" and density volume, "xTetthetsvolum" and set density 'Water' in new examination
      #  PMF.create_roi_and_set_material_in_new_examination(patient_db, case, pm, ss, new_examination_name, ROIS.z_match_l,ROIS.x_tetthetsvolum_l,'Water')
      
      #if PMF.has_roi(pm, ROIS.z_match.name):
        # Create External that goes outside the density volume in the new examination
      #  PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, [ROIS.x_tetthetsvolum])
      #elif PMF.has_roi(pm, ROIS.z_match_r.name) and PMF.has_roi(pm, ROIS.z_match_l.name):
      #  PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, [ROIS.x_tetthetsvolum_l,ROIS.x_tetthetsvolum_r])
        # Create sternum box

      #elif PMF.has_roi(pm, ROIS.z_match_r.name):
      #  PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, [ROIS.x_tetthetsvolum_r])
      #elif PMF.has_roi(pm, ROIS.z_match_l.name):
      #  PMF.create_external_outside_density_volume_new_examination(case, pm, new_examination_name, [ROIS.x_tetthetsvolum_l])
      # Set up volumes for breast robust optimization in new examination
      PMF.set_up_volumes_for_breast_robust_optimization_new_examination(case,pm,new_examination_name, region_code)
      # Set up volumes for breast robust optimization in current examination
      PMF.set_up_volumes_for_breast_robust_optimization(case,pm,examination,ss, region_code)
    # For all cases of tangential breast, the dose grid i expanded 4 cm anteriorly (because of Breast_Draft)
    size = 0.3
    plan.SetDefaultDoseGrid(VoxelSize={'x':size, 'y':size, 'z':size})
    PF.expand_dose_grid(plan, expand_y=4)
'''                                                              
