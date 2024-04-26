import connect


def save_derived_roi_expressions(case, derived_rois):

    def loop_derived_roi_expression(children, operation):
        """
        This recursive function iterates through the children in a derived roi expression for a derived ROI.
        The children alterates between a PyScriptObject and a PyScriptCollection. The function counts how many occurences
        we have of the Operation attributes which reflects if we have roi expansion/contraction, roi algebra with
        only an A expression or both A and B expressions.
        :param children: PyScriptObject or PyScriptCollection
        :param operation: Number of operations in the derived roi expression
        :return: operation
        """
        if type(children) == connect.connect_cpython.PyScriptObject:
            keys = dir(children)
            if any(["Operation" in key for key in keys]):
                operation += 1
            else:
                pass

            if children.Children:
                operation = loop_derived_roi_expression(children.Children, operation)
            else:
                pass
                #print("end of the line")
        else:
            for child in children:
                operation = loop_derived_roi_expression(child, operation)

        return operation

    def save_derived_roi_children(children, operation, dict, num_operations):
        """
        This function is used when we want to extract the derived roi expression children and not only find the number of
        operations are present in the derived roi expression
        :param children: PyScriptObject or PyScriptCollection
        :param operation: Number of operations in derived roi expression
        :return: operation
        """
        if type(children) == connect.connect_cpython.PyScriptObject:
            print("################")
            keys = dir(children)
            print(operation)
            if any("Operation" in key for key in keys):
                # We are on an operation
                if operation == 0 and num_operations < 3:
                    # We are on an A operation
                    dict["A operation"] = children.Operation
                elif operation == 0 and num_operations == 3:
                    # We are on an A&B operation
                    dict["A&B operation"] = children.Operation
                elif operation == 1:
                    # we are on the A operation
                    dict["A operation"] = children.Operation
                elif operation == 2:
                    # we are on the B operation
                    dict["B operation"] = children.Operation

                operation += 1

            elif any("AnteriorDistance" in key for key in keys):
                print(keys)
                # we are on an expression
                if operation < 2:
                    # we are on the A expression
                    dict["A expression"] = {key: getattr(children, key) for key in
                                                                        dir(children) if not key.startswith('__')
                                                                        and "Children" not in key}
                else:
                    dict["B expression"] = {key: getattr(children, key) for key in
                                            dir(children) if not key.startswith('__')
                                            and "Children" not in key}
            elif any("RegionOfInterest" in key for key in keys):
                print(children.RegionOfInterest.Name)
                # We are on a region of interest
                #print(operation)
                if operation < 3:
                    # if the A roi key is not present it should be initialized
                    if "A rois" not in dict:
                        dict["A rois"] = []
                    dict["A rois"].append(children.RegionOfInterest.Name)
                else:
                    if "B rois" not in dict:
                        dict["B rois"] = []
                    dict["B rois"].append(children.RegionOfInterest.Name)
            if children.Children:
                operation = save_derived_roi_children(children.Children, operation, dict, num_operations)
            else:
                print("end of the line")
        else:
            for child in children:
                operation = save_derived_roi_children(child, operation, dict, num_operations)

        return operation


    derived_roi_expressions = {}
    for roi in derived_rois:
        derived_roi_expressions[roi] = {}
        dependent_rois = case.PatientModel.StructureSets[0].RoiGeometries[roi].GetDependentRois()
        expression = case.PatientModel.RegionsOfInterest[roi].DerivedRoiExpression
        derived_roi_expressions[roi]["Output expression"] = {key: getattr(expression, key) for key in
                                                                                dir(expression) if not key.startswith('__')
                                                                                and "Children" not in key}

        if len(dependent_rois) < 2:
            # We have a simple expansion/contraction
            derived_roi_expressions[roi]["SimpleExpansion/Contraction"] = True
            derived_roi_expressions[roi]["A rois"] = dependent_rois
        else:
            derived_roi_expressions[roi]["SimpleExpansion/Contraction"] = True
            operation = 0
            operation = loop_derived_roi_expression(expression.Children, operation)
            save_derived_roi_children(expression.Children, operation=0, dict=derived_roi_expressions[roi], num_operations=operation)

    sorted_derived_roi_expression = {}

    return derived_roi_expressions


def generate_roi_algebra(case, derived_roi_expression, derived_roi_status, planningCT_names, Progress):
    """

    :param case:
    :param derived_roi_expression:
    :param derived_roi_status:
    :return:
    """
    error = ""
    derived_rois = [r for r in case.PatientModel.RegionsOfInterest if r.Name in derived_roi_expression]
    for roi in derived_rois:

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


        except:
            if roi.Name in error:
                pass
            else:
                error += "\n{}".format(roi.Name)
    i = 0
    for e in planningCT_names.values():
        print(e)
        examination = case.Examinations[e]
        for roi in derived_rois:
            prog = round(((i + 1) / (len(derived_rois)*len(planningCT_names))) * 100, 0)
            Progress.update_progress(prog)
            #if roi geometry not IsShapeDirty
            i += 1
            if derived_roi_status:
                # if derived roi status exists, update the derived rois
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


