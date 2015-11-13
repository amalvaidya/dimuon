#
# PLOT DIMUON MASS DISTRIBUTION 
#
import ROOT as R

file_events = R.TFile("test_data/events.root")
tree_events = file_events.Get("events")
n_events = tree_events.GetEntries()
print "Number of events =", str(n_events)

for i_event in xrange(n_events):
    tree_events.GetEntry(i_event)
    n_particles = tree_events.nPart
    print "Number of particles = " + str(n_particles)

h = R.TH1D("hist_m", "dimuon mass", 100, 0, 200)
h.Draw()

