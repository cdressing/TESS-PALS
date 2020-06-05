import numpy as np
import h5py

def get_lightcurve(toi:str):
	"""
	Extracts TOI light curves from h5 file.
	Args:
		toi (string): The TOI number (e.g., "101.01").
	Returns:
		time (numpy array): The phase-folded time from the center-of-transit in days.
		flux (numpy array): The phase-folded normalized flux.
	"""

	hf_time = h5py.File('2min_SAP_times.h5', 'r')
	hf_flux = h5py.File('2min_SAP_fluxes.h5', 'r')

	time = np.array(hf_time.get(toi))
	flux = np.array(hf_flux.get(toi))

	hf_time.close()
	hf_flux.close()

	return time, flux