# encoding: utf8

# Import local files:
import beam_set_functions as BSF
import case_functions as CF
import region_codes as RC
import rois as ROIS
import structure_set_functions as SSF
#BSF.create_three_beams(beam_set, isocenter, energy = energy_name, name1 = 'LPO', name2 = 'LAO', name3 = 'RAO', gantry_angle1 = '110', gantry_angle2 = '35', gantry_angle3 = '350', collimator_angle1 = '343', collimator_angle2 = '17', collimator_angle3 = '17', iso_index=iso_index, beam_index=beam_index)
from tkinter import *
from tkinter import messagebox

# Set up beams or arcs, based on region code (i.e. treatment site).
def setup_beams(ss, examination, beam_set, isocenter, region_code, fraction_dose, technique_name, energy_name, beam_setup_name, targets,beam_setup_palliative,  iso_index = 1, beam_index=1,beam_index2 = 2):
  if technique_name == '3D-CRT': # Conventional fields (and conventional fields for hybrid technique)
    #Two tangetial beams:
    if region_code in RC.breast_tang_r_codes : # Breast tangential right
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '54', gantry_angle2 = '231', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = beam_index+ 3)
      BSF.set_MU(beam_set,['54','231'], [110, 110] )
    elif region_code in RC.breast_partial_r_codes: # Breast boost right
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '54', gantry_angle2 = '231', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = beam_index+ 3)
      BSF.set_MU(beam_set,['54','231'], [85, 85] )
    elif region_code in RC.breast_tang_l_codes : # Breast tangential left
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '128', gantry_angle2 = '306', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = beam_index+ 3)
      BSF.set_MU(beam_set,['128','306'], [110, 110] )
    elif region_code in RC.breast_partial_l_codes : # Breast boost left
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '128', gantry_angle2 = '306', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = beam_index+ 3)
      BSF.set_MU(beam_set,['128','306'], [85, 85] )
    # Breast with regional lymph nodes:
    elif region_code in RC.breast_reg_l_codes: # Breast regional left
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '139', gantry_angle2 = '320', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = beam_index+ 5)
      BSF.set_MU(beam_set,['139','320'], [100, 100] )
    elif region_code in RC.breast_reg_r_codes: # Breast regional right
      BSF.create_two_beams(beam_set, isocenter, energy = energy_name, gantry_angle1 = '45', gantry_angle2 = '222', collimator_angle1 = '0', collimator_angle2 = '0', iso_index=iso_index, beam_index=beam_index,beam_index2 = beam_index+ 5)
      BSF.set_MU(beam_set,['45','222'], [100, 100] )
    elif region_code in RC.brain_whole_codes: # Brain whole
      beam_energy = '15'
      BSF.create_two_beams(beam_set, isocenter, energy = beam_energy, gantry_angle1 = '90', gantry_angle2 = '270', collimator_angle1 = '63', collimator_angle2 = '115', iso_index=iso_index, beam_index=beam_index,beam_index2 = beam_index+1)
      BSF.set_MU(beam_set,['270','90'], [130, 130])
  elif technique_name == 'VMAT': # VMAT
    # Brain:
    if region_code in RC.brain_whole_codes: # Brain whole
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    elif region_code in RC.brain_partial_codes: # Brain partial or stereotactic
      if fraction_dose > 6: # Brain stereotactic
        setup_brain_srt_beams( beam_set, isocenter, energy_name, beam_setup_name, targets, iso_index = 1, beam_index =beam_index)
      else: # Brain partial
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, collimator_angle = '45', iso_index=iso_index, beam_index=beam_index)
    elif region_code in RC.head_neck_codes and len(beam_setup_palliative)==0: # Head and neck
      if region_code in RC.larynx_codes: # Larynx
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '270', gantry_start_angle = '90', collimator_angle = '5', iso_index=iso_index, beam_index=beam_index)
      else: # head and neck except from larynx 
        BSF.create_single_arc(beam_set, isocenter, collimator_angle = '25',energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    elif region_code in RC.breast_partial_codes: # Breast boost 
      if SSF.has_roi_with_shape(ss, ROIS.ctv_p.name): # Not bilateral
        if region_code in RC.breast_partial_l_codes: # Breast boost left
          if beam_setup_name == 'Two': # Two short beams
            BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='110', gantry_stop_angle2='300', gantry_start_angle1='178', gantry_start_angle2='0', collimator_angle1='5', collimator_angle2='5',iso_index=2, beam_index=beam_index)
          else: # One beam
            BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '280', gantry_start_angle = '178', iso_index=2, beam_index=beam_index)
        elif region_code in RC.breast_partial_r_codes: # Breast boost right
          if beam_setup_name == 'Two': # Two short beams
            BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='0', gantry_stop_angle2='182', gantry_start_angle1='60', gantry_start_angle2='250', collimator_angle1='5', collimator_angle2='5',iso_index=2, beam_index=beam_index)
          else: # One beam
            BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '182', gantry_start_angle = '80', iso_index=2, beam_index=beam_index)
      else: # Bilateral
        BSF.create_single_arc(beam_set, isocenter,collimator_angle = '5',energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    elif region_code in RC.breast_tang_codes: # Breast tangential
      if SSF.has_roi_with_shape(ss, ROIS.ctv_p.name): # Not bilateral
        if region_code in RC.breast_tang_l_codes: # Breast tangential left
          if beam_setup_name == 'Two': # Two short beams
            BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='100', gantry_stop_angle2='280', gantry_start_angle1='178', gantry_start_angle2='0', collimator_angle1='5', collimator_angle2='5',iso_index=iso_index, beam_index=beam_index)
          else: # One beam
            BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '280', gantry_start_angle = '178', iso_index=iso_index, beam_index=beam_index)
        elif region_code in RC.breast_tang_r_codes: # Breast tangential right
          if beam_setup_name == 'Two': # Two short beams
            BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='0', gantry_stop_angle2='182', gantry_start_angle1='80', gantry_start_angle2='260', collimator_angle1='5', collimator_angle2='5',iso_index=iso_index, beam_index=beam_index)
          else: # One beam
            BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '182', gantry_start_angle = '80', iso_index=iso_index, beam_index=beam_index)
      else: # Bilateral
        BSF.create_single_arc(beam_set, isocenter,collimator_angle = '5',energy = energy_name, iso_index=iso_index, beam_index=beam_index)
        # Breast with regional lymph nodes:
    elif region_code in RC.breast_reg_l_codes: # Breast regional left
      if beam_setup_name == 'Cross': # Cross techinique with two arcs, one with couch angle 90 degrees
        BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='280', gantry_stop_angle2='0', gantry_start_angle1='178', gantry_start_angle2='38', collimator_angle1='5', collimator_angle2='185',couch_angle1='0', couch_angle2='90',iso_index=iso_index, beam_index=beam_index)
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_p.name): # One beam, not bilateral
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '280', gantry_start_angle = '178', iso_index=iso_index, beam_index=beam_index)
      else: # Bilateral
        BSF.create_single_arc(beam_set, isocenter,collimator_angle = '5',energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    elif region_code in RC.breast_reg_r_codes: # Breast regional right
      if beam_setup_name == 'Cross': # Cross techinique with two arcs, one with couch angle 90 degrees
        BSF.create_two_arcs(beam_set, isocenter, gantry_stop_angle1='182', gantry_stop_angle2='0', gantry_start_angle1='80', gantry_start_angle2='38', collimator_angle1='5', collimator_angle2='185',couch_angle1='0', couch_angle2='90',iso_index=iso_index, beam_index=beam_index)
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_p.name):  # One beam, not bilateral
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '182', gantry_start_angle = '80', iso_index=iso_index, beam_index=beam_index)
      else:  # Bilateral
        BSF.create_single_arc(beam_set, isocenter,collimator_angle = '5',energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    # Lung:
    elif region_code in RC.lung_and_mediastinum_codes+RC.liver_codes and len(beam_setup_palliative)==0: # Lung or Liver 
      if region_code in RC.lung_r_codes or region_code in RC.liver_codes: # Lung right side or liver
        if fraction_dose >= 8: # Stereotactic 
          if beam_setup_name == 'Two': # Two arcs
            BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '182', gantry_stop_angle2 = '30', gantry_start_angle1 = '30', gantry_start_angle2 = '182', iso_index=iso_index, beam_index=beam_index)
          else:
            if len(targets)==2: # Two targets, four arcs
              BSF.create_multiple_arcs(beam_set, isocenter, energy='6', gantry_stop_angles =['182','30','182','30'], gantry_start_angles=['30','182','30','182'], 
                    collimator_angles=['5','355','355','5'], couch_angles=['0','0','0','0'], iso_index=1, beam_index=beam_index)
            elif len(targets)==3: # Three targets, six arcs
              BSF.create_multiple_arcs(beam_set, isocenter, energy='6', gantry_stop_angles =['182','30','182','30','182','30'], gantry_start_angles=['30','182','30','182','30','182'], 
                    collimator_angles=['5','355','355','5','5','355'], couch_angles=['0','0','0','0','0','0'], iso_index=1, beam_index=beam_index)
        else: # One arc for non stereotactic treatments
          BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '182', gantry_start_angle = '30', iso_index=iso_index, beam_index=beam_index)
      elif region_code in RC.lung_l_codes: # Lung left side
        if fraction_dose > 8: # Stereotactic 
          if beam_setup_name == 'Two': # Two arcs
            BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '330', gantry_stop_angle2 = '178', gantry_start_angle1 = '178', gantry_start_angle2 = '330', iso_index=iso_index, beam_index=beam_index)
          else:
            if len(targets)==2: # Two targets, four arcs
              BSF.create_multiple_arcs(beam_set, isocenter, energy='6', gantry_stop_angles =['330','178','330','178'], gantry_start_angles=['178','330','178','330'], 
                    collimator_angles=['5','355','355','5'], couch_angles=['0','0','0','0'], iso_index=1, beam_index=beam_index)
            elif len(targets)==3: # Three targets, six arcs
              BSF.create_multiple_arcs(beam_set, isocenter, energy='6', gantry_stop_angles =['330','178','330','178','330','178'], gantry_start_angles=['178','330','178','330','178','330'], 
                    collimator_angles=['5','355','355','5','5','355'], couch_angles=['0','0','0','0','0','0'], iso_index=1, beam_index=beam_index)
        else:
          BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = '330', gantry_start_angle = '178', iso_index=iso_index, beam_index=beam_index)
      else: # Mediastinum or both lungs
        BSF.create_single_arc(beam_set, isocenter, energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    # Esophagus
    elif region_code in RC.esophagus_codes:
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    # Bladder:
    elif region_code in RC.bladder_codes:
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, iso_index=iso_index, beam_index=beam_index)
    # Prostate:
    elif region_code in RC.prostate_codes:
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, collimator_angle = '25', iso_index=iso_index, beam_index=beam_index)
    # Gyn:
    elif region_code in RC.gyn_codes:
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, collimator_angle = '25', iso_index=iso_index, beam_index=beam_index)
    # Rectum:  
    elif region_code in RC.rectum_codes:
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, collimator_angle = '25', iso_index=iso_index, beam_index=beam_index)
    # Palliative and stereotactic bone/spine:
    elif region_code in RC.palliative_codes or region_code in RC.lung_and_mediastinum_codes+RC.head_neck_codes and len(beam_setup_palliative)>0:
      if fraction_dose > 8: # Stereotactic palliative/bone codes:
        if abs(isocenter.x) > 5:
            if isocenter.x > 5 and CF.is_head_first_supine(examination) or not CF.is_head_first_supine(examination) and isocenter.x < -5: # Target on left side of the body
              BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '330', gantry_stop_angle2 = '178', gantry_start_angle1 = '178', gantry_start_angle2 = '330', iso_index=iso_index, beam_index=beam_index)
            else: # Target on right side of the body
              BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '182', gantry_stop_angle2 = '30', gantry_start_angle1 = '30', gantry_start_angle2 = '182', iso_index=iso_index, beam_index=beam_index)
        elif abs(isocenter.y) +5 < abs(SSF.roi_center_y(ss, ROIS.external.name)): # Target on the anterior side of the body
            BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, gantry_stop_angle1 = '270', gantry_stop_angle2 = '90', gantry_start_angle1 = '90', gantry_start_angle2 = '270', iso_index=iso_index, beam_index=beam_index)
        else: # Otherwise (target in the middle of the body)
          BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '355', collimator_angle2 = '5', iso_index=iso_index, beam_index=beam_index)
      else: # Palliative non stereotactic
        setup_palliative_beams(ss, examination, beam_set, isocenter, region_code, energy_name, beam_setup_name, beam_setup_palliative,  iso_index = 1, beam_index=beam_index)

  return len(list(beam_set.Beams))


def setup_palliative_beams(ss, examination, beam_set, isocenter, region_code, energy_name, beam_setup_name, beam_setup_palliative,  iso_index = 1, beam_index=1):
  if region_code in RC.whole_pelvis_codes: # Whole pelvis
    BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '45', collimator_angle2 = '5', iso_index=iso_index, beam_index=beam_index)
  else:
    if beam_setup_name == 'Times_Nr_PTVs' and len(beam_setup_palliative) > 0: # Number of beams are setup times number of targets (with Treat) ex. for 2 targets you get four beams if you chose the short arc setup (instead of two)
      start_angles =[]
      stop_angles =[]
      # Determine correct gantry angles based on beam_setup_palliative-choices
      if(beam_setup_palliative[0]==beam_setup_palliative[1]): # Equal choice for target 1 and 2
        if beam_setup_palliative[0]=='short': # 'short'
          start_angles = ['178','138','222','182']
          stop_angles = ['138','178','182','222']
        elif beam_setup_palliative[0]=='back': # 'back'
          start_angles = ['178','90','270','182']
          stop_angles = ['90','178','182','270']
        elif beam_setup_palliative[0]=='front': # 'front'
          start_angles = ['90','270']
          stop_angles = ['270','90']
        elif beam_setup_palliative[0]=='right': # 'right'
          start_angles = ['0','182']
          stop_angles = ['182','0']
        elif beam_setup_palliative[0]=='left': # 'left'
          start_angles = ['178','0']
          stop_angles = ['0','178']
        elif beam_setup_palliative[0]=='full': # 'full' 
          BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '355', collimator_angle2 = '5', iso_index=iso_index, beam_index=beam_index)
      else:
        if beam_setup_palliative[0] == 'short' and beam_setup_palliative[1] == 'back': # The first choice is 'short' and the second is 'back'
          start_angles = ['178','90','222','182']
          stop_angles = ['138','178','182','270']
        elif beam_setup_palliative[0] == 'back' and beam_setup_palliative[1] == 'short': # The first choice is 'back' and the second is 'short'
          start_angles = ['178','138','270','182']
          stop_angles = ['90','178','182','222']
        elif 'short' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # One of the choices is 'short'
          if 'front' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # The other choice is 'front'
            start_angles = ['178','90','222']
            stop_angles = ['138','270','182']
          elif 'right' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # The other choice is 'right'
            start_angles = ['178','0','182']
            stop_angles = ['138','182','222']
          elif 'left' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # The other choice is 'left'
            start_angles = ['178','178','222']
            stop_angles = ['138','0','182']
          elif 'full' in [beam_setup_palliative[0], beam_setup_palliative[1]]:  # The other choice is 'full'   
            start_angles = ['178','222','182']
            stop_angles = ['138','182','178']
        elif 'back' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # One of the choices is 'back'
          if 'front' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # The other choice is 'front'
            start_angles = ['178','90','270']
            stop_angles = ['90','270','182']
          elif 'right' in [beam_setup_palliative[0],beam_setup_palliative[1]]: # The other choice is 'right'
            start_angles = ['178','0','182']
            stop_angles = ['90','182','270']
          elif 'left' in [beam_setup_palliative[0], beam_setup_palliative[1]]:  # The other choice is 'left'
            start_angles = ['178','178','270']
            stop_angles = ['90','0','182']
          elif 'full' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # The other choice is 'full'
            start_angles = ['178','270','182']
            stop_angles = ['90','182','178']
        elif 'front' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # One of the choices is 'front'
          if 'right' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # The other choice is 'right'
            start_angles = ['90','182']
            stop_angles = ['270','0']
          elif 'left' in [beam_setup_palliative[0], beam_setup_palliative[1]]:  # The other choice is 'left'
            start_angles = ['270','178']
            stop_angles = ['90','0']
          elif 'full' in [beam_setup_palliative[0], beam_setup_palliative[1]]:  # The other choice is 'full'  
            start_angles = ['178','270']
            stop_angles = ['182','90']
        elif 'right' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # One of the choices is 'right'
          if 'left' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # The other choice is 'left'
            start_angles = ['178','0']
            stop_angles = ['0','182']
          elif 'full' in [beam_setup_palliative[0], beam_setup_palliative[1]]: # The other choice is 'full' 
            start_angles = ['178','182']
            stop_angles = ['182','0']
        elif beam_setup_palliative[0] in ['left','full'] and beam_setup_palliative[1] in ['full','left']:
          start_angles = ['182','178']
          stop_angles = ['178','0']

    else: # Number of beam is setup for all targets combined (without Treat), ex. for 2 targets you get 2 beams if you chose the short arc setup
      # Determine correct gantry angles based on beam_setup_palliative-choices
      if beam_setup_palliative[0]=='short':
        start_angles = ['178','222']
        stop_angles = ['138','182']
      elif beam_setup_palliative[0]=='back':
        start_angles = ['178','270']
        stop_angles = ['90','182']
      elif beam_setup_palliative[0]=='front':
        start_angles = ['90']
        stop_angles = ['270']
      elif beam_setup_palliative[0]=='right':
        start_angles = ['0']
        stop_angles = ['182']
      elif beam_setup_palliative[0]=='left':
        start_angles = ['178']
        stop_angles = ['0']
      elif beam_setup_palliative[0]=='full':
        start_angles = ['178']
        stop_angles = ['182']
    # Setup beams
    if len(start_angles) == len(stop_angles) == 4: # 4 beams
        BSF.create_multiple_arcs(beam_set, isocenter, energy='6', gantry_stop_angles =stop_angles, gantry_start_angles=start_angles,
                             collimator_angles=['5','355','355','5'], couch_angles=['0','0','0','0'], iso_index=1, beam_index=beam_index)
    elif len(start_angles) == len(stop_angles) == 3: # 3 beams
      BSF.create_multiple_arcs(beam_set, isocenter, energy='6', gantry_stop_angles =stop_angles, gantry_start_angles=start_angles,
                             collimator_angles=['5','355','355'], couch_angles=['0','0','0'], iso_index=1, beam_index=beam_index)
    elif len(start_angles) == len(stop_angles) == 2: # 2 beams
      BSF.create_multiple_arcs(beam_set, isocenter, energy='6', gantry_stop_angles =stop_angles, gantry_start_angles=start_angles,
                             collimator_angles=['5','355'], couch_angles=['0','0'], iso_index=1, beam_index=beam_index)
    elif len(start_angles) == len(stop_angles) == 1: # 1 beam
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, gantry_stop_angle = stop_angles[0], gantry_start_angle = start_angles[0], iso_index=iso_index, beam_index=beam_index)

def setup_brain_srt_beams( beam_set, isocenter, energy_name, beam_setup_name, targets, iso_index = 1, beam_index = 1):
  start_angles =[]
  if beam_setup_name == 'One':
    if len(targets)<2:
      BSF.create_single_arc(beam_set, isocenter, energy = energy_name, collimator_angle = '5', iso_index=iso_index, beam_index=beam_index)
    elif len(targets)==2:
      BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '5', collimator_angle2 = '355', iso_index=iso_index, beam_index=beam_index)
    elif len(targets)==3:   
      start_angles = ['178','182','178']
      stop_angles = ['182','178','182']
      coll_angles = ['5','355','5']
      couch_rot_angles = ['0','0','0']
    elif len(targets)==4:   
      start_angles = ['178','182','178','182']
      stop_angles = ['182','178','182','178']
      coll_angles = ['5','355','5','355']
      couch_rot_angles = ['0','0','0','0']
  elif beam_setup_name == 'Two':
    if len(targets)<2:
      BSF.create_two_arcs(beam_set, isocenter, energy = energy_name, collimator_angle1 = '5', collimator_angle2 = '355', iso_index=iso_index, beam_index=beam_index)
    elif len(targets)==2:
      start_angles = ['178','182','178','182']
      stop_angles = ['182','178','182','178']
      coll_angles = ['5','5','355','355']
      couch_rot_angles = ['0','0','0','0']
    elif len(targets)==3:
      start_angles = ['178','182','178','182','178','182']
      stop_angles = ['182','178','182','178','182','178']
      coll_angles = ['5','5','5','355','355','355']
      couch_rot_angles = ['0','0','0','0','0','0']
    elif len(targets)==4:
      start_angles = ['178','182','178','182','178','182','178','182']
      stop_angles = ['182','178','182','178','182','178','182','178']
      coll_angles = ['5','5','5','5','355','355','355','355']
      couch_rot_angles = ['0','0','0','0','0','0','0','0']
  elif beam_setup_name == 'Three':
    if len(targets)<2:
      start_angles = ['178','182','0']
      stop_angles = ['182','0','178']
      coll_angles = ['5','355','355']
      couch_rot_angles = ['0','30','330']
    elif len(targets)==2:
      start_angles = ['178','182','0','182','178','0']
      stop_angles = ['182','178','182','0','0','178']
      coll_angles = ['5','5','5','355','355','355']
      couch_rot_angles = ['0','0','30','30','330','330']
    elif len(targets)==3:
      start_angles = ['178','182','178','182','0','182','0','178','0']
      stop_angles = ['182','178','182','0','182','0','178','0','178']
      coll_angles = ['5','5','5','355','355','355','5','5','5']
      couch_rot_angles = ['0','0','0','30','30','30','330','330','330']
    elif len(targets)==4:
      start_angles = ['178','182','178','182','178','0','178','0','0','182','0','182']
      stop_angles = ['182','178','182','178','0','178','0','178','182','0','182','0']
      coll_angles = ['5','5','5','5','355','355','355','355','5','5','5','5']
      couch_rot_angles = ['0','0','0','0','330','330','330','330','30','30','30','30']
  if len(start_angles)>0:  
    BSF.create_multiple_arcs(beam_set, isocenter, energy='6', gantry_stop_angles =stop_angles, gantry_start_angles=start_angles, collimator_angles=coll_angles,couch_angles=couch_rot_angles , iso_index=1, beam_index=beam_index)
#messagebox.showinfo("",str(beam_setup_name) + " " + str(beam_setup_palliative)+ " " + str(beam_setup_palliative[0]) )
