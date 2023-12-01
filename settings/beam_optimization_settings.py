# encoding: utf8

# Import local files:
import region_codes as RC
import rois as ROIS
import plan_functions as PF
import structure_set_functions as SSF
import beam_functions as BF

# Set up beam optimization settings for different regions and fractionations
def set_beam_optimization_settings(ss, region_code, fraction_dose, nr_beams, technique, beam_setup_name, beam_set, beam):
  if region_code in RC.palliative_codes and fraction_dose > 8: # Trick to not set Max MU at all
    max_arc_mu = 0
  else:
    max_arc_mu = (fraction_dose*200)/(nr_beams)
  if BF.arc_length(beam) >= 350:
    max_del_time = 150
  elif BF.arc_length(beam) >= 60:
    max_del_time = 90
  if region_code in RC.head_neck_codes:
    max_arc_mu = fraction_dose*225
  elif region_code in RC.breast_codes:
    if BF.arc_length(beam) >= 350:
      max_arc_mu = 650/(nr_beams)
      max_del_time = 180
    elif BF.arc_length(beam) >= 250:
      max_arc_mu = 650/(2)
      max_del_time = 150
    elif BF.arc_length(beam) >= 78:
      max_arc_mu = 200/(nr_beams)
      max_del_time = 40
    else:
      if technique == 'VMAT':
        max_arc_mu = 250/(nr_beams)
        max_del_time = 40
      else:
        max_arc_mu = 40
        max_del_time = 20
    if region_code in RC.breast_reg_codes:
      if beam_setup_name == 'Cross':
        max_arc_mu = 500/(nr_beams)
  elif region_code in RC.gyn_codes:
    if fraction_dose == 1.8:
      max_arc_mu = (fraction_dose*200)/(2)
    else:
      max_arc_mu = (fraction_dose*220)/(2)

  elif region_code in RC.prostate_codes:
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name):
      max_arc_mu = (500)/(nr_beams)
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_50.name): #2.7 Gy x 25
      max_arc_mu = (650) / (nr_beams)
  elif beam.Name in ['182-0 B30','0-182 B30','178-0 B330','0-178 B330','182-0 B30 1','0-182 B30 1','178-0 B330 1','0-178 B330 1','182-0 B30 2','0-182 B30 2','178-0 B330 2','0-178 B330 2'] and int(beam.CouchRotationAngle) != 0: # Stereotactic brain with couch angels
    if len(list(beam_set.Beams)) == 2:
      if fraction_dose == 9:
        max_arc_mu = 500
        max_del_time = 90
      elif fraction_dose == 20:
        max_arc_mu = 1000
    if len(list(beam_set.Beams)) > 2:
      if fraction_dose == 9:
        max_arc_mu = 350
        max_del_time = 90
      elif fraction_dose == 20:
        max_arc_mu = 700
        max_del_time = 90
  elif region_code in RC.lung_codes+RC.liver_codes and fraction_dose > 8 and BF.arc_length(beam) < 270:
    max_arc_mu = fraction_dose*100
    max_del_time = 90
  elif beam.Name in ['178-182','182-178','178-182 1','182-178 1','178-182 2','182-178 2','178-182 3','182-178 3'] and fraction_dose > 8 and region_code in RC.brain_codes: # Stereotactic brain, the beam with couch angle zero
    max_arc_mu = 0
  elif region_code in RC.palliative_codes:
    if fraction_dose <= 8:
      if BF.arc_length(beam) >= 350:
        max_arc_mu = (fraction_dose*200)
        max_del_time = 150
      elif BF.arc_length(beam) >= 100:
        max_arc_mu = (fraction_dose*200)
        max_del_time = 90
      elif 100 > BF.arc_length(beam) >= 20 :
        max_del_time = 60
        max_arc_mu = fraction_dose*100
  return [max_arc_mu, max_del_time]


    
