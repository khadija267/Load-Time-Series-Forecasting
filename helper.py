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

def training_loop(n_epochs, optimiser, model, loss_fn, X_train,  X_val, y_train, y_val):
    for epoch in range(1, n_epochs + 1):
        output_train = model(X_train) # forwards pass
        loss_train = loss_fn(output_train, y_train) # calculate loss
        output_val = model(X_val) 
        loss_val = loss_fn(output_val, y_val)
        
        optimiser.zero_grad() # set gradients to zero
        loss_train.backward() # backwards pass
        optimiser.step() # update model parameters
        if epoch == 1 or epoch % 10000 == 0:
            print(f"Epoch {epoch}, Training loss {loss_train.item():.4f},"
                  f" Validation loss {loss_val.item():.4f}")
