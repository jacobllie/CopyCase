import sys
import time

def generate_roi_algebra(case, derived_roi_expression, derived_roi_status, planningCT_names, Progress):
    """
    Generating roi algebra expressions for derived rois
    :param case:
    :param derived_roi_expression:
    :param derived_roi_status:
    :return:
    """
    error = "Could not generate roi algebra for:"
    succesfull = []
    derived_rois = [r for r in case.PatientModel.RegionsOfInterest if r.Name in derived_roi_expression]
    for i,roi in enumerate(derived_rois):

        expression = derived_roi_expression[roi.Name]
        # we put the algebra on the first planning ct
        try:
            if expression["SimpleExpansion/Contraction"]:
                roi.SetAlgebraExpression(
                                          ExpressionA={
                                              "Operation": "Union",
                                              "SourceRoiNames": expression["A rois"],
                                              'MarginSettings': {
                                                  'Type': "Contract",
                                                  'Superior': 0,
                                                  'Inferior': 0,
                                                  'Anterior': 0,
                                                  'Posterior': 0,
                                                  'Right': 0,
                                                  'Left': 0}},
                                          ExpressionB={
                                              "Operation": "Union",
                                              "SourceRoiNames": [],
                                              'MarginSettings': {
                                                  'Type': "Contract",
                                                  'Superior': 0,
                                                  'Inferior': 0,
                                                  'Anterior': 0,
                                                  'Posterior': 0,
                                                  'Right': 0,
                                                  'Left': 0}},
                                          ResultMarginSettings={
                                              'Type': expression["Output expression"]["ExpandContractType"],
                                              'Superior': expression["Output expression"]["SuperiorDistance"],
                                              'Inferior': expression["Output expression"]["InferiorDistance"],
                                              'Anterior': expression["Output expression"]["AnteriorDistance"],
                                              'Posterior': expression["Output expression"]["PosteriorDistance"],
                                              'Right': expression["Output expression"]["RightDistance"],
                                              'Left': expression["Output expression"]["LeftDistance"]})

            elif "A&B operation" in expression.keys():
                roi.SetAlgebraExpression(
                                          ExpressionA={
                                             "Operation": expression["A operation"],
                                             "SourceRoiNames": expression["A rois"],
                                             'MarginSettings': {
                                                 'Type': expression["A expression"]["ExpandContractType"],
                                                 'Superior': expression["A expression"]["SuperiorDistance"],
                                                 'Inferior': expression["A expression"]["InferiorDistance"],
                                                 'Anterior': expression["A expression"]["AnteriorDistance"],
                                                 'Posterior': expression["A expression"]["PosteriorDistance"],
                                                 'Right': expression["A expression"]["RightDistance"],
                                                 'Left': expression["A expression"]["LeftDistance"]}},
                                         ExpressionB={
                                             "Operation": expression["B operation"],
                                             "SourceRoiNames": expression["B rois"],
                                             'MarginSettings': {
                                                 'Type': expression["B expression"]["ExpandContractType"],
                                                 'Superior': expression["B expression"]["SuperiorDistance"],
                                                 'Inferior': expression["B expression"]["InferiorDistance"],
                                                 'Anterior': expression["B expression"]["AnteriorDistance"],
                                                 'Posterior': expression["B expression"]["PosteriorDistance"],
                                                 'Right': expression["B expression"]["RightDistance"],
                                                 'Left': expression["B expression"]["LeftDistance"]}},
                                         ResultOperation=expression["A&B operation"],
                                         ResultMarginSettings={
                                             'Type': expression["Output expression"]["ExpandContractType"],
                                                 'Superior': expression["Output expression"]["SuperiorDistance"],
                                                 'Inferior': expression["Output expression"]["InferiorDistance"],
                                                 'Anterior': expression["Output expression"]["AnteriorDistance"],
                                                 'Posterior': expression["Output expression"]["PosteriorDistance"],
                                                 'Right': expression["Output expression"]["RightDistance"],
                                                 'Left': expression["Output expression"]["LeftDistance"]})
            else:
                # no B expression
                roi.SetAlgebraExpression(
                                          ExpressionA={
                                              "Operation": expression["A operation"],
                                              "SourceRoiNames": expression["A rois"],
                                              'MarginSettings': {
                                                  'Type': expression["A expression"]["ExpandContractType"],
                                                  'Superior': expression["A expression"]["SuperiorDistance"],
                                                  'Inferior': expression["A expression"]["InferiorDistance"],
                                                  'Anterior': expression["A expression"]["AnteriorDistance"],
                                                  'Posterior': expression["A expression"]["PosteriorDistance"],
                                                  'Right': expression["A expression"]["RightDistance"],
                                                  'Left': expression["A expression"]["LeftDistance"]}},
                                          ExpressionB={
                                              "Operation": "Union",
                                              "SourceRoiNames": [],
                                              'MarginSettings': {
                                                  'Type': "Contract",
                                                  'Superior': 0,
                                                  'Inferior': 0,
                                                  'Anterior': 0,
                                                  'Posterior': 0,
                                                  'Right': 0,
                                                  'Left': 0}},
                                          ResultMarginSettings={
                                              'Type': expression["Output expression"]["ExpandContractType"],
                                              'Superior': expression["Output expression"]["SuperiorDistance"],
                                              'Inferior': expression["Output expression"]["InferiorDistance"],
                                              'Anterior': expression["Output expression"]["AnteriorDistance"],
                                              'Posterior': expression["Output expression"]["PosteriorDistance"],
                                              'Right': expression["Output expression"]["RightDistance"],
                                              'Left': expression["Output expression"]["LeftDistance"]})
            # If status = ShapeIsDirty = False update derived roi
            succesfull.append(True)


        except Exception as e:
            print("Roi {}: {}".format(roi.Name, e))
            succesfull.append(False)
            if roi.Name in error:
                pass
            else:
                error += "\n{}".format(roi.Name)
    if all(succesfull):
        error = ""
    i = 0
    for e in planningCT_names.values():
        print(e)
        examination = case.Examinations[e]
        for roi in derived_rois:
            prog = round(((i + 1) / (len(derived_rois)*len(planningCT_names))) * 100, 0)
            Progress.update_progress(prog)
            #if roi geometry not IsShapeDirty
            i += 1
            try:
                if derived_roi_status[examination.Name][roi.Name] == False:
                    roi.UpdateDerivedGeometry(Examination=examination, Algorithm="Auto")
                elif derived_roi_status[examination.Name][roi.Name] == True:
                    pass
                elif derived_roi_status[examination.Name][roi.Name] == -1:
                    pass
            except:
                if roi.Name in error:
                    pass
                else:
                    error += "\n{}".format(roi.Name)
    return error