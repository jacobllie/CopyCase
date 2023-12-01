# encoding: utf8

# Import the System.Drawing namespace:
import clr
clr.AddReference('System.Drawing')
import System.Drawing

# Import local files:
import colors as COLORS


# Defines an isodose object (which contains a percentage value and a visualization color).
class Isodose(object):

    def __init__(self, percent, color):
      self.percent = percent
      self.color = color
      


# Defines a color table object (which contains a list of isodoses).
class ColorTable(object):

    def __init__(self, isodoses):
      self.isodoses = isodoses
    
    # Applies this color table object to the given case.
    def apply_to(self, case):
      # Extract the color table:
      dct = case.CaseSettings.DoseColorMap.ColorTable
      # Remove all existing dose lines:
      dct.clear() 
      # Set the dose lines of this color table object:
      for isodose in self.isodoses:
      	#dct.Add(isodose.percent, isodose.color)
        dct[isodose.percent] = isodose.color
      # Set the color table:
      case.CaseSettings.DoseColorMap.ColorTable = dct



# Colors used for isodose lines:
grey = System.Drawing.Color.FromArgb(255,128,128,128)
sea_green = System.Drawing.Color.FromArgb(255,64,128,128)
white = System.Drawing.Color.FromArgb(255,255,255,255)
blue =  System.Drawing.Color.FromArgb(255,0,0,160)
blue_light =  System.Drawing.Color.FromArgb(255,128,255,255)
green = System.Drawing.Color.FromArgb(255,0,255,0)
yellow = System.Drawing.Color.FromArgb(255,255,255,0)
orange = System.Drawing.Color.FromArgb(255,255,128,0)
orange_low = System.Drawing.Color.FromArgb(255,255,128,64)
red = System.Drawing.Color.FromArgb(255,160,0,0)
red_mid = System.Drawing.Color.FromArgb(255,128,64,64)
dark_red = System.Drawing.Color.FromArgb(255,128,0,0)
blue_mid =  System.Drawing.Color.FromArgb(255,0,128,255)
green_low = System.Drawing.Color.FromArgb(255,128,255,128)
green_low_2 = System.Drawing.Color.FromArgb(255,0,128,64)
yellow_low = System.Drawing.Color.FromArgb(255,255,255,128)
yellow_mid = System.Drawing.Color.FromArgb(255,255,220,64)
#green_mid = System.Drawing.Color.FromArgb(255,0,255,128)
green_mid = System.Drawing.Color.FromArgb(255,128,255,128)
purple = System.Drawing.Color.FromArgb(255,128,0,255)
pink = System.Drawing.Color.FromArgb(255,192,0,192)
purple_low = System.Drawing.Color.FromArgb(255,128,128,255)


# The standard isodose setup:
standard_isodoses = []
standard_isodoses.append(Isodose(30, sea_green))
standard_isodoses.append(Isodose(50, white))
standard_isodoses.append(Isodose(90, blue_light))
standard_isodoses.append(Isodose(95, green))
standard_isodoses.append(Isodose(100, yellow))
standard_isodoses.append(Isodose(105, red))
standard_isodoses.append(Isodose(110, red))

# Head Neck isodose setup

head_neck_54_60_70_isodoses = []
head_neck_54_60_70_isodoses.append(Isodose(30, sea_green))
head_neck_54_60_70_isodoses.append(Isodose(50, white))
head_neck_54_60_70_isodoses.append(Isodose(69.4286, blue_light)) #48.6 Gy
head_neck_54_60_70_isodoses.append(Isodose(73.2857, green_low_2)) # 51.3 Gy
head_neck_54_60_70_isodoses.append(Isodose(77.14286, yellow_low)) # 54 Gy
head_neck_54_60_70_isodoses.append(Isodose(81, orange)) # 56.7 Gy
head_neck_54_60_70_isodoses.append(Isodose(81.42857, green_mid)) # 57 Gy
head_neck_54_60_70_isodoses.append(Isodose(95, green)) # 66.5 Gy
head_neck_54_60_70_isodoses.append(Isodose(100, yellow)) # 70 Gy
head_neck_54_60_70_isodoses.append(Isodose(105, red)) # 73.5 Gy

head_neck_50_60_68_isodoses = []
head_neck_50_60_68_isodoses.append(Isodose(30, sea_green))
head_neck_50_60_68_isodoses.append(Isodose(50, white))
head_neck_50_60_68_isodoses.append(Isodose(66.1765, blue_light)) #45 Gy
head_neck_50_60_68_isodoses.append(Isodose(69.8529, green_low_2)) # 47.5 Gy
head_neck_50_60_68_isodoses.append(Isodose(73.5294, yellow_low)) # 50 Gy
head_neck_50_60_68_isodoses.append(Isodose(77.2059, orange)) # 52.5 Gy
head_neck_50_60_68_isodoses.append(Isodose(83.8235, green_mid)) # 57 Gy
head_neck_50_60_68_isodoses.append(Isodose(95, green)) # 64.6 Gy
head_neck_50_60_68_isodoses.append(Isodose(100, yellow)) # 68 Gy
head_neck_50_60_68_isodoses.append(Isodose(105, red)) # 71.4 Gy

head_neck_54_60_64_isodoses = []
head_neck_54_60_64_isodoses.append(Isodose(30, sea_green))
head_neck_54_60_64_isodoses.append(Isodose(50, white))
head_neck_54_60_64_isodoses.append(Isodose(75.9375, blue_light)) #48.6 Gy
head_neck_54_60_64_isodoses.append(Isodose(80.15625, green_low_2)) # 51.3 Gy
head_neck_54_60_64_isodoses.append(Isodose(84.375, yellow_low)) # 54 Gy
head_neck_54_60_64_isodoses.append(Isodose(88.59375, orange)) # 56.7 Gy
head_neck_54_60_64_isodoses.append(Isodose(89.0625, green_mid)) # 57 Gy
head_neck_54_60_64_isodoses.append(Isodose(95, green)) # 60.8 Gy
head_neck_54_60_64_isodoses.append(Isodose(100, yellow)) # 64 Gy
head_neck_54_60_64_isodoses.append(Isodose(105, red)) # 67.2 Gy

head_neck_50_60_isodoses = []
head_neck_50_60_isodoses.append(Isodose(30, sea_green))
head_neck_50_60_isodoses.append(Isodose(50, white))
head_neck_50_60_isodoses.append(Isodose(75, blue_light)) # 45Gy
head_neck_50_60_isodoses.append(Isodose(79.166, green_low_2)) # 47.5 Gy
head_neck_50_60_isodoses.append(Isodose(83.33333, yellow_low)) # 50 Gy
head_neck_50_60_isodoses.append(Isodose(88.59375, orange)) # 52.5 Gy
head_neck_50_60_isodoses.append(Isodose(95, green)) # 57 Gy
head_neck_50_60_isodoses.append(Isodose(100, yellow)) # 60 Gy
head_neck_50_60_isodoses.append(Isodose(105, red)) # 63 Gy

head_neck_54_60_isodoses = []
head_neck_54_60_isodoses.append(Isodose(30, sea_green))
head_neck_54_60_isodoses.append(Isodose(50, white))
head_neck_54_60_isodoses.append(Isodose(81, blue_light)) # 48.6 Gy
head_neck_54_60_isodoses.append(Isodose(85.5, green_low_2)) # 51.3 Gy
head_neck_54_60_isodoses.append(Isodose(90, yellow_low)) # 54 Gy
head_neck_54_60_isodoses.append(Isodose(94.5, orange)) # 56.7 Gy
head_neck_54_60_isodoses.append(Isodose(95, green)) # 57 Gy
head_neck_54_60_isodoses.append(Isodose(100, yellow)) # 60 Gy
head_neck_54_60_isodoses.append(Isodose(105, red)) # 63 Gy


# Lung isodose setup:
lung_isodoses = []
#lung_isodoses.append(Isodose(30, sea_green))
lung_isodoses.append(Isodose(50, white))
lung_isodoses.append(Isodose(90, blue_light))
lung_isodoses.append(Isodose(95, green))
lung_isodoses.append(Isodose(100, yellow))
lung_isodoses.append(Isodose(105, red))
#lung_isodoses.append(Isodose(110, red))

# Gyn vulva isodoses
gyn_48_59_64_67_isodoses = []
gyn_48_59_64_67_isodoses.append(Isodose(30, sea_green))
gyn_48_59_64_67_isodoses.append(Isodose(50, white))
#gyn_45_55_57_isodoses.append(Isodose(65, blue))
gyn_48_59_64_67_isodoses.append(Isodose(67.29166666, green_low_2))
gyn_48_59_64_67_isodoses.append(Isodose(70.833333, yellow_mid))
gyn_48_59_64_67_isodoses.append(Isodose(74.375, orange_low))
gyn_48_59_64_67_isodoses.append(Isodose(78.75, green))
gyn_48_59_64_67_isodoses.append(Isodose(86.25, green_mid))
gyn_48_59_64_67_isodoses.append(Isodose(87.5, yellow_mid))
gyn_48_59_64_67_isodoses.append(Isodose(95.833333, yellow_low))
gyn_48_59_64_67_isodoses.append(Isodose(95, green))
gyn_48_59_64_67_isodoses.append(Isodose(100, yellow))
#gyn_48_59_64_67_isodoses.append(Isodose(102, orange))
gyn_48_59_64_67_isodoses.append(Isodose(107, red))

gyn_48_64_67_isodoses = []
gyn_48_64_67_isodoses.append(Isodose(30, sea_green))
gyn_48_64_67_isodoses.append(Isodose(50, white))
gyn_48_64_67_isodoses.append(Isodose(67.29166666, green_low_2))
gyn_48_64_67_isodoses.append(Isodose(70.833333, yellow_mid))
gyn_48_64_67_isodoses.append(Isodose(74.375, orange_low))
gyn_48_64_67_isodoses.append(Isodose(86.25, green_mid))
gyn_48_64_67_isodoses.append(Isodose(95.833333, yellow_low))
gyn_48_64_67_isodoses.append(Isodose(95, green))
gyn_48_64_67_isodoses.append(Isodose(100, yellow))
gyn_48_64_67_isodoses.append(Isodose(107, red))


gyn_48_59_67_isodoses = []
gyn_48_59_67_isodoses.append(Isodose(30, sea_green))
gyn_48_59_67_isodoses.append(Isodose(50, white))
gyn_48_59_67_isodoses.append(Isodose(67.29166666, green_low_2))
gyn_48_59_67_isodoses.append(Isodose(70.833333, yellow_mid))
gyn_48_59_67_isodoses.append(Isodose(74.375, orange_low))
gyn_48_59_67_isodoses.append(Isodose(78.75, green))
gyn_48_59_67_isodoses.append(Isodose(87.5, yellow_mid))
gyn_48_59_67_isodoses.append(Isodose(95, green))
gyn_48_59_67_isodoses.append(Isodose(100, yellow))
gyn_48_59_67_isodoses.append(Isodose(107, red))

gyn_vulva_45_57_isodoses = []
gyn_vulva_45_57_isodoses.append(Isodose(30, sea_green))
gyn_vulva_45_57_isodoses.append(Isodose(50, white))
gyn_vulva_45_57_isodoses.append(Isodose(74.3478, green_low_2))
gyn_vulva_45_57_isodoses.append(Isodose(78.2608, yellow_mid))
gyn_vulva_45_57_isodoses.append(Isodose(82.2608, orange_low))
gyn_vulva_45_57_isodoses.append(Isodose(95, green))
gyn_vulva_45_57_isodoses.append(Isodose(100, yellow))
gyn_vulva_45_57_isodoses.append(Isodose(102, orange))
gyn_vulva_45_57_isodoses.append(Isodose(107, red))

gyn_45_57_isodoses = []
gyn_45_57_isodoses.append(Isodose(30, sea_green))
gyn_45_57_isodoses.append(Isodose(50, white))
gyn_45_57_isodoses.append(Isodose(74.3478, green_low_2))
gyn_45_57_isodoses.append(Isodose(78.2608, yellow_mid))
gyn_45_57_isodoses.append(Isodose(82.2608, orange_low))
gyn_45_57_isodoses.append(Isodose(90, green))
gyn_45_57_isodoses.append(Isodose(100, yellow))
gyn_45_57_isodoses.append(Isodose(102, orange))
gyn_45_57_isodoses.append(Isodose(107, red))
# Gyn cervix isodoses
gyn_45_55_57_isodoses = []
gyn_45_55_57_isodoses.append(Isodose(30, sea_green))
gyn_45_55_57_isodoses.append(Isodose(50, white))
#gyn_45_55_57_isodoses.append(Isodose(65, blue))
gyn_45_55_57_isodoses.append(Isodose(74.3478, green_low_2))
gyn_45_55_57_isodoses.append(Isodose(78.2608, yellow_mid))
gyn_45_55_57_isodoses.append(Isodose(82.2608, orange_low))
gyn_45_55_57_isodoses.append(Isodose(86.086956, green_mid))
gyn_45_55_57_isodoses.append(Isodose(95.65217, yellow_low))
gyn_45_55_57_isodoses.append(Isodose(90, green))
gyn_45_55_57_isodoses.append(Isodose(100, yellow))
gyn_45_55_57_isodoses.append(Isodose(102, orange))
gyn_45_55_57_isodoses.append(Isodose(107, red))

gyn_45_55_isodoses = []
gyn_45_55_isodoses.append(Isodose(30, sea_green))
gyn_45_55_isodoses.append(Isodose(50, white))
#gyn_45_55_57_isodoses.append(Isodose(65, blue))
gyn_45_55_isodoses.append(Isodose(77.7272, green_low_2))
gyn_45_55_isodoses.append(Isodose(81.8181, yellow_low))
gyn_45_55_isodoses.append(Isodose(86, orange_low))
gyn_45_55_isodoses.append(Isodose(90, green))
gyn_45_55_isodoses.append(Isodose(100, yellow))
gyn_45_55_isodoses.append(Isodose(105, red))


# Prostate SIB 56/70/77 isodose setup:
prostate_56_70_77_isodoses = []
prostate_56_70_77_isodoses.append(Isodose(30, sea_green))
prostate_56_70_77_isodoses.append(Isodose(50, white))
prostate_56_70_77_isodoses.append(Isodose(65.4545454545, blue_light))
prostate_56_70_77_isodoses.append(Isodose(69.0909090909, green_low_2))
prostate_56_70_77_isodoses.append(Isodose(72.72727272, yellow_low))
prostate_56_70_77_isodoses.append(Isodose(76.36363636, orange))
prostate_56_70_77_isodoses.append(Isodose(77.92, purple))
prostate_56_70_77_isodoses.append(Isodose(86.36, green_mid))
#prostate_56_70_77_isodoses.append(Isodose(90.09, yellow_low))
prostate_56_70_77_isodoses.append(Isodose(95, green))
prostate_56_70_77_isodoses.append(Isodose(100, yellow))
prostate_56_70_77_isodoses.append(Isodose(105, red))

# Prostate SIB 50/62.5/67.5 isodose setup:
prostate_50_62_5_67_5_isodoses = []
prostate_50_62_5_67_5_isodoses.append(Isodose(30, sea_green))
prostate_50_62_5_67_5_isodoses.append(Isodose(50, white))
prostate_50_62_5_67_5_isodoses.append(Isodose(66.666667, blue_light)) #45 Gy
prostate_50_62_5_67_5_isodoses.append(Isodose(70.37037037, green_low_2)) # 47.5 Gy
prostate_50_62_5_67_5_isodoses.append(Isodose(74.07407407, yellow_low)) # 50 Gy
prostate_50_62_5_67_5_isodoses.append(Isodose(77.77777778, orange)) # 52.5 Gy
prostate_50_62_5_67_5_isodoses.append(Isodose(92.5926, yellow_low)) #62.5 Gy
prostate_50_62_5_67_5_isodoses.append(Isodose(87.96296, green_mid)) #59.375 Gy
#prostate_50_62_5_67_5_isodoses.append(Isodose(90.09, yellow_low))
prostate_50_62_5_67_5_isodoses.append(Isodose(95, green))
prostate_50_62_5_67_5_isodoses.append(Isodose(100, yellow))
prostate_50_62_5_67_5_isodoses.append(Isodose(105, red))

# Prostate SIB 70/77 isodose setup:
prostate_70_77_isodoses = []
prostate_70_77_isodoses.append(Isodose(45.45, sea_green))
prostate_70_77_isodoses.append(Isodose(50, white))
prostate_70_77_isodoses.append(Isodose(77.92, grey))
prostate_70_77_isodoses.append(Isodose(81.81, blue_mid))
prostate_70_77_isodoses.append(Isodose(86.36, green_mid))
prostate_70_77_isodoses.append(Isodose(90.09, yellow_low))
prostate_70_77_isodoses.append(Isodose(95, green))
prostate_70_77_isodoses.append(Isodose(100, yellow))
prostate_70_77_isodoses.append(Isodose(105, red))


# Prostate SIB 57/60 isodose setup:
prostate_57_60_isodoses = []
prostate_57_60_isodoses.append(Isodose(30, sea_green))
prostate_57_60_isodoses.append(Isodose(50, white))
prostate_57_60_isodoses.append(Isodose(85, blue_light))
prostate_57_60_isodoses.append(Isodose(90.25, green_mid))
prostate_57_60_isodoses.append(Isodose(95, green))
prostate_57_60_isodoses.append(Isodose(100, yellow))
prostate_57_60_isodoses.append(Isodose(105, red))



# Prostate bed SIB 56/70 isodose setup:
prostate_bed_56_70_isodoses = []
prostate_bed_56_70_isodoses.append(Isodose(30, sea_green))
prostate_bed_56_70_isodoses.append(Isodose(50, white))
prostate_bed_56_70_isodoses.append(Isodose(72, blue_light))
prostate_bed_56_70_isodoses.append(Isodose(76, green_low_2))
prostate_bed_56_70_isodoses.append(Isodose(80, yellow_low))
prostate_bed_56_70_isodoses.append(Isodose(84, orange))
prostate_bed_56_70_isodoses.append(Isodose(85.7142, purple))
prostate_bed_56_70_isodoses.append(Isodose(95, green))
prostate_bed_56_70_isodoses.append(Isodose(100, yellow))
prostate_bed_56_70_isodoses.append(Isodose(105, red))

# Anus SIB 41.6/54/57.5
anus_41_54_57_isodoses = []
anus_41_54_57_isodoses.append(Isodose(30, sea_green))
anus_41_54_57_isodoses.append(Isodose(50, white))
#gyn_45_55_57_isodoses.append(Isodose(65, blue))
anus_41_54_57_isodoses.append(Isodose(68.7304, green_low_2))
anus_41_54_57_isodoses.append(Isodose(72.3478, yellow_mid))
anus_41_54_57_isodoses.append(Isodose(75.9652, orange_low))
anus_41_54_57_isodoses.append(Isodose(89.21739, green_mid))
anus_41_54_57_isodoses.append(Isodose(93.9130, yellow_low))
anus_41_54_57_isodoses.append(Isodose(95, green))
anus_41_54_57_isodoses.append(Isodose(100, yellow))
anus_41_54_57_isodoses.append(Isodose(105, red))

# Anus SIB 41.6/54
anus_41_54_isodoses = []
anus_41_54_isodoses.append(Isodose(30, sea_green))
anus_41_54_isodoses.append(Isodose(50, white))
anus_41_54_isodoses.append(Isodose(73.18518, green_low_2))
anus_41_54_isodoses.append(Isodose(77.0370, yellow_mid))
anus_41_54_isodoses.append(Isodose(80.8888, orange_low))
anus_41_54_isodoses.append(Isodose(95, green))
anus_41_54_isodoses.append(Isodose(100, yellow))
anus_41_54_isodoses.append(Isodose(105, red))

# SIB 47/50 isodose setup:
sib_47_50_isodoses = []
sib_47_50_isodoses.append(Isodose(30, sea_green))
sib_47_50_isodoses.append(Isodose(50, white))
sib_47_50_isodoses.append(Isodose(84.6, blue_light))
sib_47_50_isodoses.append(Isodose(89, green_mid))
sib_47_50_isodoses.append(Isodose(95, green))
sib_47_50_isodoses.append(Isodose(100, yellow))
sib_47_50_isodoses.append(Isodose(105, orange))
sib_47_50_isodoses.append(Isodose(110, red))

# SIB 46.5/50 isodose setup:
sib_46_5_50_isodoses = []
sib_46_5_50_isodoses.append(Isodose(30, sea_green))
sib_46_5_50_isodoses.append(Isodose(50, white))
sib_46_5_50_isodoses.append(Isodose(88.35, green_low_2))
sib_46_5_50_isodoses.append(Isodose(95, green))
sib_46_5_50_isodoses.append(Isodose(100, yellow))
sib_46_5_50_isodoses.append(Isodose(105, orange))
sib_46_5_50_isodoses.append(Isodose(110, red))

# SBRT isodose setup:
stereotactic_isodoses = []
stereotactic_isodoses.append(Isodose(30, sea_green))
stereotactic_isodoses.append(Isodose(50, white))
#stereotactic_isodoses.append(Isodose(90, blue))
#stereotactic_isodoses.append(Isodose(95, green))
stereotactic_isodoses.append(Isodose(100, green))
#stereotactic_isodoses.append(Isodose(105, orange))
stereotactic_isodoses.append(Isodose(130, pink))
stereotactic_isodoses.append(Isodose(140, red))

# SBRT isodose setup:
stereotactic_bone_isodoses = []
stereotactic_bone_isodoses.append(Isodose(30, sea_green))
stereotactic_bone_isodoses.append(Isodose(50, white))
#stereotactic_bone_isodoses.append(Isodose(90, blue))
#stereotactic_bone_isodoses.append(Isodose(95, green))
stereotactic_bone_isodoses.append(Isodose(100, green))
#stereotactic_bone_isodoses.append(Isodose(105, orange))
stereotactic_bone_isodoses.append(Isodose(119.4, yellow))
stereotactic_bone_isodoses.append(Isodose(141.7910, pink))
stereotactic_bone_isodoses.append(Isodose(149.2537, orange))
stereotactic_bone_isodoses.append(Isodose(208.955, red))

# Set up the color tables to be used:
standard = ColorTable(standard_isodoses)
prostate_56_70_77 = ColorTable(prostate_56_70_77_isodoses)
prostate_50_62_5_67_5 = ColorTable(prostate_50_62_5_67_5_isodoses)
prostate_70_77 = ColorTable(prostate_70_77_isodoses)
prostate_57_60 = ColorTable(prostate_57_60_isodoses)
sib_47_50 = ColorTable(sib_47_50_isodoses)
sib_46_5_50 = ColorTable(sib_46_5_50_isodoses)
anus_41_54_57 = ColorTable(anus_41_54_57_isodoses)
anus_41_54 = ColorTable(anus_41_54_isodoses)
prostate_bed_56_70 = ColorTable(prostate_bed_56_70_isodoses)
stereotactic = ColorTable(stereotactic_isodoses)
stereotactic_bone = ColorTable(stereotactic_bone_isodoses)
head_neck_54_60_70 = ColorTable(head_neck_54_60_70_isodoses)
head_neck_50_60_68 = ColorTable(head_neck_50_60_68_isodoses)
head_neck_54_60_64 = ColorTable(head_neck_54_60_64_isodoses)
head_neck_54_60 = ColorTable(head_neck_54_60_isodoses)
head_neck_50_60 = ColorTable(head_neck_50_60_isodoses)
gyn_45_55_57 = ColorTable(gyn_45_55_57_isodoses)
gyn_48_59_64_67=ColorTable(gyn_48_59_64_67_isodoses)
gyn_48_64_67=ColorTable(gyn_48_64_67_isodoses)
gyn_48_59_67=ColorTable(gyn_48_59_67_isodoses)
gyn_45_55 = ColorTable(gyn_45_55_isodoses)
gyn_45_57 = ColorTable(gyn_45_57_isodoses)
gyn_vulva_45_57 = ColorTable(gyn_vulva_45_57_isodoses)
lung = ColorTable(lung_isodoses)
