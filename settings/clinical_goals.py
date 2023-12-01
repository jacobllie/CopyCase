# encoding: utf8

# Import local files:
import clinical_goal as CG
import rois as ROIS
import tolerance_doses as TOL
import roi_functions as ROIF
import structure_set_functions as SSF
import region_codes as RC


# Criterias:
at_most = 'AtMost'
at_least = 'AtLeast'

# Types:
volume_at_dose = 'VolumeAtDose'
abs_volume_at_dose = 'AbsoluteVolumeAtDose'
dose_at_abs_volume = 'DoseAtAbsoluteVolume'
dose_at_volume = 'DoseAtVolume'
average_dose = 'AverageDose'
homogeneity_index = 'HomogeneityIndex'
conformity_index = 'ConformityIndex'

# Priorities:
priority1 = 1
priority2 = 2
priority3 = 3
priority4 = 4
priority5 = 5
priority6 = 6
priority7 = 7
priority8 = 8

# Absolute volumes:
cc0 = 0
cc0_1 = 0.1
cc0_2 = 0.2
cc0_03 = 0.03
cc0_05 = 0.05
cc0_35 = 0.35
cc0_5 = 0.5
cc1 = 1
cc1_2 = 1.2
cc2 = 2
cc3 = 3
cc4 = 4
cc5 = 5
cc10 = 10
cc15 = 15
cc20 = 20
cc30 = 30
cc70 = 70
cc100 =100
cc195 = 195
cc200 = 200
cc250 = 250
cc310 = 310
cc350 = 350
cc500 = 500
cc700 = 700
cc1000 = 1000
cc1500 = 1500

# Percent volumes:

pc1 = 0.01
pc2 = 0.02
pc3 = 0.03
pc5 = 0.05
pc10 = 0.1
pc15 = 0.15
pc17 = 0.17
pc20 = 0.2
pc25 = 0.25
pc26 = 0.26
pc30 = 0.3
pc33 = 0.33
pc32 = 0.32
pc35 = 0.35
pc37 = 0.37
pc40 = 0.40
pc49 = 0.49
pc74_34 = 0.7434782608695
pc50 = 0.5
pc55 = 0.55
pc60 = 0.6
pc65 = 0.65
pc66 = 0.66
pc69_1 = 0.6909090909
pc70 = 0.7
pc71_3 = 0.713
pc72_36 = 0.7236363636
pc73_09 = 0.7309090909
pc75 = 0.75
pc76 = 0.76
pc76_36 = 0.763636363636
pc77_72 = 0.7772727272
pc78 = 0.78
pc78_26 = 0.7826086956521
pc78_4 = 0.784
pc79_6 = 0.796
pc80 = 0.8
pc80_4 = 0.804
pc80_71 = 0.80714285714
pc81_81 = 0.818181818181
pc83_82 = 0.838260869565
pc84 = 0.84
pc84_27 = 0.842727272727
pc84_6 = 0.846
pc85 = 0.85
pc86 = 0.86
pc88 = 0.88
pc86_36 = 0.863636
pc87_54= 0.87545454545454
pc88_36 = 0.8836
pc89_1 = 0.891
pc89_3 = 0.893
pc90 = 0.9
pc90_24 = 0.9024
pc90_25 = 0.9025
pc90_45 = 0.9045454545
pc90_86 = 0.9086956521739
pc91_36 = 0.9136363636
pc92 = 0.92
pc92_12 = 0.9212
pc93 = 0.93
pc93_53 = 0.9353
pc94_52 = 0.94525
pc94_47 = 0.9447
pc94 = 0.94
pc95 = 0.95
pc95_47 = 0.95475
pc95_65 = 0.9565217391304
pc95_88 = 0.9588
pc96 = 0.96
pc93_1 = 0.931
pc97 = 0.97
pc97_73 = 0.9773913043478
pc98 = 0.98
pc98_5 = 0.985
pc98_7 = 0.987
pc99 = 0.99
pc99_5 = 0.995
pc99_75 = 0.9975
pc99_8 = 0.998
pc99_9 = 0.999
pc100 = 1
pc100_5 = 1.005
pc105 = 1.05
pc102 = 1.02
pc102_43 = 1.0243478260869
pc102_08=1.0208695652173
pc103 = 1.03
pc107 = 1.07
pc110 = 1.1
pc130 = 1.3
pc132 = 1.32
pc139 = 1.386
pc140 = 1.4
pc147 = 1.469475655
pc150 = 1.5
pc170 = 1.7


# Create CG.ClinicalGoal objects:
# Example:
#ClinicalGoal(name, criteria, type, tolerance, value, priority)

# Create Clinical goals for ORGANS AT RISK
# (Sorted cranio-caudally)

# Brain:
def brain_oars(nr_fractions, region_code):
  if region_code in RC.brain_whole_codes:
    brain_oars = [
      #CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean_tinnitus, None, priority3),
      #CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean_tinnitus, None, priority3),
      CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority3),
      CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority3)
      #CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_mean, None, priority3),
      #CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_mean, None, priority3),
      #CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_v003_adx, cc0, priority3)
      ]
  elif region_code in RC.brain_partial_codes:
    if nr_fractions == 1: # Stereotactic, one fraction
      brain_oars = [
        CG.ClinicalGoal(ROIS.brain_ptv.name, at_most, abs_volume_at_dose, cc10,TOL.brain_srt_1fx_v10,  priority1),
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_srt_1fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, abs_volume_at_dose, cc1,TOL.brainstem_srt_1fx_v1,  priority1),
        CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_srt_1fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_srt_1fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, abs_volume_at_dose,cc0_2, TOL.optic_chiasm_srt_1fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.optic_nrv_srt_1fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.optic_nrv_srt_1fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_nrv_srt_1fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_nrv_srt_1fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, dose_at_abs_volume, TOL.cochlea_srt_1fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, dose_at_abs_volume, TOL.cochlea_srt_1fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.eye_r.name, at_most, dose_at_abs_volume, TOL.eye_srt_1fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.eye_l.name, at_most, dose_at_abs_volume, TOL.eye_srt_1fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.skin.name, at_most, abs_volume_at_dose,cc10, TOL.skin_srt_1fx_v10,  priority4),
        CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_srt_1fx_v0, cc0_03, priority5),
        CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_srt_1fx_v0, cc0_03, priority5)
      ]
    elif nr_fractions == 3: # Stereotactic, three fractions litt strenge krav?
      brain_oars = [
        CG.ClinicalGoal(ROIS.brain_ptv.name, at_most, abs_volume_at_dose, cc10,TOL.brain_srt_3fx_v10,  priority1),
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_srt_3fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_srt_3fx_v0_35, cc0_35, priority1),
        #CG.ClinicalGoal(ROIS.brainstem.name, at_most, abs_volume_at_dose, cc0_35,TOL.brainstem_srt_3fx_v0_35,  priority1),
        CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_srt_3fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_srt_3fx_v0, cc0_03, priority1),
        CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_srt_3fx_v0_35, cc0_35, priority1),
        #CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, abs_volume_at_dose,  cc1,TOL.spinal_cord_srt_3fx_v1, priority1),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_srt_3fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_chiasm_srt_3fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.optic_nrv_srt_3fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.optic_nrv_srt_3fx_v0, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_nrv_srt_3fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, abs_volume_at_dose, cc0_2,TOL.optic_nrv_srt_3fx_v0_2,  priority2),
        CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, dose_at_abs_volume, TOL.cochlea_srt_3fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, dose_at_abs_volume, TOL.cochlea_srt_3fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.eye_r.name, at_most, dose_at_abs_volume, TOL.eye_srt_3fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.eye_l.name, at_most, dose_at_abs_volume, TOL.eye_srt_3fx_v0, cc0_03, priority4),
        CG.ClinicalGoal(ROIS.skin.name, at_most, abs_volume_at_dose,  cc10,TOL.skin_srt_3fx_v10, priority4),
        CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_srt_3fx_v0, cc0_03, priority5),
        CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_srt_3fx_v0, cc0_03, priority5)
      ]
    else: # Partial brain
      if nr_fractions == 30:
        brain_oars = [
          CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord30_v0_03_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brain_gtv.name, at_most, volume_at_dose,pc50, TOL.brain_ptv_30_mean, priority5),
          CG.ClinicalGoal(ROIS.brainstem_surface.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brainstem_core.name, at_most, dose_at_abs_volume, TOL.brainstem_core_30_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_30_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.optic_nrv_30_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.optic_nrv_30_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean_30, None, priority4),
          CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean_30, None, priority4),
          CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_mean_30, None, priority5),
          CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_mean_30, None, priority5),
          CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_30_adx, cc0_03, priority6),
          CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_30_adx, cc0_03, priority6),
          CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_mean_30, None, priority5),
          CG.ClinicalGoal(ROIS.retina_l.name, at_most, dose_at_abs_volume, TOL.retina_v003_30_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.retina_r.name, at_most, dose_at_abs_volume, TOL.retina_v003_30_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.cornea_l.name, at_most, dose_at_abs_volume, TOL.cornea_v003_30_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.cornea_r.name, at_most, dose_at_abs_volume, TOL.cornea_v003_30_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_v003_30_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.hippocampus_l.name, at_most, dose_at_volume, TOL.hippocampus_30_v40, pc40, priority4),
          CG.ClinicalGoal(ROIS.hippocampus_r.name, at_most, dose_at_volume, TOL.hippocampus_30_v40, pc40, priority4),
          #CG.ClinicalGoal(ROIS.retina_l_prv.name, at_most, dose_at_abs_volume, TOL.retina_prv_v003_30_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.retina_r_prv.name, at_most, dose_at_abs_volume, TOL.retina_prv_v003_30_adx, cc0_03, priority7),
          CG.ClinicalGoal(ROIS.optic_chiasm_prv.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_prv_30_v003_adx, cc0_03, priority7),
          CG.ClinicalGoal(ROIS.optic_nrv_l_prv.name, at_most, dose_at_abs_volume, TOL.optic_nrv_prv_30_v003_adx, cc0_03, priority7),
          CG.ClinicalGoal(ROIS.optic_nrv_r_prv.name, at_most, dose_at_abs_volume, TOL.optic_nrv_prv_30_v003_adx, cc0_03, priority7),
          CG.ClinicalGoal(ROIS.brainstem_surface_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_prv_30_v003_adx, cc0_03, priority7)
        ]
      elif nr_fractions == 33:
        brain_oars = [
          CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord33_v0_03_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brain_gtv.name, at_most, volume_at_dose,pc50, TOL.brain_ptv_33_mean, priority5),
          CG.ClinicalGoal(ROIS.brainstem_surface.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_33_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brainstem_core.name, at_most, dose_at_abs_volume, TOL.brainstem_core_33_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.brainstem_core_33_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.brainstem_core_33_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.brainstem_core_33_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean_33, None, priority4),
          CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean_33, None, priority4),
          CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_mean_33, None, priority5),
          CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_mean_33, None, priority5),
          CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_33_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_33_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_mean_33, None, priority5),
          CG.ClinicalGoal(ROIS.retina_l.name, at_most, dose_at_abs_volume, TOL.retina_v003_33_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.retina_r.name, at_most, dose_at_abs_volume, TOL.retina_v003_33_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.cornea_l.name, at_most, dose_at_abs_volume, TOL.cornea_v003_33_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.cornea_r.name, at_most, dose_at_abs_volume, TOL.cornea_v003_33_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_v003_33_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.hippocampus_l.name, at_most, dose_at_volume, TOL.hippocampus_33_v40, pc40, priority4),
          CG.ClinicalGoal(ROIS.hippocampus_r.name, at_most, dose_at_volume, TOL.hippocampus_33_v40, pc40, priority4),
          #CG.ClinicalGoal(ROIS.retina_l_prv.name, at_most, dose_at_abs_volume, TOL.retina_prv_v003_33_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.retina_r_prv.name, at_most, dose_at_abs_volume, TOL.retina_prv_v003_33_adx, cc0_03, priority7),
          CG.ClinicalGoal(ROIS.optic_chiasm_prv.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_prv_33_v003_adx, cc0_03, priority7),
          CG.ClinicalGoal(ROIS.optic_nrv_l_prv.name, at_most, dose_at_abs_volume, TOL.optic_nrv_prv_33_v003_adx, cc0_03, priority7),
          CG.ClinicalGoal(ROIS.optic_nrv_r_prv.name, at_most, dose_at_abs_volume, TOL.optic_nrv_prv_33_v003_adx, cc0_03, priority7),
          CG.ClinicalGoal(ROIS.brainstem_surface_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_prv_33_v003_adx, cc0_03, priority7)
        ]
      elif nr_fractions == 15:
        brain_oars = [
          CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brain_gtv.name, at_most, volume_at_dose,pc50, TOL.brain_ptv_33_mean, priority5),
          CG.ClinicalGoal(ROIS.brainstem_surface.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brainstem_core.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean_15, None, priority4),
          CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean_15, None, priority4),
          CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_mean_15, None, priority5),
          CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_mean_15, None, priority5),
          CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_mean_15, None, priority5),
          CG.ClinicalGoal(ROIS.retina_l.name, at_most, dose_at_abs_volume, TOL.retina_v003_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.retina_r.name, at_most, dose_at_abs_volume, TOL.retina_v003_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.cornea_l.name, at_most, dose_at_abs_volume, TOL.cornea_v003_15_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.cornea_r.name, at_most, dose_at_abs_volume, TOL.cornea_v003_15_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_v003_15_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.hippocampus_l.name, at_most, dose_at_volume, TOL.hippocampus_15_v40, pc40, priority4),
          CG.ClinicalGoal(ROIS.hippocampus_r.name, at_most, dose_at_volume, TOL.hippocampus_15_v40, pc40, priority4)
          #CG.ClinicalGoal(ROIS.retina_l_prv.name, at_most, dose_at_abs_volume, TOL.retina_prv_v003_33_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.retina_r_prv.name, at_most, dose_at_abs_volume, TOL.retina_prv_v003_33_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.optic_chiasm_prv.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_prv_33_v003_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.optic_nrv_l_prv.name, at_most, dose_at_abs_volume, TOL.optic_nrv_prv_33_v003_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.optic_nrv_r_prv.name, at_most, dose_at_abs_volume, TOL.optic_nrv_prv_33_v003_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.brainstem_surface_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_prv_33_v003_adx, cc0_03, priority7)
        ]
      elif nr_fractions == 13:
        brain_oars = [
          CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brain_gtv.name, at_most, volume_at_dose,pc50, TOL.brain_ptv_33_mean, priority5),
          CG.ClinicalGoal(ROIS.brainstem_surface.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brainstem_core.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean_13, None, priority4),
          CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean_13, None, priority4),
          CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_mean_13, None, priority5),
          CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_mean_13, None, priority5),
          CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_mean_13, None, priority5),
          CG.ClinicalGoal(ROIS.retina_l.name, at_most, dose_at_abs_volume, TOL.retina_v003_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.retina_r.name, at_most, dose_at_abs_volume, TOL.retina_v003_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.cornea_l.name, at_most, dose_at_abs_volume, TOL.cornea_v003_13_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.cornea_r.name, at_most, dose_at_abs_volume, TOL.cornea_v003_13_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_v003_13_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.hippocampus_l.name, at_most, dose_at_volume, TOL.hippocampus_13_v40, pc40, priority4),
          CG.ClinicalGoal(ROIS.hippocampus_r.name, at_most, dose_at_volume, TOL.hippocampus_13_v40, pc40, priority4)
          #CG.ClinicalGoal(ROIS.retina_l_prv.name, at_most, dose_at_abs_volume, TOL.retina_prv_v003_33_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.retina_r_prv.name, at_most, dose_at_abs_volume, TOL.retina_prv_v003_33_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.optic_chiasm_prv.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_prv_33_v003_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.optic_nrv_l_prv.name, at_most, dose_at_abs_volume, TOL.optic_nrv_prv_33_v003_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.optic_nrv_r_prv.name, at_most, dose_at_abs_volume, TOL.optic_nrv_prv_33_v003_adx, cc0_03, priority7),
          #CG.ClinicalGoal(ROIS.brainstem_surface_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_prv_33_v003_adx, cc0_03, priority7)
        ]
      else:
        brain_oars = [
          CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brain_gtv.name, at_most, volume_at_dose,pc50, TOL.brain_ptv_30_mean, priority5),
          CG.ClinicalGoal(ROIS.brainstem_surface.name, at_most, dose_at_abs_volume, TOL.brainstem_surface_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.brainstem_core.name, at_most, dose_at_abs_volume, TOL.brainstem_core_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_chiasm.name, at_most, dose_at_abs_volume, TOL.optic_chiasm_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_l.name, at_most, dose_at_abs_volume, TOL.optic_nrv_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.optic_nrv_r.name, at_most, dose_at_abs_volume, TOL.optic_nrv_v003_adx, cc0_03, priority2),
          CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean_tinnitus, None, priority5),
          CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean_tinnitus, None, priority5),
          CG.ClinicalGoal(ROIS.lacrimal_l.name, at_most, average_dose, TOL.lacrimal_mean, None, priority5),
          CG.ClinicalGoal(ROIS.lacrimal_r.name, at_most, average_dose, TOL.lacrimal_mean, None, priority5),
          CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_mean, None, priority5),
          CG.ClinicalGoal(ROIS.pituitary.name, at_most, average_dose, TOL.pituitary_2_mean, None, priority5),
          CG.ClinicalGoal(ROIS.retina_l.name, at_most, dose_at_abs_volume, TOL.retina_v003_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.retina_r.name, at_most, dose_at_abs_volume, TOL.retina_v003_adx, cc0_03, priority4),
          CG.ClinicalGoal(ROIS.cornea_l.name, at_most, dose_at_abs_volume, TOL.cornea_v003_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.cornea_r.name, at_most, dose_at_abs_volume, TOL.cornea_v003_adx, cc0_03, priority5),
          CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_v003_adx, cc0_03, priority6),
          CG.ClinicalGoal(ROIS.cochlea_l.name, at_most, average_dose, TOL.cochlea_mean, None, priority4),
          CG.ClinicalGoal(ROIS.cochlea_r.name, at_most, average_dose, TOL.cochlea_mean, None, priority4),
          CG.ClinicalGoal(ROIS.hippocampus_l.name, at_most, dose_at_volume, TOL.hippocampus_v40, pc40, priority6),
          CG.ClinicalGoal(ROIS.hippocampus_r.name, at_most, dose_at_volume, TOL.hippocampus_v40, pc40, priority6)
        ]
  return brain_oars

# Head and neck:
def head_neck_oars(ss, total_dose):
  if total_dose < 40:
    head_neck_oars = [
      #CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_v003_adx_eqd2, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx_eqd2, cc0_03, priority2),
      #CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcord_prv_v003_adx_eqd2, cc0_03, priority2) 
    ]
    if SSF.has_roi_with_shape(ss, ROIS.brainstem.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_v003_adx_eqd2, cc0_03, priority2),
        #CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_v003_adx_eqd2, cc0_03, priority2)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.parotid_l.name) or SSF.has_roi_with_shape(ss, ROIS.parotid_r.name) :
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.parotid_l.name, at_most, average_dose, TOL.parotids_mean_eqd2, None, priority4),
        CG.ClinicalGoal(ROIS.parotid_r.name, at_most, average_dose, TOL.parotids_mean_eqd2, None, priority4),
      ])
    if SSF.has_roi_with_shape(ss, ROIS.submand_l.name) or  SSF.has_roi_with_shape(ss, ROIS.submand_r.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.submand_l.name, at_most, average_dose, TOL.submand_mean_eqd2, None, priority5),
        CG.ClinicalGoal(ROIS.submand_r.name, at_most, average_dose, TOL.submand_mean_eqd2, None, priority5),
      ])
    if SSF.has_roi_with_shape(ss, ROIS.a_carotid_l.name) or SSF.has_roi_with_shape(ss, ROIS.a_carotid_r.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.a_carotid_l.name, at_most, dose_at_abs_volume, TOL.carotid_v003_adx_eqd2, cc0_03, priority5),
        CG.ClinicalGoal(ROIS.a_carotid_r.name, at_most, dose_at_abs_volume, TOL.carotid_v003_adx_eqd2, cc0_03, priority5)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.oral_cavity.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.oral_cavity.name, at_most, average_dose, TOL.oral_cavity_mean_eqd2, None, priority5),
      ])
  else:
    head_neck_oars = [
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_v003_adx, cc0_03, priority2), 
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_45_v003_adx, cc0_03, priority2), 
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcord_prv_v003_adx, cc0_03, priority2), 
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_v0_03_adx, cc0_03, priority2) 
    ]
    if SSF.has_roi_with_shape(ss, ROIS.brainstem.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_v003_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.brainstem_prv.name, at_most, dose_at_abs_volume, TOL.brainstem_prv_v003_adx, cc0_03, priority2)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.parotid_l.name) :
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.parotid_l.name, at_most, average_dose, TOL.parotid_mean, None, priority4)
      ])

    if SSF.has_roi_with_shape(ss, ROIS.parotid_r.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.parotid_r.name, at_most, average_dose, TOL.parotid_mean, None, priority4)
      ])

    if SSF.has_roi_with_shape(ss, ROIS.submand_l.name): # egen for l og r sidan ikkje alltid begge er med og da stopper skriptet
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.submand_l.name, at_most, average_dose, TOL.submand_mean, None, priority5),
      ])
    if SSF.has_roi_with_shape(ss, ROIS.submand_r.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.submand_r.name, at_most, average_dose, TOL.submand_mean, None, priority5),
      ])

    if SSF.has_roi_with_shape(ss, ROIS.pharynx_constr_s.name) or SSF.has_roi_with_shape(ss, ROIS.pharynx_constr_i.name) or SSF.has_roi_with_shape(ss, ROIS.pharynx_constr_m.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.pharynx_constr_s.name, at_most, average_dose, TOL.pharynx_constr_mean, None, priority5),
        CG.ClinicalGoal(ROIS.pharynx_constr_m.name, at_most, average_dose, TOL.pharynx_constr_mean, None, priority5),
        CG.ClinicalGoal(ROIS.pharynx_constr_i.name, at_most, average_dose, TOL.pharynx_constr_mean, None, priority5)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.a_carotid_l.name) or SSF.has_roi_with_shape(ss, ROIS.a_carotid_r.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.a_carotid_l.name, at_most, dose_at_abs_volume, TOL.carotid_v003_adx, cc0_03, priority5),
        CG.ClinicalGoal(ROIS.a_carotid_r.name, at_most, dose_at_abs_volume, TOL.carotid_v003_adx, cc0_03, priority5)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.oral_cavity.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.oral_cavity.name, at_most, average_dose, TOL.oral_cavity_mean, None, priority5),
      ])
    if SSF.has_roi_with_shape(ss, ROIS.esophagus.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.esophagus.name, at_most, average_dose, TOL.esophagus_mean_head, None, priority5),
      ])
    if SSF.has_roi_with_shape(ss, ROIS.larynx_sg.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.larynx_sg.name, at_most, average_dose, TOL.larynx_sg_mean, None, priority5),
      ])
    if SSF.has_roi_with_shape(ss, ROIS.larynx_g.name):
      head_neck_oars.extend([
        CG.ClinicalGoal(ROIS.larynx_g.name, at_most, average_dose, TOL.larynx_sg_mean, None, priority5),
      ])
  return head_neck_oars

# Breast tangential:
breast_tang_oars = [
  CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_breast, None, priority3),
  CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc15, TOL.lung_v15_adx, priority4),
  CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc15, TOL.lung_v15_adx, priority4)
]


# Breast with regional lymph nodes, clinical goal for 'Humeral_L' is added for left sided and vice versa
def breast_oars(region_code, nr_fractions, target):
  breast = [
    CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_breast_15, None, priority4),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx_chemo, cc0_03, priority2),
  ]
  if region_code in RC.breast_l_codes: # Left
    contralateral_lung = ROIS.lung_r.name
    ipsilateral_lung = ROIS.lung_l.name
    contralateral_breast = ROIS.breast_r.name
  else: # Right
    contralateral_lung = ROIS.lung_l.name
    ipsilateral_lung = ROIS.lung_r.name
    contralateral_breast = ROIS.breast_l.name
  if target in [ROIS.ctv_p.name, ROIS.ctv.name, ROIS.ctv_boost.name]: # Not bilateral
    breast.extend([
      CG.ClinicalGoal(contralateral_breast, at_most, average_dose, TOL.contralat_breast_mean, None, priority5),
    ])
    if region_code in RC.breast_reg_codes: # Breast regional
      breast.extend([
        CG.ClinicalGoal(contralateral_lung, at_most, average_dose, TOL.lung_contralateral_mean_reg, None, priority5)
      ])
    elif region_code in RC.breast_tang_and_partial_codes: # Breast only or boost
      breast.extend([
        CG.ClinicalGoal(contralateral_lung, at_most, average_dose, TOL.lung_contralateral_mean, None, priority5)
      ])
  else: # Bilateral
    if region_code in RC.breast_reg_codes: # Breast regional
      breast.extend([
        CG.ClinicalGoal(contralateral_lung, at_most, volume_at_dose, pc33, TOL.lung_v30_adx_15, priority4),
        CG.ClinicalGoal(contralateral_lung, at_most, volume_at_dose, pc55, TOL.lung_v65_adx_15, priority5),
      ])
    elif region_code in RC.breast_tang_codes: # Breast only or boost
      breast.extend([
        CG.ClinicalGoal(contralateral_lung, at_most, volume_at_dose, pc15, TOL.lung_v15_adx, priority4),
      ])
    elif region_code in RC.breast_partial_codes: # Breast boost, with bilateral breast
      breast.extend([
        CG.ClinicalGoal(contralateral_lung, at_most, average_dose, TOL.lung_contralateral_mean, None, priority5) # Ipsilateral lung?
      ])
  if region_code in RC.breast_reg_codes: # Breast regional
    breast.extend([
      CG.ClinicalGoal(ipsilateral_lung, at_most, volume_at_dose, pc33, TOL.lung_v30_adx_15, priority4),
      CG.ClinicalGoal(ipsilateral_lung, at_most, volume_at_dose, pc55, TOL.lung_v65_adx_15, priority5),
    ])
  elif region_code in RC.breast_tang_codes: # Breast only 
    breast.extend([
      CG.ClinicalGoal(ipsilateral_lung, at_most, volume_at_dose, pc15, TOL.lung_v15_adx, priority4),
    ])
      
  return breast

# Øsofagus
def esophagus_oars(ss, total_dose):
  esophagus = [
    CG.ClinicalGoal(ROIS.lung_r.name, at_most, volume_at_dose, pc20, TOL.lung_v30_adx, priority6),
    CG.ClinicalGoal(ROIS.lung_l.name, at_most, volume_at_dose, pc20, TOL.lung_v30_adx, priority6),
    CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc20, TOL.lung_v30_adx, priority6),
    CG.ClinicalGoal(ROIS.lungs.name, at_most, average_dose, TOL.lung_mean, None, priority4),
    CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc50, TOL.lung_v55_adx, priority7),
    CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx, priority4), 
    CG.ClinicalGoal(ROIS.kidneys.name, at_most, average_dose, TOL.kidney_mean_18, None, priority4),#kidneys?
    CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx, priority4), 
    CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_18, None, priority4),#kidneys?
    CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx, priority4), 
    CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_18, None, priority4),#kidneys?
    CG.ClinicalGoal(ROIS.liver.name, at_most, volume_at_dose, pc60, TOL.liver_v60_adx, priority7),
    CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_v30_eso_adx, priority5),
    CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_v30_eso_adx, None, priority5),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcord_v003_adx, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.spinal_canal_prv.name, at_most, dose_at_abs_volume, TOL.spinalcord_prv_v003_adx, cc0_03, priority7)
  ]
  if SSF.has_roi_with_shape(ss, ROIS.stomach.name):
    esophagus.extend([
      CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_v003_adx, cc0_03, priority8)
    ])
  return esophagus

# Lung:
# In cases where a GTV/IGTV is present, clinical goals are created for 'Lungs-GTV'/'Lungs-IGTV' instead of 'Lungs'.
def lung_oars(ss, total_dose, nr_fractions):
  narlal = False
  fraction_dose = total_dose/nr_fractions
  lung = [
    CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc20, TOL.heart_narlal_v20_adx, priority4),
    CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_v30_adx, priority4),
    CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc50, TOL.heart_narlal_v50_adx, priority4),
    CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean, None, priority4),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume,  TOL.esophagus_v1_adx,cc1, priority4)
  ]
  if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
    l = ROIS.lungs_gtv.name
  elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
    l = ROIS.lungs_igtv.name
  else:
    l = ROIS.lungs.name
  lung.extend([
    CG.ClinicalGoal(l, at_most, volume_at_dose, pc35, TOL.lung_v35_adx, priority4),
    CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_v55_adx, priority4),
    CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_mean, None, priority4)
  ])
  if nr_fractions == 33:
    lung.extend([
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_33_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_33_v0_03_adx_chemo, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_33_v0_03_adx_chemo, cc0_03, priority6)
    ])
    optional_clinical_goals = [
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinalcanal_prv_33_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinalcord_33_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.esophagus_prv.name, at_most, dose_at_abs_volume,  TOL.esophagus_v1_adx,cc1, priority4),
      CG.ClinicalGoal(ROIS.trachea_prv.name, at_most, dose_at_abs_volume,  TOL.trachea_prv_v1_33_adx ,cc1, priority4),
      CG.ClinicalGoal(ROIS.bronchus_prv.name, at_most, dose_at_abs_volume,  TOL.bronchus_prv_v1_33_adx ,cc1, priority4),
      CG.ClinicalGoal(ROIS.connective_tissue.name, at_most, dose_at_abs_volume,  TOL.connective_tissue_v1_33_adx ,cc1, priority4),
      CG.ClinicalGoal(ROIS.chestwall.name, at_most, dose_at_abs_volume,  TOL.chestwall_v1_33_adx ,cc1, priority4),
      CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume,  TOL.trachea_v1_33_adx ,cc1, priority5),
      CG.ClinicalGoal(ROIS.bronchus.name, at_most, dose_at_abs_volume,  TOL.bronchus_v1_33_adx ,cc1, priority5),
      CG.ClinicalGoal(ROIS.a_aorta.name, at_most, dose_at_abs_volume,  TOL.aorta_v1_33_adx ,cc1, priority5),
    ]
    for cg in optional_clinical_goals:
      if SSF.has_roi_with_shape(ss, cg.name):
        lung.extend([cg])
        if cg.name == 'Esophagus_PRV':
          narlal = True
    if narlal:
      lung.extend([CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume,  TOL.heart_v1_33_adx ,cc1, priority4)])        
  elif nr_fractions == 30:
    if total_dose == 60 and fraction_dose == 1.5:
      lung.extend([
        CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_40_v0_03_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_40_v0_03_adx_chemo, cc0_03, priority6),
        CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_40_v0_03_adx_chemo, cc0_03, priority2)
      ])
    elif total_dose == 60 and fraction_dose == 2:
      lung.extend([
        CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_30_v0_03_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_30_v0_03_adx_chemo, cc0_03, priority6),
        CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_30_v0_03_adx_chemo, cc0_03, priority2)
      ])
    elif total_dose == 45:
      lung.extend([
        CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_30_2_v0_03_adx, cc0_03, priority2),
        CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_30_2_v0_03_adx_chemo, cc0_03, priority6),
        CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_30_2_v0_03_adx_chemo, cc0_03, priority2)
      ])
  elif nr_fractions == 35:
    lung.extend([
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_35_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_35_v0_03_adx_chemo, cc0_03, priority6),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_35_v0_03_adx_chemo, cc0_03, priority2)
    ])
  elif nr_fractions == 40:
    lung.extend([
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_40_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_40_v0_03_adx_chemo, cc0_03, priority6),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_40_v0_03_adx_chemo, cc0_03, priority2)
    ])
  elif nr_fractions == 15:
    lung.extend([
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_15_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_15_v0_03_adx_chemo, cc0_03, priority6),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_15_v0_03_adx_chemo, cc0_03, priority2)
    ])
  elif nr_fractions == 17:
    lung.extend([
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_17_v0_03_adx, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_17_v0_03_adx_chemo, cc0_03, priority6),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_17_v0_03_adx_chemo, cc0_03, priority2)
    ])
  else:

    lung = [
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority2),
      #CG.ClinicalGoal(ROIS.x_spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx, cc0_03, priority6),
      CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_v0_03_adx_chemo, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc25, TOL.heart_narlal_35_v20_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_35_v30_adx, priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_35_v50_adx, priority4), #gj snitt 35
      #CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_v1_35_adx,cc1,  priority4),
      CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean, None, priority6)
    ]
    if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
      l = ROIS.lungs_gtv.name
    elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
      l = ROIS.lungs_igtv.name
    else:
      l = ROIS.lungs.name
    lung.extend([
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc35, TOL.lung_35_v35_adx, priority4),
      CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_35_v55_adx, priority4),
      CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_35_mean, None, priority4)
    ])
    #if nr_fractions == 10: Tilpasset triplex studien. Skal disse være i tillegg eller i stedet for de over?
    #  lung.extend([
    #    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcanal_10_v0_03_adx, cc0_03, priority2),
    #    CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc10, TOL.heart_v10_adx, priority4),
    #    #CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc25, TOL.heart_narlal_35_v20_adx, priority4),
    #    #CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_35_v30_adx, priority4),
    #    #CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_35_v50_adx, priority4), #gj snitt 35
    #    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_10_v0_03_adx,cc0_03,  priority4),
    #    CG.ClinicalGoal(ROIS.esophagus.name, at_most, average_dose, TOL.esophagus_mean, None, priority6),
    #    CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_eqd2, None, priority6)
    # ])
    #  if SSF.has_roi_with_shape(ss, ROIS.lungs_gtv.name):
    #    l = ROIS.lungs_gtv.name
    #  elif SSF.has_roi_with_shape(ss, ROIS.lungs_igtv.name):
    #    l = ROIS.lungs_igtv.name
    #  else:
    #    l = ROIS.lungs.name
    #  lung.extend([
    #    CG.ClinicalGoal(l, at_most, volume_at_dose, pc30, TOL.lung_v30_adx, priority4),
    #    CG.ClinicalGoal(l, at_most, volume_at_dose, pc55, TOL.lung_v55_adx, priority4),
    #    CG.ClinicalGoal(l, at_most, average_dose, TOL.lung_10_mean, None, priority4)
    #  ])
  return lung



# Lung SBRT:
# For a treatment with three fractions, from the region code, one finds if the
# tumor is right or left sided and clinical goals are added accordingly.
def lung_stereotactic_3fx_oars(ss, region_code):
  lung = [
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0_35, cc0_35, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0, cc0_03, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v5, cc5, priority2),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v10, cc10, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v15, cc15, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_3fx_v5, cc5, priority1),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_3fx_v0, cc0_03, priority1),
    #CG.ClinicalGoal(ROIS.chestwall.name, at_most, abs_volume_at_dose, cc30, TOL.chestwall_sbrt_3fx_v30, priority4),
    CG.ClinicalGoal(ROIS.chestwall.name, at_most, dose_at_abs_volume,  TOL.chestwall_sbrt_3fx_v30,cc30, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_3fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_3fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_3fx_v10, priority2),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc37, TOL.lung_sbrt_3fx_v37, priority2),
    CG.ClinicalGoal(ROIS.liver.name, at_most, average_dose, TOL.liver_sbrt_3fx_mean, None, priority2),
    CG.ClinicalGoal(ROIS.ribs.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0_03, priority4),
  ]
  if region_code in [248, 250]: # Right
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_3fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_3fx_v5, cc5, priority1)
    ])
  elif region_code in [247, 249]: # Left
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_3fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_3fx_v5, cc5, priority1)
    ])
  else:
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_3fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_3fx_v5, cc5, priority1),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_3fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_3fx_v5, cc5, priority1)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.brachial_plexus.name):
    lung.extend([
      CG.ClinicalGoal(ROIS.brachial_plexus.name, at_most, dose_at_abs_volume, TOL.brachial_sbrt_sbrt_3fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.brachial_plexus.name, at_most, dose_at_abs_volume, TOL.brachial_sbrt_sbrt_3fx_v3, cc3, priority1)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.stomach.name):
    lung.extend([
      CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v10, cc10, priority4)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
    lung.extend([
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc25, TOL.kidneys_3fx_v25, priority4)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
    lung.extend([
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc25, TOL.kidneys_3fx_v25, priority4)
    ])
  return lung


# Lung SBRT:
# For a treatment with five fractions, from the region code, one finds if the
# tumor is right or left sided and clinical goals are added accordingly.
def lung_stereotactic_5fx_oars(ss, region_code):
  lung = [
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_5fx_v0_35, cc0_35, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_5fx_v0, cc0_03, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_5fx_v5, cc5, priority2),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_5fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v10, cc10, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_5fx_v15, cc15, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_5fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.liver.name, at_most, average_dose, TOL.liver_sbrt_3fx_mean, None, priority2),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_5fx_v5, cc5, priority1),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_5fx_v0, cc0_03, priority1),
    #CG.ClinicalGoal(ROIS.chestwall.name, at_most, abs_volume_at_dose, cc30, TOL.chestwall_sbrt_5fx_v30, priority4),
    CG.ClinicalGoal(ROIS.chestwall.name, at_most, dose_at_abs_volume,  TOL.chestwall_sbrt_5fx_v30, cc30, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_5fx_v10, priority2),
    #CG.ClinicalGoal(ROIS.bronchus.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v0, cc0, priority1),
    #CG.ClinicalGoal(ROIS.bronchus.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v5, cc5, priority1),
    CG.ClinicalGoal(ROIS.ribs.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc37, TOL.lung_sbrt_5fx_v37, priority2)
  ]
  if SSF.has_roi_with_shape(ss, ROIS.brachial_plexus.name):
    lung.extend([
      CG.ClinicalGoal(ROIS.brachial_plexus.name, at_most, dose_at_abs_volume, TOL.brachial_sbrt_sbrt_5fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.brachial_plexus.name, at_most, dose_at_abs_volume, TOL.brachial_sbrt_sbrt_5fx_v3, cc3, priority1)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.stomach.name):
    lung.extend([
      CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_5fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_5fx_v10, cc10, priority4)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
    lung.extend([
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc25, TOL.kidneys_5fx_v25, priority4)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
    lung.extend([
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc25, TOL.kidneys_5fx_v25, priority4)
    ])
  if region_code in [248, 250]: # Right
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v5, cc5, priority1)
    ])
  elif region_code in [247, 249]: # Left
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v5, cc5, priority1)
    ])
  else:
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v5, cc5, priority1),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v5, cc5, priority1)
    ])
  return lung

# Lung SBRT:
# For a treatment with eight fractions, from the region code, one finds if the
# tumor is right or left sided and clinical goals are added accordingly.
def lung_stereotactic_8fx_oars(region_code):
  lung= [
    #CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_5fx_v1_2, cc1_2, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_8fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_5fx_v5, cc5, priority2),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_8fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v10, cc10, priority2), #?
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_5fx_v15, cc15, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_8fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.liver.name, at_most, average_dose, TOL.liver_sbrt_3fx_mean, None, priority3),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_8fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.chestwall.name, at_most, abs_volume_at_dose, cc30, TOL.chestwall_sbrt_5fx_v30, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v0, cc0, priority4),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_8fx_v10, priority2),
  ]
  if region_code in [248, 250]: # Right
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_8fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_contra_sbrt_8fx_v0, cc0, priority1),
      #CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v4, cc4, priority1)
    ])
  elif region_code in [247, 249]: # Left
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_8fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_contra_sbrt_8fx_v0, cc0, priority1),
      #CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v4, cc4, priority1)
    ])
  else:
    lung.extend([
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_8fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_contra_sbrt_8fx_v0, cc0, priority1),
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_5fx_v4, cc4, priority1),
      CG.ClinicalGoal(ROIS.bronchus_l.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_8fx_v0, cc0, priority4),
      CG.ClinicalGoal(ROIS.bronchus_r.name, at_most, dose_at_abs_volume, TOL.bronchus_contra_sbrt_8fx_v0, cc0, priority1),
    ])
  return lung

def lung_stereotactic_12fx_oars(region_code):
  lung= [
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_12fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_12fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_12fx_v0, cc0, priority2),
    CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_12fx_v0, cc0, priority1),
    CG.ClinicalGoal(ROIS.lungs_igtv.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_12fx_v10, priority3),
    CG.ClinicalGoal(ROIS.bronchus.name, at_most, dose_at_abs_volume, TOL.bronchus_sbrt_12fx_v0, cc0, priority4)
  ]
# Liver stereotactic 3 fractions
def liver_stereotactic_3fx_oars(ss):
  liver = [
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0, cc0_03, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0_35, cc0_35, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v5, cc5, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v10, cc10, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v15, cc15, priority2),
    CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_3fx_v10, priority2),
    CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc37, TOL.lung_sbrt_3fx_v37, priority2),
    CG.ClinicalGoal(ROIS.chestwall.name, at_most, dose_at_abs_volume,  TOL.chestwall_sbrt_3fx_v30,cc30, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_3fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_3fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.duodenum.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.duodenum.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc25, TOL.kidneys_3fx_v25, priority3),
    CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc25, TOL.kidneys_3fx_v25, priority3),
    CG.ClinicalGoal(ROIS.ribs.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0_03, priority4),
  ]
  if SSF.has_roi_with_shape(ss, ROIS.bile_duct.name):
    liver.extend([
      CG.ClinicalGoal(ROIS.bile_duct.name, at_most, dose_at_abs_volume, TOL.bile_duct_sbrt_3fx_v0, cc0_03, priority5)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.bowel_small.name):
    liver.extend([
      CG.ClinicalGoal(ROIS.bowel_small.name, at_most, dose_at_abs_volume, TOL.bowel_small_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.bowel_small.name, at_most, dose_at_abs_volume, TOL.bowel_small_sbrt_3fx_v10, cc10, priority4),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.bowel_large.name):
    liver.extend([
      CG.ClinicalGoal(ROIS.bowel_large.name, at_most, dose_at_abs_volume, TOL.bowel_large_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.bowel_large.name, at_most, dose_at_abs_volume, TOL.bowel_large_sbrt_3fx_v20, cc20, priority4),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.liver_gtv.name):
    l = ROIS.liver_gtv.name
  elif SSF.has_roi_with_shape(ss, ROIS.liver_igtv.name):
    l = ROIS.liver_igtv.name
  elif SSF.has_roi_with_shape(ss, ROIS.liver_ctv.name):
    l = ROIS.liver_ctv.name
  elif SSF.has_roi_with_shape(ss, ROIS.liver_ictv.name):
    l = ROIS.liver_ictv.name
  else:
    l = ROIS.liver.name
  liver.extend([
    CG.ClinicalGoal(l, at_most, average_dose, TOL.liver_sbrt_3fx_mean, None, priority3),
  ])
  return liver

# Liver stereotactic 5 fractions
def liver_stereotactic_5fx_oars(ss):
  liver = [
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_5fx_v0, cc0_03, priority1),
    CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_5fx_v0_35, cc0_35, priority1),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_5fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_5fx_v5, cc5, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_5fx_v10, cc10, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_5fx_v0, cc0_03, priority2),
    CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_5fx_v15, cc15, priority2),
    CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_5fx_v10, priority2),
    CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc37, TOL.lung_sbrt_5fx_v37, priority2),
    CG.ClinicalGoal(ROIS.chestwall.name, at_most, dose_at_abs_volume,  TOL.chestwall_sbrt_5fx_v30, cc30, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_5fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.ribs.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_5fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_5fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_5fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.duodenum.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_5fx_v0, cc0_03, priority4),
    CG.ClinicalGoal(ROIS.duodenum.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_5fx_v10, cc10, priority4),
    CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc25, TOL.kidneys_5fx_v25, priority3),
    CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc25, TOL.kidneys_5fx_v25, priority3)
  ]
  if SSF.has_roi_with_shape(ss, ROIS.bile_duct.name):
    liver.extend([
      CG.ClinicalGoal(ROIS.bile_duct.name, at_most, dose_at_abs_volume, TOL.bile_duct_sbrt_5fx_v0, cc0_03, priority5),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.bowel_small.name):
    liver.extend([
      CG.ClinicalGoal(ROIS.bowel_small.name, at_most, dose_at_abs_volume, TOL.bowel_small_sbrt_5fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.bowel_small.name, at_most, dose_at_abs_volume, TOL.bowel_small_sbrt_5fx_v10, cc10, priority4),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.bowel_large.name):
    liver.extend([
      CG.ClinicalGoal(ROIS.bowel_large.name, at_most, dose_at_abs_volume, TOL.bowel_large_sbrt_5fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.bowel_large.name, at_most, dose_at_abs_volume, TOL.bowel_large_sbrt_5fx_v20, cc20, priority4),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.liver_gtv.name):
    l = ROIS.liver_gtv.name
  elif SSF.has_roi_with_shape(ss, ROIS.liver_igtv.name):
    l = ROIS.liver_igtv.name
  elif SSF.has_roi_with_shape(ss, ROIS.liver_ctv.name):
    l = ROIS.liver_ctv.name
  elif SSF.has_roi_with_shape(ss, ROIS.liver_ictv.name):
    l = ROIS.liver_ictv.name
  else:
    l = ROIS.liver.name
  liver.extend([
    CG.ClinicalGoal(l, at_most, average_dose, TOL.liver_sbrt_3fx_mean, None, priority3),
  ])
  return liver
# Gyn:
'''
gyn_45_oars = [
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority3),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority3),
  CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority2),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc2, TOL.bladder_v2_adx, priority4)
]
'''
def gyn_oars(pm, examination, ss, region_code, total_dose):
  if total_dose > 44:
    gyn_oars = [
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc85, TOL.bladder_v85_adx,  priority4),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc75, TOL.bladder_v75_adx,  priority4),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_abs_volume, TOL.femoral_v003_adx, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_abs_volume, TOL.femoral_v003_adx, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc95, TOL.rectum_v95_adx,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc85, TOL.rectum_v85_adx,  priority4)
      #CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_38_v003_adx, cc0_03, priority5),
      #CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinal_cord_prv_v003_adx, cc0_03, priority3),
    ]
    if region_code in RC.gyn_except_vulva_codes:
      gyn_oars.extend([
        CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_48_v003_adx, cc0_03, priority2)
      ])
    if 35 < total_dose < 54:
      gyn_oars.extend([
        CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc350, TOL.bowelbag_v350_adx, priority5),
        CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc100, TOL.bowelbag_v100_adx, priority5)
      ])
      if SSF.has_roi_with_shape(ss, ROIS.ctv_45.name):
        gyn_oars.extend([
          CG.ClinicalGoal(ROIS.bladder.name, at_most, dose_at_abs_volume, TOL.bladder_v003_adx, cc0_03, priority3),
          CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, dose_at_abs_volume, TOL.bowelbag_v003_adx, cc0_03, priority3),
          CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_v003_adx, cc0_03, priority3),
          CG.ClinicalGoal(ROIS.sigmoid.name, at_most, dose_at_abs_volume, TOL.sigmoid_v003_adx, cc0_03, priority4)
        ])
    elif total_dose > 54:
      gyn_oars.extend([
        CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc500, TOL.bowelbag_v350_adx, priority5),
        CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc250, TOL.bowelbag_v100_adx, priority5)
      ])
      if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
        gyn_oars.extend([
          CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_10, None, priority4),
          CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_10, None, priority4)
        ])
      oars = [ROIS.bladder, ROIS.rectum, ROIS.sigmoid, ROIS.bowel_bag]
      x_oars = [ROIS.x_bladder_ptv_n, ROIS.x_rectum_ptv_n, ROIS.x_sigmoid_ptv_n, ROIS.x_bowelbag_ptv_n]
      tolerances = [TOL.bladder_v003_adx,TOL.rectum_v003_adx,TOL.sigmoid_v003_adx,TOL.bowelbag_v003_adx]
      x_tolerances_57 = [TOL.bladder_v003_57_adx,TOL.rectum_v003_57_adx,TOL.sigmoid_v003_57_adx,TOL.bowelbag_v003_57_adx]
      x_tolerances_55 = [TOL.bladder_v003_55_adx,TOL.rectum_v003_55_adx,TOL.sigmoid_v003_55_adx,TOL.bowelbag_v003_55_adx]
      for i in range(len(oars)):
        if SSF.has_roi_with_shape(ss, oars[i].name):
          if SSF.has_roi_with_shape(ss, ROIS.ptv_n_57.name):
            gyn_oars.extend([
              CG.ClinicalGoal(oars[i].name, at_most, dose_at_abs_volume, x_tolerances_57[i], cc0_03, priority4),
              CG.ClinicalGoal(x_oars[i].name, at_most, dose_at_abs_volume, tolerances[i], cc0_03, priority7)
            ])
          else:
            if SSF.has_roi_with_shape(ss, ROIS.ptv_n_55.name):   
              gyn_oars.extend([
                CG.ClinicalGoal(oars[i].name, at_most, dose_at_abs_volume, x_tolerances_55[i], cc0_03, priority4),
                CG.ClinicalGoal(x_oars[i].name, at_most, dose_at_abs_volume, tolerances[i], cc0_03, priority7)
              ])
  else:
    gyn_oars = [
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc85, TOL.bladder_v85_adx_eqd2,  priority4),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc75, TOL.bladder_v75_adx_eqd2,  priority4),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_abs_volume, TOL.femoral_v003_adx_eqd2, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_abs_volume, TOL.femoral_v003_adx_eqd2, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc95, TOL.rectum_v95_adx_eqd2,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc85, TOL.rectum_v85_adx_eqd2,  priority4),
      CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc350, TOL.bowelbag_v350_adx_eqd2, priority5),
      CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc100, TOL.bowelbag_v100_adx_eqd2, priority5)
      #CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_cord_38_v003_adx, cc0_03, priority5),
      #CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinal_cord_prv_v003_adx, cc0_03, priority3),
    ]

  if SSF.has_roi_with_shape(ss, ROIS.ovary_r.name):
    gyn_oars.extend([
      CG.ClinicalGoal(ROIS.ovary_r.name, at_most, average_dose, TOL.ovary_mean_8, None, priority4),
      CG.ClinicalGoal(ROIS.ovary_l.name, at_most, average_dose, TOL.ovary_mean_8, None, priority4)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
    gyn_oars.extend([
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_5, None, priority4),
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_5, None, priority4)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.duodenum.name):
    gyn_oars.extend([
      CG.ClinicalGoal(ROIS.duodenum.name, at_most, abs_volume_at_dose, cc15, TOL.duodenum_v15_adx, priority6)

    ])
  return gyn_oars

def rectum_oars(total_dose):
  rectum_oars = [
    CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc310, TOL.bowelspace_25_v310_adx, priority5),
    CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc70, TOL.bowelspace_25_v70_adx, priority5),
  ]  
  if total_dose == 25:
    rectum_oars.extend([
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume, TOL.femoral_5_v2_adx, pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_5_v2_adx, pc2,  priority6),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, average_dose, TOL.bladder_mean_5_adx,None, priority5)
    ])
  else:
    rectum_oars.extend([
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume, TOL.femoral_25_v2_adx, pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_25_v2_adx, pc2,  priority6),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, average_dose, TOL.bladder_mean_25_adx,None, priority5)
    ])
  return rectum_oars

# Rectum re-irradiation:
rectum_re_oars = [
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume, TOL.femoral_30_v2_adx, pc2,  priority6),
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_30_v2_adx, pc2,  priority6),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc310, TOL.bowelspace_30_v310_adx, priority5),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc70, TOL.bowelspace_30_v70_adx, priority5),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, average_dose, TOL.bladder_mean_30_adx,None, priority5)
]
# Anus:
anus_oars = [
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_27_v2_adx, pc2, priority6),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume, TOL.femoral_27_v2_adx, pc2, priority6),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc310, TOL.bowelspace_27_v310_adx, priority5),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc70, TOL.bowelspace_27_v70_adx, priority5),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, average_dose, TOL.bladder_mean_27_adx, None,priority5)
]


# Bladder:
bladder_oars = [
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_bladder,  priority2),
  CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume, TOL.femoral_30_v2_adx, pc2,  priority6),
  CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_30_v2_adx, pc2,  priority6),
  #CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc35, TOL.rectum_v35_adx,  priority2),
  #CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc25, TOL.rectum_v25_adx,  priority2),
  #CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc15, TOL.rectum_v15_adx,  priority2),
  #CG.ClinicalGoal(ROIS.femoral_l.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority4),
  #CG.ClinicalGoal(ROIS.femoral_r.name, at_most, average_dose, TOL.femoral_mean_adx, None, priority4),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc195, TOL.bowelbag_v195_45_gy_adx, priority3)
]


# Prostate:
def prostate_oars(ss, total_dose):
  if total_dose in [55, 60]:
    prostate = [
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx_hypo, priority5),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc35, TOL.bladder_v35_adx_hypo, priority5),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc35, TOL.rectum_v35_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc25, TOL.rectum_v25_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx_hypo,  priority4),
      #CG.ClinicalGoal(ROIS.anal_canal.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.anal_canal.name, at_most, average_dose, TOL.anal_canal_mean_adx_hypo, None, priority5),
      CG.ClinicalGoal(ROIS.penile_bulb.name, at_most, volume_at_dose, pc90, TOL.penile_bulb_v90_adx_hypo,  priority6),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume,  TOL.femoral_v2_adx_hypo,pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_v2_adx_hypo,pc2,   priority6)
    ]
  elif total_dose == 67.5:
    prostate = [
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx_hypo2_7, priority5),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc35, TOL.bladder_v35_adx_hypo2_7, priority5),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc25, TOL.bladder_v25_adx_hypo2_7, priority5),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_hypo2_7,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc35, TOL.rectum_v35_adx_hypo2_7,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc25, TOL.rectum_v25_adx_hypo2_7,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx_hypo2_7,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc15, TOL.rectum_v15_adx_hypo2_7, priority4),
      CG.ClinicalGoal(ROIS.penile_bulb.name, at_most, volume_at_dose, pc90, TOL.penile_bulb_v90_adx_hypo2_7,  priority6),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume, TOL.femoral_v2_adx_hypo2_7, pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_v2_adx_hypo2_7, pc2,  priority6),
      CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx_hypo2_7, priority5),
      CG.ClinicalGoal(ROIS.anal_canal.name, at_most, average_dose, TOL.anal_canal_mean_adx_hypo2_7, None, priority5)
    ]
  elif total_dose > 68:
    prostate = [
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx, priority5),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc35, TOL.bladder_v35_adx, priority5),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc35, TOL.rectum_v35_adx,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc25, TOL.rectum_v25_adx,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx,  priority4),
      CG.ClinicalGoal(ROIS.penile_bulb.name, at_most, volume_at_dose, pc90, TOL.penile_bulb_v90_adx,  priority6),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume, TOL.femoral_v2_adx,pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_v2_adx,pc2,  priority6),
      CG.ClinicalGoal(ROIS.bowel_space.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx, priority5)
    ]
    if total_dose > 70:
      prostate.extend([
        CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc15, TOL.rectum_v15_adx,  priority4),
        CG.ClinicalGoal(ROIS.anal_canal.name, at_most, volume_at_dose, pc15, TOL.rectum_v15_adx,  priority4),
        CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc25, TOL.bladder_v25_adx, priority5),
        CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc15, TOL.bladder_v15_adx, priority5)
      ])
    else:
      prostate.extend([
        CG.ClinicalGoal(ROIS.anal_canal.name, at_most, volume_at_dose, pc20, TOL.rectum_v20_adx,  priority4) # endre til gjennomsnittdose (40 Gy EQD2)
      ])

  elif total_dose <40:
    prostate = [
      CG.ClinicalGoal(ROIS.anal_canal.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_hypo,  priority4),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_volume,  TOL.femoral_v2_adx_hypo,pc2,  priority6),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_volume, TOL.femoral_v2_adx_hypo,pc2,   priority6),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx_hypo, priority5)
    ]

  return prostate

# Bone/Spine SBRT:
# For a treatment with three fractions, from the region code, one finds whether the
# tumor is in the thoracic or pelvis area, and clinical goals are added accordingly.
# There is also a separation between spine/non-spine treatment.
def bone_stereotactic_3fx_oars(ss, region_code):
  spine= [
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_3fx_v10, cc10, priority5),
    CG.ClinicalGoal(ROIS.skin.name, at_most, dose_at_abs_volume, TOL.skin_sbrt_3fx_v0, cc0_03, priority5),
  ]
  if region_code in RC.stereotactic_spine_thorax_codes+RC.stereotactic_spine_pelvis_codes+RC.palliative_cervical_codes:
    spine.extend([
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0_35, cc0_35, priority1),
      CG.ClinicalGoal(ROIS.spinal_cord.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0, cc0_03, priority1),
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0_35, cc0_35, priority1),
      CG.ClinicalGoal(ROIS.spinal_cord_prv.name, at_most, dose_at_abs_volume, TOL.spinal_canal_sbrt_3fx_v0, cc0_03, priority1),
    ])
    if region_code in RC.stereotactic_spine_thorax_codes+RC.palliative_cervical_codes:
      spine.extend([
        CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v5, cc5, priority2),
        CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v0, cc0_03, priority2),
        #CG.ClinicalGoal(ROIS.esophagus.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v5, cc5, priority2),
        CG.ClinicalGoal(ROIS.esophagus_prv.name, at_most, dose_at_abs_volume, TOL.esophagus_sbrt_3fx_v0, cc0_03, priority6),

        CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_3fx_v5, cc5, priority2),
        CG.ClinicalGoal(ROIS.trachea.name, at_most, dose_at_abs_volume, TOL.trachea_sbrt_3fx_v0, cc0_03, priority2),
        #CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v0, cc0_03, priority2),
        #CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v10, cc10, priority2),
      ])
  if region_code in RC.stereotactic_thorax_codes:
    spine.extend([  
      CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc10, TOL.lung_sbrt_3fx_v10, priority2),
      CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc37, TOL.lung_sbrt_3fx_v37, priority2),
      CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v15, cc15, priority2),
      CG.ClinicalGoal(ROIS.heart.name, at_most, dose_at_abs_volume, TOL.heart_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.chestwall.name, at_most, dose_at_abs_volume, TOL.chestwall_sbrt_3fx_v30, cc30, priority4),
      CG.ClinicalGoal(ROIS.ribs.name, at_most, dose_at_abs_volume, TOL.ribs_sbrt_3fx_v0, cc0_03, priority4),
    ])
  if region_code in RC.stereotactic_spine_pelvis_codes:
    spine.extend([
      CG.ClinicalGoal(ROIS.cauda_equina.name, at_most, dose_at_abs_volume, TOL.cauda_equina_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.cauda_equina.name, at_most, dose_at_abs_volume, TOL.cauda_equina_sbrt_3fx_v3, cc3, priority4),
      CG.ClinicalGoal(ROIS.cauda_equina_prv.name, at_most, dose_at_abs_volume, TOL.cauda_equina_sbrt_3fx_v0, cc0_03, priority6),
      CG.ClinicalGoal(ROIS.cauda_equina_prv.name, at_most, dose_at_abs_volume, TOL.cauda_equina_sbrt_3fx_v3, cc3, priority6)
    ])
  if region_code in RC.stereotactic_spine_pelvis_codes or region_code in RC.stereotactic_pelvis_codes:
    spine.extend([
      CG.ClinicalGoal(ROIS.bowel_small.name, at_most, dose_at_abs_volume, TOL.bowel_small_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.bowel_small.name, at_most, dose_at_abs_volume, TOL.bowel_small_sbrt_3fx_v10, cc10, priority2),
      CG.ClinicalGoal(ROIS.bowel_small_prv.name, at_most, dose_at_abs_volume, TOL.bowel_small_sbrt_3fx_v0, cc0_03, priority6),
      #CG.ClinicalGoal(ROIS.bowel_small_prv.name, at_most, dose_at_abs_volume, TOL.bowel_small_sbrt_3fx_v10, cc10, priority6),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.rectum.name, at_most, dose_at_abs_volume, TOL.rectum_sbrt_3fx_v20, cc20, priority2),
      CG.ClinicalGoal(ROIS.rectum_prv.name, at_most, dose_at_abs_volume, TOL.rectum_sbrt_3fx_v0, cc0_03, priority6),
      #CG.ClinicalGoal(ROIS.rectum_prv.name, at_most, dose_at_abs_volume, TOL.rectum_sbrt_3fx_v20, cc20, priority6),
      CG.ClinicalGoal(ROIS.bowel_large.name, at_most, dose_at_abs_volume, TOL.bowel_large_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.bowel_large.name, at_most, dose_at_abs_volume, TOL.bowel_large_sbrt_3fx_v20, cc20, priority2),
      CG.ClinicalGoal(ROIS.bowel_large_prv.name, at_most, dose_at_abs_volume, TOL.bowel_large_sbrt_3fx_v0, cc0_03, priority6),
      #CG.ClinicalGoal(ROIS.bowel_large_prv.name, at_most, dose_at_abs_volume, TOL.bowel_large_sbrt_3fx_v20, cc20, priority6),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, dose_at_abs_volume, TOL.bladder_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.bladder.name, at_most, dose_at_abs_volume, TOL.bladder_sbrt_3fx_v15, cc15, priority2),
      CG.ClinicalGoal(ROIS.bladder_prv.name, at_most, dose_at_abs_volume, TOL.bladder_sbrt_3fx_v0, cc0_03, priority6),   
    ])#BLADDER
  if region_code in RC.stereotactic_pelvis_codes:
    spine.extend([
      CG.ClinicalGoal(ROIS.penile_bulb.name, at_most, dose_at_abs_volume, TOL.penile_bulb_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.penile_bulb.name, at_most, dose_at_abs_volume, TOL.penile_bulb_sbrt_3fx_v3, cc3, priority4),
      CG.ClinicalGoal(ROIS.femoral_r.name, at_most, dose_at_abs_volume, TOL.femoral_sbrt_3fx_v10, cc10, priority4),
      CG.ClinicalGoal(ROIS.femoral_l.name, at_most, dose_at_abs_volume, TOL.femoral_sbrt_3fx_v10, cc10, priority4)
    ])
      
  if SSF.has_roi_with_shape(ss, ROIS.ureter.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.ureter.name, at_most, dose_at_abs_volume, TOL.ureter_sbrt_3fx_v0, cc0_03, priority5)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.anal_canal.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.anal_canal.name, at_most, dose_at_abs_volume, TOL.anal_canal_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.anal_canal_prv.name, at_most, dose_at_abs_volume, TOL.anal_canal_sbrt_3fx_v0, cc0_03, priority6)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.sacral_plexus.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.sacral_plexus.name, at_most, dose_at_abs_volume, TOL.sacral_plexus_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.sacral_plexus.name, at_most, dose_at_abs_volume, TOL.sacral_plexus_sbrt_3fx_v3, cc3, priority4),
      CG.ClinicalGoal(ROIS.sacral_plexus_prv.name, at_most, dose_at_abs_volume, TOL.sacral_plexus_sbrt_3fx_v0, cc0_03, priority6),
      CG.ClinicalGoal(ROIS.sacral_plexus_prv.name, at_most, dose_at_abs_volume, TOL.sacral_plexus_sbrt_3fx_v3, cc3, priority6)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.nerve_roots.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.nerve_roots.name, at_most, dose_at_abs_volume, TOL.nerve_root_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.nerve_roots.name, at_most, dose_at_abs_volume, TOL.nerve_root_sbrt_3fx_v3, cc3, priority4),
      CG.ClinicalGoal(ROIS.nerve_roots_prv.name, at_most, dose_at_abs_volume, TOL.nerve_root_sbrt_3fx_v0, cc0_03, priority6),
      CG.ClinicalGoal(ROIS.nerve_roots_prv.name, at_most, dose_at_abs_volume, TOL.nerve_root_sbrt_3fx_v3, cc3, priority6)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.nerve_peripheral.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.nerve_peripheral.name, at_most, dose_at_abs_volume, TOL.nerve_peripheral_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.nerve_peripheral_prv.name, at_most, dose_at_abs_volume, TOL.nerve_peripheral_sbrt_3fx_v0, cc0_03, priority6),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.brachial_plexus.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.brachial_plexus.name, at_most, dose_at_abs_volume, TOL.brachial_sbrt_sbrt_3fx_v0, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.brachial_plexus.name, at_most, dose_at_abs_volume, TOL.brachial_sbrt_sbrt_3fx_v3, cc3, priority1)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.stomach.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.stomach.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v10, cc10, priority2),
      CG.ClinicalGoal(ROIS.stomach_prv.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v0, cc0_03, priority6),
      #CG.ClinicalGoal(ROIS.stomach_prv.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v10, cc10, priority6)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.duodenum.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.duodenum.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.duodenum.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v10, cc10, priority2),
      CG.ClinicalGoal(ROIS.duodenum_prv.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v0, cc0_03, priority6),
      #CG.ClinicalGoal(ROIS.duodenum_prv.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v10, cc10, priority6)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.great_vessels.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v10, cc10, priority2),
      CG.ClinicalGoal(ROIS.great_vessels.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v0, cc0_03, priority2),
      CG.ClinicalGoal(ROIS.great_vessels_prv.name, at_most, dose_at_abs_volume, TOL.greatves_sbrt_3fx_v0, cc0_03, priority6),
      #CG.ClinicalGoal(ROIS.duodenum_prv.name, at_most, dose_at_abs_volume, TOL.stomach_sbrt_3fx_v10, cc10, priority6)
    ]) 
  if SSF.has_roi_with_shape(ss, ROIS.kidney_r.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.kidney_r.name, at_most, volume_at_dose, pc25, TOL.kidneys_3fx_v25, priority2),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.kidney_l.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.kidney_l.name, at_most, volume_at_dose, pc25, TOL.kidneys_3fx_v25, priority2),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.humeral_l.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.humeral_l.name, at_most, dose_at_abs_volume, TOL.humeral_sbrt_3fx_v10, cc10, priority4)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.humeral_r.name):
    spine.extend([
      CG.ClinicalGoal(ROIS.humeral_r.name, at_most, dose_at_abs_volume, TOL.humeral_sbrt_3fx_v10, cc10, priority4)
    ])
  return spine



# Palliative:
head = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx_eqd2, cc0_03, priority1),
  CG.ClinicalGoal(ROIS.lens_l.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx_eqd2, cc0_03, priority4),
  CG.ClinicalGoal(ROIS.lens_r.name, at_most, dose_at_abs_volume, TOL.lens_v003_adx_eqd2, cc0_03, priority4),
  CG.ClinicalGoal(ROIS.brainstem.name, at_most, dose_at_abs_volume, TOL.brainstem_v003_adx_eqd2, cc0_03, priority2),
  CG.ClinicalGoal(ROIS.brain.name, at_most, dose_at_abs_volume, TOL.brain_v003_eqd2, cc0_03, priority3)
]
neck = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx_eqd2, cc0_03, priority1),
  CG.ClinicalGoal(ROIS.parotid_r.name, at_most, average_dose, TOL.parotids_mean_eqd2, None, priority4),
  CG.ClinicalGoal(ROIS.parotid_l.name, at_most, average_dose, TOL.parotids_mean_eqd2, None, priority4),
  CG.ClinicalGoal(ROIS.oral_cavity.name, at_most, average_dose, TOL.oral_cavity_mean_eqd2, None, priority5),
]
thorax = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx_eqd2, cc0_03, priority1),
  CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_eqd2, None, priority4),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc20, TOL.heart_narlal_v20_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_v30_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc50, TOL.heart_narlal_v50_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, average_dose, TOL.lung_mean_eqd2, None, priority4),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc35, TOL.lung_v35_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc55, TOL.lung_v55_adx_eqd2, priority4),

]
thorax_and_abdomen = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx_eqd2, cc0_03, priority1),
  CG.ClinicalGoal(ROIS.heart.name, at_most, average_dose, TOL.heart_mean_eqd2, None, priority4),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc20, TOL.heart_narlal_v20_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc30, TOL.heart_narlal_v30_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.heart.name, at_most, volume_at_dose, pc50, TOL.heart_narlal_v50_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, average_dose, TOL.lung_mean_eqd2, None, priority4),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc35, TOL.lung_v35_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.lungs.name, at_most, volume_at_dose, pc55, TOL.lung_v55_adx_eqd2, priority4),
  CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2), #JSK 2023-08-03
  CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2), #JSK 2023-08-03
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc55, TOL.kidney_v55_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc32, TOL.kidney_v32_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc20, TOL.kidney_v20_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx_eqd2, priority2)
]
abdomen = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx_eqd2, cc0_03, priority1),
  CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2), #JSK 2023-08-03
  CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2), #JSK 2023-08-03
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc55, TOL.kidney_v55_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc32, TOL.kidney_v32_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc20, TOL.kidney_v20_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx_eqd2, priority2)
]
abdomen_and_pelvis = [
  CG.ClinicalGoal(ROIS.spinal_canal.name, at_most, dose_at_abs_volume, TOL.spinalcord_v2_adx_eqd2, cc0_03, priority1),
  CG.ClinicalGoal(ROIS.kidney_l.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2), #JSK 2023-08-03
  CG.ClinicalGoal(ROIS.kidney_r.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2), #JSK 2023-08-03
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, average_dose, TOL.kidney_mean_eqd2, None, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc55, TOL.kidney_v55_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc32, TOL.kidney_v32_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc30, TOL.kidney_v30_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.kidneys.name, at_most, volume_at_dose, pc20, TOL.kidney_v20_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx_eqd2, priority3),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_eqd2,  priority2)
]
pelvis = [
  CG.ClinicalGoal(ROIS.bowel_bag.name, at_most, abs_volume_at_dose, cc195, TOL.bowelspace_v195_adx_eqd2, priority2),
  CG.ClinicalGoal(ROIS.bladder.name, at_most, volume_at_dose, pc50, TOL.bladder_v50_adx_eqd2, priority3),
  CG.ClinicalGoal(ROIS.rectum.name, at_most, volume_at_dose, pc50, TOL.rectum_v50_adx_eqd2,  priority2)
]
other = []




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Clinical goals for TARGETS
# (Sorted cranio-caudally)

# Common targets:
# Used for simple cases and most palliative cases.
targets = [
  CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv.name, at_least, volume_at_dose, pc95, pc99_5, priority2),
  CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority2),
  #CG.ClinicalGoal(ROIS.ctv.name, at_least, homogeneity_index, pc95, pc98, priority5),
  #CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc95, priority5),
  CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
]

# Palliative thorax targets:
# FIXME: Er det riktig å ha andre krav for thorax relaterte palliative MV?!? Vurdere å ta bort.
thorax_targets = [
  CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc95, pc98, priority2),
  CG.ClinicalGoal(ROIS.ctv.name, at_least, homogeneity_index, pc95, pc98, priority5),
  CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc95, pc95, priority5),
  CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_volume, pc90, pc95, priority5),
  CG.ClinicalGoal(ROIS.external.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
]


# Palliative:
def palliative_targets(ss, plan, target):
  targets = [CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)]
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
  #messagebox.showinfo("",str(target) )  
  if nr_targets > 1:
    if len(target) > 0: # Multiple targets
      #target_list = set(list(target))
      #messagebox.showinfo("",str(target_list) ) 
      for i in range(len(target)):
        targets.extend([
          CG.ClinicalGoal(target[i], at_least, dose_at_volume, pc99_5, pc50, priority1),
          CG.ClinicalGoal(target[i], at_most, dose_at_volume, pc100_5, pc50, priority1),
          CG.ClinicalGoal(target[i], at_least, volume_at_dose, pc95, pc99_5, priority3),
          CG.ClinicalGoal(target[i].replace("C", "P"), at_least, volume_at_dose, pc95, pc98, priority3)
        ])
  else:
    targets.extend([
      CG.ClinicalGoal(target, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(target, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(target, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(target.replace("C", "P"), at_least, volume_at_dose, pc95, pc98, priority3),
      #CG.ClinicalGoal(target, at_least, homogeneity_index, pc95, pc98, priority5),
      #CG.ClinicalGoal(target.replace("C", "P"), at_least, conformity_index, pc90, pc95, priority5)
    ])
  return targets


# Brain:
def brain_targets(ss, region_code, nr_fractions, target):
  if nr_fractions in [1,3]: # Stereotactic, one target
    if nr_fractions == 1:
      max_dose = 30
    elif nr_fractions == 3:
      max_dose = 38
    brain_targets = []
    # ta vekk conformity på flere målvolum
    nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
    if target == ROIS.ptv.name:
      brain_targets.extend([
        CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc100, pc99, priority3),
        CG.ClinicalGoal(ROIS.ptv.name, at_most, dose_at_abs_volume, pc150, cc0_03, priority3)
        #CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority5)
      ])
    elif nr_targets == 1: # Stereotactic, 1 target
      brain_targets.extend([
        CG.ClinicalGoal(ROIS.ptv1.name, at_least, volume_at_dose, pc100, pc99, priority3),
        CG.ClinicalGoal(ROIS.ptv1.name, at_most, dose_at_abs_volume, pc150, cc0_03, priority3)
        #CG.ClinicalGoal(ROIS.ptv1.name, at_least, conformity_index, pc90, pc100, priority5)
      ])
    elif nr_targets in [2, 3, 4]: # Stereotactic, 2, 3 or 4 targets
      brain_targets.extend([
        CG.ClinicalGoal(ROIS.ptv1.name, at_least, volume_at_dose, pc100, pc99, priority3),
        CG.ClinicalGoal(ROIS.ptv1.name, at_most, dose_at_abs_volume, pc150, cc0_03, priority3),
        #CG.ClinicalGoal(ROIS.ptv1.name, at_least, conformity_index, pc90, pc100, priority5),
        CG.ClinicalGoal(ROIS.ptv2.name, at_least, volume_at_dose, pc100, pc99, priority3),
        CG.ClinicalGoal(ROIS.ptv2.name, at_most, dose_at_abs_volume, pc150, cc0_03, priority3)
        #CG.ClinicalGoal(ROIS.ptv2.name, at_least, conformity_index, pc90, pc100, priority5),
      ])
      if nr_targets in [3, 4]: # Stereotactic, 3 or 4 targets
        brain_targets.extend([
          CG.ClinicalGoal(ROIS.ptv3.name, at_least, volume_at_dose, pc100, pc99, priority3),
          CG.ClinicalGoal(ROIS.ptv3.name, at_most, dose_at_abs_volume, pc150, cc0_03, priority3)
          #CG.ClinicalGoal(ROIS.ptv3.name, at_least, conformity_index, pc90, pc100, priority5)
        ])
        if nr_targets == 4: # Stereotactic, 4 targets
          brain_targets.extend([
            CG.ClinicalGoal(ROIS.ptv4.name, at_least, volume_at_dose, pc100, pc99, priority3),
            CG.ClinicalGoal(ROIS.ptv4.name, at_most, dose_at_abs_volume, pc150, cc0_03, priority3)
            #CG.ClinicalGoal(ROIS.ptv4.name, at_least, conformity_index, pc90, pc100, priority5)
        ])
    if target == ROIS.ptv.name:
      brain_targets.extend([
        CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority5)
      ])
    elif len(target) > 0:

      for i in range(len(target)):
        brain_targets.extend([
          CG.ClinicalGoal(target[i], at_least, conformity_index, pc90, pc100, priority5)
        ])
      if len(target) > 1:
        brain_targets.extend([
          CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority5)
        ])
  else: # Whole brain or partial brain 
    brain_targets = [
      CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv.name, at_least, volume_at_dose, pc95,pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority3),
      #CG.ClinicalGoal(ROIS.ctv.name, at_least, homogeneity_index, pc95, pc98, priority5),
      #CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc95, pc95, priority5),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ]
  return brain_targets

def head_neck_targets(ss, total_dose):
  head_neck_targets = []
  low = 0
  if total_dose in [60, 64, 66, 68, 70]:
    high = int(total_dose)
    dose_high = str(high)
  if SSF.has_roi_with_shape(ss, ROIS.x_ctv_54.name):
    low = 54
  elif SSF.has_roi_with_shape(ss, ROIS.x_ctv_50.name):
    low = 50
  dose_low = str(low)
  mid = 60
  dose_mid = str(mid)
  head_neck_targets.extend([
    CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
  ])
  if low >0: # If there are any elective lymph nodes
    ctv_e = SSF.return_named_roi_with_contours(ss,[ROIS.ctv_e_50, ROIS.ctv_e_54, ROIS.ctv_e_r_50,ROIS.ctv_e_l_50,ROIS.ctv_e_r_54,ROIS.ctv_e_l_54])
    head_neck_targets.extend([
      CG.ClinicalGoal(ROIS.x_ctv_.name+'_'+dose_low, at_least, dose_at_volume, pc99_5*low, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_.name+'_'+dose_low, at_most, dose_at_volume, pc100_5*low, pc50, priority1),
      CG.ClinicalGoal(ctv_e.name, at_least, volume_at_dose, pc95*low, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_e.name+'_'+dose_low, at_least, volume_at_dose, pc95*low, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_.name+'_'+dose_low, at_most, dose_at_abs_volume, pc105*low, cc2, priority4)
    ])
  if total_dose in [60,64]: # Postoperative to 60 or 64 Gy
    if total_dose == 64: # Postoperative to 64 Gy
      head_neck_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_sb_64.name, at_least, dose_at_volume, pc99_5*64, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_sb_64.name, at_most, dose_at_volume, pc100_5*64, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_sb_64.name, at_least, volume_at_dose, pc95*64, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_sb_64.name, at_least, volume_at_dose, pc95*64, pc98, priority3)
      ])
    if total_dose == 60: 
      # In both cases, there exists a 60 Gy level
      head_neck_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_least, dose_at_volume, pc99_5*mid, pc50, priority1), 
        CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_most, dose_at_volume, pc100_5*mid, pc50, priority1),
      ])
    head_neck_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_sb_60.name, at_least, volume_at_dose, pc95*mid, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.ptv_sb_60.name, at_least, volume_at_dose, pc95*mid, pc98, priority3)
    ])
  elif total_dose > 65: # Primary radiotherapy
    # Highest level of PTVp
    head_neck_targets.extend([
      CG.ClinicalGoal(ROIS.ptv_p.name+'_'+dose_high, at_least, volume_at_dose, pc95*total_dose, pc98, priority3)
    ])
    # PTVp_60
    if SSF.has_roi_with_shape(ss, ROIS.ptv_p.name+'_'+dose_mid):
      head_neck_targets.extend([
        CG.ClinicalGoal(ROIS.ptv_p_60.name, at_least, volume_at_dose, pc95*60, pc98, priority3)
      ])
    # PTVn
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name+'_'+dose_high):
      head_neck_targets.extend([
        CG.ClinicalGoal(ROIS.ptv_n.name+'_'+dose_high, at_least, volume_at_dose, pc95*68, pc98, priority3),
        CG.ClinicalGoal(ROIS.ptv_n_60.name, at_least, volume_at_dose, pc95*60, pc98, priority3)
      ])
    # All possible CTVp/CTVn of the highest dose level are added if they exist
    ctv_high = [ROIS.ctv_p.name+'_'+dose_high, ROIS.ctv_n.name+'_'+dose_high, ROIS.ctv_n1.name+'_'+dose_high,ROIS.ctv_n2.name+'_'+dose_high,ROIS.ctv_n3.name+'_'+dose_high,ROIS.ctv_n4.name+'_'+dose_high]
    for c in ctv_high:
     if SSF.has_roi_with_shape(ss, c):
       head_neck_targets.extend([                             
         CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3),
         CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*total_dose, pc50, priority1),
         CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*total_dose, pc50, priority1)
      ])
    # All possible CTVp_60/CTVn_60 are added if they exist
    ctv_60 = [ROIS.ctv_p_60.name, ROIS.ctv_n_60.name, ROIS.ctv_n1_60.name,ROIS.ctv_n2_60.name,ROIS.ctv_n3_60.name,ROIS.ctv_n4_60.name]
    for c in ctv_60:
     if SSF.has_roi_with_shape(ss, c):
       head_neck_targets.extend([  
         CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*60, pc99_5, priority3)
       ])
  else:
    if SSF.has_roi_with_shape(ss, ROIS.ctv.name):
      head_neck_targets = [
        CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority3),
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
        #CG.ClinicalGoal(ROIS.ptv_n.name+"_"+dose, at_least, volume_at_dose, pc95, pc98, priority3)
      ]
  return head_neck_targets

# Breast:
def breast_targets(ss, region_code, target):
  ctv_p = []
  breast_targets = [
    CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
  ]
  if region_code in RC.breast_partial_codes:
    ctv = [ROIS.ctv_boost.name, ROIS.ctv_boost_r.name, ROIS.ctv_boost_l.name]
    ptv = [ROIS.ptv_boost.name, ROIS.ptv_boost_r.name, ROIS.ptv_boost_l.name]
  else:
    ctv = [ROIS.ctv_n.name, ROIS.ctv_n_l.name, ROIS.ctv_n_r.name, ROIS.ctv_n_imn.name,  ROIS.ctv_n_imn_r.name,  ROIS.ctv_n_imn_l.name ]
    ptv = [ROIS.ptv_nc.name, ROIS.ptv_nc_l.name, ROIS.ptv_nc_r.name,ROIS.ptv_n_imn.name,ROIS.ptv_n_imn_r.name,ROIS.ptv_n_imn_l.name]
    ctv_p = [ROIS.ctv_p.name, ROIS.ctv_p_l.name, ROIS.ctv_p_r.name]
    ptv_pc = [ROIS.ptv_pc.name, ROIS.ptv_pc_l.name, ROIS.ptv_pc_r.name]

  for i in range(len(ctv)):
    if SSF.has_roi_with_shape(ss, ctv[i]):
      breast_targets.extend([
        CG.ClinicalGoal(ctv[i], at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ctv[i], at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ctv[i], at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ptv[i], at_least, volume_at_dose, pc95, pc98, priority3)
      ])
  if len(ctv_p)>0:
    for i in range(len(ctv_p)):
      if SSF.has_roi_with_shape(ss, ctv_p[i]):
        breast_targets.extend([
          CG.ClinicalGoal(ctv_p[i], at_least, dose_at_volume, pc99_5, pc50, priority1),
          CG.ClinicalGoal(ctv_p[i], at_most, dose_at_volume, pc100_5, pc50, priority1),
          CG.ClinicalGoal(ctv_p[i], at_least, volume_at_dose, pc95, pc99_5, priority3),
          CG.ClinicalGoal(ptv_pc[i], at_least, volume_at_dose, pc95, pc99, priority3)
        ])
  
  return breast_targets

def esophagus_targets(ss, total_dose):
  target  = ''
  if SSF.has_roi_with_shape(ss, ROIS.ctv_p_66.name) or SSF.has_roi_with_shape(ss, ROIS.ictv_p_66.name):
    dose = str(66)
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p_66.name):
      target = ROIS.ictv_p_66.name
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p_66.name):
      target = ROIS.ctv_p_66.name
    ptv_target = ROIS.ptv.name+"_"+dose
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_p_60.name) or SSF.has_roi_with_shape(ss, ROIS.ictv_p_60.name):
    dose = str(60)
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p_60.name):
      target = ROIS.ictv_p_60.name
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p_60.name):
      target = ROIS.ctv_p_60.name
    ptv_target = ROIS.ptv.name+"_"+dose
  elif total_dose == 50 and SSF.has_roi_with_shape(ss, ROIS.ctv_p_50.name) or total_dose == 50 and SSF.has_roi_with_shape(ss, ROIS.ictv_p_50.name)or total_dose == 50 and SSF.has_roi_with_shape(ss, ROIS.ictv_p.name) or total_dose == 50 and SSF.has_roi_with_shape(ss, ROIS.ctv_p.name):
    dose = str(50)
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p_50.name):
      target = ROIS.ictv_p_50.name
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p_50.name):
      target = ROIS.ctv_p_50.name
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p.name):
      target = ROIS.ctv_p.name
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p.name):
      target = ROIS.ictv_p.name
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p_50.name) or SSF.has_roi_with_shape(ss, ROIS.ctv_p_50.name):
      ptv_target = ROIS.ptv.name+"_"+dose
    else:
      ptv_target = ROIS.ptv.name
  if SSF.has_roi_with_shape(ss, target):
    esophagus_targets = [
      CG.ClinicalGoal(target, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(target, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(target, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ptv_target, at_least, volume_at_dose, pc95, pc98, priority3),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
      #CG.ClinicalGoal(ROIS.ptv_n.name+"_"+dose, at_least, volume_at_dose, pc95, pc98, priority3)
    ]
    ctv_n = [ROIS.ctv_n.name+"_"+dose,ROIS.ctv_n1.name+"_"+dose,ROIS.ctv_n2.name+"_"+dose, ROIS.ctv_n3.name+"_"+dose, ROIS.ictv_n.name+"_"+dose,ROIS.ictv_n1.name+"_"+dose,ROIS.ictv_n2.name+"_"+dose, ROIS.ictv_n3.name+"_"+dose,
             ROIS.ctv_n.name,ROIS.ctv_n1.name,ROIS.ctv_n2.name, ROIS.ctv_n3.name, ROIS.ictv_n.name,ROIS.ictv_n1.name,ROIS.ictv_n2.name, ROIS.ictv_n3.name]
    for c in ctv_n:
     if SSF.has_roi_with_shape(ss, c):
       esophagus_targets.extend([                             
         CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5, pc50, priority1),
         CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5, pc50, priority1),
         CG.ClinicalGoal(c, at_least, volume_at_dose, pc95, pc99_5, priority3)
       ])
  else:
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p.name):
      esophagus_targets = [
        CG.ClinicalGoal(ROIS.ctv_p.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_p.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_p.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority3),
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
        #CG.ClinicalGoal(ROIS.ptv_n.name+"_"+dose, at_least, volume_at_dose, pc95, pc98, priority3)
      ]
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p.name):
      esophagus_targets = [
        CG.ClinicalGoal(ROIS.ictv_p.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ictv_p.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ictv_p.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority3),
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
        #CG.ClinicalGoal(ROIS.ptv_n.name+"_"+dose, at_least, volume_at_dose, pc95, pc98, priority3)
      ]
    if SSF.has_roi_with_shape(ss, ROIS.gtv_n.name):
      esophagus_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_n.name, at_least, dose_at_volume, pc99_5, pc50, priority1), #Skal det være CTVn?
        CG.ClinicalGoal(ROIS.ctv_n.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_n.name, at_least, volume_at_dose, pc95, pc99_5, priority3)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.igtv_n.name):
      esophagus_targets.extend([
        CG.ClinicalGoal(ROIS.ictv_n.name, at_least, dose_at_volume, pc99_5, pc50, priority1), #Skal det være CTVn?
        CG.ClinicalGoal(ROIS.ictv_n.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ictv_n.name, at_least, volume_at_dose, pc95, pc99_5, priority3)
      ])
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e.name):
    esophagus_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_e.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      #CG.ClinicalGoal(ROIS.ptv_e.name, at_least, volume_at_dose, pc95, pc98, priority3)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e_46_5.name):
    esophagus_targets.extend([
      CG.ClinicalGoal(ROIS.x_ctv_46_5.name, at_least, dose_at_volume, pc99_5*46.5, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_46_5.name, at_most, dose_at_volume, pc100_5*46.5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_46_5.name, at_least, volume_at_dose, pc95*46.5, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_e_46_5.name, at_least, volume_at_dose, pc95*46.5, pc98, priority3)
    ])
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_e_46.name) and total_dose == 46:
    esophagus_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_e_46.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_46.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_46.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_e_46.name, at_least, volume_at_dose, pc95, pc98, priority3)
    ])

  return esophagus_targets
  


# Lung SBRT:
def lung_stereotactic_targets(ss, nr_fractions, target):
  targets = [
    CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc140, cc0_03, priority4) 
  ]
  if nr_fractions == 3:
    max_dose_volume = 1.388888888
    min_max_dose_volume = 1.29629629
  elif nr_fractions == 5:
    max_dose_volume = 1.4
    min_max_dose_volume = 1.2909090909
  else:
    max_dose_volume = 1.4
    min_max_dose_volume = 1.3
  if target == ROIS.ptv.name:
    targets.extend([
      CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc100, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc88, pc100, priority5),
      CG.ClinicalGoal(ROIS.ptv.name, at_most, dose_at_abs_volume, max_dose_volume, cc0_03, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_abs_volume, min_max_dose_volume, cc0_03, priority3)
    ])
  elif len(target)>0:
    for i in range(len(target)):
      targets.extend([
        CG.ClinicalGoal(target[i], at_least, volume_at_dose, pc100, pc98, priority3),
        CG.ClinicalGoal(target[i], at_least, conformity_index, pc88, pc100, priority5),
        CG.ClinicalGoal(target[i], at_most, dose_at_abs_volume, max_dose_volume, cc0_03, priority3),
        CG.ClinicalGoal(target[i], at_least, dose_at_abs_volume, min_max_dose_volume, cc0_03, priority3)
      ])
    if len(target) > 1:
      targets.extend([
        CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority5)
      ])
  return targets


# Liver SBRT:
def liver_stereotactic_targets(ss, nr_fractions, target):
  targets = [
    CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc140, cc0_03, priority4), 
  ]
  if nr_fractions == 3:
    max_dose_volume = 1.4
    min_max_dose_volume = 1.28888888
  elif nr_fractions == 5:
    max_dose_volume = 1.4
    min_max_dose_volume = 1.30
  else:
    max_dose_volume = 1.4
    min_max_dose_volume = 1.3
  if target == ROIS.ptv.name:
    targets.extend([
      CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc100, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc88, pc100, priority5),
      CG.ClinicalGoal(ROIS.ptv.name, at_most, dose_at_abs_volume, max_dose_volume, cc0_03, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_abs_volume, min_max_dose_volume, cc0_03, priority3)
    ])
  elif len(target)>0:
    for i in range(len(target)):
      targets.extend([
        CG.ClinicalGoal(target[i], at_least, volume_at_dose, pc100, pc98, priority3),
        CG.ClinicalGoal(target[i], at_least, conformity_index, pc88, pc100, priority5),
        CG.ClinicalGoal(target[i], at_most, dose_at_abs_volume, max_dose_volume, cc0_03, priority3),
        CG.ClinicalGoal(target[i], at_least, dose_at_abs_volume, min_max_dose_volume, cc0_03, priority3)
      ])
    if len(target) > 1:
      targets.extend([
        CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority5)
      ])
  return targets


# Lung:
def lung_targets(ss, target, total_dose):
  if total_dose > 40:
    lung = [
      CG.ClinicalGoal(ROIS.x_ptv_vev.name, at_least, volume_at_dose, pc95, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_lunge.name, at_least, volume_at_dose, pc90, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ]
    if SSF.has_roi_with_shape(ss, ROIS.ictv_p.name):
      c = ROIS.ictv_p.name
    elif SSF.has_roi_with_shape(ss, ROIS.ictv.name):
      c = ROIS.ictv.name
    elif SSF.has_roi_with_shape(ss, ROIS.ctv.name):
      c = ROIS.ctv.name
    lung.extend([ 
      CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(c, at_least, volume_at_dose, pc95, pc99_5, priority3),
    ])
    ictv_n = [ROIS.ictv_n.name,ROIS.ictv_n1.name, ROIS.ictv_n2.name,ROIS.ictv_n3.name,ROIS.ictv_n4.name,ROIS.ictv_n5.name,ROIS.ictv_n6.name]
    for c in ictv_n:
     if SSF.has_roi_with_shape(ss, c):
       lung.extend([                             
         CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5, pc50, priority1),
         CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5, pc50, priority1),
         CG.ClinicalGoal(c, at_least, volume_at_dose, pc95, pc99_5, priority3)
       ])
    if SSF.has_roi_with_shape(ss, ROIS.bronchus_prv.name): 
      lung.extend([
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc110*66, cc0_03, priority5),
        CG.ClinicalGoal(ROIS.body.name, at_most, abs_volume_at_dose, pc107*66,cc5, priority5) #denne er litt rart definert i funksjon
      ])
  elif total_dose < 40: #FIKME ha alternativ med CTV her? 
    lung = [
      CG.ClinicalGoal(target, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(target, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ptv_vev.name, at_least, volume_at_dose, pc95, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_lunge.name, at_least, volume_at_dose, pc90, pc99_5, priority3),
      CG.ClinicalGoal(target, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
    ]
  return lung


# Bone/Spine SBRT:
def bone_stereotactic_targets(total_dose):
  if total_dose >= 25.2:
    bone_targets= [
      CG.ClinicalGoal(ROIS.gtv.name, at_least, dose_at_volume, 35.63/total_dose, pc99, priority3),
      CG.ClinicalGoal(ROIS.gtv.name, at_least, average_dose, 37.5, None, priority3),
      CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc100*30, pc99, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_volume, pc100, pc99, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority7),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, 37.5*1.4*pc100, cc0_1, priority3),
      CG.ClinicalGoal(ROIS.body_gtv.name, at_most, dose_at_abs_volume, 37.5*pc107/total_dose, cc1, priority5),
      CG.ClinicalGoal(ROIS.body_ptv.name, at_most, dose_at_abs_volume, 37.5*pc107/total_dose, cc1, priority6),
      CG.ClinicalGoal(ROIS.body_ptv.name, at_most, dose_at_abs_volume, 37.5*pc107/total_dose, cc2, priority6),
      CG.ClinicalGoal(ROIS.body_ptv.name, at_most, dose_at_abs_volume, 37.5*pc107/total_dose, cc5, priority6)
    ]
  else:
    bone_targets= [
      CG.ClinicalGoal(ROIS.gtv.name, at_least, dose_at_volume, 35.63/total_dose, pc99, priority3),
      CG.ClinicalGoal(ROIS.gtv.name, at_least, average_dose, 37.5, None, priority3),
      CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc100*30, pc99, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, dose_at_volume, pc100*25.12, pc99, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, conformity_index, pc90, pc100, priority7),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, 37.5*1.4*pc100, cc0_1, priority3),
      CG.ClinicalGoal(ROIS.body_gtv.name, at_most, dose_at_abs_volume, 37.5*pc107/total_dose, cc1, priority5),
      CG.ClinicalGoal(ROIS.body_ptv.name, at_most, dose_at_abs_volume, 37.5*pc107/total_dose, cc1, priority6),
      CG.ClinicalGoal(ROIS.body_ptv.name, at_most, dose_at_abs_volume, 37.5*pc107/total_dose, cc2, priority6),
      CG.ClinicalGoal(ROIS.body_ptv.name, at_most, dose_at_abs_volume, 37.5*pc107/total_dose, cc5, priority6)
    ]
  return bone_targets



bladder_targets = [
  CG.ClinicalGoal(ROIS.ctv_p.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv_p.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
  CG.ClinicalGoal(ROIS.ctv_p.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
  CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority3),
  CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
]


# Prostate:
def prostate_targets(ss, total_dose):
  prostate = [CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)]
  if total_dose == 77: # Normo-fractionation
    prostate.extend([
      CG.ClinicalGoal(ROIS.ctv_p1_77.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_77.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ptv_70.name, at_least, dose_at_volume, pc99_5*70, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ptv_70.name, at_most, dose_at_volume, pc100_5*70, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_77.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ctv_p2_70.name, at_least, volume_at_dose, pc95*70, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_p1_77.name, at_least, volume_at_dose, pc95, pc98,  priority3),
      CG.ClinicalGoal(ROIS.ptv_p2_70.name, at_least, volume_at_dose, pc95*70, pc98, priority3),
    ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name): # With lymph node volume
      prostate.extend([
        CG.ClinicalGoal(ROIS.x_ctv_56.name, at_least, dose_at_volume, pc99_5*56, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_56.name, at_most, dose_at_volume, pc100_5*56, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_56.name, at_least, volume_at_dose, pc95*56, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_e_56.name, at_least, volume_at_dose, pc95*56, pc98, priority3),
        CG.ClinicalGoal(ROIS.x_ptv_56.name, at_most, dose_at_abs_volume, 56*pc100*1.07, cc2, priority6)
      ])
  elif total_dose == 67.5:  # Hypo-fx 2.7 Gy x 25
    prostate.extend([
      CG.ClinicalGoal(ROIS.ctv_p1_67_5.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_67_5.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ptv_62_5.name, at_least, dose_at_volume, pc99_5 * 62.5, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ptv_62_5.name, at_most, dose_at_volume, pc100_5 * 62.5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_67_5.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ctv_p2_62_5.name, at_least, volume_at_dose, pc95 * 62.5, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_p1_67_5.name, at_least, volume_at_dose, pc95, pc98, priority3),
      CG.ClinicalGoal(ROIS.ptv_p2_62_5.name, at_least, volume_at_dose, pc95 * 62.5, pc98, priority3),
      CG.ClinicalGoal(ROIS.x_ptv_62_5.name, at_most, dose_at_abs_volume, 62.5 * pc100 * 1.05, cc2, priority6) # nytt 7/6-23
    ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_50.name):  # With lymph node volume
      prostate.extend([
        CG.ClinicalGoal(ROIS.x_ctv_50.name, at_least, dose_at_volume, pc99_5 * 50, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_50.name, at_most, dose_at_volume, pc100_5 * 50, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_50.name, at_least, volume_at_dose, pc95 * 50, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_e_50.name, at_least, volume_at_dose, pc95 * 50, pc98, priority3),
        CG.ClinicalGoal(ROIS.x_ptv_50.name, at_most, dose_at_abs_volume, 50 * pc100 * 1.07, cc2, priority6)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_62_5.name):
      prostate.extend([
        CG.ClinicalGoal(ROIS.ptv_n_62_5.name, at_least, volume_at_dose, pc95 * 62.5, pc98, priority3)
      ])
    ctv_n_62_5 = [ROIS.ctv_n_62_5.name, ROIS.ctv_n1_62_5.name, ROIS.ctv_n2_62_5.name, ROIS.ctv_n3_62_5.name]
    for c in ctv_n_62_5:
      if SSF.has_roi_with_shape(ss, c):
        prostate.extend([
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5 * 62.5, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5 * 62.5, pc50, priority1),
          CG.ClinicalGoal(c, at_least, volume_at_dose, pc95 * 62.5, pc99_5, priority3),
        ])
  elif total_dose == 60:  # Hypofractionation
    prostate.extend([
      CG.ClinicalGoal(ROIS.ctv_p1_60.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_60.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p1_60.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_p1_60.name, at_least, volume_at_dose, pc95, pc98, priority3),
    ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_p2_57.name):  # because p2 not always present VIL ALLTID VERE DET FRA PÅSKE!
      prostate.extend([
        CG.ClinicalGoal(ROIS.ctv_p2_57.name, at_least, volume_at_dose, pc95 * 57, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_p2_57.name, at_least, volume_at_dose, pc95 * 57, pc98, priority3),
        CG.ClinicalGoal(ROIS.x_ptv_57.name, at_most, dose_at_abs_volume, 57 * pc100 * 1.05, cc2, priority6) # nytt 7/6-23
      ])
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p2_57.name):  # because p2 not always present
      prostate.extend([
        CG.ClinicalGoal(ROIS.x_ptv_57.name, at_least, dose_at_volume, pc99_5 * 57, pc50, priority1),
        # vanligvis ctv-krav, men xCTV!_57 vil bli veldig lite
        CG.ClinicalGoal(ROIS.x_ptv_57.name, at_most, dose_at_volume, pc100_5 * 57, pc50, priority1),
      ])

  else: # Hypofractionation
    prostate.extend([
      CG.ClinicalGoal(ROIS.ctv.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98,  priority3)
    ])

  if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name):
    prostate.extend([
      CG.ClinicalGoal(ROIS.ptv_n_70.name, at_least, volume_at_dose, pc95*70, pc98, priority3)
    ])
  ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
  for c in ctv_n_70:
    if SSF.has_roi_with_shape(ss, c):
      prostate.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*70, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*70, pc50, priority1),
          CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*70, pc99_5, priority3),
        ])

  return prostate

def prostate_bed_targets(ss):
  prostate_bed= [
    CG.ClinicalGoal(ROIS.ctv_sb_70.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_sb_70.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_sb_70.name, at_least, volume_at_dose,pc95, pc99_5, priority3),
    CG.ClinicalGoal(ROIS.ptv_sb_70.name, at_least, volume_at_dose, pc95, pc98, priority3),
    CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
  ]
  if SSF.has_roi_with_shape(ss, ROIS.ptv_e_56.name): # With lymph node volume
    prostate_bed.extend([
      CG.ClinicalGoal(ROIS.x_ctv_56.name, at_least, dose_at_volume, pc99_5*56, pc50, priority1),
      CG.ClinicalGoal(ROIS.x_ctv_56.name, at_most, dose_at_volume, pc100_5*56, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_56.name, at_least, volume_at_dose, pc95*56, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_e_56.name, at_least, volume_at_dose, pc95*56, pc98, priority3),
    ])
  # With boost to positive lymph node 
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n_70.name):
    prostate_bed.extend([
      CG.ClinicalGoal(ROIS.ptv_n_70.name, at_least, volume_at_dose, pc95, pc98, priority3)
    ])
  ctv_n_70 = [ROIS.ctv_n_70.name, ROIS.ctv_n1_70.name,ROIS.ctv_n2_70.name,ROIS.ctv_n3_70.name]
  for c in ctv_n_70:
    if SSF.has_roi_with_shape(ss, c):
      prostate_bed.extend([                             
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5, pc50, priority1),
          CG.ClinicalGoal(c, at_least, volume_at_dose, pc95, pc99_5, priority3),
        ])
  return prostate_bed


def gyn_targets(ss, total_dose):
  if total_dose >44 and SSF.has_roi_with_shape(ss, ROIS.ctv_45.name):
    gyn = [
      CG.ClinicalGoal(ROIS.ctv_45.name, at_least, volume_at_dose, pc95*45, pc99_5, priority3), #average?
      CG.ClinicalGoal(ROIS.ptv_45.name, at_least, volume_at_dose, pc95*45, pc98, priority3), #V95 > 95%
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc107, cc0_03, priority4),
      CG.ClinicalGoal(ROIS.x_ctv_p.name, at_most, dose_at_abs_volume, pc103*45, cc0_03, priority6)
    ]
    if total_dose > 54:
      if total_dose == 55:
        gyn.extend([  
          CG.ClinicalGoal(ROIS.x_body_ptv_n.name, at_most, dose_at_abs_volume, 0.87636363, cc0_03, priority4),
        ])
      #gyn.extend([
      #  CG.ClinicalGoal(ROIS.x_ptv_45.name, at_most, dose_at_abs_volume, 50, cc2, priority6),
      #  
      #])
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n_55.name):
        gyn.extend([
          CG.ClinicalGoal(ROIS.ptv_n_55.name, at_least, volume_at_dose, pc90*55, pc98, priority3) #flere ptv_n?
        ])
      ctv_n_55 = [ROIS.ctv_n1_55.name,ROIS.ctv_n2_55.name,ROIS.ctv_n3_55.name,ROIS.ctv_n4_55.name,ROIS.ctv_n5_55.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_55.name):
        for c in ctv_n_55:
          if SSF.has_roi_with_shape(ss, c):
            gyn.extend([                             
              CG.ClinicalGoal(c, at_least, volume_at_dose, pc100*55, pc98, priority1)
            ])
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_55.name):
        gyn.extend([   
          CG.ClinicalGoal(ROIS.ctv_n_55.name, at_least, volume_at_dose, pc100*55, pc98, priority1) #???
        ])
      if total_dose == 57.5:
        gyn.extend([  
          CG.ClinicalGoal(ROIS.ptv_n_57.name, at_least, volume_at_dose, pc90, pc98, priority3), #90?
          CG.ClinicalGoal(ROIS.x_body_ptv_n.name, at_most, dose_at_abs_volume, 0.8382608, cc0_03, priority7),
        ])
        ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name,ROIS.ctv_n5_57.name]
        if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
          for c in ctv_n_57:
            if SSF.has_roi_with_shape(ss, c):
              gyn.extend([                             
                CG.ClinicalGoal(c, at_least, volume_at_dose, pc100, pc98, priority1)
              ])
        elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_57.name):
          gyn.extend([   
            CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, volume_at_dose, pc100, pc98, priority1)
          ])
      if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ing_r_45.name): 
        gyn.extend([     
          CG.ClinicalGoal(ROIS.ctv_e_ing_r_45.name, at_least, volume_at_dose, pc95*45, pc99_5, priority3),
          CG.ClinicalGoal(ROIS.ctv_e_ing_l_45.name, at_least, volume_at_dose, pc95*45, pc99_5, priority3), 
          CG.ClinicalGoal(ROIS.ptv_e_ing_45.name, at_least, volume_at_dose, pc95*45, pc98, priority3)
        ])
  elif total_dose in [30,50]:
    gyn = [
      CG.ClinicalGoal(ROIS.ctv.name, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3), #average?
      CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95*total_dose, pc98, priority3), #V95 > 95%
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc0_03, priority4),
    ]
    if SSF.has_roi_with_shape(ss, ROIS.ptv_p.name): 
      gyn.extend([     
        CG.ClinicalGoal(ROIS.ctv_p.name, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_p.name, at_least, volume_at_dose, pc95*total_dose, pc98, priority3)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing.name): 
      gyn.extend([     
        CG.ClinicalGoal(ROIS.ctv_e_ing_r.name, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ctv_e_ing_l.name, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3), 
        CG.ClinicalGoal(ROIS.ptv_e_ing.name, at_least, volume_at_dose, pc95*total_dose, pc98, priority3)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_e_pelvic.name): 
      gyn.extend([     
        CG.ClinicalGoal(ROIS.ctv_e_pelvic.name, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_e_pelvic.name, at_least, volume_at_dose, pc95*total_dose, pc98, priority3)
      ])
    ctv_n = [ROIS.ctv_n.name, ROIS.ctv_n1.name,ROIS.ctv_n2.name,ROIS.ctv_n3.name,ROIS.ctv_n4.name,ROIS.ctv_n5.name]
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name):
      for c in ctv_n:
        if SSF.has_roi_with_shape(ss, c):
          gyn.extend([                             
            CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3)
          ])
      gyn.extend([   
        CG.ClinicalGoal(ROIS.ptv_n.name, at_least, volume_at_dose, pc95*total_dose, pc98, priority3)
      ])
  return gyn

def gyn_vulva_targets(ss, total_dose):
  if SSF.has_roi_with_shape(ss, ROIS.ctv_e_pelvic_48.name): # Primary radiotherapy
    gyn = [
      CG.ClinicalGoal(ROIS.ctv_p_67.name, at_least, dose_at_volume, pc99_5*67.2, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_67.name, at_most, dose_at_volume, pc100_5*67.2, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_pelvic_48.name, at_least, volume_at_dose, pc95*47.6, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.ptv_e_pelvic_48.name, at_least, volume_at_dose, pc95*47.6, pc98, priority3), 
      CG.ClinicalGoal(ROIS.ctv_p_67.name, at_least, volume_at_dose, pc95*67.2, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.ptv_p_67.name, at_least, volume_at_dose, pc95*67.2, pc98, priority3),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc107, cc0_03, priority4),
    ]
    if SSF.has_roi_with_shape(ss, ROIS.x_ptv_48.name):
      gyn.extend([
        CG.ClinicalGoal(ROIS.x_ptv_48.name, at_most, dose_at_abs_volume, 47.6*pc100*1.07, cc0_03, priority6),
        CG.ClinicalGoal(ROIS.x_ctv_48.name, at_least, dose_at_volume, pc99_5*47.6, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_48.name, at_most, dose_at_volume, pc100_5*47.6, pc50, priority1)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_59.name):
      gyn.extend([
        CG.ClinicalGoal(ROIS.ptv_n_59.name, at_least, volume_at_dose, pc90*58.8, pc98, priority3) 
      ])
      ctv_n_59 = [ROIS.ctv_n1_59.name,ROIS.ctv_n2_59.name,ROIS.ctv_n3_59.name,ROIS.ctv_n4_59.name,ROIS.ctv_n5_59.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_59.name):
        for c in ctv_n_59:
          if SSF.has_roi_with_shape(ss, c):
            gyn.extend([                             
              CG.ClinicalGoal(c, at_least, volume_at_dose, pc100*58.8, pc98, priority1)
            ])
      else:
        gyn.extend([   
          CG.ClinicalGoal(ROIS.ctv_n_59.name, at_least, volume_at_dose, pc100*58.8, pc98, priority1) 
        ])
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_64.name):
      gyn.extend([  
        CG.ClinicalGoal(ROIS.ptv_n_64.name, at_least, volume_at_dose, pc90*64.4, pc98, priority3),
      ])
      ctv_n_64 = [ROIS.ctv_n1_64.name,ROIS.ctv_n2_64.name,ROIS.ctv_n3_64.name,ROIS.ctv_n4_64.name,ROIS.ctv_n5_64.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_64.name):
        for c in ctv_n_64:
          if SSF.has_roi_with_shape(ss, c):
            gyn.extend([                             
              CG.ClinicalGoal(c, at_least, volume_at_dose, pc100*64.4, pc98, priority1)
            ])
      else:
        gyn.extend([   
          CG.ClinicalGoal(ROIS.ctv_n_64.name, at_least, volume_at_dose, pc100*64.4, pc98, priority1)
        ])
    if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ing_r_48.name): 
      gyn.extend([     
        CG.ClinicalGoal(ROIS.ctv_e_ing_r_48.name, at_least, volume_at_dose, pc95*47.6, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ctv_e_ing_l_48.name, at_least, volume_at_dose, pc95*47.6, pc99_5, priority3), 
        CG.ClinicalGoal(ROIS.ptv_e_ing_48.name, at_least, volume_at_dose, pc95*47.6, pc98, priority3)
      ])
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_e_pelvic_45.name): # Primary radiotherapy
    gyn = [
      CG.ClinicalGoal(ROIS.ctv_sb_57.name, at_least, dose_at_volume, pc99_5*57.5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_sb_57.name, at_most, dose_at_volume, pc100_5*57.5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_e_pelvic_45.name, at_least, volume_at_dose, pc95*45, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.ptv_e_pelvic_45.name, at_least, volume_at_dose, pc95*45, pc98, priority3), 
      CG.ClinicalGoal(ROIS.ctv_sb_57.name, at_least, volume_at_dose, pc95*57.5, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.ptv_sb_57.name, at_least, volume_at_dose, pc95*57.5, pc98, priority3),
      CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc107, cc0_03, priority4),
    ]
    if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ing_r_45.name): 
      gyn.extend([     
        CG.ClinicalGoal(ROIS.ctv_e_ing_r_45.name, at_least, volume_at_dose, pc95*45, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ctv_e_ing_l_45.name, at_least, volume_at_dose, pc95*45, pc99_5, priority3), 
        CG.ClinicalGoal(ROIS.ptv_e_ing_45.name, at_least, volume_at_dose, pc95*45, pc98, priority3)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.x_ptv_45.name):
      gyn.extend([
        CG.ClinicalGoal(ROIS.x_ptv_45.name, at_most, dose_at_abs_volume, 45*pc100*1.05, cc0_03, priority6),
        CG.ClinicalGoal(ROIS.x_ctv_45.name, at_least, dose_at_volume, pc99_5*45, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_45.name, at_most, dose_at_volume, pc100_5*45, pc50, priority1)
      ])
  return gyn



# Rectum:
def rectum_targets(ss,total_dose):
  if total_dose == 50:
    if SSF.has_roi_with_shape(ss, ROIS.ctv_p_50.name):
      rectum_targets = [
        CG.ClinicalGoal(ROIS.ctv_p_50.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_p_50.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_46_5.name, at_least, dose_at_volume, pc99_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.x_ctv_46_5.name, at_most, dose_at_volume, pc100_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_p_50.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ctv_e_pelvic_46_5.name, at_least, volume_at_dose, pc95*46.5, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_p_50.name, at_least, volume_at_dose, pc95, pc98,  priority3),
        CG.ClinicalGoal(ROIS.ptv_e_pelvic_46_5.name, at_least, volume_at_dose, pc95*46.5, pc98, priority3),
        CG.ClinicalGoal(ROIS.x_ptv_46_5.name, at_most, dose_at_abs_volume, pc105*46.5, cc2, priority6),
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
      ]
    if SSF.has_roi_with_shape(ss, ROIS.ctv_sb.name):
      rectum_targets = [
        CG.ClinicalGoal(ROIS.ctv_sb.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_sb.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_pelvic.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_pelvic.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_sb.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ctv_e_pelvic.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_sb.name, at_least, volume_at_dose, pc95, pc98,  priority3),
        CG.ClinicalGoal(ROIS.ptv_e_pelvic.name, at_least, volume_at_dose, pc95, pc98, priority3),
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
      ]
    ctv_n_50 = [ROIS.ctv_n1_50.name,ROIS.ctv_n2_50.name,ROIS.ctv_n3_50.name,ROIS.ctv_n4_50.name]
    if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_50.name):
      for c in ctv_n_50:
        if SSF.has_roi_with_shape(ss, c):
          rectum_targets.extend([                             
            CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*50, pc99_5, priority3),
            CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*50, pc50, priority1),
            CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*50, pc50, priority1)
          ])
    elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_50.name):
      rectum_targets.extend([   
        CG.ClinicalGoal(ROIS.ctv_n_50.name, at_least, volume_at_dose, pc95*50, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ctv_n_50.name, at_least, dose_at_volume, pc99_5*50, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_n_50.name, at_most, dose_at_volume, pc100_5*50, pc50, priority1)
      ])  
    if SSF.has_roi_with_shape(ss, ROIS.ptv_n_50.name):
      rectum_targets.extend([
        CG.ClinicalGoal(ROIS.ptv_n_50.name, at_least, volume_at_dose, pc95, pc98,  priority3)
      ])
    if SSF.has_roi_with_shape(ss, ROIS.ctv_e_ing_l_46.name):
      rectum_targets.extend([
        CG.ClinicalGoal(ROIS.ctv_e_ing_l_46.name, at_least, dose_at_volume, pc99_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_ing_l_46.name, at_most, dose_at_volume, pc100_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_ing_r_46.name, at_least, dose_at_volume, pc99_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_ing_r_46.name, at_most, dose_at_volume, pc100_5*46.5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e_ing_l_46.name, at_least, volume_at_dose, pc95*46.5, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ctv_e_ing_r_46.name, at_least, volume_at_dose, pc95*46.5, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_e_ing_46.name, at_least, volume_at_dose, pc95*46.5, pc98, priority3)
      ])
  else:
    if total_dose > 40:
      rectum_targets = [
        CG.ClinicalGoal(ROIS.ctv_p.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_p.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_p.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ptv_p.name, at_least, volume_at_dose, pc95, pc98,  priority3),
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
      ]
      ctv_n = [ROIS.ctv_n1.name,ROIS.ctv_n2.name,ROIS.ctv_n3.name,ROIS.ctv_n4.name]
      if SSF.has_roi_with_shape(ss, ROIS.ctv_n1.name):
        for c in ctv_n:
          if SSF.has_roi_with_shape(ss, c):
            rectum_targets.extend([                             
              CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3),
              CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*total_dose, pc50, priority1),
              CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*total_dose, pc50, priority1)
            ])
      elif SSF.has_roi_with_shape(ss, ROIS.ctv_n.name):
        rectum_targets.extend([   
          CG.ClinicalGoal(ROIS.ctv_n.name, at_least, volume_at_dose, pc95*total_dose, pc99_5, priority3),
          CG.ClinicalGoal(ROIS.ctv_n.name, at_least, dose_at_volume, pc99_5*total_dose, pc50, priority1),
          CG.ClinicalGoal(ROIS.ctv_n.name, at_most, dose_at_volume, pc100_5*total_dose, pc50, priority1)
        ])
      if SSF.has_roi_with_shape(ss, ROIS.ptv_n.name):
        rectum_targets.extend([
          CG.ClinicalGoal(ROIS.ptv_n.name, at_least, volume_at_dose, pc95, pc98,  priority3)
        ])
    else:
      rectum_targets = [
        CG.ClinicalGoal(ROIS.ctv_e.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
        CG.ClinicalGoal(ROIS.ctv_e.name, at_least, volume_at_dose, pc95, pc99_5, priority3),
        CG.ClinicalGoal(ROIS.ctv_p.name, at_least, volume_at_dose, pc95, pc99_5, priority3),  #JSK 24 feb 2023 
        CG.ClinicalGoal(ROIS.ptv.name, at_least, volume_at_dose, pc95, pc98, priority3),
        CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4)
      ]
  return rectum_targets

# Anus:
def anus_targets(ss, total_dose, target):
  anus_targets = [
    CG.ClinicalGoal(ROIS.x_ctv_41.name, at_least, dose_at_volume, pc99_5*41.6, pc50, priority1),
    CG.ClinicalGoal(ROIS.x_ctv_41.name, at_most, dose_at_volume, pc100_5*41.6, pc50, priority1),
    CG.ClinicalGoal(ROIS.ctv_e_pelvic_41.name, at_least, volume_at_dose, pc95*41.6, pc99_5, priority3),
    CG.ClinicalGoal(ROIS.ptv_e_pelvic_41.name, at_least, volume_at_dose, pc95*41.6, pc98, priority3),
    CG.ClinicalGoal(ROIS.body.name, at_most, dose_at_abs_volume, pc105, cc2, priority4),
    CG.ClinicalGoal(ROIS.x_ptv_41.name, at_most, dose_at_abs_volume, pc105*41.6, cc2, priority6),
  ]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_p_57.name):
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ctv_p_57.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_57.name, at_most, dose_at_volume, pc100_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_57.name, at_least, volume_at_dose, pc95, pc99_5, priority3), 
      CG.ClinicalGoal(ROIS.ptv_p_57.name, at_least, volume_at_dose, pc95, pc98, priority3)
    ])
  if SSF.has_roi_with_shape(ss, ROIS.ctv_p_54.name):
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ctv_p_54.name, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_54.name, at_most, dose_at_volume, pc100_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_p_54.name, at_least, volume_at_dose, pc95*54, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_p_54.name, at_least, volume_at_dose, pc95*54, pc98, priority3)
    ])  
  ctv_n_54 = [ROIS.ctv_n1_54.name,ROIS.ctv_n2_54.name,ROIS.ctv_n3_54.name,ROIS.ctv_n4_54.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_54.name):
    for c in ctv_n_54:
      if SSF.has_roi_with_shape(ss, c):
        anus_targets.extend([                             
          CG.ClinicalGoal(c, at_least, volume_at_dose, pc95*54, pc99_5, priority3),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5*54, pc50, priority1)
        ])
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_54.name):
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_54.name, at_least, volume_at_dose, pc95*54, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ctv_n_54.name, at_least, dose_at_volume, pc99_5*54, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_54.name, at_most, dose_at_volume, pc100_5*54, pc50, priority1)
    ])       
  ctv_n_57 = [ROIS.ctv_n1_57.name,ROIS.ctv_n2_57.name,ROIS.ctv_n3_57.name,ROIS.ctv_n4_57.name]
  if SSF.has_roi_with_shape(ss, ROIS.ctv_n1_57.name):
    for c in ctv_n_57:
      if SSF.has_roi_with_shape(ss, c):
        anus_targets.extend([                             
          CG.ClinicalGoal(c, at_least, volume_at_dose, pc95, pc98, priority3),
          CG.ClinicalGoal(c, at_least, dose_at_volume, pc99_5, pc50, priority1),
          CG.ClinicalGoal(c, at_most, dose_at_volume, pc100_5, pc50, priority1)
        ])
  elif SSF.has_roi_with_shape(ss, ROIS.ctv_n_57.name):
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, dose_at_volume, pc95, pc98, priority3),
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_least, dose_at_volume, pc99_5, pc50, priority1),
      CG.ClinicalGoal(ROIS.ctv_n_57.name, at_most, dose_at_volume, pc100_5, pc50, priority1)
    ])

  if SSF.has_roi_with_shape(ss, ROIS.ptv_n_54.name):
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ptv_n_54.name, at_least, volume_at_dose, pc95*54, pc98, priority3),
    ])       
  if SSF.has_roi_with_shape(ss, ROIS.ptv_n_57.name):
    anus_targets.extend([   
      CG.ClinicalGoal(ROIS.ptv_n_57.name, at_least, volume_at_dose, pc95, pc98, priority3),
    ])
  if SSF.has_roi_with_shape(ss, ROIS.ptv_e_ing_41.name):
    anus_targets.extend([
      CG.ClinicalGoal(ROIS.ctv_e_ing_l_41.name, at_least, volume_at_dose, pc95*41.6, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ctv_e_ing_r_41.name, at_least, volume_at_dose, pc95*41.6, pc99_5, priority3),
      CG.ClinicalGoal(ROIS.ptv_e_ing_41.name, at_least, volume_at_dose, pc95*41.6, pc98, priority3)
    ])


  return anus_targets



