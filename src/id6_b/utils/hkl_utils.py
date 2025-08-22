from apsbits.core.instrument_init import oregistry
import numpy as np

class Geometries:
    """Register the diffractometer geometries."""

    _psic = None
    _psic_sim = None
    _psic_q2 = None
    _psic_psi = None

    def __init__(self, psic_nm, sim_nm, q2_nm, psi_nm):
        self.psic = oregistry.find(psic_nm)
        self.sim = oregistry.find(sim_nm)
        self.q2 = oregistry.find(q2_nm)
        self.psi = oregistry.find(psi_nm)

    @property
    def sim(self):
        return self._psic_sim

    @sim.setter
    def sim(self, value):
        self._psic_sim = value

    @property
    def psic(self):
        return self._psic

    @psic.setter
    def psic(self, value):
        self._psic = value

    @property
    def q2(self):
        return self._psic_q2

    @q2.setter
    def q2(self, value):
        self._psic_q2 = value

    @property
    def psi(self):
        return self._psic_psi

    @psi.setter
    def psi(self, value):
        self._psic_psi = value


geometries = Geometries("psic", "psic_sim", "psic_q", "psic_psi")
# geometries.psic = oregistry.find("psic")
# geometries.sim = oregistry.find("psic_sim")
# geometries.q2 = oregistry.find("psic_q")
# geometries.psi = oregistry.find("psic_psi")


 def _wh():
    import numpy as np
    """
    Retrieve information on the current reciprocal space position.

    WARNING: This function will only work with six circles. This will be fixed
    in future releases.
    """
    _geom_ = geometries.psic
    _geom_for_psi_ = geometries.psi
    #_geom_for_psi_.calc.sample.UB=_geom_.calc._sample.UB
    _geom_for_psi_.sample.UB = _geom_.sample.UB
    _geom_for_q_ = geometries.q2
    print(
        f"\n   {' '.join(_geom_.pseudo_positioners._fields).upper()}"
        f" = {', '.join([f'{v.position:5f}' for v in _geom_.pseudo_positioners])}"
    )
    print(
        f"\n   Lambda (Energy) = {_geom_.beam.wavelength.get():6.4f} \u212b"
        f" ({_geom_.beam.energy.get():6.4f}) keV"
    )
    print(
        f"\n{''.join(f'{k:>10}' for k in _geom_.real_positioners._fields)}"
        f"\n{''.join(f'{v.position:>10.3f}' for v in _geom_.real_positioners)}"
    )
    print(
        "\n   PSI = {:5.4f} ".format(
            _geom_for_psi_.inverse(0).psi,
        )
    )
    _h2, _k2, _l2 = _geom_for_psi_.core.extras.values()
    print(
        "   PSI reference vector = {:3.3f} {:3.3f} {:3.3f}".format(
            _h2,
            _k2,
            _l2,
        )
    )
    tth_from_q = 2*np.emath.arcsin(_geom_for_q_.inverse(0).q/4/_geom_.beam.wavelength.get())*180/np.pi
    print(
        "\n   Q = {:5f}  tth = {:5f}".format(
            _geom_for_q_.inverse(0).q, tth_from_q
        )
    )
 