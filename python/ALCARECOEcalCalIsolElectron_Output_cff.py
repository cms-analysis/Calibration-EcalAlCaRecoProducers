import FWCore.ParameterSet.Config as cms

OutALCARECOEcalCalElectron = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalElectron')
    ),
    outputCommands = cms.untracked.vstring('drop  *', 
#	'keep recoGsfTracks_*_*_*',
#	'keep recoGsfTrackExtras_*_*_*',
	'keep recoGsfElectronCores_*_*_*',
	'keep recoSuperClusters_*_*_*',
	'keep *_electronGsfTracks_*_*', 
        'keep  *_gsfElectrons_*_*', 
        'keep  *_alCaIsolatedElectrons_*_*', 
        'keep recoCaloMETs_met_*_*',
        'keep edmTriggerResults_TriggerResults__*', 
        'keep edmHepMCProduct_*_*_*',                                   
        'keep *_MEtoEDMConverter_*_*')
)
