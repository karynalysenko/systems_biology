from cobra.io import read_sbml_model
model = read_sbml_model('iEK1008.xml')
print(model.summary())
model_bounds = {r.id:(r.lower_bound, r.upper_bound) for r in model.reactions}
for i in model_bounds:
    print(i, model_bounds[i])


from mewpy.simulation import get_simulator
simul = get_simulator(model)
print(simul.essential_reactions)
print(simul.essential_genes)
print(simul.objective)
result = simul.simulate(method='pFBA')
print(result)

for k,v in result.fluxes.items():
    print(k,v)


#environmental conditions
envcond = {'EX_GLC_e': (-10.0, 100000.0), 'EX_O2_e':(-5,1000)}
from mewpy.simulation import get_simulator
simul = get_simulator(model, envcond=envcond)
result = simul.simulate(method='pFBA')
print(result.data_frame)
