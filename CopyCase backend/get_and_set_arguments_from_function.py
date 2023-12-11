# Define a function that will get and set optimization objectives
# and put it in a dictionary. RaySearch created this function

def get_arguments_from_function(function):
    dfp = function.DoseFunctionParameters
    arg_dict = {}
    arg_dict['RoiName'] = function.ForRegionOfInterest.Name
    arg_dict['IsRobust'] = function.UseRobustness
    arg_dict['Weight'] = dfp.Weight
    if hasattr(dfp, 'FunctionType'):
        if dfp.FunctionType == 'UniformEud':
            arg_dict['FunctionType'] = 'TargetEud'
        else:
            arg_dict['FunctionType'] = dfp.FunctionType
        arg_dict['DoseLevel'] = dfp.DoseLevel
        if 'Eud' in dfp.FunctionType:
            arg_dict['EudParameterA'] = dfp.EudParameterA
        elif 'Dvh' in dfp.FunctionType:
            arg_dict['PercentVolume'] = dfp.PercentVolume
    elif hasattr(dfp, 'HighDoseLevel'):
        # Dose fall-off function does not have function type attribute.
        arg_dict['FunctionType'] = 'DoseFallOff'
        arg_dict['HighDoseLevel'] = dfp.HighDoseLevel
        arg_dict['LowDoseLevel'] = dfp.LowDoseLevel
        arg_dict['LowDoseDistance'] = dfp.LowDoseDistance
    elif hasattr(dfp, 'PercentStdDeviation'):
        # Uniformity constraint does not have function type.
        arg_dict['FunctionType'] = 'UniformityConstraint'
        arg_dict['PercentStdDeviation'] = dfp.PercentStdDeviation
    else:
        # Unknown function type, raise exception.
        raise ('Unknown function type')

    return arg_dict


# Define a function that will use information in arg_dict to set
# optimization function parameters. RaySearch created this function
def set_function_arguments(function, arg_dict):
    dfp = function.DoseFunctionParameters
    dfp.Weight = arg_dict['Weight']
    if arg_dict['FunctionType'] == 'DoseFallOff':
        dfp.HighDoseLevel = arg_dict['HighDoseLevel']
        dfp.LowDoseLevel = arg_dict['LowDoseLevel']
        dfp.LowDoseDistance = arg_dict['LowDoseDistance']
    elif arg_dict['FunctionType'] == 'UniformityConstraint':
        dfp.PercentStdDeviation = arg_dict['PercentStdDeviation']
    else:
        dfp.DoseLevel = arg_dict['DoseLevel']
        if 'Eud' in dfp.FunctionType:
            dfp.EudParameterA = arg_dict['EudParameterA']
        elif 'Dvh' in dfp.FunctionType:
            dfp.PercentVolume = arg_dict['PercentVolume']