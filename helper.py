def LLR(model1,model2,deg_free=1):
    # deg_free= 1 as we are searching for 1 differ
    from scipy.stats.distributions import chi2
    '''
    Compares if 2 models are signinfantly different or not
    Input : models and degrees of freedom
    Output : p_value
    '''
    L1=model1.fit().llf
    L2=model2.fit().llf
    # test statistics - log-likelihood ration
    # we need to compare the information criterion of each model ( searching for the lower AIC and BIC)
    LR=(2*(L2-L1))
    p_value=chi2.sf(LR,deg_free).round(3)
    return p_value

