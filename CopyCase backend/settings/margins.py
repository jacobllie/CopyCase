# encoding: utf8

# Import local files:
import margin as MARGIN

# Examples:
# MARGIN.Expansion(superior, inferior, anterior, posterior, right, left)
# MARGIN.Contraction(superior, inferior, anterior, posterior, right, left)


# Commonly used margins:
zero = MARGIN.Expansion(0, 0, 0, 0, 0, 0)
zero_contract = MARGIN.Contraction(0, 0, 0, 0, 0, 0)

# Expansion margins:
uniform_20mm_expansion = MARGIN.Expansion(2, 2, 2, 2, 2, 2) # (Brain tumor CTV)
uniform_50mm_expansion = MARGIN.Expansion(5, 5, 5, 5, 5, 5) 
bladder_expansion = MARGIN.Expansion(1.5, 1.5, 1.5, 1.5, 1.5, 1.5)
uniform_1mm_expansion = MARGIN.Expansion(0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
uniform_2mm_expansion = MARGIN.Expansion(0.2, 0.2, 0.2, 0.2, 0.2, 0.2) # (SRT, Cranial PRVs)
uniform_3mm_expansion = MARGIN.Expansion(0.3, 0.3, 0.3, 0.3, 0.3, 0.3) # (Brain, Head & Neck PTV)
uniform_4mm_expansion = MARGIN.Expansion(0.4, 0.4, 0.4, 0.4, 0.4, 0.4) # (Standard extra cranial daily online bone match IGRT)
uniform_5mm_expansion = MARGIN.Expansion(0.5, 0.5, 0.5, 0.5, 0.5, 0.5) # (Standard extra cranial daily online bone match IGRT)
uniform_6mm_expansion = MARGIN.Expansion(0.6, 0.6, 0.6, 0.6, 0.6, 0.6) 
uniform_7mm_expansion = MARGIN.Expansion(0.7, 0.7, 0.7, 0.7, 0.7, 0.7)
uniform_8mm_expansion = MARGIN.Expansion(0.8, 0.8, 0.8, 0.8, 0.8, 0.8)
uniform_10mm_expansion = MARGIN.Expansion(1.0, 1.0, 1.0, 1.0, 1.0, 1.0) # (Seminal vesicles, cases of poor fixation)
uniform_15mm_expansion = MARGIN.Expansion(1.5, 1.5, 1.5, 1.5, 1.5, 1.5)

lung_sclc_without_4dct = MARGIN.Expansion(1.5, 1.5, 1.3, 1.3, 1.3, 1.3)
prostate_MR_expansion = MARGIN.Expansion(0.0, 0.3, 0.3, 0.3, 0.3, 0.3)
prostate_seed_expansion = MARGIN.Expansion(0.7, 0.7, 0.7, 0.7, 0.5, 0.5)
prostate_lymph_nodes_seed_expansion = MARGIN.Expansion(1.2, 1.2, 1.2, 1.2, 0.8, 0.8)
prostate_bone_match_expansion = MARGIN.Expansion(1.2, 1.2, 1.2, 1.2, 0.8, 0.8)
prostate_bed_lymph_nodes_bone_match_expansion = MARGIN.Expansion(1.2, 1.2, 1.2, 1.2, 0.8, 0.8)
rectum_ctv_primary_risk_expansion = MARGIN.Expansion(0.5, 0.5, 0.8, 0.5, 0.5, 0.5)
rectum_ptv_50_expansion = MARGIN.Expansion(0.8, 0.8, 1.1, 0.8, 0.8, 0.8)
gyn_ptv_p_45_expansion = MARGIN.Expansion(1.5, 2.0, 2.0, 1.5, 1.5, 1.5)
esophagus_ctv_p_expansion = MARGIN.Expansion(2.0, 2.0, 1.0, 1.0, 1.0, 1.0)
esophagus_ptv_6d_expansion = MARGIN.Expansion(0.8, 1.2, 1.0, 0.8, 0.8, 0.8)
esophagus_ptv_3d_expansion = MARGIN.Expansion(1.0, 1.4, 1.2, 1.0, 1.0, 1.0)
esophagus_x_ctv_e_expansion = MARGIN.Expansion(3, 3, 1, 1, 1, 1)
z_mask_for_brain_expansion = MARGIN.Expansion(1, 0.5, 1.0, 1.0, 1.0, 1.0) 
#x_ptv_n_ring_expansion = MARGIN.Expansion(2, 0, 2, 2, 2, 2)
x_ptv_n_ring_expansion = MARGIN.Expansion(7, 0, 7, 7, 7, 7)
x_spare_cran_expansion = MARGIN.Expansion(7, 1, 1, 2, 1, 1)
breast_ptv_p_l_expansion = MARGIN.Expansion(1, 1, 1.5, 0.5, 0.5, 1.5)
breast_ptv_p_r_expansion = MARGIN.Expansion(1, 1, 1.5, 0.5, 1.5, 0.5)
breast_ptv_p_l_vmat_expansion = MARGIN.Expansion(1, 1, 1.5, 0.5, 0.5, 1.5) #
breast_ptv_p_r_vmat_expansion = MARGIN.Expansion(1, 1, 1.5, 0.5, 1.5, 0.5) #
breast_ptv_pc_l_expansion = MARGIN.Expansion(1, 1, 1, 0.5, 0.5, 1)
breast_ptv_pc_r_expansion = MARGIN.Expansion(1, 1, 1, 0.5, 1, 0.5)

breast_ptv_n_l_expansionA = MARGIN.Expansion(0.7, 0.5, 0.7, 0.7, 0.5, 0.7) #
breast_ptv_n_l_expansionB = MARGIN.Expansion(1, 0.5, 1, 1, 0.5, 1) #

breast_ptv_n_r_expansionA = MARGIN.Expansion(0.7, 0.5, 0.7, 0.7, 0.7, 0.5) #
breast_ptv_n_r_expansionB = MARGIN.Expansion(1, 0.5, 1, 1, 0.5, 1) #

breast_ptv_n_r_expansion = MARGIN.Expansion(1, 1, 1, 0.7, 1, 0.5)
breast_tang_ptv_p_expansion = MARGIN.Expansion(1, 1, 0.5, 0.5, 0.5, 0.5)
breast_tang_r_match_expansion = MARGIN.Expansion(1.5, 1.5, 2, 0.5, 2, 0.5) #(superior, inferior, anterior, posterior, right, left)
breast_tang_l_match_expansion = MARGIN.Expansion(1.5, 1.5, 2, 0.5, 0.5, 2)
lung_mask_expansion = MARGIN.Expansion(0, 0, 0.5, 0.5, 0.5, 0.5)
chest_wall_temp_expansion = MARGIN.Expansion(0, 0, 3, 3, 3, 3)
chest_wall_temp_2_expansion = MARGIN.Expansion(0, 0, 2, 2, 2, 2)
chest_wall_temp_1_5_expansion = MARGIN.Expansion(0, 0, 1.5, 1.5, 1.5, 1.5)
chest_wall_expansion = MARGIN.Expansion(15, 15, 4, 9, 1, 1)
liver_sbrt_ptv_expansion = MARGIN.Expansion(0.8, 0.8, 0.6, 0.6, 0.6, 0.6)
liver_sbrt_z_mask_expansion = MARGIN.Expansion(1, 1, 0.5, 0.5, 0.5, 0.5)
liver_temp_expansion = MARGIN.Expansion(1, 1, 0, 0, 0, 4)
esophagus_itv_distal_expansion = MARGIN.Expansion(1, 1, 0.3, 0.3, 0.3, 0.3)
esophagus_itv_prox_expansion = MARGIN.Expansion(0, 1, 0.3, 0.3, 0.3, 0.3)
# Contraction margins:
uniform_5mm_contraction = MARGIN.Contraction(0.5, 0.5, 0.5, 0.5, 0.5, 0.5) # (typically used with external)
uniform_2mm_contraction = MARGIN.Contraction(0.2, 0.2, 0.2, 0.2, 0.2, 0.2)
brainstem_2mm_contraction = MARGIN.Contraction(0.2, 0, 0.2, 0.2, 0.2, 0.2)
skin_contraction = MARGIN.Contraction(0, 0, 0.5, 0.5, 0.5, 0.5)
skin_contraction_10 = MARGIN.Contraction(0, 0, 1, 1, 1, 1)
