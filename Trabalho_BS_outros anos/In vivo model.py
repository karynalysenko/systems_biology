from cobra.io import load_json_model
import cobra
model = cobra.io.load_json_model('iEK1011_inVivo_media.json')
print(model.summary())
model_bounds = {r.id:(r.lower_bound, r.upper_bound) for r in model.reactions}
#for i in model_bounds:
    #print(i, model_bounds[i])

from mewpy.simulation import get_simulator
simul = get_simulator(model)
for i in simul.essential_reactions:
    print(i)
print('------------------------------------------')
for i in simul.essential_genes:
    print(i)

result = simul.simulate(method='pFBA')
print(result)
print(result.fluxes['biomass'])
#for k,v in result.fluxes.items():
    #print(k,v)