# encoding: utf8

# Import local files:
import property as P
import structure_set_functions as SSF
from tkinter import messagebox

density_create_new = P.Property('Lag ny External som inkluderer tetthetsvolumet','yes', default = True)
density_not_create_new = P.Property('Ikke lag ny External, tetthetsvolumet er allerede inkludert','no')

# Setup techniques:
conformal = P.Property('Hybrid VMAT','Conformal', default = True)
vmat = P.Property('VMAT','VMAT')

# Stereotactic brain
one_arc_s = P.Property('En bue','One', default = True)
two_arcs_s = P.Property('To fulle buer','Two')
three_arcs_s = P.Property('Tre buer, to bordvinkler','Three')

# Breast

# Breast tangential/ breast boost, plan setup
#conformal_tang = P.Property('Hybrid VMAT','Conformal', default = True)
#vmat_tang = P.Property('VMAT','VMAT',next_category = 'feltoppsett')
# Breast tangential/ breast boost, beam setup
#one_arc_tang = P.Property('En bue, dual arc','One', parent = vmat_tang, next_category = 'optimalisering', default = True)
#two_arcs_tang = P.Property('To korte buer, dual arc','Two',parent = vmat_tang, next_category = 'optimalisering')
# Breast tangential/ breast boost, beam setup
one_arc_tang = P.Property('En bue, dual arc','One', next_category = 'optimalisering', default = True)
two_arcs_tang = P.Property('To korte buer, dual arc','Two', next_category = 'optimalisering')

# Breast tangential/ breast boost, optimization setup
for tech in [one_arc_tang, two_arcs_tang ]:
  auto_opt_tang = P.Property('Automatisk optimalisering','auto',parent = tech, default = True)
  opt_tang = P.Property('Vanlig, en runde optimalisering','VMAT',parent = tech)


# Breast regional, plan setup
#conformal_reg = P.Property('Hybrid VMAT','Conformal', default = True)
#vmat_reg = P.Property('VMAT','VMAT', next_category = 'optimalisering')
# Breast regional, optimization setup
#for tech in [conformal_reg, vmat_reg]:

#auto_opt_reg = P.Property('Automatisk optimalisering','auto',parent = vmat_reg)
#opt_reg = P.Property('Vanlig, en runde optimalisering','VMAT',parent = vmat_reg, default = True)
auto_opt_reg = P.Property('Automatisk optimalisering','auto', default = True)
opt_reg = P.Property('Vanlig, en runde optimalisering','VMAT')

# Breast regional with IMN, plan setup
#conformal_imn = P.Property('Hybrid VMAT','Conformal', default = True)
#vmat_imn = P.Property('VMAT','VMAT',next_category = 'feltoppsett')
# Breast regional with IMN, beam setup
one_arc_imn = P.Property('En bue','One',next_category = 'optimalisering', default = True)
cross_imn = P.Property('Kryss med bordvinkel','Cross', next_category = 'optimalisering')
# Breast regional with IMN, optimization setup
for tech in [one_arc_imn, cross_imn]:
  auto_opt_imn = P.Property('Automatisk optimalisering','auto', parent = tech, default = True)
  opt_imn = P.Property('Vanlig, en runde optimalisering','VMAT', parent = tech)


# Breast bilateral, optimization setup
vmat_auto = P.Property('Automatisk optimalisering','auto', default = True)
vmat_one_round = P.Property('Vanlig, en runde optimalisering','VMAT')



stereotactic_two_arcs = P.Property('To halve buer totalt','Two', default = True)
stereotactic_two_arcs_times_number_of_ptvs = P.Property('To halve buer per målvolum','Two_ptv')

palliative_common = P.Property('buer som gjelder for alle valgte målvolum (uten Treat)','Common',next_category = 'feltoppsett for begge målvolum', default = True)
palliative_arcs_times_number_of_ptvs = P.Property('buer per målvolum (med Treat)','Times_Nr_PTVs', next_category = 'feltoppsett for første valgte målvolum')

palliative_small_arcs = P.Property('To korte buer bakfra','short',parent = palliative_common, default = True)
palliative_longer_arcs = P.Property('To kvarte buer bakfra','back',parent = palliative_common)
palliative_front_arcs = P.Property('En halv bue forfra','front',parent = palliative_common)
palliative_right_arcs = P.Property('En halv bue høyre side','right',parent = palliative_common)
palliative_left_arcs = P.Property('En halv bue venstre side','left',parent = palliative_common)
palliative_full_arcs = P.Property('En hel bue','full',parent = palliative_common)

palliative_small_arcs_1 = P.Property('To korte buer bakfra','short',parent = palliative_arcs_times_number_of_ptvs, next_category = 'feltoppsett for andre valgte målvolum', default = True)
palliative_longer_arcs_1 = P.Property('To kvarte buer bakfra','back',parent = palliative_arcs_times_number_of_ptvs,next_category = 'feltoppsett for andre valgte målvolum')
palliative_front_arcs_1 = P.Property('En halv bue forfra','front',parent = palliative_arcs_times_number_of_ptvs,next_category = 'feltoppsett for andre valgte målvolum')
palliative_right_arcs_1 = P.Property('En halv bue høyre side','right',parent = palliative_arcs_times_number_of_ptvs,next_category = 'feltoppsett for andre valgte målvolum')
palliative_left_arcs_1 = P.Property('En halv bue venstre side','left',parent = palliative_arcs_times_number_of_ptvs,next_category = 'feltoppsett for andre valgte målvolum')
palliative_full_arcs_1 = P.Property('En hel bue','full',parent = palliative_arcs_times_number_of_ptvs,next_category = 'feltoppsett for andre valgte målvolum')

for p in [palliative_small_arcs_1, palliative_longer_arcs_1, palliative_front_arcs_1, palliative_right_arcs_1, palliative_left_arcs_1, palliative_full_arcs_1]:
  palliative_small_arcs_2 = P.Property('To korte buer bakfra','short',parent = p, default = True)
  palliative_longer_arcs_2 = P.Property('To kvarte buer bakfra','back',parent = p)
  palliative_front_arcs_2 = P.Property('En halv bue forfra','front',parent = p)
  palliative_right_arcs_2 = P.Property('En halv bue høyre side','right',parent = p)
  palliative_left_arcs_2 = P.Property('En halv bue venstre side','left',parent = p)
  palliative_full_arcs_2 = P.Property('En hel bue','full',parent = p)

palliative_small_arcs_0=  P.Property('To korte buer bakfra','short', default = True)
palliative_longer_arcs_0 = P.Property('To kvarte buer bakfra','back')
palliative_front_arcs_0 = P.Property('En halv bue forfra','front')
palliative_right_arcs_0 = P.Property('En halv bue høyre side (0-182)','right')
palliative_left_arcs_0 = P.Property('En halv bue venstre side (178-0)','left')
palliative_full_arcs_0 = P.Property('En hel bue','full')


# List of choices:
#techniques_tang = [conformal_tang, vmat_tang]
techniques_tang = [one_arc_tang, two_arcs_tang]
#techniques_reg = [conformal_reg, vmat_reg]
techniques_reg = [auto_opt_reg, opt_reg]
techniques_imn = [one_arc_imn,cross_imn]
optimization_auto = [vmat_auto, vmat_one_round]
techniques = [conformal, vmat]

beam_setup = [one_arc_s, two_arcs_s, three_arcs_s]
beam_setup_sbrt = [stereotactic_two_arcs,stereotactic_two_arcs_times_number_of_ptvs]
beam_setup_palliative = [palliative_common,palliative_arcs_times_number_of_ptvs]
beam_arc_setup_palliative = [palliative_small_arcs_0, palliative_longer_arcs_0, palliative_front_arcs_0, palliative_right_arcs_0, palliative_left_arcs_0, palliative_full_arcs_0]

#optimization = [opt_without, opt_init, opt_init_oar]
#optimization_simple = [opt_without, opt_init_oar]
plan_iso = P.Property('Felles iso','commun_iso', default = True)
sep_plan = P.Property('Velg målvolum ','sep_plan')
#iso_choice = P.Property('Separate planer, flere målvolum per iso','sep_plan_multiple')
density = [density_create_new, density_not_create_new]

plan_setup = [plan_iso, sep_plan]

def plan_choices(ss):
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)

  property_list = []
  for i in range(nr_targets):
    property_list.append(P.Property('CTV' + str(i+1),'CTV' + str(i+1), parent = sep_plan))

  
  return [sep_plan, iso_choice, plan_iso] 

def beam_set_choices(ss):
  nr_targets = SSF.determine_nr_of_indexed_ptvs(ss)
  
  sep_plan = P.Property('Separate planer','sep_plan', next_category = 'målvolum')
  sep_beamset_sep_iso = P.Property('Separate beam set - separate isosenter','sep_beamset_sep_iso')
  sep_beamset_iso = P.Property('Separate beam set - felles isosenter','sep_beamset_iso', default = True)
  beamset_iso = P.Property('Samme beam set - felles isosenter','beamset')

  for i in range(nr_targets):
    P.Property('CTV' + str(i+1),'CTV' + str(i+1), parent = sep_plan)
  return [sep_plan, sep_beamset_sep_iso, sep_beamset_iso, beamset_iso] 
