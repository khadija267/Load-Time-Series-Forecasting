def LLR(model1,model2,deg_free):
    '''
    Compares if 2 models are signinfantly different or not
    Input : models and degrees of freedom
    Output : 
    '''
    L1=model1.fit().llf
    L2=model2.fit().llf
    # test statistics
    LR=(2*(L2-L1))
    p_value=chi2.sf(LR,deg_free)

