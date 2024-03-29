import FWCore.ParameterSet.Config as cms

# output block for alcastream Electron
OutALCARECOEcalCalElectron_specific = cms.untracked.vstring(
    'drop reco*Clusters_hfEMClusters_*_*',
    'drop reco*Clusters_pfPhotonTranslator_*_*',
    'drop *EcalRecHit*_ecalRecHit_*_*',
    'drop *EcalrecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*',
    'drop *EcalRecHit*_reducedEcalRecHitsE*_*_*',
    'drop *_*Unclean*_*_*',
    'drop *_*unclean*_*_*',
    'drop *_*_*Unclean*_*',
    'drop *_*_*unclean*_*',
    )

OutALCARECOEcalCalElectron_noDrop = cms.PSet(
    # put this if you have a filter
    SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 'pathALCARECOEcalCalWElectron')
    #SelectEvents = cms.vstring('pathALCARECOEcalCalZElectron', 'pathALCARECOEcalCalZSCElectron', 'pathALCARECOEcalCalWElectron')
    ),
    outputCommands = cms.untracked.vstring( 
    'keep *_pfMet_*_*',
    'keep *_kt6PFJetsForRhoCorrection_rho_*',
    'keep *_kt6PFJets_rho_*',
    'keep *_offlinePrimaryVerticesWithBS_*_*',
    'keep *BeamSpot_offlineBeamSpot_*_*',
    'keep *_allConversions_*_*',
    'keep *_conversions_*_*',
    'keep *GsfTrack*_*_*_*',
    'keep *_generator_*_*',
    'keep *_addPileupInfo_*_*',
    'keep *_genParticles_*_*',
    'keep recoGsfElectron*_gsfElectron*_*_*',
    'keep recoCaloClusters_*_*_*',
    'keep recoSuperClusters_*_*_*',
    'keep recoPreshowerCluster*_*_*_*',
    'keep *_TriggerResults_*_*',
    'keep *_*_*_HLT',
    'keep *_alcaElectronTracksReducer_*_*',
    'keep *EcalRecHit*_alCaIsolatedElectrons_*_*',
    'keep *EcalRecHit*_reducedEcalRecHitsES_alCaRecHitsES_*',
    'keep *_pfElectronTranslator_*_*',
    )
)

#OutALCARECOEcalCalElectron_noDrop.outputCommands+=OutALCARECOEcalCalElectron_specific


import copy
OutALCARECOEcalCalElectron=copy.deepcopy(OutALCARECOEcalCalElectron_noDrop)
OutALCARECOEcalCalElectron.outputCommands.insert(0, "drop *")
OutALCARECOEcalCalElectron.outputCommands+=OutALCARECOEcalCalElectron_specific
