from ophyd import (EpicsMotor, EpicsSignalRO, Device, Component as Cpt)

class MyEpicsMotor(EpicsMotor):
    dial_readback = Cpt(EpicsSignalRO, '.DRBV')
    dial_counts = Cpt(EpicsSignalRO, '.RRBV')
    motor_res = Cpt(EpicsSignalRO, '.MRES')
    encoder_res = Cpt(EpicsSignalRO, '.ERES')
    motor_stat = Cpt(EpicsSignalRO, '.STAT')

class Condenser(Device):
    x = Cpt(MyEpicsMotor, '{CLens:1-Ax:X}Mtr')
    y1 = Cpt(MyEpicsMotor, '{CLens:1-Ax:Y1}Mtr')
    y2 = Cpt(MyEpicsMotor, '{CLens:1-Ax:Y2}Mtr')
    z1 = Cpt(MyEpicsMotor, '{CLens:1-Ax:Z1}Mtr')
    z2 = Cpt(MyEpicsMotor, '{CLens:1-Ax:Z2}Mtr')
    p = Cpt(MyEpicsMotor, '{CLens:1-Ax:P}Mtr')  

class Zoneplate(Device):
    x = Cpt(MyEpicsMotor, '{ZP:1-Ax:X}Mtr')
    y = Cpt(MyEpicsMotor, '{ZP:1-Ax:Y}Mtr')
    z = Cpt(MyEpicsMotor, '{TXM-ZP:1-Ax:Z}Mtr')

class Aperture(Device):
    x = Cpt(MyEpicsMotor, '{Aper:1-Ax:X}Mtr')
    y = Cpt(MyEpicsMotor, '{Aper:1-Ax:Y}Mtr')
    z = Cpt(MyEpicsMotor, '{TXM-Aper:1-Ax:Z}Mtr')

class PhaseRing(Device):
    x = Cpt(MyEpicsMotor, '{PR:1-Ax:X}Mtr')
    y = Cpt(MyEpicsMotor, '{PR:1-Ax:Y}Mtr')
    z = Cpt(MyEpicsMotor, '{TXM-PH:1-Ax:Z}Mtr')

class BetrandLens(Device):
    x = Cpt(MyEpicsMotor, '{BLens:1-Ax:X}Mtr')
    y = Cpt(MyEpicsMotor, '{BLens:1-Ax:Y}Mtr')
    z = Cpt(MyEpicsMotor, '{BLens:1-Ax:Z}Mtr')

class TXMSampleStage(Device):
    sx = Cpt(MyEpicsMotor, '{Env:1-Ax:Xl}Mtr')
    sy = Cpt(MyEpicsMotor, '{Env:1-Ax:Yl}Mtr')
    sz = Cpt(MyEpicsMotor, '{Env:1-Ax:Zl}Mtr')
    pi_x = Cpt(MyEpicsMotor, '{TXM:1-Ax:X}Mtr')
    pi_r = Cpt(MyEpicsMotor, '{TXM:1-Ax:R}Mtr')


class DetSupport(Device):
    x = Cpt(MyEpicsMotor, '-Ax:X}Mtr')
    y = Cpt(MyEpicsMotor, '-Ax:Y}Mtr')
    z = Cpt(MyEpicsMotor, '-Ax:Z}Mtr')

DetU = DetSupport('XF:18IDB-OP{DetS:U', name='DetU')
DetD = DetSupport('XF:18IDB-OP{DetS:D', name='DetD')

clens = Condenser('XF:18IDB-OP', name='clens')
aper = Aperture('XF:18IDB-OP', name='p_hole')
zp = Zoneplate('XF:18IDB-OP', name='zp')
phase_ring = PhaseRing('XF:18IDB-OP', name='phase_ring')
betr = BetrandLens('XF:18IDB-OP', name='betr')
zps = TXMSampleStage('XF:18IDB-OP', name='zps')
XEng = MyEpicsMotor('XF:18IDA-OP{Mono:DCM-Ax:En}Mtr', name='XEng')

motor_txm = [clens.x, clens.y1, clens.y2, clens.z1, clens.z2, clens.p,
             aper.x, aper.y, aper.z,
             zp.x, zp.y, zp.z,
             phase_ring.x, phase_ring.y, phase_ring.z,
             betr.x, betr.y, betr.z,
             zps.sx, zps.sy, zps.sz, zps.pi_x, zps.pi_r,
             DetU.x, DetU.y, DetU.z,
             DetD.x, DetD.y, DetD.z,
             XEng]
